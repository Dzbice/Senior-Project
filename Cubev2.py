import numpy as np
import collections
import copy
import time

start = time.perf_counter()
class Piece:
    def __init__(self, colors) -> None:
        self.colors = colors

    def movePiece(self, clockwise, face):
        sides = {
            "Up": ["F", "R", "B", "L"],
            "Down": ["F", "L", "B", "R"],
            "Right": ["F", "U", "B", "D"],
            "Left": ["F", "D", "B", "U"],
            "Front": ["U", "R", "D", "L"],
            "Back": ["U", "R", "D", "L"],
        }
        if face not in sides:
            return

        faces = sides[face]
        new_colors = {}
        for i, side in enumerate(faces):
            new_colors[faces[(i + (1 if clockwise else -1)) % 4]] = self.colors[side]
        for other in self.colors:
            if other not in faces:
                new_colors[other] = self.colors[other]
        self.colors = new_colors


class Cube:
    def __init__(self) -> None:
        self.cube = np.empty((3, 3, 3), dtype=object)
        self.make_cube()

    def make_cube(self):
        for z in range(3):
            for y in range(3):
                for x in range(3):
                    colors = {}
                    match x:  # Left and Right sides
                        case 0:
                            colors["Left"] = "R"
                        case 2:
                            colors["Right"] = "O"
                    match y:  # Top and bottom
                        case 0:
                            colors["Up"] = "Y"
                        case 2:
                            colors["Down"] = "W"
                    match z:  # front and back
                        case 0:
                            colors["Front"] = "G"
                        case 2:
                            colors["Back"] = "B"
                    self.cube[x, y, z] = Piece(colors)

    def move(self, face, clockwise=None):
        if clockwise is None:
            clockwise = True
        self.CubeRot = np.copy(self.cube)
        match face:
            case "L":
                clockwise = not clockwise
                self.FC = self.CubeRot[0, :, :]
            case "R":
                self.FC = self.CubeRot[2, :, :]
            case "U":
                self.FC = self.CubeRot[:, 0, :]
            case "D":
                clockwise = not clockwise
                self.FC = self.CubeRot[:, 2, :]
            case "F":
                self.FC = self.CubeRot[:, :, 0]
            case "B":
                clockwise = not clockwise
                self.FC = self.CubeRot[:, :, 2]

        # Rotate the slice (FC) either clockwise or counter-clockwise
        if not clockwise:
            self.FC = np.rot90(self.FC, 1, (0, 1))
        else:
            self.FC = np.rot90(self.FC, 1, (1, 0))

        # Update the rotated slice back to the CubeRot
        match face:
            case "L":
                self.CubeRot[0, :, :] = self.FC
                for i in self.CubeRot[0, :, :]:  # Iterate over 2D slice
                    for piece in i:
                        piece.movePiece(clockwise, face)
            case "R":
                self.CubeRot[2, :, :] = self.FC
                for i in self.CubeRot[2, :, :]:  # Iterate over 2D slice
                    for piece in i:
                        piece.movePiece(clockwise, face)
            case "U":
                self.CubeRot[:, 0, :] = self.FC
                for i in self.CubeRot[:, 0, :]:  # Iterate over 2D slice
                    for piece in i:
                        piece.movePiece(clockwise, face)
            case "D":
                self.CubeRot[:, 2, :] = self.FC
                for i in self.CubeRot[:, 2, :]:  # Iterate over 2D slice
                    for piece in i:
                        piece.movePiece(clockwise, face)
            case "F":
                self.CubeRot[:, :, 0] = self.FC
                for i in self.CubeRot[:, :, 0]:  # Iterate over 2D slice
                    for piece in i:
                        piece.movePiece(clockwise, face)
            case "B":
                self.CubeRot[:, :, 2] = self.FC
                for i in self.CubeRot[:, :, 2]:  # Iterate over 2D slice
                    for piece in i:
                        piece.movePiece(clockwise, face)

        self.cube = self.CubeRot

    def print_Cube(self):
        for z in range(3):
            for y in range(3):
                print([self.cube[x, y, z].colors for x in range(3)])
            print()

    def print_piece(self, piece):
        print(self.cube[piece[0], piece[1], piece[2]].colors)
    
    def Scramble_Read(self,scramble):
        for i in scramble:
            self.move(i)


def solve_cube(cube):
    """
    Solves the Rubik's Cube using a breadth-first search (BFS) approach with a full goal state.
    """
    # Define the full goal state for all cube pieces
    goal_state = {
    (0, 0, 0):{"Left":"R","Up":"Y","Front":"G"},
    (0, 0, 1):{"Left":"R","Up":"Y"},
    (0, 0, 2):{"Left": "R", "Up": "Y", "Back": "B"},
    (0, 1, 0):{"Left": "R", "Front": "G"},
    (0, 1, 1):{"Left": "R"},
    (0, 1, 2):{"Left": "R", "Back": "B"},
    (0, 2, 0):{"Left": "R", "Down": "W", "Front": "G"},
    (0, 2, 1):{"Left": "R", "Down": "W"},
    (0, 2, 2):{"Left": "R", "Down": "W", "Back": "B"},
    (1, 0, 0):{"Up": "Y", "Front": "G"},
    (1, 0, 1):{"Up": "Y"},
    (1, 0, 2):{"Up": "Y", "Back": "B"},
    (1, 1, 0):{"Front": "G"},
    (1, 1, 2):{"Back": "B"},
    (1, 2, 0):{"Down": "W", "Front": "G"},
    (1, 2, 1):{"Down": "W"},
    (1, 2, 2):{"Down": "W", "Back": "B"},
    (2, 0, 0):{"Right": "O", "Up": "Y", "Front": "G"},
    (2, 0, 1):{"Right": "O", "Up": "Y"},
    (2, 0, 2):{"Right": "O", "Up": "Y", "Back": "B"},
    (2, 1, 0):{"Right": "O", "Front": "G"},
    (2, 1, 1):{"Right": "O"},
    (2, 1, 2):{"Right": "O", "Back": "B"},
    (2, 2, 0):{"Right": "O", "Down": "W", "Front": "G"},
    (2, 2, 1):{"Right": "O", "Down": "W"},
    (2, 2, 2):{"Right": "O", "Down": "W", "Back": "B"},
}

    queue = collections.deque([(cube, [])])  # Store cube state and moves
    visited = set()  # Set to track visited states

    while queue: # as long as there are elements in the queue
        current_cube, moves = queue.popleft()
        print(len(moves))
        MAXDEPTH = 20
       


        if matches_goal_state(current_cube, goal_state):
            return moves
        
        if len(moves) > MAXDEPTH:
            print("dddddddddddddddddddddddddddddddddddddddddddddd")
            break

        for face in ["U", "D", "L", "R", "F", "B"]:
            for clockwise in [False,True]:

                new_cube = copy.deepcopy(current_cube)
                new_cube.move(face, clockwise)

                state_tuple = encode_cube(new_cube)

                if state_tuple not in visited:
                    queue.append((new_cube, moves + [(face, clockwise)]))
                    visited.add(state_tuple)

    return "kms"


def matches_goal_state(cube, goal_state):
    for position, target_colors in goal_state.items():
        current_colors = cube.cube[position[0], position[1], position[2]].colors
        if current_colors != target_colors:
            return False
    return True


def encode_cube(cube):
    encoded = []
    for x in range(3):
        for y in range(3):
            for z in range(3):
                piece = cube.cube[x, y, z]
                encoded.append(tuple(sorted(piece.colors.items())))
    return tuple(encoded)



if __name__ == "__main__":
    cube = Cube()
    cube.print_Cube()
    cube.move("R")
    cube.move("U")
    cube.move("F")
    cube.move("B")
    cube.move("D",False)

    
    print("Solving the cube...")
    solution = solve_cube(cube)
    print("yo")
    print("Solution:", solution)
    end = time.perf_counter()
    print(end-start)

import collections
import copy
import time
import Cube


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
        print(queue)

        current_cube, moves = queue.popleft()
        print(current_cube, moves)
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
        

    return "Blank"


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
    cube = Cube.Cube()
    cube.print_Cube()
    print("Please input moves spaced apart")
    x = input()
    cube.Scramble_Read(x.upper())
    start = time.perf_counter()

    
    print("Solving the cube...")
    solution = solve_cube(cube)
    print("")
    print("Solution:", solution)
    end = time.perf_counter()
    print(end-start)

import numpy as np
import Piece
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
                    self.cube[x, y, z] = Piece.Piece(colors)

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
        scramble =scramble.split()
        moves = {
            "R": lambda:self.move("R"),
            "R2": lambda: [self.move("R") for i in range(2)],
            "R'": lambda:self.move("R",False),
            "L": lambda:self.move("L"),
            "L2": lambda: [self.move("L") for i in range(2)],
            "L'": lambda:self.move("L",False),
            "U": lambda:self.move("U"),
            "U2": lambda: [self.move("U") for i in range(2)],
            "U'": lambda:self.move("U",False),
            "D": lambda:self.move("D"),
            "D2": lambda: [self.move("D") for i in range(2)],
            "D'": lambda:self.move("D",False),
            "F": lambda:self.move("F"),
            "F2": lambda: [self.move("F") for i in range(2)],
            "F'": lambda:self.move("F",False),
            "B": lambda:self.move("B"),
            "B2": lambda: [self.move("B") for i in range(2)],
            "B'": lambda:self.move("B",False),
            
        }
        for i in scramble: 
            moves[i]()
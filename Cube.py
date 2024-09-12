import numpy as np


class Piece:
    def __init__(self, colors) -> None:
        self.colors = colors


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
                            colors["L"] = "R"
                        case 2:
                            colors["R"] = "O"
                    match y:  # Top and bottom
                        case 0:
                            colors["U"] = "Y"
                        case 2:
                            colors["D"] = "W"
                    match z:  # front and back
                        case 0:
                            colors["F"] = "G"
                        case 2:
                            colors["B"] = "B"
                    self.cube[x, y, z] = Piece(colors)

    def Lmove(self, clockwise=False):
        self.CubeRotL = np.copy(self.cube)
        self.FC = self.CubeRotL[0, :, :]
        if not clockwise:
            self.FC = np.rot90(self.FC, 1, (0, 1))
        else:
            self.FC = np.rot90(self.FC, 1, (1, 0))
        self.CubeRotL[0, :, :] = self.FC
        self.cube = self.CubeRotL

    def print_Cube(self):
        for z in range(3):
            for y in range(3):
                print([self.cube[x, y, z].colors for x in range(3)])
            print()


if __name__ == "__main__":
    cube = Cube()
    cube.print_Cube()
    print("L")
    cube.Lmove()
    cube.print_Cube()

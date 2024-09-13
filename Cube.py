import numpy as np


class Piece:
    def __init__(self, colors) -> None:
        self.colors = colors
    def movePiece(self,clockwise):
        print(self.colors)
        pass


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

    def move(self,face,clockwise = False):
        self. CubeRot = np.copy(self.cube)
        match face:
            case "L":
                self.FC = self.CubeRot[0, :, :]
            case "R":
                self.FC = self.CubeRot[2, :, :]
            case "U":
                self.FC = self.CubeRot[:,0,:]
            case "D":
                self.FC = self.CubeRot[:,2,:]
            case "F":
                self.FC = self.CubeRot[:,:,0]
            case "B":
                self.FC = self.CubeRot[:,:,2]
        if not clockwise:
            self.FC = np.rot90(self.FC, 1, (1,0))
        else:
            self.FC = np.rot90(self.FC, 1, (0,1))
        match face:
            case "L":
                self.CubeRot[0, :, :] = self.FC
                for i in self.CubeRot[0]:
                    for piece in i:
                        piece.movePiece(clockwise)
            case "R":
                self.CubeRot[2, :, :] = self.FC
            case "U":
                self.CubeRot[:,0,:]=self.FC 
            case "D":
                self.CubeRot[:,2,:]=self.FC
            case "F":
                self.CubeRot[:,:,0] = self.FC
            case "B":
                self.CubeRot[:,:,2] = self.FC
        self.cube = self.CubeRot
    def print_Cube(self):
        for z in range(3):
            for y in range(3):
                print([self.cube[x, y, z].colors for x in range(3)])
            print()


if __name__ == "__main__":
    cube = Cube()
    cube.print_Cube()
    cube.move("L",True)
    cube.print_Cube()

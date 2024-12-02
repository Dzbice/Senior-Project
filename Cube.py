import numpy as np
import collections


class Piece:
    def __init__(self, colors) -> None:
        self.colors = colors
    def movePiece(self, clockwise,face):
        '''sides = list(self.colors.keys())
        colors = list(self.colors.values())
        print(sides)
        match face: 
            case "U":
                if clockwise: 
                    for i in range(len(sides)):
                        if sides[i] == "Front":
                            sides[i] = "Left"
                        elif sides[i] == "Right":
                            sides[i] = "Front"
                        elif sides[i] == "Back":
                            sides[i] = "Right"
                        elif sides[i] == "Left":
                            sides[i] = "Right"
        self.colors = dict(zip(sides,colors))
        print(self.colors)'''
        sides = {
            "U": ["F", "R", "B", "L"],
            "D": ["F", "L", "B", "R"],
            "R": ["F", "U", "B", "D"],
            "L":["F", "D", "B", "U"],
            "F": ["U","R","D","L"],
            "B": ["U","R","D","L"]
        }
        colors = list(self.colors.values())
        facesides = sides[face]
        if clockwise: 
            print("we",facesides[1:], facesides[0:1])
            facesides = facesides[1:] + facesides[0:1]
        else:
            facesides = facesides[-1:-2] + facesides[0:2]
        self.colors = dict(zip(sides,colors))
        print(self.colors)
             
                        
             
                        


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
                            colors["Left"] = "R"
                        case 2:
                            colors["Right"] = "O"
                            colors["Right"] = "O"
                    match y:  # Top and bottom
                        case 0:
                            colors["Up"] = "Y"
                            colors["Up"] = "Y"
                        case 2:
                            colors["Down"] = "W"
                            colors["Down"] = "W"
                    match z:  # front and back
                        case 0:
                            colors["Front"] = "G"
                            colors["Front"] = "G"
                        case 2:
                            colors["Back"] = "B"
                            colors["Back"] = "B"
                    self.cube[x, y, z] = Piece(colors)

    def move(self,face,clockwise = True):
        self. CubeRot = np.copy(self.cube)
        match face:
            case "L":
                clockwise = False
                clockwise = False
                self.FC = self.CubeRot[0, :, :]
            case "R":
                self.FC = self.CubeRot[2, :, :]
            case "U":
                self.FC = self.CubeRot[:,0,:]
            case "D":
                clockwise = False
                clockwise = False
                self.FC = self.CubeRot[:,2,:]
            case "F":
                self.FC = self.CubeRot[:,:,0]
            case "B":
                clockwise = False
                clockwise = False
                self.FC = self.CubeRot[:,:,2]
        if not clockwise:
            self.FC = np.rot90(self.FC, 1, (0,1))
        else:
            self.FC = np.rot90(self.FC, 1, (1,0))
            
        match face:
            case "L":
                self.CubeRot[0, :, :] = self.FC
                for i in self.CubeRot[0]:
                    for piece in i:
                        piece.movePiece(clockwise,face)
            case "R":
                self.CubeRot[2, :, :] = self.FC
                for i in self.CubeRot[2]:
                    for piece in i:
                        piece.movePiece(clockwise,face)
            case "U":
                self.CubeRot[:,0,:]=self.FC 
                for i in self.CubeRot[:,0,:]:
                    for piece in i:
                        piece.movePiece(clockwise,face)
                for i in self.CubeRot[:,0,:]:
                    for piece in i:
                        piece.movePiece(clockwise,face)
            case "D":
                self.CubeRot[:,2,:]=self.FC
                for i in self.CubeRot[:,2:,]:
                    for piece in i:
                        piece.movePiece(clockwise,face)
            case "F":
                self.CubeRot[:,:,0] = self.FC
                for i in self.CubeRot[:,:,0]:
                    for piece in i:
                        piece.movePiece(clockwise,face)
            case "B":
                self.CubeRot[:,:,2] = self.FC
                for i in self.CubeRot[:,:,0]:
                    for piece in i:
                        piece.movePiece(clockwise,face)
        self.cube = self.CubeRot
    def print_Cube(self):
        for z in range(3):
            for y in range(3):
                print([self.cube[x, y, z].colors for x in range(3)])
            print()
    def print_piece(self,piece):
        print(self.cube[piece[0],piece[1],piece[2]].colors)


if __name__ == "__main__":
    cube = Cube()
    cube.print_Cube()
    print("space")
    cube.move("U",True)
    print("space")
    cube.move("U",True)
    cube.print_Cube()
    print("space")
    cube.print_piece([1,2,2])

    print("space")
    cube.print_piece([1,2,2])


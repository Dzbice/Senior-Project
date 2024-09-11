import numpy as np
class Piece():
    def __init__(self,colors) -> None:
        self.colors = colors


class Cube():
    def __init__(self) -> None:
        self.cube = np.empty((3,3,3),dtype=object)
        self.make_cube()
    
    
    def make_cube(self):
        for y in range(3):
            for x in range(3):
                for z in range(3):
                    colors = {}
                    match x:  # Left and Right sides
                        case 0:
                            colors['L'] = 'R'
                        case 2: 
                            colors['R'] = 'O'
                    match y: # Top and bottom
                        case 0: 
                            colors['U'] = 'Y'
                        case 2: 
                            colors['D'] = 'W'
                    match z: # front and back 
                        case 0:
                            colors['F'] = 'G'
                        case 2: 
                            colors['B'] = 'B'
                    self.cube[x,y,z] = Piece(colors)
    def print_Cube(self):
        for z in range(3):
            for x in range(3):
                print([self.cube[x,y,z ].colors for y in range(3)])
            print()

if __name__== '__main__':
    cube = Cube()
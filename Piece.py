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
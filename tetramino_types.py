from tetramino import Tetramino
from essentials import Position, block_side

class LBlock(Tetramino):
    def __init__(self):
        super().__init__()
        self.cells = {
            0: [Position(0,1 * block_side), Position(1 * block_side,1 * block_side), Position(2 * block_side,1 * block_side), Position(2 * block_side,0)],
            1: [Position(1 * block_side,0), Position(1 * block_side,1 * block_side), Position(1 * block_side,2 * block_side), Position(2 * block_side,2 * block_side)],
            2: [Position(0,1 * block_side), Position(1 * block_side,1 * block_side), Position(2 * block_side,1 * block_side), Position(0,2 * block_side)],
            3: [Position(0,0), Position(1 * block_side,0), Position(1 * block_side,1 * block_side), Position(1 * block_side,2 * block_side)]
        }
        self.move(28, -24)

class JBlock(Tetramino):
    def __init__(self):
        super().__init__()
        self.cells = {
            0: [Position(0,0), Position(0,1 * block_side), Position(1 * block_side,1 * block_side), Position(2 * block_side,1 * block_side)],
            1: [Position(1 * block_side,0), Position(1 * block_side,1 * block_side), Position(1 * block_side,2 * block_side), Position(2 * block_side,0)],
            2: [Position(0,1 * block_side), Position(1 * block_side,1 * block_side), Position(2 * block_side,1 * block_side), Position(2 * block_side,2 * block_side)],
            3: [Position(0,2 * block_side), Position(1 * block_side,0), Position(1 * block_side,1 * block_side), Position(1 * block_side,2 * block_side)]
        }
        self.move(28,-24)

class IBlock(Tetramino):
    def __init__(self):
        super().__init__()
        self.cells = {
            0: [Position(0,1 * block_side), Position(1 * block_side,1 * block_side), Position(2 * block_side,1 * block_side), Position(3 * block_side,1 * block_side)],
            1: [Position(2 * block_side,0), Position(2 * block_side,1 * block_side), Position(2 * block_side,2 * block_side), Position(2 * block_side,3 * block_side)],
            2: [Position(0,2 * block_side), Position(1 * block_side,2 * block_side), Position(2 * block_side,2 * block_side), Position(3 * block_side,2 * block_side)],
            3: [Position(1 * block_side,0), Position(1 * block_side,1 * block_side), Position(1 * block_side,2 * block_side), Position(1 * block_side,3 * block_side)],
        }
        self.move(24, -32)

class OBlock(Tetramino):
    def __init__(self):
        super().__init__()
        self.cells = {
            0: [Position(0,0), Position(0,1 * block_side), Position(1 * block_side,0), Position(1 * block_side,1 * block_side)],
            1: [Position(0,0), Position(0,1 * block_side), Position(1 * block_side,0), Position(1 * block_side,1 * block_side)],
            2: [Position(0,0), Position(0,1 * block_side), Position(1 * block_side,0), Position(1 * block_side,1 * block_side)],
            3: [Position(0,0), Position(0,1 * block_side), Position(1 * block_side,0), Position(1 * block_side,1 * block_side)],
        }
        self.move(32,-16)

class SBlock(Tetramino):
    def __init__(self):
        super().__init__()
        self.cells = {
            0: [Position(1 * block_side,0), Position(2 * block_side,0), Position(0,1 * block_side), Position(1 * block_side,1 * block_side)],
            1: [Position(1 * block_side,0), Position(1 * block_side,1 * block_side), Position(2 * block_side,1 * block_side), Position(2 * block_side,2 * block_side)],
            2: [Position(1 * block_side,1 * block_side), Position(2 * block_side,1 * block_side), Position(0,2 * block_side), Position(1 * block_side,2 * block_side)],
            3: [Position(0,0), Position(0,1 * block_side), Position(1 * block_side,1 * block_side), Position(1 * block_side,2 * block_side)],
        }
        self.move(28,-24)

class ZBlock(Tetramino):
    def __init__(self):
        super().__init__()
        self.cells = {
            0: [Position(0,0), Position(1 * block_side,0), Position(1 * block_side,1 * block_side), Position(2 * block_side,1 * block_side)],
            1: [Position(2 * block_side,0), Position(1 * block_side,1 * block_side), Position(2 * block_side,1 * block_side), Position(1 * block_side,2 * block_side)],
            2: [Position(0,1 * block_side), Position(1 * block_side,1 * block_side), Position(1 * block_side,2 * block_side), Position(2 * block_side,2 * block_side)],
            3: [Position(1 * block_side,0), Position(0,1 * block_side), Position(1 * block_side,1 * block_side), Position(0,2 * block_side)],
        }
        self.move(28,-24)

class TBlock(Tetramino):
    def __init__(self, ):
        super().__init__()
        self.cells = {
            0: [Position(1 * block_side,0), Position(0,1 * block_side), Position(1 * block_side,1 * block_side), Position(1 * block_side,2 * block_side)],
            1: [Position(1 * block_side,0), Position(0,1 * block_side), Position(1 * block_side,1 * block_side), Position(2 * block_side,1 * block_side)],
            2: [Position(1 * block_side,0), Position(1 * block_side,1 * block_side), Position(2 * block_side,1 * block_side), Position(1 * block_side,2 * block_side)],
            3: [Position(0,1 * block_side), Position(1 * block_side,1 * block_side), Position(2 * block_side,1 * block_side), Position(1 * block_side,2 * block_side)],
        }
        self.move(28,-24)
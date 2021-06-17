from models import Board

class Data:
    
    def __init__(self):
        self.boards=list()

    def addData(self, title, content):
        board = Board()
        board.id = len(self.boards) + 1
        board.title = title
        board.content = content
        self.boards.append(board)

    def getData(self):
        return self.boards
    

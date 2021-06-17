class Board:
    def __init__(self) :
        self.id = 0
        self.title = ''
        self.content = ''

    def __str__(self):
        return "id:{}\ntitle:{}\ncontent:{}".format(self.id, self.title, self.content)

class User:
    def __init__(self) :
        self.id = 0
        self.name = ''
        
    def __repr__(self) :
        return self.name
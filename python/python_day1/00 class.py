


class Player():

    type = "player"

    def __init__(self, id, name, email):
        self.id = id
        self.name = name
        self.__email = email # private var

    def print_name(self):
        print(self.name)




class FreePlayer(Player):

    type = "free_player"

    def __init__(self, id, name, email, premium):
        Player.__init__(self, id, name, email)
        self.premium = premium

    def print_name(self):
        print(self.name)
    
    def is_premium(self):
        return self.premium
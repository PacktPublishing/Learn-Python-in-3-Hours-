class Chess:

    def __init__(self, player_one, player_two):
        self.player_one = player_one
        self.player_two = player_two
        self.winner = None

    def checkmate(self, winner):
        self.winner = winner
        return self.winner

    @staticmethod
    def print_game_header():
        print('GAME START: CHESS.')

    @classmethod
    def print_game_name(cls):
        print('Chess')


game1 = Chess()
game1.print_game_header()


class Car:

    def __init__(self, brand):
        self.top_speed = 0.0

    def go(self):
        print('VRRROOOM')


class SuperCar(Car):

    def name(self):
        return 'Super Car'


class ElecticCar(Car):

    def name(self):
        return 'Electric Car'

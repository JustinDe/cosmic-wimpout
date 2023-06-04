from random import randint

class Regular_Die():
    def __init__(self, roll):
        self.roll = roll
        self.output = ''

        if self.roll == 0:
            self.output = '10'
        elif self.roll == 1:
            self.output = '5'
        elif self.roll == 2:
            self.output = '2 shooting stars'
        elif self.roll == 3:
            self.outut = '3 triangles'
        elif self.roll == 4:
            self.output = '4 diamonds'
        elif self.roll == 5:
            self.output = '6 stars'
        else:
            raise Exception(f'Invalid roll submitted to Regular_Die {self.roll=}')

def regular_roll(dice: int):
    rolls = []
    for die in range(0,dice):
        rolls.append(randint(0, 5))
    return rolls


def special_die():
    die = randint(0, 5)
    return die

def game_loop():
    win_condition = False
    while True:
        if win_condition == True:
            break
        print(f'{str(regular_roll(4))=}')
        print(f'{special_die()=}')



if __name__ == '__main__':
    game_loop()

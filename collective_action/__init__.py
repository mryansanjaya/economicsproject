from otree.api import *




doc = """
Instruction.
"""


class C(BaseConstants):
    NAME_IN_URL = 'collective_action'
    PLAYERS_PER_GROUP = 2
    NUM_ROUNDS = 1
    ENDOWMENT = cu(100)
    MULTIPLIER = 1.8


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass


class Player(BasePlayer):
    username = models.StringField(label="Nama pengguna")
    password = models.StringField(label="Kata sandi")


# FUNCTIONS
def set_payoffs(group: Group):
    players = group.get_players()
    group.total_requests = sum([p.request for p in players])
    if group.total_requests <= C.AMOUNT_SHARED:
        for p in players:
            p.payoff = p.request
    else:
        for p in players:
            p.payoff = cu(0)


def other_player(player: Player):
    return player.get_others_in_group()[0]


# PAGES
class Login(Page):
    form_model = 'player'
    form_fields = ['username', 'password']

    def is_displayed(self):
        return True


class Panduan(Page):
    def is_displayed(self):
        return True

class Cognitivetest(Page):
    def Soal_Satu(a, b, c):
        user_answer = int(input(f'{a} x {b} + {c} ='))
        if user_answer == ((a * b) + c):
            print(round(user_answer))
            return (False)
        else:
            print("salah")
            return (True)

    def Soal_Dua(a, b, c):
        user_answer = int(input(f'{a} x {b} - {c} ='))
        if user_answer == ((a * b) - c):
            print(round(user_answer))
            return (False)
        else:
            print("salah")
            return (True)

    def Soal_Tiga(a, b, c):
        user_answer = int(input(f'{a} : {b} + {c} ='))
        if user_answer == ((a / b) + c):
            print(round(user_answer))
            return (False)
        else:
            print("salah")
            return (True)

    def Soal_empat(a, b, c):
        user_answer = int(input(f'{a} : {b} - {c} ='))
        if user_answer == ((a / b) - c):
            print(round(user_answer))
            return (False)
        else:
            print("salah")
            return (True)

    def genRandom():
        a = random.randint(1, 100)
        b = random.randint(1, 10)
        c = random.randint(1, 5)
        return a, b, c

    Questions = [Soal_Satu, Soal_Dua, Soal_Tiga, Soal_empat]

    isContinue = True
    while isContinue <= 2:
        a, b, c = genRandom()
        isContinue = Questions[random.randint(0, 3)](a, b, c)
        isContinue += 1

    def is_displayed(self):
        return True

page_sequence = [Login, Panduan, Cognitivetest]

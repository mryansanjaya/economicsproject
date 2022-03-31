from otree.api import (
    models,
    BaseConstants,
    BaseSubsession,
    BaseGroup,
    BasePlayer,
    Currency as cu
)

doc = """
Collective Action
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

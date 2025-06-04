
from otree.api import *
c = cu

doc = 'Last page'
class C(BaseConstants):
    NAME_IN_URL = 'Thank_All'
    PLAYERS_PER_GROUP = None
    NUM_ROUNDS = 1
class Subsession(BaseSubsession):
    pass
class Group(BaseGroup):
    pass
class Player(BasePlayer):
    pass
class Thanks(Page):
    form_model = 'player'
page_sequence = [Thanks]
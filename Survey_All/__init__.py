
from otree.api import *
c = cu

doc = ''
class C(BaseConstants):
    NAME_IN_URL = 'Survey_All'
    PLAYERS_PER_GROUP = None
    NUM_ROUNDS = 1
    SHOWUP_FEE = cu(5)
class Subsession(BaseSubsession):
    pass
class Group(BaseGroup):
    pass
def set_payoffs(group: Group):
    for player in group.get_players():
        player.payoff = C.SHOWUP_FEE
        player.participant.vars["clerpay_amount"] = float(player.participant.payoff) ## for Max
class Player(BasePlayer):
    Satisfaction_with_democracy = models.StringField(choices=[['sehr zufrieden', 'sehr zufrieden'], ['zufrieden', 'eher zufrieden'], ['unzufrieden', 'eher unzufrieden'], ['sehr unzufrieden', 'sehr unzufrieden']], label='Wie zufrieden sind Sie insgesamt mit der Art und Weise, wie die Entscheidungen in diesem Experiment getroffen wurden?')
    Democratic_governance = models.IntegerField(choices=[[10, '10  (Vollkommen demokratisch)'], [9, '9'], [8, '8'], [7, '7'], [6, '6'], [5, '5'], [4, '4'], [3, '3'], [2, '2'], [1, '1  (Überhaupt nicht demokratisch)']], label='Wie demokratisch würden Sie den Entscheidungsprozess in diesem Experiment beschreiben?')
    Personal_outcome = models.StringField(choices=[['sehr zufrieden', 'sehr zufrieden'], ['zufrieden', 'eher zufrieden'], ['unzufrieden', 'eher unzufrieden'], ['sehr unzufrieden', 'sehr unzufrieden']], label='Wie zufrieden sind Sie mit Ihrem persönlichen Ergebnis in diesem Experiment?')
    Representation = models.StringField(choices=[['Sehr stark', 'Sehr stark'], ['Eher stark', 'Eher stark'], ['Kaum', 'Kaum'], ['Gar nicht', 'Gar nicht']], label='Inwieweit fühlen Sie, dass Ihre Präferenzen im Entscheidungsprozess dieses Experiments berücksichtigt wurden?')
    Fairness = models.StringField(choices=[['Very fair', 'sehr fair'], ['Fair', 'eher fair'], ['Unfair', 'eher unfair'], ['Very unfair', 'Sehr unfair']], label='Wie fair empfanden Sie den Entscheidungsprozess in diesem Experiment?')
    Gender = models.StringField(choices=[['Weiblich', 'Weiblich'], ['Männlich', 'Männlich'], ['Divers', 'Divers'], ['Keine Angabe', 'Keine Angabe']], label='Was ist Ihr Geschlecht?', widget=widgets.RadioSelect)
    Comments = models.LongStringField(blank=True, label='Comments')
class Payoff_calculation(WaitPage):
    after_all_players_arrive = set_payoffs
class Satisfaction(Page):
    form_model = 'player'
    form_fields = ['Satisfaction_with_democracy', 'Democratic_governance', 'Personal_outcome', 'Representation', 'Gender', 'Comments']
    @staticmethod
    def before_next_page(player: Player, timeout_happened):
        pass
page_sequence = [Payoff_calculation, Satisfaction]
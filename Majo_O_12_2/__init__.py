
from otree.api import *
c = cu

doc = 'Majo_12_2Pl'
class C(BaseConstants):
    NAME_IN_URL = 'Majo_O_12_2'
    PLAYERS_PER_GROUP = None
    NUM_ROUNDS = 20
    SHOWUP_FEE = cu(5)
    CANDIDATE_A_ROLE = 'A'
    CANDIDATE_B_ROLE = 'B'
    VOTER_1_ROLE = '1'
    VOTER_2_ROLE = '2'
    VOTER_3_ROLE = '3'
    VOTER_4_ROLE = '4'
    VOTER_5_ROLE = '5'
    VOTER_6_ROLE = '6'
    VOTER_7_ROLE = '7'
    VOTER_8_ROLE = '8'
    VOTER_9_ROLE = '9'
    VOTER_10_ROLE = '10'
    VOTER_11_ROLE = '11'
    VOTER_12_ROLE = '12'
    BONUS = cu(1.2)
    BUDGET = cu(7.2)
class Subsession(BaseSubsession):
    pass
class Group(BaseGroup):
    winner = models.StringField()
def determine_winner_and_payoffs(group: Group):
    # For random winner selection
    import random
    
    # Determine Winner in Majo 2
    # Voters start with id 3
    
    votes = [
        group.get_player_by_id(3).vote_for,
        group.get_player_by_id(4).vote_for,
        group.get_player_by_id(5).vote_for,
        group.get_player_by_id(6).vote_for,
        group.get_player_by_id(7).vote_for,
        group.get_player_by_id(8).vote_for,
        group.get_player_by_id(9).vote_for,
        group.get_player_by_id(10).vote_for,
        group.get_player_by_id(11).vote_for,
        group.get_player_by_id(12).vote_for,
        group.get_player_by_id(13).vote_for,
        group.get_player_by_id(14).vote_for
    ]
    
    votes_for_A = votes.count("A")
    votes_for_B = votes.count("B")
    
    # Determine the winner with random tie break
    if votes_for_A > votes_for_B: 
        group.winner = "A"  # A wins
    elif votes_for_A < votes_for_B: 
        group.winner = "B"  # B wins
    else:
        # Randomly choose the winner in case of a tie
        group.winner = random.choice(["A", "B"])
    
    # Determine payoffs    
    candidate_A = group.get_player_by_id(1)
    candidate_B = group.get_player_by_id(2)
    
    # Total voters selected by the candidates
    # Here voters start with v01
    
    total_voters_by_A = sum([
        candidate_A.v01,
        candidate_A.v02,
        candidate_A.v03,
        candidate_A.v04,
        candidate_A.v05,
        candidate_A.v06,
        candidate_A.v07,
        candidate_A.v08,
        candidate_A.v09,  
        candidate_A.v10, 
        candidate_A.v11, 
        candidate_A.v12   
    ])
    total_voters_by_B = sum([
        candidate_B.v01,
        candidate_B.v02,
        candidate_B.v03,
        candidate_B.v04,
        candidate_B.v05,
        candidate_B.v06,
        candidate_B.v07,
        candidate_B.v08,
        candidate_B.v09,  
        candidate_B.v10,  
        candidate_B.v11,  
        candidate_B.v12  
    ])
    
    amount_per_voter_A = 0 # To be sure, set to zero, actually not needed
    amount_per_voter_B = 0
    
    if total_voters_by_A > 0:
        amount_per_voter_A = C.BUDGET / total_voters_by_A   ### RECENT CHANGE: 7.20 --> C.BUDGET
    if total_voters_by_B > 0:
        amount_per_voter_B = C.BUDGET / total_voters_by_B   ### RECENT CHANGE: 7.20 --> C.BUDGET
    
    voter_1 = group.get_player_by_id(3)
    voter_2 = group.get_player_by_id(4)
    voter_3 = group.get_player_by_id(5)
    voter_4 = group.get_player_by_id(6)
    voter_5 = group.get_player_by_id(7)
    voter_6 = group.get_player_by_id(8)
    voter_7 = group.get_player_by_id(9)
    voter_8 = group.get_player_by_id(10)
    voter_9 = group.get_player_by_id(11)  
    voter_10 = group.get_player_by_id(12) 
    voter_11 = group.get_player_by_id(13) 
    voter_12 = group.get_player_by_id(14)
    
    if group.winner == "A":
        voter_1.payoff = amount_per_voter_A * candidate_A.v01
        voter_2.payoff = amount_per_voter_A * candidate_A.v02
        voter_3.payoff = amount_per_voter_A * candidate_A.v03
        voter_4.payoff = amount_per_voter_A * candidate_A.v04
        voter_5.payoff = amount_per_voter_A * candidate_A.v05
        voter_6.payoff = amount_per_voter_A * candidate_A.v06
        voter_7.payoff = amount_per_voter_A * candidate_A.v07
        voter_8.payoff = amount_per_voter_A * candidate_A.v08
        voter_9.payoff = amount_per_voter_A * candidate_A.v09  
        voter_10.payoff = amount_per_voter_A * candidate_A.v10 
        voter_11.payoff = amount_per_voter_A * candidate_A.v11 
        voter_12.payoff = amount_per_voter_A * candidate_A.v12 
        candidate_A.payoff = C.BONUS   ### RECENT CHANGE: 1.2 --> C.BONUS
        candidate_B.payoff = 0 
    else: 
        voter_1.payoff = amount_per_voter_B * candidate_B.v01
        voter_2.payoff = amount_per_voter_B * candidate_B.v02
        voter_3.payoff = amount_per_voter_B * candidate_B.v03
        voter_4.payoff = amount_per_voter_B * candidate_B.v04
        voter_5.payoff = amount_per_voter_B * candidate_B.v05
        voter_6.payoff = amount_per_voter_B * candidate_B.v06
        voter_7.payoff = amount_per_voter_B * candidate_B.v07
        voter_8.payoff = amount_per_voter_B * candidate_B.v08   
        voter_9.payoff = amount_per_voter_B * candidate_B.v09  
        voter_10.payoff = amount_per_voter_B * candidate_B.v10 
        voter_11.payoff = amount_per_voter_B * candidate_B.v11 
        voter_12.payoff = amount_per_voter_B * candidate_B.v12 
        candidate_A.payoff = 0
        candidate_B.payoff = C.BONUS   ### RECENT CHANGE: 1.2 --> C.BONUS
    
    #Accumulated wealth
    for other_player in group.get_players():
        other_player.accumulated_wealth = other_player.accumulated_wealth + other_player.payoff   
    
class Player(BasePlayer):
    v01 = models.BooleanField(widget=widgets.RadioSelectHorizontal)
    v02 = models.BooleanField(widget=widgets.RadioSelectHorizontal)
    v03 = models.BooleanField(widget=widgets.RadioSelectHorizontal)
    v04 = models.BooleanField(widget=widgets.RadioSelectHorizontal)
    v05 = models.BooleanField(widget=widgets.RadioSelectHorizontal)
    v06 = models.BooleanField(widget=widgets.RadioSelectHorizontal)
    v07 = models.BooleanField(widget=widgets.RadioSelectHorizontal)
    v08 = models.BooleanField(widget=widgets.RadioSelectHorizontal)
    v09 = models.BooleanField(widget=widgets.RadioSelectHorizontal)
    v10 = models.BooleanField(widget=widgets.RadioSelectHorizontal)
    v11 = models.BooleanField(widget=widgets.RadioSelectHorizontal)
    v12 = models.BooleanField(widget=widgets.RadioSelectHorizontal)
    vote_for = models.StringField()
    accumulated_wealth = models.CurrencyField()
    is_dropout = models.BooleanField(initial=False)
def custom_export(players):
    yield ['participant_code', 'id_in_group']
    for p in players:
        pp = p.participant
        yield [pp.code, p.id_in_group]
class Welcome(Page):
    form_model = 'player'
    @staticmethod
    def is_displayed(player: Player):
        return player.round_number == 1
class RoundInfo(Page):
    form_model = 'player'
    timeout_seconds = 10
    @staticmethod
    def before_next_page(player: Player, timeout_happened):
        payoffs = [p.payoff for p in player.in_all_rounds()]
        player.accumulated_wealth = sum(payoffs)
class WaitForOthers(WaitPage):
    @staticmethod
    def is_displayed(player: Player):
        group = player.group
        return player.id_in_group < 15  # because Majo_2 has 14 palayers, 2+12.
class Campaigning(Page):
    form_model = 'player'
    form_fields = ['v01', 'v02', 'v03', 'v04', 'v05', 'v06', 'v07', 'v08', 'v09', 'v10', 'v11', 'v12']
    timeout_seconds = 120
    @staticmethod
    def is_displayed(player: Player):
        group = player.group
        return player.id_in_group < 3 # 2 Candidates in Majo_2
    @staticmethod
    def vars_for_template(player: Player):
        group = player.group
        voter_1 = group.get_player_by_id(3)
        voter_2 = group.get_player_by_id(4)
        voter_3 = group.get_player_by_id(5)
        voter_4 = group.get_player_by_id(6)   
        voter_5 = group.get_player_by_id(7)   
        voter_6 = group.get_player_by_id(8)   
        voter_7 = group.get_player_by_id(9)   
        voter_8 = group.get_player_by_id(10)   
        voter_9 = group.get_player_by_id(11)   
        voter_10 = group.get_player_by_id(12)  
        voter_11 = group.get_player_by_id(13)  
        voter_12 = group.get_player_by_id(14)  
        
        # To be sure, set accumulated wealth to zero in round 1
        if group.round_number == 1:
            voter_1.accumulated_wealth = 0
            voter_2.accumulated_wealth = 0
            voter_3.accumulated_wealth = 0
            voter_4.accumulated_wealth = 0
            voter_5.accumulated_wealth = 0
            voter_6.accumulated_wealth = 0
            voter_7.accumulated_wealth = 0
            voter_8.accumulated_wealth = 0
            voter_9.accumulated_wealth = 0     
            voter_10.accumulated_wealth = 0    
            voter_11.accumulated_wealth = 0    
            voter_12.accumulated_wealth = 0    
        
        # Return a dict
        return dict(
            # No calculations in the HTML page possible, therfore the budgets calculations
            budget1 = C.BUDGET,
            budget2 = C.BUDGET/2,
            budget3 = C.BUDGET/3,
            budget4 = C.BUDGET/4,
            budget5 = C.BUDGET/5,
            budget6 = C.BUDGET/6,
            budget7 = C.BUDGET/7,
            budget8 = C.BUDGET/8,
            budget9 = C.BUDGET/9,
            budget10 = C.BUDGET/10,
            budget11 = C.BUDGET/11,
            budget12 = C.BUDGET/12,
            # voters. Had issues when putting the voter calcuation into here. Therefore the "double step"
            voter_1=voter_1,    
            voter_2=voter_2,    
            voter_3=voter_3,    
            voter_4=voter_4,   
            voter_5=voter_5,    
            voter_6=voter_6,   
            voter_7=voter_7,   
            voter_8=voter_8,  
            voter_9=voter_9,
            voter_10=voter_10,
            voter_11=voter_11, 
            voter_12=voter_12 
        )
        
    @staticmethod
    def before_next_page(player: Player, timeout_happened):
        if timeout_happened:
            player.is_dropout = True
class WaitingForCandidates(WaitPage):
    body_text = 'Die Wahlprogamme werden erstellt.'
    @staticmethod
    def is_displayed(player: Player):
        group = player.group
        return player.id_in_group > 2 # 2 Candidates
class WaitingForTheOtherCandidate(WaitPage):
    body_text = 'Es sind noch nicht alle Wahlprogramme erstellt worden.'
    @staticmethod
    def is_displayed(player: Player):
        group = player.group
        return player.id_in_group < 3 # 2 candidates
class Voting(Page):
    form_model = 'player'
    form_fields = ['vote_for']
    timeout_seconds = 60
    @staticmethod
    def is_displayed(player: Player):
        group = player.group
        return player.id_in_group > 2 # Display to voters; 2 candidates!
    @staticmethod
    def vars_for_template(player: Player):
        group = player.group
        candidate_A = group.get_player_by_id(1)
        candidate_B = group.get_player_by_id(2)
        
        # Total number of voters selected by candidates
        total_voters_by_A = sum([
            candidate_A.v01,
            candidate_A.v02,
            candidate_A.v03,
            candidate_A.v04, 
            candidate_A.v05,
            candidate_A.v06,
            candidate_A.v07,
            candidate_A.v08,
            candidate_A.v09,
            candidate_A.v10,
            candidate_A.v11,
            candidate_A.v12
        ])
        
        total_voters_by_B = sum([
            candidate_B.v01,
            candidate_B.v02,
            candidate_B.v03,
            candidate_B.v04, 
            candidate_B.v05,
            candidate_B.v06,
            candidate_B.v07,
            candidate_B.v08,
            candidate_B.v09,
            candidate_B.v10,
            candidate_B.v11,
            candidate_B.v12
        ])
        
        #Amount offered per selected voter
        total_voters_rel_by_A = cu(0)
        if total_voters_by_A >0: 
            total_voters_rel_by_A = cu(round(C.BUDGET/total_voters_by_A,2)) # RECENTLY CHANGED: 7.2 --> c.budget
        total_voters_rel_by_B = cu(0)
        if total_voters_by_B >0:
            total_voters_rel_by_B = cu(round(C.BUDGET/total_voters_by_B,2)) # RECENTLY CHANGED: 7.2 --> c.budget
        
        return dict(
            candidate_A = candidate_A,
            candidate_B = candidate_B,
            voter_1 = group.get_player_by_id(3),
            voter_2 = group.get_player_by_id(4),
            voter_3 = group.get_player_by_id(5),
            voter_4 = group.get_player_by_id(6),
            voter_5 = group.get_player_by_id(7),
            voter_6 = group.get_player_by_id(8),
            voter_7 = group.get_player_by_id(9),
            voter_8 = group.get_player_by_id(10),
            voter_9 = group.get_player_by_id(11),
            voter_10 = group.get_player_by_id(12),
            voter_11 = group.get_player_by_id(13),
            voter_12 = group.get_player_by_id(14),
            total_voters_by_A = total_voters_by_A,
            total_voters_by_B = total_voters_by_B,
            total_voters_rel_by_A = total_voters_rel_by_A,
            total_voters_rel_by_B = total_voters_rel_by_B
        )    
    @staticmethod
    def before_next_page(player: Player, timeout_happened):
        if timeout_happened:
            player.is_dropout = True
            player.vote_for = "abstain"
class WaitingForVoters(WaitPage):
    after_all_players_arrive = determine_winner_and_payoffs
    body_text = 'Die Wählerinnen und Wähler geben ihre Stimme ab.'
    @staticmethod
    def is_displayed(player: Player):
        group = player.group
        return player.id_in_group > 0 # everything starts with 1 here!
class Outcome(Page):
    form_model = 'player'
    timeout_seconds = 60
    @staticmethod
    def vars_for_template(player: Player):
        group = player.group
        votes = [
            group.get_player_by_id(3).vote_for,
            group.get_player_by_id(4).vote_for,
            group.get_player_by_id(5).vote_for,
            group.get_player_by_id(6).vote_for,
            group.get_player_by_id(7).vote_for,
            group.get_player_by_id(8).vote_for,
            group.get_player_by_id(9).vote_for,
            group.get_player_by_id(10).vote_for,
            group.get_player_by_id(11).vote_for,
            group.get_player_by_id(12).vote_for,
            group.get_player_by_id(13).vote_for,
            group.get_player_by_id(14).vote_for
        ]
        
        votes_for_A = 0
        votes_for_B = 0
        votes_for_abstain = 0
        votes_for_A = votes.count("A")
        votes_for_B = votes.count("B")
        votes_for_abstain = votes.count("abstain")
        budget_A = 7.2   
        budget_B = 7.2    
        
        votes_rel_for_A = 0
        votes_rel_for_B = 0
        votes_rel_for_abstain = 0
        if votes_for_A + votes_for_B > 0:
            votes_rel_for_A = int((votes_for_A / (votes_for_A + votes_for_B)) * 100)
            votes_rel_for_B = int((votes_for_B / (votes_for_A + votes_for_B)) * 100)     
        
        candidate_A = group.get_player_by_id(1)
        candidate_B = group.get_player_by_id(2)
        
        total_voters_by_A = sum([
            candidate_A.v01,
            candidate_A.v02,
            candidate_A.v03,
            candidate_A.v04, 
            candidate_A.v05,
            candidate_A.v06,
            candidate_A.v07,
            candidate_A.v08,
            candidate_A.v09,
            candidate_A.v10,
            candidate_A.v11,
            candidate_A.v12
        ])
        total_voters_by_B = sum([
            candidate_B.v01,
            candidate_B.v02,
            candidate_B.v03,
            candidate_B.v04, 
            candidate_B.v05,
            candidate_B.v06,
            candidate_B.v07,
            candidate_B.v08,
            candidate_B.v09,
            candidate_B.v10,
            candidate_B.v11,
            candidate_B.v12
        ])
        
        budget_A_per_voter = 0
        if total_voters_by_A > 0: 
            budget_A_per_voter = round(budget_A / total_voters_by_A, 2) 
        budget_B_per_voter = 0
        if total_voters_by_B > 0:
            budget_B_per_voter = round(budget_B / total_voters_by_B, 2)
        
        return dict(
            votes_rel_for_A = votes_rel_for_A,
            votes_rel_for_B = votes_rel_for_B,
            votes_rel_for_abstain = votes_rel_for_abstain,    
            votes_for_A = votes_for_A,
            votes_for_B = votes_for_B,      
            votes_for_abstain = votes_for_abstain,    
            budget_A = budget_A,
            budget_B = budget_B,
            total_voters_by_A = total_voters_by_A, 
            total_voters_by_B = total_voters_by_B,
            budget_A_per_voter = budget_A_per_voter,
            budget_B_per_voter = budget_B_per_voter,
            candidate_A = candidate_A,
            candidate_B = candidate_B,
        
            # for wealth before voting
        voter_1_wealth_before_voting = group.get_player_by_id(3).accumulated_wealth - group.get_player_by_id(3).payoff,
        voter_2_wealth_before_voting = group.get_player_by_id(4).accumulated_wealth - group.get_player_by_id(4).payoff,
        voter_3_wealth_before_voting = group.get_player_by_id(5).accumulated_wealth - group.get_player_by_id(5).payoff,
        voter_4_wealth_before_voting = group.get_player_by_id(6).accumulated_wealth - group.get_player_by_id(6).payoff,
        voter_5_wealth_before_voting = group.get_player_by_id(7).accumulated_wealth - group.get_player_by_id(7).payoff,
        voter_6_wealth_before_voting = group.get_player_by_id(8).accumulated_wealth - group.get_player_by_id(8).payoff,
        voter_7_wealth_before_voting = group.get_player_by_id(9).accumulated_wealth - group.get_player_by_id(9).payoff,
        voter_8_wealth_before_voting = group.get_player_by_id(10).accumulated_wealth - group.get_player_by_id(10).payoff,
        voter_9_wealth_before_voting = group.get_player_by_id(11).accumulated_wealth - group.get_player_by_id(11).payoff,
        voter_10_wealth_before_voting = group.get_player_by_id(12).accumulated_wealth - group.get_player_by_id(12).payoff,
        voter_11_wealth_before_voting = group.get_player_by_id(13).accumulated_wealth - group.get_player_by_id(13).payoff,
        voter_12_wealth_before_voting = group.get_player_by_id(14).accumulated_wealth - group.get_player_by_id(14).payoff    
        
        )
        
page_sequence = [Welcome, RoundInfo, WaitForOthers, Campaigning, WaitingForCandidates, WaitingForTheOtherCandidate, Voting, WaitingForVoters, Outcome]
import Majo_O_12_2 as pages
from . import *
c = cu

class PlayerBot(Bot):
    def play_round(self):
        yield Welcome
        if self.player.id_in_group < 3:
            yield Campaigning, dict(
                v01=False,
                v02=False,
                v03=False,
                v04=False,
                v05=False,
                v06=False,
                v07=False,
                v08=False,
                v09=False,
                v10=False,
                v11=False,
                v12=False,
            )
        if self.player.id_in_group > 2:
            yield Voting, dict(vote_for="xyz")
        yield Outcome
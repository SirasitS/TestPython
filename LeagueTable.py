from collections import Counter
from collections import OrderedDict

class LeagueTable:
    def __init__(self, players):
        self.standings = OrderedDict([(player, Counter()) for player in players])
       
    def record_result(self, player, score):
        self.standings[player]['games_played'] += 1
        self.standings[player]['score'] += score        
      
    def player_rank(self, rank):
        if rank > len(self.standings):
            return None
        # print("length of self.standings =", len(self.standings))
        print("Current table scores =", self.standings)

        score_list = sorted({v['score'] for k,v in self.standings.items()}, reverse=True)
        print("scores =", score_list)
        print("score of rank {0} = {1}".format(rank, score_list[rank-1]))

        min_play =  min({v2['games_played'] for k2,v2 in self.standings.items()})
        print("min game play =", min_play)

        highest_player_score = {k:v['games_played'] for k,v in self.standings.items() if v['score'] == score_list[rank-1]}
        print("The top score player =", highest_player_score)
        soretd_game = sorted(highest_player_score, key=lambda x: highest_player_score[x], reverse=False)        # Still bug
        print("sort game play =", soretd_game)
        
        print("First player =", soretd_game[0])

        # if len(highest_player_score) >= 2:
        #     pass
        # return highest_player_score[0]

if __name__ == "__main__":
    table = LeagueTable(['Mike', 'Chris', 'Arnold'])
    table.record_result('Mike', 2)
    table.record_result('Mike', 1)
    table.record_result('Arnold', 5)
    table.record_result('Chris', 2)
    table.record_result('Chris', 3)
    print(table.player_rank(1))
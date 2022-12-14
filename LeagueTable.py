from collections import Counter
from collections import OrderedDict

class LeagueTable:
    def __init__(self, players):
        self.standings = OrderedDict([(player, Counter()) for player in players])
       
    def record_result(self, player, score):
        self.standings[player]['games_played'] += 1
        self.standings[player]['score'] += score        
      
    def player_rank(self, rank):
        scores = set()         # Create empty dict to collect the score
        least_game = 0

        for key, counterObj in self.standings.items():                        
            # print(counterObj['score'])
            scores.add(counterObj['score'])
            # print(key, counterObj)
            # print(counterObj['score'])
            # scores.add(list(counterObj.items())[1][1])


        # sortedHigestScores = sorted(scores, reverse=True)
        # print(sortedHigestScores)
        # print("rank {0} score = {1}".format(rank, sortedHigestScores[rank - 1]))
        print(self.standings.values())
        # highest_score = max(self.standings, key=self.standings.get['score'])
        # print(highest_score)

        # highestScorePlayer = filter(lambda item: item[1]['score'] == sortedHigestScores[rank - 1], self.standings.items())
        # for key, value in highestScorePlayer:
        #     print(key, value)



        return None


if __name__ == "__main__":
    table = LeagueTable(['Mike', 'Chris', 'Arnold'])
    table.record_result('Mike', 2)
    table.record_result('Mike', 1)
    table.record_result('Arnold', 5)
    table.record_result('Chris', 5)
    print(table.player_rank(1))
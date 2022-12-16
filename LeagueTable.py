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
        
        # print("Current table scores =", self.standings)        
        # Sort table by score
        table_list = sorted([(k,v['score'],v['games_played']) for k,v in self.standings.items()], key=lambda s:s[1], reverse=True)
        print("table_list = {0} and table_count = {1}".format(table_list, len(table_list)))

        target_score = table_list[rank-1][1]        
        # max_score =  max({v['score'] for k,v in self.standings.items()})
        target_count = len([(k,v['score'],v['games_played']) for k,v in self.standings.items() if v['score'] == target_score])
        print("target_score = {0} and target_count = {1}".format(target_score, target_count))

        if target_count > 1:
            target_player = [t for t in table_list if t[1] == target_score]
            print("target_playert =", target_player)    
            game_sorted = sorted(target_player, key=lambda s:s[2], reverse=False)
            print("game_sorted = {0} and game_sorted_count = {1}".format(game_sorted, len(game_sorted)))   
            print("Player rank {0} = {1}".format(rank, game_sorted[0][0]))   
            return game_sorted[0][0]

        # print("player_list = {0} and player_count = {1}".format(player_list, len(player_list)))

        # min_play =  min({v2['games_played'] for k2,v2 in self.standings.items()})
        # print("min game play =", min_play)

        # highest_player_score = {k:v['games_played'] for k,v in self.standings.items() if v['score'] == score_list[rank-1]}
        # print("highest_player_score =", highest_player_score)
        
        # soretd_player = sorted(highest_player_score, key=lambda x: highest_player_score[x], reverse=False)
        # print("sorted player =", soretd_player)
        print("Player rank {0} = {1}".format(rank, table_list[rank-1][0]))
        return table_list[rank-1][0]

if __name__ == "__main__":
    table = LeagueTable(['Mike', 'Chris', 'Arnold'])
    table.record_result('Mike', 2)
    table.record_result('Mike', 1)
    # table.record_result('Mike', 5)
    table.record_result('Arnold', 5)
    table.record_result('Chris', 5)
    # table.record_result('Chris', 2)
    print("Player Rank 1 = {0}\nPlayer Rank 2 = {1}\nPlayer Rank 3 = {2}\n".format(table.player_rank(1), table.player_rank(2), table.player_rank(3)))
    # print("Player Rank 2 =", table.player_rank(2))
    # print("Player Rank 3 =", table.player_rank(3))
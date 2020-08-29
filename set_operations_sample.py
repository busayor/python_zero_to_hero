# sets...
top_players = {'varday', 'mane', 'auba', 'trent'}
top_players_youth = {'trent', 'saka', 'greenwood','pope'}
top_gks = {'leno','kepa','pope'}

# get union(that is all items) of both sets, anyone works
# all_players = top_players | top_players_youth
all_players = top_players_youth.union(top_players) | top_gks
# print(all_players)

# get intersection (that is what all sets have in common)
# unique_players = top_players_youth & top_gks 
mvp_players = top_gks.intersection(top_players_youth)
# print(mvp_players)

friend1 = {'reading', 'clubbing', 'adventure', 'biking'}
friend2 = {'adventure', 'eating', "reading", 'playing soccer'}

friends_common = friend1 & friend2
print(friends_common)

# get the difference between 2 sets (the order matters)
# diff_players = top_players - top_players_youth
diff_players = top_players_youth - top_players
diff_players = top_players.difference(top_players_youth)
# print(diff_players)

# get a new set that contains the differences in the sets
# non_mvp_players = top_players ^ top_players_youth
non_mvp_players = top_players_youth.symmetric_difference(top_players)
# print(non_mvp_players)
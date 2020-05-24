# to find the strike rate , maximim sixes and total runs of the players

p1_run = int(input("Enter the runs scored by player1 : "))
p2_run = int(input("Enter the runs scored by player2 : "))
p3_run = int(input("Enter the runs scored by player3 : "))
stkrate1 = p1_run * 100/60
stkrate2 = p2_run * 100/60
stkrate3 = p3_run * 100/60
print("Strike rate of player 1 is :", stkrate1)
print("Strike rate of player 2 is :", stkrate2)
print("Strike rate of player 3 is :", stkrate3)
print("Maximum no. of 6 player 1 could hit :",p1_run//6 )
print("Maximum no. of 6 player 2 could hit :",p2_run//6 )
print("Maximum no. of 6 player 3 could hit :",p3_run//6 )
print("Runs scored if 60 more balls are played by player 1 :",p1_run * 2 )
print("Runs scored if 60 more balls are played by player 2 :",p2_run * 2 )
print("Runs scored if 60 more balls are played by player 3 :",p3_run * 2 )

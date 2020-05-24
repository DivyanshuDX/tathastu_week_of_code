#to count the vote and find who has maximum votes

totalvotes = int(input("Enter the no of votes: "))
votes = []
for i in range(totalvotes):
    votes.append(input("Enter the name of the Candidate to cast the Vote: "))
vote = []
for name in votes:
    vote.append((name, votes.count(name)))  
vote.sort(key = lambda x : x[0], reverse = True )
vote.sort(key = lambda x : x[1])
print("The name of the candidate who won the election is", vote[-1][0])

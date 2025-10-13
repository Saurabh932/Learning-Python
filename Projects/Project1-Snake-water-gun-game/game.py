import random

def play_game(move1, move2):
    if move1==move2:
        return "It's Draw Play again"
    elif move1=='S' and move2=='G':
        return "Gun wins"
    elif move1=="S" and move2=="W":
        return "Sanke wins"
    elif move1=="W" and move2=="G":
        return "Water wins"
    else:
        return "Computer Wins"
    
p1 = input("Select your move(S-Sanke, W-Watera and G-Gun): ").upper() 
comp = random.choice(["S", "W", "G"])
print(f"Computer chose: {comp}")

print(play_game(p1,comp))
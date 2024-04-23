import random

scores = [0, 0]
rounds = [0, 1]
print(rounds)

def player(currentRound):
    if (currentRound%2) == 0:
        return "1"
    else:
        return "2"

def winner(s1, s2, max):
    if s1 > max:
        if s2 > max:
            return "Tie!"
        elif s2 <= max:
            return "Player 2 wins!"
    elif s1 == max:
        if s2 > max:
            return "Player 1 wins!"
        elif s2 == max:
            return "Tie!"
        elif s2 < max:
            return "Player 1 wins!"
    elif s1 < max:
        if s2 > max:
            return "Player 1 wins!"
        elif s2 > s1:
            return "Player 2 wins!"
        elif s2 == s1:
            return "Tie!"
        elif s2 < s1:
            return "Player 1 wins!"

def game(max):
    print("The objective of this game is to roll dice and try to get a higher score than the other player without going over the set limit.")
    print("")

    print(" - GAME START - ")
    for i in rounds:
        print("")
        print("      SCORES:")
        print("Player 1: ", scores[0], " | Player 2: ", scores[1])
        print("")

        choice = "y"
        print(" - Player", player(i), "turn - ")
        while choice == "y":
            roll = random.randint(1, 6)
            scores[int(player(i))-1] += roll
            sc = scores[int(player(i))-1]
            print("Rolled:", roll, " Total: ", sc)

            if sc > max:
                print("Score over maximum")
                choice = "n"
            elif sc == max:
                print("Max score reached")
                choice = "n"
            elif sc < max:
                choice = input("Would you like to roll again? (y or n) ")
                print("")
    
    print(winner(scores[0], scores[1], max))

game(int(input("Pick a maximum score: ")))
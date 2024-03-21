import random

scores = [0, 0]
rounds = list(range(2))

def player(currentRound):
    if (currentRound%2) == 0:
        return "1"
    else:
        return "2"

def winner(s1, s2):
    if s1 > 13:
        if s2 > 13:
            return "Tie!"
        elif s2 <= 13:
            return "Player 2 wins!"
    elif s1 == 13:
        if s2 > 13:
            return "Player 1 wins!"
        elif s2 == 13:
            return "Tie!"
        elif s2 < 13:
            return "Player 1 wins!"
    elif s1 < 13:
        if s2 > 13:
            return "Player 1 wins!"
        elif s2 > s1:
            return "Player 2 wins!"
        elif s2 == s1:
            return "Tie!"
        elif s2 < s1:
            return "Player 1 wins!"

def game():
    print("The objective of this game is to roll dice and try to get a higher score than the other player without going over 13.")
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

            if sc > 13:
                print("Score over 13")
                choice = "n"
            elif sc == 13:
                print("Max score reached")
                choice = "n"
            elif sc < 13:
                choice = input("Would you like to roll again? (y or n) ")
                print("")
    
    print(winner(scores[0], scores[1]))

game()
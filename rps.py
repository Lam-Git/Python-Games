import random


def play():
    user = input("What's your choice?  'r' for Rock, 'p' for Paper, 's' for Scissors: ")
    # fruit = ["apple", "banana", "cherry"]
    # #print(random.choice(fruit))

    computer = random.choice(["r", "p", "s"])

    if user == computer:
        return "It's a tie game"

    if is_win(user, computer):
        return "You won! Yea... "

    return "You lost!"


def is_win(player, opponent):
    # return true if the player wins
    # Rule = r > s, s > p, p > r
    if (
        (player == "r" and opponent == "s")
        or (player == "s" and opponent == "p")
        or (player == "p" and opponent == "r")
    ):
        return True


print(play())

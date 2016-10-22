from get_diff import get_diff

def get_scores():

    p1 = input("What is Player 1's current score?\n")
    p2 = input("What is Player 2's current score?\n")
    return get_diff(p1, p2)


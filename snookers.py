import math
from get_scores import get_scores
from get_remaining import get_remaining

# get_diff()
# get_remaining()

def snookers():
    pts_left = get_remaining()
    score_diff = get_scores()
    snooks = (float(score_diff)-pts_left)/4
    snooks_roundup = math.ceil(snooks)
    if pts_left >= score_diff:
        print "No snookers are required."
    else:
        print str(int(snooks_roundup)) + " snookers are required."

snookers()
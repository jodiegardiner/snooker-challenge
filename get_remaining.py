def get_remaining():
    red = input("How many RED balls remain?\n")
    red_score = red*8
    colors = raw_input("Are ALL the other colours still on the table?\n(Y/N)\n").lower()
    if colors == 'y':
        color_score = 27
        total_score = color_score + red_score
        print "There are " + str(total_score) + " points available."
        return total_score
    colors = raw_input("Is the GREEN ball still on the table?\n(Y/N)\n").lower()
    if colors == 'y':
        color_score = 25
        total_score = color_score + red_score
        print "There are " + str(total_score) + " points available."
        return total_score
    colors = raw_input("Is the BROWN ball still on the table?\n(Y/N)\n").lower()
    if colors == 'y':
        color_score = 22
        total_score = color_score + red_score
        print "There are " + str(total_score) + " points available."
        return total_score
    colors = raw_input("Is the BLUE ball still on the table?\n(Y/N)\n").lower()
    if colors == 'y':
        color_score = 18
        total_score = color_score + red_score
        print "There are " + str(total_score) + " points available."
        return total_score
    colors = raw_input("Is the PINK ball still on the table?\n(Y/N)\n").lower()
    if colors == 'y':
        color_score = 13
        total_score = color_score + red_score
        print "There are " + str(total_score) + " points available."
        return total_score
    colors = raw_input("Is the BLACK ball still on the table?\n(Y/N)\n").lower()
    if colors == 'y':
        color_score = 7
        total_score = color_score + red_score
        print "There are " + str(total_score) + " points available."
        return total_score









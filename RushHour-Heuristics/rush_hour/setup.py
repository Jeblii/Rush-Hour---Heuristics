def load_text(txtfile):
    textlines = []
    with open('boards/' + txtfile + ".txt") as file:
        for line in file.readlines():
            line = line.strip('\n')
            line = line.split('\t')
            textlines.append(line)
    return textlines

def user_setup():
    """
    Deze functie moet uiteindelijk user input vragen (bord en grootte) en het
    goede rush hour bord aanmaken
    """
    game_start = input("Do you want to start the game (Y/N): ")
    if game_start == "Y":
        filename = input("What board would you like to use: ")
        result = load_text(filename)
        return result
    elif game_start == "N":
        print("Goodbye")



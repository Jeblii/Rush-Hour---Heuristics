def load_text(txtfile):
    """
    This function reads the textfile to generate the four attributes of each
    vehicle 
    """
    textlines = []
    with open('boards/' + "jam_" + txtfile + ".txt") as file:
        for line in file.readlines():
            line = line.strip('\n')
            line = line.split('\t')
            textlines.append(line)
    return textlines

def user_setup():
    """
    This function asks teh user whether they want to start up the game or quit.
    """
    game_start = input("Do you want to start the game (Y/N): ")
    if game_start == "Y":
        filename = input("What board would you like to use: ")
        result = load_text(filename) #calls on the function above
        return result
    elif game_start == "N": #Ends the game
        print("Goodbye")

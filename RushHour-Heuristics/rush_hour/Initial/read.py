class read(object):
    def __init__(self):
        self = self

    def load_file(filename):
        """
        Leest de "boards" bestanden in.
        Filename: naam van de file
        """
        textlines = []
        with open('boards\\' + filename + ".txt") as file:
            for line in file.readlines():
                line = line.strip('\n')
                line = line.split('\t')
                textlines.append(line)
        return textlines

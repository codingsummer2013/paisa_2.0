import os


def read_nifty_50():
    nifty50 = []
    directory = os.path.dirname(__file__)
    filename = os.path.join(directory, '../veda/nifty_50.txt')
    nifty50_file = open(filename, "r")
    while 1:
        # reading the file
        line = nifty50_file.readline()
        if len(line) == 0:
            break
        nifty50.append(line.strip())
    return nifty50

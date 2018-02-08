import csv

def open_file(filename,row):
    try:
        opened = open(filename, row)
        return opened
    except FileNotFoundError:
        raise FileNotFoundError
    except Exception as e:
        infile.close()

def compare(fna,fnb):
    fa = open_file(fna,'r')
    fb = open_file(fnb,'r')
    if fa.__sizeof__() != fb.__sizeof__():
        return 1
    far = csv.reader(fa,delimiter=',')
    fbr = csv.reader(fb,delimiter=',')
    try:
        while True:
            an, bn = far.__next__(), fbr.__next__()
            if an != bn:
                return 2
    except StopIteration:
        return 0

if __name__ == "__main__":
    print(compare("t.csv","angles_UCI_CS_out.csv"))

import math
import urllib

URL = "http://rapid-hub.org/data/angles_UCI_CS.csv"
FILENAME = "angles_UCI_CS.csv"

def get_data():
    response = urllib.request.urlopen(URL)
    content = response.read()
    newfile = open(FILENAME,"w")
    newfile.write(content.decode('utf-8'))
    newfile.close()
    
def open_file(filename):
    try:
        infile = open(filename,'r')
        return infile
    except FileNotFoundError:
        raise FileNotFoundError
    except Exception as e:
        infile.close()
        raise e

def print_data(infile):
    try:
        head = infile.readline().rstrip()
        head += ", cosine_values"
        print(head)
        for line in infile:
            line = line.rstrip()
            print(line, str(math.cos(math.pi*int(line.split(',')[1])/180)),sep=',')
        infile.close()
    except:
        infile.close()

def main():
    get_data()
    infile = open_file(FILENAME)
    print_data(infile)


if __name__ == "__main__":
    main()

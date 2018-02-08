import csv
import math


def open_file(filename,row):
    try:
        opened = open(filename, row)
        return opened
    except FileNotFoundError:
        raise FileNotFoundError
    except Exception as e:
        infile.close()
        raise e

def csvread(infile):
    return csv.reader(infile, delimiter=',')

def csvwrite(outfile):
    return csv.writer(outfile, delimiter=',')

def compute_cosines_out(reader,writer):
    header = reader.__next__()
    header.append("angle_cosine")
    writer.writerow(header)
    for ll in reader:
        ll.append("{:.3f}".format(math.cos(math.pi*int(ll[1])/180)))
        writer.writerow(ll)

def main():
    try:
        infile = open_file("angles_UCI_CS.csv",'r')
        outfile = open_file("t.csv",'w')
        reader = csvread(infile)
        writer = csvwrite(outfile)
        compute_cosines_out(reader,writer)
    finally:
        infile.close()
        outfile.close()
    

if __name__ == "__main__":
    main()

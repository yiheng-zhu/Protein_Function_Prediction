import sys
import os

def read_sequence(sequence_file):

    f = open(sequence_file, "r")
    text = f.read()
    f.close()

    sequence_dict = dict()

    for line in text.splitlines():
        line = line.strip()
        if(line.startswith(">")):
            name = line
        else:
            sequence = line
            sequence_dict[name[1:]] = sequence

    return sequence_dict

def extract(sequence_dict, name_file, extract_file):

    f = open(name_file, "r")
    text = f.read()
    f.close()

    name_list = text.splitlines()

    f = open(extract_file, "w")
    for i in range(len(name_list)):
        f.write(">" + name_list[i] + "\n" + sequence_dict[name_list[i]] + "\n")
    f.flush()
    f.close()


if __name__ == '__main__':

    sequence_dict = read_sequence(sys.argv[1])
    extract(sequence_dict, sys.argv[2], sys.argv[3])





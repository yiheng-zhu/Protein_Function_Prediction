import os
import sys
from decimal import Decimal

def copy_result(name_file, table_file, result_dir):

    f = open(name_file, "r")
    text = f.read()
    f.close()

    name_list = text.splitlines()
    for name in name_list:
        tempdir = result_dir + "/" + name + "/"
        os.makedirs(tempdir)
        os.system("cp " + table_file + " " + tempdir + "/")

def create_native_table(train_label_file, table_file, type):  # create navie table

    f = open(train_label_file, "r")
    text = f.read()
    f.close()

    term_number_dict = dict()
    number = 0

    for line in text.splitlines():

        line = line.strip()
        term_list = line.split()[1].split(",")

        for term in term_list:

            if(term not in term_number_dict):
                term_number_dict[term] = 1
            else:
                term_number_dict[term] = term_number_dict[term] + 1

        number = number + 1

    term_result_list = [(term_number_dict[term], term) for term in term_number_dict]
    term_result_list = sorted(term_result_list, reverse=True)

    f = open(table_file, "w")
    for value, term in term_result_list:
        naive_p = value/float(number)
        if(naive_p>=0.01):
            f.write(term+" "+type[1]+" "+str(Decimal(naive_p).quantize(Decimal("0.000")))+"\n")



if __name__ == '__main__':

    workdir = sys.argv[1]
    type_list = ["MF", "BP", "CC"]
    data_type_list  = ["evaluate", "test"]
    for type in type_list:
        train_label_file = workdir + "/" + type + "/train_gene_label"
        table_file = workdir + "/naive_" + type + "_new"
        create_native_table(train_label_file, table_file, type)

        for data_type in data_type_list:
            name_file = workdir + "/" + type + "/" + data_type + "_gene_list"
            result_dir = workdir + "/" + type + "/" + data_type + "/"
            os.system("rm -rf " + result_dir)
            copy_result(name_file, table_file, result_dir)





import cos_sim_calc
import numpy as np
import math
from random import randint
import os

def create_random_string(num=100):
    filenames = get_file_names()
    s = ""
    for i in range(0, num):
        if len(filenames) > 0 :
            x = randint(0,len(filenames) - 1)
            if 1 == randint(0, 2):
                s += filenames[x] + " "
        s += chr(randint(65, 90)) + " "
    return s


def create_files(num=4, path="files"):
    file_name = []
    for i in range(0, num):
        file_name.append(path + "/file" + str(i + 1) + ".txt")          #file name with its path
    for i in range(0, len(file_name)):
        write_file(file_name[i], create_random_string(randint(1, 20)))  #creating randomn string and write it inside the file
    return file_name

def write_file(file_path, string_input):
    file = open(file_path, "w")
    file.write(string_input)               #taking any incoming string input and write it inside the writable file
    file.close()

def get_file_names(path="files"):
    file_names = []                         #array bengama3 feha asma2 elfiles elly fe folder file
    for file in os.listdir(path):           #os is library reads file name
        filename = os.fsdecode(file)
        if filename.endswith('.txt'):  # whatever file types you're using...
            file_names.append("files/" + filename)
    # print('file_names', file_names)
    return file_names

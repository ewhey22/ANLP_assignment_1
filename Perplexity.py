import re
import sys
import random
from math import log
from collections import defaultdict
import numpy as np

def read_txt_file(filename):
    """
    This function takes a txt file in the format of model-br.en and outputs a dictionary of dictionaries
    so that each probability is one of the values of the nested dictionary.
    :param filename
    :return: dictionary of dictionaries
    """

    with open(filename, 'r') as f:
        lines = f.readlines()
        keys = sorted(list(set([y[0:2] for y in lines])))
        prob_dict = {i: {} for i in keys}
        for j in lines:
            req_dic = prob_dict[j[:2]]
            req_dic[j[2]] = float(j[3:])
    return prob_dict

mm = read_txt_file("model-br.en")

def preprocess_line(line):
    x = re.sub(r'[^A-Za-z0-9\s\.]+', "", line)
    x = re.sub(r'\n', '', x)
    # convert all digits to 0
    x = re.sub(r'\d', "0", x)

    # add start of sequence and end of sequence character '#' to each sequence
    x = f"##{x}#"

    return x.lower()

def perplexity(doc, model):
    """
    Function takes in a test document (WHICH HAS NOT BEEN PREPROCESSED) and a model (of the form dictionary of dictionaries.
    It outputs the perplexity of the document under this model
    """
    with open(doc) as f:
        logsum = 0
        char_count = 0
        for line in f:
            line = preprocess_line(line)
            print(line)
            for i in range(len(line)-2):
                dic = model[line[i:i+2]]
                #print(dic)
                prob = float(dic[line[i+2]])
                #print(prob)
                logsum += np.log2(prob)
                char_count += 1
                #print(logsum)
        #print(char_count)
        cross_ent = (-1/char_count)*logsum
    return print(2**cross_ent)

test_model = {'##':{'a':0.2, 'b':0.8, '#':0.0}, '#a':{'a':0.2, 'b':0.7, '#':0.1},'#b':{'a':0.15, 'b':0.75, '#':0.1},'aa':{'a':0.4, 'b':0.5, '#':0.1},'ab':{'a':0.6, 'b':0.3, '#':0.1},'ba':{'a':0.25, 'b':0.65, '#':0.1},'bb':{'a':0.5, 'b':0.4, '#':0.1} }
mm = read_txt_file("model-br.en")

#perplexity("messy_test.txt", test_model)
perplexity("test", mm)


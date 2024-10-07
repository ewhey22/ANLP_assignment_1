#Here are some libraries you're likely to use. You might want/need others as well.
import re
import sys
from random import random
from math import log
from collections import defaultdict
from itertools import product



tri_counts=defaultdict(int) #counts of all trigrams in input


def preprocess_line(line):
    x = re.sub(r'[^A-Za-z0-9\s\.]+', "", line)
    # convert all digits to 0
    x = re.sub(r'\d', "0", x)
        

    return x.lower()


#here we make sure the user provides a training filename when
#calling this program, otherwise exit with a usage error.
if len(sys.argv) != 2:
    print("Usage: ", sys.argv[0], "<training_file>")
    sys.exit(1)

infile = sys.argv[1] #get input argument: the training file



# makes a list to store list of all characters found in training document
char_list = []

#This bit of code gives an example of how you might extract trigram counts
#from a file, line by line. If you plan to use or modify this code,
#please ensure you understand what it is actually doing, especially at the
#beginning and end of each line. Depending on how you write the rest of
#your program, you may need to modify this code.


with open(infile) as f:
    for line in f:
        line = preprocess_line(line) 
        for j in range(len(line)-(3)):
            trigram = line[j:j+3]
            tri_counts[trigram] += 1
            for char in trigram:
                char_list.append(char)

# with open(infile) as f:
#     for line in f:
#         line = preprocess_line(line) 
#         for j in range(len(line)-(2)):
#             bigram = line[j:j+2]
#             tri_counts[bigram] += 1
#             for char in bigram:
#                 char_list.append(char)

# Vocabulary = sorted set of characters len = 29
char_set = sorted(set(char_list))

# cartesian product of all possible bigrams based on character set. len = 841
all_bi_counts = list(product(char_set, char_set))

# all_tri_counts holds a dictionary of all possible bigrams from vocabulary (all_bi_counts) as keys, with values of each bigram being another dictionary of trigrams as keys
# the values stored in trigram keys have count values based on training data 
all_tri_counts = {}
for i in all_bi_counts:
    all_tri_counts[i] = {i:0 for i in char_set}



print(all_tri_counts)


## EXAMPLE OF HOW TO IMPOSE tri_counts ONTO all_tri_counts:
# key=ti: value={keys=(vocab_i:values=count in tri_counts}

# for bigram in all_tri_counts.keys(): ## Look through every possible bigram from vocab 
#   for i in tri_counts.keys(): ## for every possible bigram from vocab, look through trigram list tri_counts
#       if bigram == i[0:1]: # if bigram is the same as the first two letters in trigram, 
#           all_tri_counts[bigram][i] = tri_counts[i] ## access nested dictionary by key: bigram, then key: trigram
#                                                       ## change count of this trigram w tri_counts
#           



# #Some example code that prints out the counts. For small input files
# #the counts are easy to look at but for larger files you can redirect
# #to an output file (see Lab 1).
# print("Trigram counts in ", infile, ", sorted alphabetically:")
# for trigram in sorted(tri_counts.keys()):
#     print(trigram, ": ", tri_counts[trigram])
# print("Trigram counts in ", infile, ", sorted numerically:")
# for tri_count in sorted(tri_counts.items(), key=lambda x:x[1], reverse = True):
#     print(tri_count[0], ": ", str(tri_count[1]))



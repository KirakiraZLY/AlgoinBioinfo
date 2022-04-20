##########################################################################
#
# Proj3.py
# Version 1.6
# Date: 2022-3-19
#
##########################################################################

"""
How to run:
python Proj3.py -cmd -file

"""

import sys
import os
import random
from datetime import datetime
import FileReader as fr
import sp_msa as sp
import sp_app
import sp_3
import sp_score as ss

dict_str2seq = {'a':0, 'c':1, 'g':2, 't':3, 'n':4, 'A':0, 'C':1, 'G':2, 'T':3, 'N':4}
dict_seq2str = {0:'a', 1:'c', 2:'g', 3:'t', 4:'n'}
UNDEF = 9999

def seq2str_2(s):
    seq = [UNDEF] + list(map (lambda c : dict_str2seq[c], list (s)))
    return seq
def seq2str(s):
    seq = list(map (lambda c : dict_str2seq[c], list (s)))
    return seq

if __name__ == '__main__':
    cmd = sys.argv[1]

    if cmd == '0': # unfinished
        s1 = []
        readfile_1 = sys.argv[2]
        genome1, name1 = fr.readFastA(readfile_1)
        # print(genome1)
        len1 = len(genome1)
        for i in range(0, len1):
            s1.append(seq2str_2(genome1[i]))
        # print(s1)
        lener = [0 for i in range(0,len1)]
        for i in range(0, len1):
            # print(len(s1[i]))
            lener[i] = len(s1[i])
            # maxlen = maxlen(maxlen,lener[i])
            # print(lener[i])
        # print("lener: ",lener)
        sp.msa(s1,lener)

    elif cmd == '1':
        s1 = []
        readfile_1 = sys.argv[2]
        genome1, name1 = fr.readFastA(readfile_1)
        # print(name1)
        len1 = len(genome1)
        for i in range(0, len1):
            s1.append(seq2str(genome1[i]))
        # print(s1[1][2])
        lener = [0 for i in range(0, len1)]
        for i in range(0, len1):
            # print(len(s1[i]))
            lener[i] = len(s1[i])

        len0 = len(s1[0])
        len1 = len(s1[1])
        len2 = len(s1[2])
        T = [[[UNDEF for i in range(0, len2)] for j in range(0, len1)] for k in range(0, len0)]
        T = sp_3.sp3(s1)

    elif cmd == '2': # -cmd -file -length
        s1 = []
        readfile_1 = sys.argv[2]
        a = int(sys.argv[3])

        genome1, name1 = fr.readFastA(readfile_1)
        # print(genome1)
        len1 = len(genome1)
        print("len1: ",len(genome1[0]))
        if a > len1:
            a = len1
        # s2 = genome1
        for i in range(0, len1):
            s1.append(genome1[i])
        s2 = []
        for i in range(0,a):
            s2.append(s1[i])
        # print(s1[1][2])
        # lener = [0 for i in range(0, len1)]
        # for i in range(0, len1):
        #     # print(len(s1[i]))
        #     lener[i] = len(s1[i])
        sp_app.app(s2,name1)
    elif cmd == '3': # -cmd -file -length
        s1 = []
        readfile_1 = sys.argv[2]
        a = int(sys.argv[3])

        genome1, name1 = fr.readFastA(readfile_1)
        # print(genome1)
        len1 = len(genome1)
        print(ss.approximate_score(s))
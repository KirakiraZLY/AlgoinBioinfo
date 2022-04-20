#! /usr/bin/python
#
#  spdist.py
#
#  Implementation of multiple alignment of k seqs using SP score
#
#  Usage:
#
#  spdist.py <seq1> <seq2> ... <seqk>
#
#  where <seq1> ... <seqk> are strings over the alphabeth {a,c,g,t}
#
# #  24-2-21: Converted to Python3 

import os
import sys

###########################################################################
#  gapcost and score matrix
###########################################################################

gapcost = 5

dist = [[0,5,2,5],
        [5,0,5,2],
        [2,5,0,5],
        [5,2,5,0]]

###########################################################################
#  multi-dimensional table - used to represent the dynamic prog table
###########################################################################

class MultiDimTable:

    def __init__ (self, n, val):
        self.n = n
        self.t = self.init(n, val)

    def __getitem__ (self, i):
        return self.lookup(self.t, i)

    def __setitem__ (self, i, val):
        self.set(self.t, i, val)

    def init (self, n, val):
        if len(n) == 1:
            t = n[0] * [val]
        else:
            t = []
            for i in range(n[0]):
                t.append(self.init(n[1:], val))
        return t

    def lookup (self, t, i):
        if len(i) == 1:
            return t[i[0]]
        else:
            return self.lookup(t[i[0]], i[1:])

    def set (self, t, i, val):
        if len(i) == 1:
            t[i[0]] = val
        else:
            self.set(t[i[0]], i[1:], val)

###########################################################################
#  helper functions - input strings are converted to integer sequences
###########################################################################

dict_str2seq = {'a':0, 'c':1, 'g':2, 't':3, 'A':0, 'C':1, 'G':2, 'T':3}
dict_seq2str = {0:'a', 1:'c', 2:'g', 3:'t'}

def str2seq (s):
    try:
        seq = [UNDEF] + list(map (lambda c : dict_str2seq[c], list (s)))
        return seq
    except KeyError as h:
        print("ERROR: Illegal character", h, "in input string")
        sys.exit(1)

###########################################################################
#  helper functions - handling last columns
###########################################################################

def is_last_column_legal (i, last):
    "is the last column 'last' possible for position 'i'?"
    legal = 1
    for j in range(len(i)):
        # print(i[j],last[j])
        if i[j] - last[j] < 0:
            legal = 0
    return legal

def sp_score_last_column (i, last):
    "compute the score of last column 'last' for position 'i'"
    score = 0
    # print("a: ",s[0][i[0]])
    for a in range(len(i)):
        for b in range(a+1, len(i)):
            # print(i[a])
            if last[a] == 1 and last[b] == 1:
                # print(s[a][i[a]],s[b][i[b]])
                score = score + dist[s[a][i[a]]][s[b][i[b]]]
            elif (last[a] == 1 and last[b] == 0) or (last[a] == 0 and last[b] == 1):
                score = score + gapcost
    # print("sp: ",score)
    return score

def prev_column (i, last):
    "compute the previous column of 'i' according to 'last'"
    prev = []
    for k in range(len(i)):
        prev.append(i[k] - last[k])
    # print("prev: ",prev)
    return prev

###########################################################################
#  spdist(i) - compute the optimal SP-distance between the k strings
#              s[0])[1..i[0]], ..., (s[k-1])[1..i[k-1]], where the array s
#              of strings and the value k are global variables. Uses global
#              table t.
###########################################################################

def spdist (i):
    # print(i)
    if t[i] == UNDEF:
        if sum(i) == 0:
            # base case i = [0,....,0]
            val = 0
        else:
            val = UNDEF
            # look at all possible last columns, since there are k sequences,
            # the last columns can be enumerated by the number 1, ..., 2**k
            for v in range(1, 2**k):
                # convert v to a last column, the binary representation of v
                # gives the last column, where a '1' is a symbol and a '0' is
                # a '-'
                last = []
                for j in range(k):
                    last.append(int((v // 2**j) % 2))
                # compute score for last column
                if is_last_column_legal(i, last):
                    # print("BBB: ",i)
                    # print(s[0][i[0]])
                    # print(last)
                    val = min(val, \
                              spdist(prev_column(i, last)) + \
                              sp_score_last_column(i, last))
        t[i] = val
        # print(t[i])
    # print(t)
    return t[i]

###########################################################################
#  backtrack(i) - compute an optimal SP-alignment between the k strings
#                 s[0])[1..i[0]], ..., (s[k-1])[1..i[k-1]], where the array
#                 s of strings and the value k are global variables, based
#                 on a computation of spdist(i) which has filled out the
#                 dynamic programming table t.
###########################################################################

def backtrack (i):
    opt = []
    while sum(i) != 0:
        optlast = UNDEF
        optv = UNDEF
        for v in range(1, 2**k):
            # get last column
            last = []
            for j in range(k):
                last.append((v // 2**j) % 2)
                # print((v // 2**j) % 2)
                # print(last)
            # compute score for last column
            if is_last_column_legal(i, last):
                val = spdist(prev_column(i, last)) + sp_score_last_column(i, last)
                if t[i] == val:
                    optv = v
                    optlast = last
        opt.append(optv)
        i = prev_column(i, optlast) 
    opt.reverse()
    # print(opt)
    return opt
        
###########################################################################
#  Main program
###########################################################################

# global constants
UNDEF = sys.maxsize

# read and convert input strings 
k = len(sys.argv) - 1
s = []
for t in sys.argv[1:]:
    s.append(str2seq(t))

# print(s)
# for seq in s:
# print([len(seq)-1 for seq in s])
# allocate dynamic programming tabel
t = MultiDimTable([len(seq) for seq in s], UNDEF)
# print(t)
# compute optimal sp-score
print
print("SP-score = %d" % (spdist([len(seq)-1 for seq in s])))

# print an optimal alignment
print
opt = backtrack([len(seq)-1 for seq in s])
for j in range(k):
    i = 1
    for v in opt:
        if (v // 2**j) % 2 == 1:
            print(dict_seq2str[(s[j])[i]], end="")
            i = i + 1
        else:
            print("-", end="")
    print()

# print(s)
    
        

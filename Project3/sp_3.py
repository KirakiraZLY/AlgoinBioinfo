"""
version 7
"""
import sys
import os

score_matrix = [[0,5,2,5],
                [5,0,5,2],
                [2,5,0,5],
                [5,2,5,0]]


# score_matrix = [[0, 1, 1, 1],  # A
#                 [1, 0, 1, 1],  # C
#                 [1, 1, 0, 1],  # G
#                 [1, 1, 1, 0]]  # T

dict_str2seq = {'a':0, 'c':1, 'g':2, 't':3, 'A':0, 'C':1, 'G':2, 'T':3}
dict_seq2str = {0:'a', 1:'c', 2:'g', 3:'t'}
gap = 5
UNDEF = 9999
x = 2000000
sys.setrecursionlimit(x)

def score(a,b,c):
    x = [0 for i in range(0,3)]
    x[0] = a
    x[1] = b
    x[2] = c
    SCORE = 0
    for i in range(0,3):
        for j in range(i+1,3):
            if(x[i] == "_" or x[j] == "_"):
                SCORE += gap
            else:
                # print(x[i],x[j])
                SCORE += score_matrix[x[i]][x[j]]
    # print(SCORE)
    return SCORE

def dfs(T,s,i,j,k):

    def execute(i,j,k,x,y,z):
        # print(i, j, k)
        if i == 0 and j == 0 and k == 0:
            # x = dict_seq2str[s[0][i]] + x; y = dict_seq2str[s[1][j]] + y; z = dict_seq2str[s[2][k]] + z
            xx.append(x)
            yy.append(y)
            zz.append(z)
            return

        elif i > 0 and j > 0 and k > 0 and T[i][j][k] == T[i-1][j-1][k-1] + score(s[0][i-1],s[1][j-1],s[2][k-1]):
            # print(dict_seq2str[s[0][i-1]] + x,dict_seq2str[s[1][j-1]] + y, dict_seq2str[s[2][k-1]] + z)
            execute(i-1,j-1,k-1,dict_seq2str[s[0][i-1]] + x, dict_seq2str[s[1][j-1]] + y, dict_seq2str[s[2][k-1]] + z)

        elif i > 0 and j > 0 and k >= 0 and T[i][j][k] == T[i-1][j-1][k] + score(s[0][i-1],s[1][j-1],"_"):
            # print(dict_seq2str[s[0][i-1]] + x, dict_seq2str[s[1][j-1]] + y, '_' + z)
            execute(i-1,j-1,k,dict_seq2str[s[0][i-1]] + x, dict_seq2str[s[1][j-1]] + y, '_' + z)

        elif i > 0 and j >= 0 and k > 0 and T[i][j][k] == T[i-1][j][k-1] + score(s[0][i-1],"_",s[2][k-1]):
            # print(dict_seq2str[s[0][i-1]] + x, '_' + y, dict_seq2str[s[2][k-1]] + z)
            execute(i-1,j,k-1, dict_seq2str[s[0][i-1]] + x, '_' + y, dict_seq2str[s[2][k-1]] + z)

        elif i >= 0 and j > 0 and k > 0 and T[i][j][k] == T[i][j-1][k-1] + score("_",s[1][j-1],s[2][k-1]):
            # print('_' + x, dict_seq2str[s[1][j-1]] + y, dict_seq2str[s[2][k-1]] + z)
            execute(i,j-1,k-1,'_' + x, dict_seq2str[s[1][j-1]] + y, dict_seq2str[s[2][k-1]] + z)

        elif i > 0 and j >= 0 and k >= 0 and T[i][j][k] == T[i-1][j][k] + score(s[0][i-1],"_","_"):
            # print(dict_seq2str[s[0][i - 1]] + x, "_" + y, "_" + z)
            execute(i - 1, j, k, dict_seq2str[s[0][i-1]] + x, "_" + y, "_" + z)

        elif i >= 0 and j > 0 and k >= 0 and T[i][j][k] == T[i][j-1][k] + score("_",s[1][j-1],"_"):
            # print("_" + x, dict_seq2str[s[1][j - 1]] + y,"_" + z)
            execute(i, j - 1, k, "_" + x, dict_seq2str[s[1][j-1]] + y,"_" + z)

        elif i >= 0 and j >= 0 and k > 0 and T[i][j][k] == T[i][j][k-1] + score("_","_",s[2][k-1]):
            # print("_" + x, "_" + y,dict_seq2str[s[2][k - 1]] + z)
            execute(i, j, k - 1, "_" + x, "_" + y,dict_seq2str[s[2][k-1]] + z)

    x = ''
    y = ''
    z = ''
    xx = []
    yy = []
    zz = []
    # print(i,j,k)
    execute(i,j,k,x,y,z)
    return xx,yy,zz

def sp3(s):
    # print(s)
    len0 = len(s[0])
    len1 = len(s[1])
    len2 = len(s[2])
    T = [[[UNDEF for i in range(0,len2+1)] for j in range(0,len1+1)] for k in range(0,len0+1)]

    for i in range(0,len0+1):
        for j in range(0,len1+1):
            for k in range(0,len2+1):
                # print(i,j,k)
                v0 = v1 = v2 = v3 = v4 = v5 = v6 = v7 = 9999
                if i == 0 and j == 0 and k == 0:
                    v0 = 0
                if i > 0 and j > 0 and k > 0:
                    v1 = T[i-1][j-1][k-1] + score(s[0][i-1],s[1][j-1],s[2][k-1])
                if i > 0 and j > 0 and (k > 0 or k == 0):
                    v2 = T[i-1][j-1][k] + score(s[0][i-1],s[1][j-1],"_")
                if i > 0 and j >= 0 and k > 0:
                    v3 = T[i-1][j][k-1] + score(s[0][i-1],"_",s[2][k-1])
                if (i >= 0) and j > 0 and k > 0:
                    v4 = T[i][j-1][k-1] + score("_",s[1][j-1],s[2][k-1])
                if i > 0 and j >= 0 and k >= 0:
                    v5 = T[i-1][j][k] + score(s[0][i-1],"_","_")
                if i >= 0 and j > 0 and k >= 0:
                    v6 = T[i][j-1][k] + score("_",s[1][j-1],"_")
                if i >= 0 and j >= 0 and k > 0:
                    v7 = T[i][j][k-1] + score("_","_",s[2][k-1])
                T[i][j][k] = min(v0,v1,v2,v3,v4,v5,v6,v7)

    print("SCORE= ",T[len0][len1][len2])
    # print(T[0][0][0])
    # print(len0-1,len1-1,len2-1)
    x,y,z = dfs(T,s,len0,len1,len2)
    # print(str(x),str(y),str(z))
    print("".join(x))
    print("".join(y))
    print("".join(z))
    return T
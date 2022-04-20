"""

version 6
2022-3-19

"""
import sys
import os
x = 2000000
sys.setrecursionlimit(x)

score_matrix = [[0,5,2,5,0,0,2], # A
                [5,0,5,2,0,5,0], # C
                [2,5,0,5,0,0,0], # G
                [5,2,5,0,0,5,2], # T
                [0,0,0,0,0,0,0], # N
                [0,5,0,5,0,0,0], # R
                [2,0,0,2,0,0,0]  # S
                ]

alphabet = ['A','C','G','T','N','R','S']
########### 'N' can be ACGT, 'R' can be AG, 'S' can be CG ################
gap = 5
UNDEF = 99999

def score(s1,s2):
    sc = 0
    D = [[0 for j in range(0,len(s2)+1)] for i in range(0,len(s1)+1)]
    # print(len(s1))
    for i in range(1,len(s1)+1):
        D[i][0] = D[i-1][0] + 5
    for j in range(1,len(s2)+1):
        D[0][j] = D[0][j-1] + 5

    for i in range(0,len(s1)):
        for j in range(0,len(s2)):
            # print("aaa")
            D[i+1][j+1] = min(D[i][j+1] + 5,
                              min(D[i+1][j] + 5,
                                  D[i][j]+score_matrix[alphabet.index(s1[i])][alphabet.index(s2[j])]))
    # print(D)

    return D[len(s1)-1][len(s2)-1]

def find_s1(s):
    lens = len(s)
    minsco = UNDEF
    loc = 0
    for i in range(0,lens):
        sco = 0
        for j in range(0,lens):
            if (i != j):
                # print("now: ", i,j)
                sco += score(s[i],s[j])
        # minsco = min(minsco,sco)
        if(minsco >= sco):
            minsco = sco
            loc = i
            # print(loc)
    return loc




def Score(s1,s2):
    sc = 0
    D = [[0 for j in range(0,len(s2)+1)] for i in range(0,len(s1)+1)]
    # print(len(s1))
    for i in range(1,len(s1)+1):
        D[i][0] = D[i-1][0] + 5
    for j in range(1,len(s2)+1):
        D[0][j] = D[0][j-1] + 5

    for i in range(0,len(s1)):
        for j in range(0,len(s2)):
            # print("aaa")
            D[i+1][j+1] = min(D[i][j+1] + 5,
                              min(D[i+1][j] + 5,
                                  D[i][j]+score_matrix[alphabet.index(s1[i])][alphabet.index(s2[j])]))
    # print(D)

    return D

def dfs(D,s1,s2,i,j):

    def execute(i, j, x, y):
        if i == 0 and j == 0:
            xx.append(x)
            yy.append(y)
            return
        elif i > 0 and j == 0:
            execute(i - 1, j, s1[i - 1] + x, '_' + y)
        elif i == 0 and j > 0:
            execute(i, j - 1, '_' + x, s2[j - 1] + y)
        elif (i > 0) and (j > 0) and D[i][j] == D[i - 1][j - 1] + score_matrix[alphabet.index(s1[i - 1])][
            alphabet.index(s2[j - 1])]:
            # x.append(s1[i-1])
            # y.append(s2[j-1])
            # print(i, j)
            execute(i - 1, j - 1, s1[i - 1] + x, s2[j - 1] + y)
        elif (i > 0) and (j >= 0) and D[i][j] == D[i - 1][j] + 5:
            # x.append(s1[i-1])
            # y.append('_')
            # print(i, j)
            execute(i - 1, j, s1[i - 1] + x, '_' + y)
        elif (i >= 0) and (j > 0) and D[i][j] == D[i][j - 1] + 5:
            # x.append('_')
            # y.append(s2[j-1])
            # print(i, j)
            execute(i, j - 1, '_' + x, s2[j - 1] + y)

    x = ''
    y = ''
    xx = []
    yy = []
    execute(i,j,x,y)
    return xx,yy


def align(s,loc,i):
    D = [[0 for j in range(0, len(s[loc]) + 1)] for i in range(0, len(s[i]) + 1)]
    D = Score(s[loc],s[i])
    x,y = dfs(D, s[loc],s[i], len(s[loc]), len(s[i]))
    return x,y

def extend(M,I,A):
    i = 0; j = 0;
    # print(len(M[0]))
    # print(len(A[1]))
    # print(M[0])
    # print(A[1])
    # print(M[0][106])
    # print(M[0][len(M[0])-1])
    while(i < (len(M[0])) or j < (len(A[1]))):
        # print(i,j)
        # print(len(M[0]),len(A[1]))
        # if i == len(M[0]) - 1:
        #     while j < len(A[1]):
        #         print("eeeeeeeeeeeeeeeeeeeeeeeeeeeeee")
        #         if A[1][j] != '_':
        #             for k in range(0, I):
        #                 # for l in range(len(M[k]), i,-1):
        #                 #     M[k][l+1] = M[k][l]
        #                 M[k].insert(i, '_')
        #             # print(M[k][i])
        #             M[I][i] = A[1][j]
        #             i += 1; j += 1
        # if j == len(M[0]) - 1:
        #     while i < len(M[0]):
        #         print("fffffffffffffffffffffffffffffffff")
        #         print(len(M[0]),len(M[I]))
        #         M[I][i] = '_'
        #         i += 1
        if(M[0][i] == 0): # if j reaches to the last column before i
            break
        if M[0][i] == '_' and A[0][j] == '_': # C1
            # print("aaaaaaaaaaaaaaaaaaaaa")
            # print(A[0][j],A[1][j])
            M[I][i] = A[1][j]
            i += 1; j += 1
        elif M[0][i] == '_' and A[0][j] != '_': # C2
            # print("bbbbbbbbbbbbbbbbbbbbbbb")
            # print(A[0][j],A[1][j])
            M[I][i] = '_'
            i += 1
        elif M[0][i] != '_' and A[0][j] == '_': # C3
            # print("ccccccccccccccccccccccccccc")
            # print(A[0][j],A[1][j])
            for k in range(0,I):
                # for l in range(len(M[k]), i,-1):
                #     M[k][l+1] = M[k][l]
                M[k].insert(i,'_')
            # print(M[k][i])
            M[I][i] = A[1][j]
            # print(len(M[0]))
            i += 1 ########### ith position is a gap right now, so we still need to i++ ###########
            j += 1
        elif M[0][i] != '_' and A[0][j] != '_': # C4
            # print("ddddddddddddddddddddddddddddd")
            # print(A[0][j],A[1][j])
            M[I][i] = A[1][j]
            i += 1;j += 1
    lenm = len(M[0])
    return M,lenm

def approximate_score(M,lens):
    SCORE = 0
    # print(type(M[2][0]))
    for k in range(0,len(M[0])):
        if(M[0][k] == 0):
            break
        for i in range(0,lens):
            for j in range(i+1,lens):
                if i != j:
                    if(M[i][k] == '_' or M[j][k] == '_'):
                        SCORE += gap
                    else:
                        SCORE += score_matrix[alphabet.index(M[i][k])][alphabet.index(M[j][k])]
    return SCORE

def app(s,name):
    # print(s)
    lens = len(s)
    # print("num of sequences: ",lens)
    s1loc = find_s1(s) ###########  to find the S1 as center of star   ##############
    tmp = 0
    tmpstr = name[s1loc]
    for i in range(s1loc-1,-1,-1):
        name[i+1] = name[i]
    name[0] = tmpstr
    # print("center location: ",s1loc)
    A = [[0 for i in range(0,20000)] for j in range(0,10)]
    M = [[0 for i in range(0,20000)] for j in range(0,20)]
    # M = []
    M[0] = s[s1loc]
    M[0] = list(M[0])
    for i in range(len(M[0]),len(M[0])+100):
        M[0].append(0)
    # print(M[0])

    # print(s)
    # print(M[0])

    loc2 = 1
    for i in range(0,lens):
        if i != s1loc:
            # print("NOW: ", i)
            # print(s[s1loc])
            # print(s[i])
            A[0],A[1] = align(s,s1loc,i)
            A[0] = ''.join(A[0])
            A[1] = ''.join(A[1])
            M,lenm = extend(M,loc2,A)
            loc2 += 1
    # print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")

    # print("M: ",M)
    cnt = 0 # Count the length
    """
    for i in range(0,lens):
        cnt = 0
        print(name[i])
        for j in range(0,len(M[i])):
            if(M[i][j] == 0):
                break
            print(M[i][j],end='')
            cnt += 1
        # print(cnt,end='')
        print('')
    """

    print("Approximate Score = ",approximate_score(M,lens))


    ################### Check if it is wrong #########################
    cnt = 0
    for i in range(0,len(M[0])):
        cnt = 0
        for j in range(0,lens):
            if M[j][i] == '_':
                cnt += 1
        if cnt == lens:
            print("Wrong")
            # break
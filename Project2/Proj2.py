import sys
import os
import random
from datetime import datetime
import numpy as np
import FileReader as fr
import Score
"""
python Proj2.py -cmd -file1 [-file2] 
"""

if __name__ == '__main__':

    cmd = sys.argv[1]


    if cmd == "1": # global alignment with linear gap
        readfile_1 = sys.argv[2]
        readfile_2 = sys.argv[3]
        genome1, name1 = fr.readFastA(readfile_1)
        genome2, name2 = fr.readFastA(readfile_2)

        len1 = len(genome1)
        len2 = len(genome2)
        i = 0
        j = 0
        s1 = genome1[0]
        s2 = genome2[0]
        s1 = s1.upper()
        s2 = s2.upper()
        # print(s1,s2)


        D = [[0 for j in range(0, len(s2) + 1)] for i in range(0, len(s1) + 1)]
        D = Score.score(s1, s2)
        for i in range(0, len(s1) + 1):
            for j in range(0, len(s2) + 1):
                print(D[i][j], end='\t')
            print('')
        print("Score: ", D[len(s1)][len(s2)])
        i=len(s1)
        j=len(s2)
        x=[]
        y=[]
        # print(i,j)
        x,y = Score.dfs(D,s1,s2,i,j)
        for i in range(0,len(x)):
            print(x[i],end='')
        print('\n',end='')
        for i in range(0,len(y)):
            print(y[i],end='')
        print('\n',end='')

    elif cmd == "2": # global with affine O(n2)
        readfile_1 = sys.argv[2]
        readfile_2 = sys.argv[3]
        genome1, name1 = fr.readFastA(readfile_1)
        genome2, name2 = fr.readFastA(readfile_2)

        len1 = len(genome1)
        len2 = len(genome2)
        i = 0
        j = 0
        s1 = genome1[0]
        s2 = genome2[0]
        s1 = s1.upper()
        s2 = s2.upper()
        # print(s1,s2)

        print("input s1: ",s1)
        print("input s2: ",s2)
        D,I,M = Score.affine(s1,s2)
        print("Score: ",min(M[len(s1)][len(s2)],D[len(s1)][len(s2)],I[len(s1)][len(s2)]))
        # print(M[len(s1)][len(s2)])
        [str1,str2] = Score.backtrack(s1,s2,D,I,M,s1,s2)
        for i in range(len(str1)):
            print(str1[len(str1)-1-i],end='')
        print('')
        for i in range(len(str1)):
            print(str2[len(str1)-1-i],end='')

    elif cmd == "3": # linear with 5 seqs
        s1 = []
        readfile_1 = sys.argv[2]
        genome1, name1 = fr.readFastA(readfile_1)
        # print(genome1)
        len1 = len(genome1)
        for i in range(0,len1):
            s1.append(genome1[i])
            s1[i] = s1[i].upper()
        sc_mat = np.zeros([len1,len1])

        for I in range(0,len1):
            for J in range(0,len1):
                D = [[0 for j in range(0, len(s1[J]) + 1)] for i in range(0, len(s1[I]) + 1)]
                D = Score.score(s1[I], s1[J])
                # for i in range(0, len(s1[I]) + 1):
                #     for j in range(0, len(s1[J]) + 1):
                #         print(D[i][j], end='\t')
                #     print('')
                # print("Score: ", D[len(s1[I])][len(s1[J])])
                sc_mat[I,J] = D[len(s1[I])][len(s1[J])]
        np.around(sc_mat,0)
        print(sc_mat)

    elif cmd == "4": # linear with 5 seqs
        s1 = []
        readfile_1 = sys.argv[2]
        genome1, name1 = fr.readFastA(readfile_1)
        # print(genome1)
        len1 = len(genome1)
        for i in range(0,len1):
            s1.append(genome1[i])
            s1[i] = s1[i].upper()
        sc_mat = np.zeros([len1,len1])

        for I in range(0,len1):
            for J in range(0,len1):
                sc_mat[I,J] = Score.affine2(s1[I],s1[J])
                # print("Score: ", min(M[len(s1)][len(s2)], D[len(s1)][len(s2)], I[len(s1)][len(s2)]))
                # print(M)
                # sc_mat[I,J] = min(D[len(s1[I])][len(s1[J])],I[len(s1[I])][len(s1[J])],M[len(s1[I])][len(s1[J])])
        print(sc_mat)
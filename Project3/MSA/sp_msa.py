"""

version 6

"""
import sys
import os
import FileReader as fr

score_matrix = [[0,5,2,5],
                [5,0,5,2],
                [2,5,0,5],
                [5,2,5,0]]
dict_str2seq = {'a':0, 'c':1, 'g':2, 't':3, 'A':0, 'C':1, 'G':2, 'T':3}
dict_seq2str = {0:'a', 1:'c', 2:'g', 3:'t'}
gap = 5
UNDEF = 9999

def seq2str_2(s):
    seq = [UNDEF] + list(map (lambda c : dict_str2seq[c], list (s)))
    return seq

def cal_score(s,i,r,k):
    # 1 without gap, 0 with gap.
    sp = 0
    # print(i)
    for l in range(0,k):
        for m in range(l+1,k):
            # print(i[l],s[l][i[l]])
            if r[l] == 1 and r[m] == 1:
                # print(s[l][i[l]],s[m][i[m]])
                sp += score_matrix[s[l][i[l]]][s[m][i[m]]]
            else:
                sp += gap
            """
            if(r[j] == 1 and r[l] == 1):
                sp += score_matrix[s[j][i[j]]][s[l][i[l]]]
            # print(sp)
            if(r[j] == 0 and r[l] == 1):
                sp += gap
            if(r[j] == 1 and r[l] == 0):
                sp += gap
            """
    # print("sp: ",sp)
    return sp

def last_column_legal(s,i,r,k):
    ############## if s[l][i[l]] == UNDEF while i[l] == 1, it is illegal #####################
    legal = 1
    for l in range(0,k):
        # print(i[l], r[l])
        if i[l] - r[l] < 0:
            legal = 0
        # if(legal == 0):
        #     print("illegal")
    return legal

def prev_column (s,i,k,T,maxlens,r):
    ############## T[i-1][j-1][k-1]... ####################
    loc = 0
    for l in range(0,k):
        loc += (maxlens ** l) * (i[l]-r[l])
        # print("loc: ",maxlens**l,i[l],loc)
    return T[loc]


def backtrack (s,i,k,T,maxlens,r):
    opt = []
    # print(T[0])
    while sum(i) != 0:
        optlast = UNDEF
        optv = UNDEF
        for v in range(1, 2**k):
            # get last column
            r = []
            for j in range(k):
                r.append((v // 2**j) % 2)
                # print((v // 2**j) % 2)
                # print(last)
            # compute score for last column
            if last_column_legal(s, i, r, k):
                # print("i: ",i)
                val = cal_score(s, i, r, k) + prev_column(s, i, k, T, maxlens, r)
                # print(val)
                # print(T[i])
                loc = 0
                for l in range(0, k):
                    loc += (maxlens ** l) * i[l]
                if T[loc] == val:
                    optv = v
                    optlast = r
        opt.append(optv)

        for l in range(0, k):
            # loc += (maxlens ** l) * (lener[l]-1)
            i[l] = i[l] - optlast[l]



        # loc = 0
        # for l in range(0, k):
        #     loc += (maxlens ** l) * (i[l] - r[l])
        # print("loc: ",loc)
        # i = loc
    opt.reverse()
    return opt




def msa(s,lener):
    k = len(s)
    # print(k)
    maxlens = 0
    for ii in range(0,k):
        maxlens = max(maxlens,len(s[ii]))
    # print(maxlens)
    # print(lens)
    i = [0 for t in range(0,k)]
    r = [0 for t in range(0,k)]
    T = [UNDEF for t in range(0,(maxlens**k)+1)] # change to 1 dimension
    for t in range(0,k-1):
        T[(maxlens ** t)] = 0

    T[0] = 0
    # print(i)
    """
    for t in range(1, 2 ** k):  # cases with gaps.
        r = [0 for t in range(0, k)]
        # print(t)
        loc = t
        ind = 0
        lenloc = len(str(loc))
        while loc > 0:
            r[k - 1 - ind] = loc % 2
            ind += 1
            loc //= 2
        print(sum(r))

    """

    for j in range(0,maxlens**k): # switch multiple dimensions into one dimension
        # i = [0 for t in range(0, k)]
        # print(j)
        loc = j
        ind = 0
        flag = 0
        while loc > 0:
            i[k - ind - 1] = loc % maxlens
            # print(loc % maxlens, lener[ind])
            if loc % maxlens >= lener[k - ind - 1]:
                flag = 1
            ind += 1
            loc //= maxlens
        # print(i,flag)

        if(flag == 1): ################### if beyond the length of one dimension, just skip it ################################
            continue
        # print(i)

        if j == 0:
            val = 0
        else:
            val = UNDEF
        ##################  (up)loop all the i[k], same as for i... for j... for k... ###########################
            for t in range(1, 2 ** k):  # cases with gaps.
                r = [0 for t in range(0, k)]
                # print(t)
                loc = t
                ind = 0
                lenloc = len(str(loc))
                while loc > 0:
                    r[k - 1 - ind] = loc % 2
                    ind += 1
                    loc //= 2
                # print(sum(r))

                # if(t == 1):
                #     print("r: ", r)
            ##################   (up)for the cases as with or without gaps  ######################
                if last_column_legal(s,i,r,k):
                    val = min(val,cal_score(s,i,r,k) + prev_column(s,i,k,T,maxlens,r))
        loc = 0
        for l in range(0,k):
            loc += (maxlens ** l) * i[l]
        T[loc] = val

        """
                loc = 0
                for tt in range(0,k):
                    if(r[lenloc - tt - 1] == 0): ############   T[i-1][j-1][k-1]   #################
                        loc += i[tt] * (maxlens**tt)
                    else:
                        loc += i[tt] * (maxlens**tt) - 1

                loc1 = 0
                for tt in range(0,k): ##########   T[i][j][k]         #################
                    loc1 += i[tt] * (maxlens**tt)
                if loc1 == 0:
                    T[loc1] = 0
                else:
                    if (loc1 == 1 and loc == 0):
                        print("right: ", val + T[loc])
                        print("left: ", T[loc1])
                    T[loc1] = min(T[loc1], val + T[loc])
        """
    loc = 0
    for l in range(0, k):
        loc += (maxlens ** l) * (lener[l]-1)
    #     print(loc,maxlens ** l,lener[l])
    # print(lener)
    print("score: ",T[loc])
    # print(T)
    for l in range(0, k):
        # loc += (maxlens ** l) * (lener[l]-1)
        i[l] = lener[l] - 1
    # print("iii: ",i)
    # print(s[0][4])
    opt = backtrack(s,i,k,T,maxlens,r)
    for l in range(k):
        m = 1
        for v in opt:
            if (v // 2 ** l) % 2 == 1:
                print(dict_seq2str[(s[l])[m]], end="")
                # ans.append(dict_seq2str[(s[l])[m]])
                m = m + 1
            else:
                print("-", end="")
                # ans.append("_")
        print()
    # print(ans)
    # return ans






if __name__ == '__main__':
    s1 = []
    readfile_1 = sys.argv[1]
    genome1, name1 = fr.readFastA(readfile_1)
    # print(genome1)
    len1 = len(genome1)
    for i in range(0, len1):
        s1.append(seq2str_2(genome1[i]))
    # print(s1)
    lener = [0 for i in range(0, len1)]
    for i in range(0, len1):
        # print(len(s1[i]))
        lener[i] = len(s1[i])
        # maxlen = maxlen(maxlen,lener[i])
        # print(lener[i])
    # print("lener: ",lener)
    msa(s1, lener)
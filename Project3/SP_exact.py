score_matrix = [[0,5,2,5],
                [5,0,5,2],
                [2,5,0,5],
                [5,2,5,0]]
alphabet = ['A','C','G','T']
maxx = 9999

def SP(a,b,c):
    sc = 0
    if(a != '_' and b != '_'):
        sc += score_matrix[alphabet.index(a)][alphabet.index(b)]
    else:
        sc += 5 # gap
    if(a != '_' and c != '_'):
        sc += score_matrix[alphabet.index(a)][alphabet.index(c)]
    else:
        sc += 5
    if(b != '_' and c != '_'):
        sc += score_matrix[alphabet.index(b)][alphabet.index(c)]
    else:
        sc += 5
    return sc

def score(seq):
    n = max(len(seq[0]), len(seq[1]), len(seq[2]))
    print("aaa")
    T = [[[0 for k in range(0,len(seq[2])+1)] for j in range(0,len(seq[1])+1)] for i in range(0,len(seq[0])+1)]
    print("bbb")

    for i in range(len(seq[0]) + 1):
        for j in range(len(seq[1]) + 1):
            for k in range(len(seq[2]) + 1):
                print(i,j,k)
                v0 = v1 = v2 = v3 = v4 = v5 = v6 = v7 = maxx
                if i == 0 and j == 0 and k == 0:
                    v0 = 0
                if i > 0 and j > 0 and k > 0 :
                    v1 = T[i-1][j-1][k-1] + SP(seq[0][i],seq[1][j],seq[2][k])
                if i > 0 and j > 0 and k >= 0:
                    v2 = T[i-1][j-1][k] + SP(seq[0][i],seq[1][j],'_')
                if i > 0 and j >= 0 and k > 0:
                    v3 = T[i-1][j][k-1] + SP(seq[0][i],'_',seq[2][k])
                if i >= 0 and j > 0 and k > 0:
                    v4 = T[i][j-1][k-1] + SP('_',seq[1][j],seq[2][k])
                if i > 0 and j >= 0 and k >= 0:
                    v5 = T[i-1][j][k] + SP(seq[0][i],'_','_')
                if i >= 0 and j > 0 and k >= 0:
                    v6 = T[i][j-1][k] + SP('_',seq[1][j], '_')
                if i >= 0 and j >= 0 and k > 0:
                    v7 = T[i][j][k-1] + SP('_','_',seq[2][k])
                T[i][j][k] = min(v0,v1,v2,v3,v4,v5,v6,v7)

    return T[len(seq[0])][len(seq[1])][len(seq[2])]

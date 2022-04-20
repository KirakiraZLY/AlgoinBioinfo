score_matrix = [[0,5,2,5],
                [5,0,5,2],
                [2,5,0,5],
                [5,2,5,0]]
alphabet = ['A','C','G','T']
# x = []
# y = []

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
def affine(x,y):
    a = 5; b = 5
    MAX = 9999
    # print(x)

    def init_d(i,j):
        if i > 0 and j == 0:
            return MAX
        elif j > 0:
            return a+(b*j)
        else:
            return 0
    def init_i(i,j):
        if i == 0 and j > 0:
            return MAX
        elif i > 0:
            return a+(b*i)
        else:
            return 0
    def init_s(i,j):
        if j == 0 and i == 0:
            return 0
        elif j == 0 or i == 0:
            return MAX
        else:
            return 0

    lenx = len(x) + 1
    leny = len(y) + 1
    DM = [[init_d(i,j) for j in range(0,leny)] for i in range(0,lenx)]
    IM = [[init_i(i,j) for j in range(0,leny)] for i in range(0,lenx)]
    MM = [[init_s(i,j) for j in range(0,leny)] for i in range(0,lenx)]

    for i in range(1,lenx):
        for j in range(1,leny):
            # print(alphabet.index(x[i-1]),alphabet.index(y[j-1]))
            MM[i][j] = min(score_matrix[alphabet.index(x[i - 1])][alphabet.index(y[j - 1])] + MM[i - 1][j - 1],
                           score_matrix[alphabet.index(x[i - 1])][alphabet.index(y[j - 1])] + DM[i - 1][j - 1],
                           score_matrix[alphabet.index(x[i - 1])][alphabet.index(y[j - 1])] + IM[i - 1][j - 1])
            DM[i][j] = min((a + b + MM[i][j-1]),
                           (b + DM[i][j-1]))
            IM[i][j] = min((a + b + MM[i-1][j]),
                           (b + IM[i-1][j]))
    # print(MM)

    return [DM,IM,MM]
def affine2(x,y):
    a = 5; b = 5
    MAX = 9999
    # print(x)

    def init_d(i,j):
        if i > 0 and j == 0:
            return MAX
        elif j > 0:
            return a+(b*j)
        else:
            return 0
    def init_i(i,j):
        if i == 0 and j > 0:
            return MAX
        elif i > 0:
            return a+(b*i)
        else:
            return 0
    def init_s(i,j):
        if j == 0 and i == 0:
            return 0
        elif j == 0 or i == 0:
            return MAX
        else:
            return 0

    lenx = len(x) + 1
    leny = len(y) + 1
    DM = [[init_d(i,j) for j in range(0,leny)] for i in range(0,lenx)]
    IM = [[init_i(i,j) for j in range(0,leny)] for i in range(0,lenx)]
    MM = [[init_s(i,j) for j in range(0,leny)] for i in range(0,lenx)]

    for i in range(1,lenx):
        for j in range(1,leny):
            # print(alphabet.index(x[i-1]),alphabet.index(y[j-1]))
            MM[i][j] = min(score_matrix[alphabet.index(x[i - 1])][alphabet.index(y[j - 1])] + MM[i - 1][j - 1],
                           score_matrix[alphabet.index(x[i - 1])][alphabet.index(y[j - 1])] + DM[i - 1][j - 1],
                           score_matrix[alphabet.index(x[i - 1])][alphabet.index(y[j - 1])] + IM[i - 1][j - 1])
            DM[i][j] = min((a + b + MM[i][j-1]),
                           (b + DM[i][j-1]))
            IM[i][j] = min((a + b + MM[i-1][j]),
                           (b + IM[i-1][j]))
    # print(MM)

    return min(MM[len(x)][len(y)],DM[len(x)][len(y)],IM[len(x)][len(y)])

def backtrack(s1,s2,D,I,M,x,y):
    seq1 = ''
    seq2 = ''
    i = len(s1)
    j = len(s2)
    a = 5;
    b = 5

    if M[i][j] < D[i][j] and M[i][j] < I[i][j]:
        current = 'M'
        optimalScore = M[i][j]
    if D[i][j] < M[i][j] and D[i][j] < I[i][j]:
        current = 'D'
        optimalScore = D[i][j]
    else:
        current = "I"
        optimalScore = I[i][j]

    while(i > 0 or j > 0 ):
        if current == 'M':
            seq1 += s1[i-1]
            seq2 += s2[j-1]
            if score_matrix[alphabet.index(x[i - 1])][alphabet.index(y[j - 1])] + M[i - 1][j - 1] == M[i][j]:
                i -= 1
                j -= 1
                current = 'M'
            elif score_matrix[alphabet.index(x[i - 1])][alphabet.index(y[j - 1])] + D[i - 1][j - 1] == M[i][j]:
                i -= 1
                j -= 1
                current = 'D'
            elif score_matrix[alphabet.index(x[i - 1])][alphabet.index(y[j - 1])] + I[i - 1][j - 1] == M[i][j]:
                i -= 1
                j -= 1
                current = 'I'


        elif current == 'D':
            seq1 += '_'
            seq2 += s2[j-1]
            if D[i][j-1] + b == D[i][j]:
                j -= 1
                current = 'D'
            elif M[i][j-1] + a + b == D[i][j]:
                j -= 1
                current = 'M'
        elif current == 'I':
            seq1 += s1[i-1]
            seq2 += '_'
            if I[i-1][j] + b == I[i][j]:
                i -= 1
                current = 'I'
            elif M[i-1][j] + a + b == I[i][j]:
                i -= 1
                current = 'M'

    return [seq1,seq2]


    
    


    """
    if i == 0 and j == 0:
        return x,y
    elif i == 0:
        # print('_',s2[j-1], end=" -> ")
        x += '_'
        y += s2[j-1]
        dfs(D,s1,s2,i,j-1,x,y)
    elif j == 0:
        # print(s1[i-1], '_', end=" -> ")
        x += s1[i-1]
        y += '_'
        dfs(D, s1, s2, i-1, j,x,y)
    elif i>0 and j>0 and D[i][j] == D[i-1][j-1]+score_matrix[alphabet.index(s1[i-1])][alphabet.index(s2[j-1])]:
        # print(s1[i-1],s2[j-1],end=" -> ")
        x += s1[i-1]
        y += s2[j - 1]
        dfs(D,s1,s2,i-1,j-1,x,y)
    elif i>0 and j>0 and D[i][j] == D[i-1][j] + 5:
        # print(s1[i-1],"_",end=" -> ")
        x += s1[i-1]
        y += '_'
        dfs(D,s1,s2,i-1,j,x,y)
    elif i>0 and j>0 and D[i][j] == D[i][j-1] + 5:
        # print("_",s2[j-1],end=" -> ")
        x += '_'
        y += s2[j - 1]
        dfs(D,s1,s2,i,j-1,x,y)
    # print(i,j)
    """

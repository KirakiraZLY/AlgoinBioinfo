score_matrix = [[10,2,5,2],
                [2,10,2,5],
                [5,2,10,2],
                [2,5,2,10]]

# score_matrix = [[0,5,2,5],
#                 [5,0,5,2],
#                 [2,5,0,5],
#                 [5,2,5,0]]

alphabet = ['A','C','G','T']
# x = []
# y = []

def score(s1,s2):
    sc = 0
    D = [[0 for j in range(0,len(s2)+1)] for i in range(0,len(s1)+1)]
    # print(len(s1))
    for i in range(1,len(s1)+1):
        D[i][0] = D[i-1][0]-5
    for j in range(1,len(s2)+1):
        D[0][j] = D[0][j-1]-5



    for i in range(0,len(s1)):
        for j in range(0,len(s2)):
            # print("aaa")
            D[i+1][j+1] = max(D[i][j+1]-5,
                              max(D[i+1][j]-5,
                                  D[i][j]+score_matrix[alphabet.index(s1[i])][alphabet.index(s2[j])]))

    return D

def dfs(D,s1,s2,i,j):

    def execute(i,j,x,y):
        if i == 0 and j == 0:
            xx.append(x)
            yy.append(y)
            return
        elif i > 0 and j == 0:
            execute(i - 1, j, s1[i-1] + x, '_' + y)
        elif i == 0 and j > 0:
            execute(i, j - 1, '_'+x, s2[j - 1] + y)
        elif (i > 0) and (j > 0) and D[i][j] == D[i - 1][j - 1] + score_matrix[alphabet.index(s1[i - 1])][
            alphabet.index(s2[j - 1])]:
            # x.append(s1[i-1])
            # y.append(s2[j-1])
            # print(i, j)
            execute(i - 1, j - 1,s1[i - 1] + x,s2[j - 1] + y)
        elif (i > 0) and (j >= 0) and D[i][j] == D[i - 1][j] - 5:
            # x.append(s1[i-1])
            # y.append('_')
            # print(i, j)
            execute(i - 1, j,s1[i-1]+x,'_'+y)
        elif (i >= 0) and (j > 0) and D[i][j] == D[i][j - 1] - 5:
            # x.append('_')
            # y.append(s2[j-1])
            # print(i, j)
            execute(i, j - 1,'_'+x,s2[j-1]+y)

    x = ''
    y = ''
    xx = []
    yy = []
    execute(i,j,x,y)
    return xx,yy




    
    


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
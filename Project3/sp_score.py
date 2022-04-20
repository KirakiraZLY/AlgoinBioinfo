score_matrix = [[0,5,2,5,0,0,2], # A
                [5,0,5,2,0,5,0], # C
                [2,5,0,5,0,0,0], # G
                [5,2,5,0,0,5,2], # T
                [0,0,0,0,0,0,0], # N
                [0,5,0,5,0,0,0], # R
                [2,0,0,2,0,0,0]  # S
                ]

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
class Deque(object):
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def addFront(self,item):
        self.items.insert(0,item)

    def addRear(self,item):
        self.items.append(item)

    def removeFront(self):
        return self.items.pop(0)

    def removeRear(self):
        return self.items.pop()

    def size(self):
        return len(self.items)
r = [0 for i in range(0,3000)]
RS = [0 for i in range(0,3000)]
n = [[0 for i in range(0,3000)] for j in range(0,3000)]
Dis_comb = [[0 for i in range(0,3000)] for j in range(0,2)]
distMatrix_tmp = [[0 for i in range(0,3000)] for j in range(0,3000)]

def R(distMatrix,i, num):
    cnt = 0
    for j in range(0,num):
        # print(distMatrix[i][j])
        cnt += float(distMatrix[i][j])
        cnt = round(cnt,3)
    RS[i] = cnt
    cnt /= (num - 2)
    return cnt

def nj_recur(num,distMatrix,name,ii_last,jj_last,NUM):

    if num == 2:
        print("Remaining:  1")
        # print(combo.items)
        name[0] = '(' + name[0] + ':' + str(distMatrix[0][1]/2) + ',' + name[1] + ':' + str(distMatrix[0][1]/2) + '):'
        # print(name[0])
        global zly
        zly = name[0]
        # print(x)
        return zly
    ######################################################################################################################


    minnij = 999999
    ii = 0; jj = 0

    if num == NUM: ### This first time computing
        for i in range(0, len(distMatrix)):  # O(n3)
            r[i] = R(distMatrix, i, num)
        for i in range(0, num-1):
            for j in range(i + 1, num):
                # print("matrix: ",distMatrix[i][j])
                n[i][j] = distMatrix[i][j] - r[i] - r[j]
                # print("dij: ",d[i][j])
                if minnij >= n[i][j]:
                    minnij = n[i][j]
                    ii = i
                    jj = j
        for i in range(0,num):
            Dis_comb[0][i] = distMatrix[i][ii]
            Dis_comb[1][i] = distMatrix[i][jj]
        # print(Dis_comb)

    else:
        # print(ii_last)
        for i in range(0, num):
            if i != ii_last:
            # print(i,Dis_comb[0][i],Dis_comb[1][i])
                RS[i] = RS[i] - Dis_comb[0][i] - Dis_comb[1][i] + distMatrix[i][ii_last]
                r[i] = RS[i] / (num-2)
            else:
                r[i] = R(distMatrix, i, num)
        """
        for i in range(0, num):
            print("R: ", r[i], end=" ")
        print("")
        """
        for i in range(0, num-1):
            for j in range(i + 1, num):
                # print("matrix: ",distMatrix[i][j])
                n[i][j] = distMatrix[i][j] - r[i] - r[j]
                # print("dij: ",d[i][j])
                if minnij > n[i][j]:
                    minnij = n[i][j]
                    ii = i
                    jj = j
                    # print(n[i][j],ii,jj,name[ii],name[jj])
        for i in range(0, num):
            Dis_comb[0][i] = distMatrix[i][ii]
            Dis_comb[1][i] = distMatrix[i][jj]

    """
    print("DIJ: ")
    for i in range(0, num):
        print(name[i], end="\t")
    print("")
    for i in range(0, num):
        for j in range(0, num):
            # print("", end="\t")
        # for j in range(i + 1, num):
            print(distMatrix[i][j], end="\t")
            # print(i,j)
        print("")
    print("NIJ: ")
    for i in range(0, num - 1):
        for j in range(i + 1, num):
            print(n[i][j],end="\t")
        print("")

    print("R: ", end = " ")
    for i in range(0, num):
        print(r[i], end=" ")
    print("")
    """

    Vi = (distMatrix[ii][jj] + (r[ii] - r[jj])) / 2
    Vj = (distMatrix[ii][jj] + (r[jj] - r[ii])) / 2
    # print("Vi,Vj: ",Vi,Vj)
    # print(distMatrix[ii][jj] , r[ii] , r[jj])
    # print(r[:len(distMatrix)])
    ### add k


    for i in range(0,num-1):
        # print(i)
        if (i < ii) or (i > ii and i < jj):
            ########## dim & djm
            for k in range(i+1,num):
                if k < ii :
                    distMatrix_tmp[i][k] = distMatrix[i][k]
                elif k > ii and k < jj:
                    distMatrix_tmp[i][k] = distMatrix[i][k]
                elif k > jj:
                    distMatrix_tmp[i][k-1] = distMatrix[i][k]
                elif k == jj:
                    continue
                elif k == ii:
                    distMatrix_tmp[i][k] = (distMatrix[i][ii] + distMatrix[i][jj] - (Vi + Vj)) / 2
                    # print(i,j,distMatrix[i][ii] , distMatrix[i][jj] , (Vi + Vj))
                    # print("AAA: ",distMatrix_tmp[i][k])
        elif i > jj:
            for k in range(i+1,num):
                if k < ii:
                    distMatrix_tmp[i-1][k] = distMatrix[i-1][k]
                elif k > ii and k < jj:
                    distMatrix_tmp[i-1][k] = distMatrix[i-1][k]
                elif k > jj:
                    distMatrix_tmp[i-1][k - 1] = distMatrix[i-1][k]
                elif k == jj:
                    continue
                elif k == ii:
                    distMatrix_tmp[i-1][k] = (distMatrix[i][ii] + distMatrix[i][jj] - (Vi + Vj)) / 2
                    # print(distMatrix[i][ii] , distMatrix[i][jj] , Vi , Vj)
                    # print("BBB: ",distMatrix_tmp[i-1][k])
        elif i == jj:
            continue
        elif i == ii:
            for k in range(i + 1, num):
                if k < jj:
                    distMatrix_tmp[i][k] = (distMatrix[i][ii] + distMatrix[i][jj] - (Vi + Vj)) / 2
                    # print(distMatrix[i][ii], distMatrix[i][jj], Vi, Vj)
                    # print("CCC: ",distMatrix_tmp[i][k])
                elif k == jj:
                    continue
                elif k > jj:
                    distMatrix_tmp[i][k-1] = (distMatrix[i][k] + distMatrix[jj][k] - (Vi + Vj)) / 2




    # distMatrix = [[0 for i in range(0,3000)] for j in range(0,3000)]
    """
    combo.addFront('(')
    combo.addRear(name[ii])
    combo.addRear(',')
    combo.addRear(name[jj])
    combo.addRear(')')
    combo.addRear(':')
    """

    for i in range(0, num):
        if i == ii:
            name[i] = '(' + name[ii] + ':' + str(Vi) + ',' + name[jj] + ':' + str(Vj) + ')'
        elif i == jj :
            continue
        elif i > jj:
            name[i-1] = name[i]
    name.pop()
    # print("lenname: ",len(name))


    num -= 1
    for i in range(0,num-1):
        for j in range(i+1,num):
            distMatrix[i][j] = distMatrix_tmp[i][j]

    for i in range(0,num):
        for j in range(0,i+1):
            distMatrix[i][j] = distMatrix[j][i]


    """
    ############### OUTPUT ###############
    for i in range(0,num):
        print(name[i], end="\t")
    print("")
    for i in range(0,num):
        for j in range(0,num):
            print(distMatrix[i][j],end="\t")
            # print(i,j)
        print("")
    # print("")
    """

    ii_last = ii
    jj_last = jj

    print("Remaining: ",num)
    # print("")

    # print(distMatrix[num-2][num-1])
    nj_recur(num,distMatrix,name,ii_last,jj_last,NUM)

def nj(num,distMatrix,name):
    # deque = Deque()
    nj_recur(num,distMatrix,name,-1,-1,num)
    # print(x)
    return zly








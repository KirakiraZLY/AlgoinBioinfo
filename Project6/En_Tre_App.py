import En_Fire_App as efa
Direction = {0:'e', 1:'s', 2:'w', 3:'n'}
fold = []

def Even_Odd(string1):
    lefteven = 0; leftodd = 0; righteven = 0; rightodd = 0
    len1 = len(string1)
    even = []
    odd = []
    for i in range(len1):
        if string1[i] == 'h':
            if i % 2 == 0:
                even.append(i)
                if i < (len1 / 2):
                    lefteven += 1
                else:
                    righteven += 1
            else:
                odd.append(i)
                if i < (len1 / 2):
                    leftodd += 1
                else:
                    rightodd += 1
    EtoO = min(lefteven,rightodd)
    OtoE = min(leftodd,righteven)

    if EtoO < OtoE:
        return 0, OtoE, even, odd
    return 1, EtoO, even, odd

def en_tre_app(string1):
    direc, pairnum, even, odd = Even_Odd(string1)
    # print(even)
    es = len(even)
    os = len(odd)
    # print("Es,Os: ",es,os)
    tmp = 0
    if es < os:
        tmp = 1
    elif es > os:
        tmp = 2
    if tmp == 1: ###### es < os, change some h in odd-1 into p
        ii = 0
        while ii < os - es:
            ii += 1
            odd.pop()
        os = len(odd)
    elif tmp == 2:
        ii = 0
        while ii < es - os:
            ii += 1
            even.pop()
        es = len(even)

    # print(even,odd)
    # print("ES,OS: ", es,os)
    ############## OS == ES
    j = 0; k = 0
    # if p_pos % 2 == 0:
    #     even,odd = odd,even
    ### 左odd, 右even，自己even
    j = 0; k = 0
    cnt = 0
    mincnt = 999
    tmp = 0
    while j < es or k < os:
        if j == es:
            cnt -= 1
            k += 1
            tmp = 0
        elif k == os:
            cnt += 1
            j += 1
            tmp = 1
        elif even[j] < odd[k]:
            cnt += 1
            j += 1
            tmp = 1
        elif j == es or odd[k] < even[j] :
            cnt -= 1
            k += 1
            tmp = 0
        if mincnt > cnt:
            mincnt = cnt
            if tmp == 0:
                p_pos = odd[k-1]
                ii = k-1
            else:
                p_pos = even[j-1]
                ii = j-1

    p_pos = odd[int(os/2)]
    ii = int(os/2)
    #
    # print("P: ",p_pos)
    for jj in range(0,es):
        if even[jj] > p_pos:
            break
    if k < 0:
        return 0 ######################## Score should be zero
    # print("111")
    # jj = j
    # print("ii,jj ",ii,jj)
    left = []
    right = [] # odd[j+1] -> odd[0]
    ############ Case 0
    # print(odd[ii],mid+1,even[jj]+1)
    # print("ii,jj,es: ", ii, jj, es)
    # print("1,2: ",odd[ii],even[jj])
    if ii > 0 and jj < es-1:
        mid = int((odd[ii] + even[jj]) / 2)
        # print("mid: ", mid)
        for i in range(odd[ii],mid): # {0:'e', 1:'s', 2:'w', 3:'n'} ############ But take it mirrorly
            left.append(1)
        for i in range(mid+1,even[jj]):
            right.append(1)
        left.append(1)
        right.append(1)
        # print(odd[ii],even[jj])
    else:
        print("Back to 1/4")
        return efa.en_fire_app(string1)
    # print("ii,jj: ",ii,jj)
    # print(left,right)



    while ii > 0 and jj < es-1:
        ############################################################# Case 1
        if odd[ii] - odd[ii-1] == 2 and even[jj+1] - even[jj] == 2:
            left.append(1)
            right.append(1)
            # left.append(1)
            # right.append(1)
            if ii-2 < 0 or jj + 2 >= es:
                ii -= 1; jj += 1
                left.append(1)
                right.append(1)
                continue
            # print(midd)
            if odd[ii-1]-odd[ii-2] == 2: ###### CASE A
                # print("AAAAAA")
                left.append(1)
                left.append(0) ### Godt
                left.append(1)
                # print(left)
            else: ########## Case B
                midd = int((odd[ii - 1] + odd[ii - 2]) / 2) + 1
                # print("123: ",midd)
                for i in range(odd[ii-1],odd[ii-2], -1):
                    if i > midd:
                        left.append(2)
                    elif i == midd:
                        left.append(1)
                    else:
                        left.append(0)
                left.append(1)

            if even[jj+2]-even[jj+1] == 2: ########## CASE A
                right.append(0)
                right.append(1)
                right.append(1)
            else: ########### CASE B
                # print("even+1+2:",even[jj+1] , even[jj+2])
                # print(right)
                midd = int((even[jj+1] + even[jj+2]) / 2)
                for j in range(even[jj+1], even[jj+2]):
                    if j < midd:
                        right.append(0)
                    elif j == midd:
                        right.append(1)
                    else:
                        right.append(2)
                right.append(1)
            ii -= 2
            jj += 2

        ############################################################################################################ CASE 2
        elif odd[ii] - odd[ii-1] >= 4 and even[jj+1] - even[jj] >= 4:
            if odd[ii] - odd[ii-1] == 4:
                left.append(1);left.append(1);left.append(1)
            else:
                left.append(1)
                mid = int((odd[ii] + odd[ii-1]) / 2)
                for i in range(odd[ii]-2,odd[ii-1]+1,-1):
                    if i > mid:
                        left.append(2)
                    elif i == mid:
                        left.append(1)
                    else:
                        left.append(0)
                left.append(1)

            if even[jj+1] - even[jj] == 4:
                right.append(1);right.append(1);right.append(1)
            else:
                right.append(1)
                mid = int((even[jj] + even[jj + 1]) / 2)
                for j in range(even[jj]+2,even[jj+1]-1):
                    if j < mid:
                        right.append(0)
                    elif j == mid:
                        right.append(1)
                    else:
                        right.append(2)
                right.append(1)

            if ii-2 < 0 or jj + 2 >= es:
                ii -= 1;jj += 1
                left.append(1)
                right.append(1)
                continue

            if odd[ii-1]-odd[ii-2] == 2: ###### CASE A
                left.append(1);left.append(0);left.append(1)
            else: ########## Case B

                midd = int((odd[ii - 1] + odd[ii - 2]) / 2) + 1
                for i in range(odd[ii-1],odd[ii-2]+1,-1):
                    if i > midd:
                        left.append(2)
                    elif i == midd:
                        left.append(1)
                    else:
                        left.append(0)
                left.append(1)
            if even[jj+2]-even[jj+1] == 2: ########## CASE A
                right.append(0);right.append(1);right.append(1)
            else: ########### CASE B
                midd = int((even[jj+1] + even[jj+2]) / 2)
                for j in range(even[jj+1], even[jj+2]):
                    if j < midd:
                        right.append(0)
                    elif j == midd:
                        right.append(1)
                    else:
                        right.append(2)
                right.append(1)
            ii -= 2
            jj += 2
        ################################################################################ CASE 3
        elif odd[ii] - odd[ii-1] >= 4 and even[jj+1] - even[jj] == 2:
            ################################## First seperation
            right.append(0)
            if odd[ii] - odd[ii-1] == 4:
                left.append(1);left.append(0);left.append(0)
            else:
                midd = int((odd[ii] + odd[ii-1])/2) + 1
                for i in range(odd[ii]-1,odd[ii-1],-1):
                    if i > midd:
                        left.append(2)
                    elif i == midd:
                        left.append(1)
                    else:
                        left.append(0)
                # left.append(0);left.append(0);left.append(1)

            ################################# Second seperation
            if jj + 2 >= es:
                jj += 1; ii -= 1
                left.append(1)
                right.append(0)
                continue

            left.append(1) # Left just jump by 1
            if even[jj+2] - even[jj+1] == 2:
                right.append(0);right.append(1);right.append(1)
            else:
                midd = int((even[jj+1] + even[jj+2])/2)
                for j in range(even[jj+1],even[jj+2]):
                    if j < midd:
                        right.append(0)
                    elif j == midd:
                        right.append(1)
                    else:
                        right.append(2)
                right.append(1)
            jj += 2
            ii -= 1
        ################################################################################ Case 4
        else:
            ################################## First seperation
            left.append(2)
            if even[jj+1] - even[jj] == 4:
                right.append(1);right.append(2);right.append(2)
            else:
                midd = int((even[jj] + even[jj+1]) / 2) - 1
                for j in range(even[jj] + 1 , even[jj+1]):
                    if j < midd:
                        right.append(0)
                    elif j == midd:
                        right.append(1)
                    else:
                        right.append(2)

            ################################## Second seperation
            if ii - 2 < 0:
                ii -= 1; jj += 1
                left.append(2)
                right.append(1)
                continue

            right.append(1) ######### right only goes down
            if odd[ii-1] - odd[ii-2] == 2:
                left.append(2);left.append(1);left.append(1)
            else:
                midd = int((odd[ii-1] + odd[ii-2])/2)
                for i in range(odd[ii-1] , odd[ii-2], -1):
                    if i > midd:
                        left.append(2)
                    elif i == midd:
                        left.append(1)
                    else:
                        left.append(0)
                left.append(1)
            ii -= 2
            jj += 1
        # print("ii,jj: ", ii, jj)
    # print(ii,jj)
    # print(left,right)
    # print("lenleft, lenright: ", len(left), len(right))
    # print(ii,odd[ii],string1[odd[ii]])
    # print(jj,even[jj],string1[even[jj]])
    # print("len: ",len(string1))
    # print(string1)
    # print("lenleft, lenright: ", len(left), len(right))
    if ii == 0 and odd[ii] == 0 and string1[odd[ii]] == 'h':
        left.pop()
    if jj == es - 1 and even[jj] == len(string1)-1 and string1[even[jj]] == 'h':
        right.pop()
    # print("lenleft, lenright: ", len(left), len(right))
    for i in range(0,odd[ii]-1):
        left.append(1)
    for i in range(even[jj],len(string1)-2):
        right.append(1)
    # print("lenleft, lenright: ",len(left), len(right))
    str = ""
    for i in range(len(left) - 1, -1 ,-1):
        str += Direction[(left[i]+1)%4]
    str += 'n'
    for i in range(0, len(right)):
        str += Direction[(right[i]-1)%4]
    # print(str)
    return str

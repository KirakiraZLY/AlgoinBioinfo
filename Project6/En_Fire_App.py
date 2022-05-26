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


def en_fire_app(string1):
    direc, pairnum, even, odd = Even_Odd(string1) # 1: left even and right odd; 0: left odd and right even
    if direc == 0: ### 反过来就交换
        even,odd = odd, even
    len1 = len(string1)
    lenE = len(even)
    lenO = len(odd)
    # print("Direc: ",direc)
    # print(len1)
    # print(even,odd,pairnum)
    # if direc == 1: # E to O

    for i in range(0,even[0]):
        fold.append(0) # East
    if lenO == 0:
        for i in range(even[0],len1):
            fold.append(0)
        return 0

    ######### between even[0] and even[pairnum-1]
    for i in range(0,pairnum-1):
        if even[i+1] - even[i] > 3: ### Need to fold
            # cnt = int((even[i+1] - even[i]) / 2 + even[i])
            if (even[i+1] - even[i]) % 2 == 0:
                cnt = int((even[i+1] - 1 - even[i]) / 2 + even[i])
                # print("CNT1: ",cnt)
                for j in range(even[i],even[i+1]-1):
                    if j < cnt:
                        fold.append(3)
                    elif j == cnt:
                        fold.append(0)
                    else:
                        fold.append(1)
                fold.append(0)
            else:
                cnt = int((even[i + 1] - even[i]) / 2 + even[i])
                # print("CNT2: ",cnt)
                for j in range(even[i],even[i+1]):
                    if j < cnt:
                        fold.append(3)
                    elif j == cnt:
                        fold.append(0)
                    else:
                        fold.append(1)
        else:
            for j in range(even[i],even[i+1]):
                fold.append(0)
    # print(even[pairnum-1],odd[lenO - pairnum]) #### 折叠的位置
    cnt = int((odd[lenO - pairnum] - even[pairnum-1]) / 2 + even[pairnum - 1])
    # print("CNT3: ",cnt)
    fold.append(0)
    # print("LEN: ",len(fold))
    for i in range(even[pairnum-1]+1,odd[lenO - pairnum]):
        # print(i)
        if i < cnt:
            fold.append(0)
        elif i == cnt:
            fold.append(1)
        else:
            fold.append(2)
    # print(fold)

    ################ Take turn, and use odd[]

    for i in range(lenO - pairnum, lenO - 1):
        if odd[i+1] - odd[i] > 3: ### Need to fold
            # cnt = int((even[i+1] - even[i]) / 2 + even[i])
            if (odd[i+1] - odd[i]) % 2 == 0:
                cnt = int((odd[i+1] - 1 - odd[i]) / 2 + odd[i])
                # print("CNT1: ",cnt)
                for j in range(odd[i],odd[i+1]-1):
                    if j < cnt:
                        fold.append(1)
                    elif j == cnt:
                        fold.append(2)
                    else:
                        fold.append(3)
                fold.append(2)
            else:
                cnt = int((odd[i + 1] - odd[i]) / 2 + odd[i])
                # print("CNT2: ",cnt)
                for j in range(odd[i],odd[i+1]):
                    if j < cnt:
                        fold.append(1)
                    elif j == cnt:
                        fold.append(2)
                    else:
                        fold.append(3)
        else:
            for j in range(odd[i],odd[i+1]):
                fold.append(2)
    for i in range(odd[lenO-1],len1-1):
        fold.append(2)
    # print(fold)
    str = ""
    for i in range(0,len(fold)):
        str += Direction[fold[i]]
    # print(str)
    return str
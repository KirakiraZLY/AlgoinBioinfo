def read(filename):
    cnt = 0
    line = []
    with open(filename, 'r') as fh:
        while True:
            lines = fh.readline().rstrip('\n')
            # print("S: ",lines)
            if len(lines) == 0:
                break
            line.append(lines)
    # print(line)
    num = int(line[0])
    distMatrix = line[1:]
    name = []
    for i in range(0,len(distMatrix)):
        distMatrix[i] = distMatrix[i].split(' ') # split by space
        name.append(distMatrix[i][0])
        distMatrix[i] = distMatrix[i][1:]

    for i in range(0,len(distMatrix)):
        for j in range(0,len(distMatrix[i])):
            distMatrix[i][j] = round(float(distMatrix[i][j]),3)
    return num,distMatrix,name

if __name__ == "__main__":
    filename = "a.phy"
    num,distMatrix,name = read(filename)
    print(name)

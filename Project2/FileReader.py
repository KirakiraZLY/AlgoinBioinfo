def readFastA(filename):
    name = []
    genome = []
    gen = ''
    flag = False
    with open(filename, 'r') as fh:
        i = 0
        while True:
            '''
            nav = fh.readline().rstrip()
            gen = fh.readline().rstrip()
            '''
            cnt = fh.readline().rstrip()
            cnt = cnt.replace('\n','')
            cnt = cnt.replace(' ','')
            # print(cnt)

            # print(cnt)
            if len(cnt) == 0:
                break

            if(cnt[0] == '>'):
                cnt = cnt.strip('>')
                name.append(cnt.rstrip())
                flag = True
                if gen != '':
                    genome.append(gen)
                    gen = ''
            elif(flag == True):
                # genome.append(cnt.rstrip())
                gen = cnt.rstrip()
                flag = False
            elif(flag == False):
                # genome.append(cnt)
                # genome = genome + cnt
                gen += cnt

            # print(genome)
            # x = {nav:i}
            # print(x)

            # name.append(nav)
            # genome.append(gen)
            i += 1
    genome.append(gen)
    # print(genome)
    return genome,name

# def readmultiFastA(filename):

def readFastQ(filename):
    sequences = []
    qualities = []
    FileName = []
    with open(filename) as fh:
        while True:
            fna = fh.readline().rstrip()
            seq = fh.readline().rstrip()
            fh.readline()
            qual = fh.readline().rstrip()
            if len(seq) == 0:
                break
            fna = fna.strip('@')
            FileName.append(fna)
            sequences.append(seq)
            qualities.append(qual)
    return FileName,sequences, qualities
import sys

class HPFold:

    def __init__(self, s):
        legal = {'h': 'h', 'p': 'p', 'H': 'h', 'P': 'p'}
        self.seq = []
        i = 1
        for c in s:
            if c in legal.keys():
                if legal[c] == 'h' and i % 2 == 0:
                    self.seq.append('H')
                else:
                    self.seq.append(legal[c])
                i = i + 1

    def __len__(self):
        return len(self.seq)

    def SetRelFold(self, relfold):
        turn = {'f': 0, 'l': -1, 'r': 1}
        direction = {0: 'e', 1: 's', 2: 'w', 3: 'n'}
        absfold = []
        curr = 0
        for relstep in relfold:
            absstep = (curr + turn[relstep]) % 4
            absfold.append(direction[absstep])
            curr = absstep
        print(absfold)
        return self.SetAbsFold(absfold)

    def SetAbsFold(self, absfold):
        self.legal_fold = (True, 0)
        self.grid = {}
        self.grid[0, 0] = [0]
        i = j = self.min_i = self.max_i = self.min_j = self.max_j = 0
        k = 1
        for step in absfold:
            if step == 'n':
                i = i - 1
            elif step == 's':
                i = i + 1
            elif step == 'e':
                j = j + 1
            elif step == 'w':
                j = j - 1
            if (i, j) in self.grid.keys():
                self.legal_fold = (False, k)
                self.grid[i, j].append(k)
            else:
                self.grid[i, j] = [k]
            k = k + 1
            self.min_i = min(i, self.min_i)
            self.max_i = max(i, self.max_i)
            self.min_j = min(j, self.min_j)
            self.max_j = max(j, self.max_j)
        return self.legal_fold[0]

    def ContainNeighbors(self, l1, l2):
        res = False
        for k1 in l1:
            for k2 in l2:
                if abs(k1 - k2) == 1:
                    res = True
        return res

    def ContainHHs(self, l1, l2):

        res = False
        for k1 in l1:
            for k2 in l2:
                if (self.seq[k1] == "h" or self.seq[k1] == "H") and (self.seq[k2] == "h" or self.seq[k2] == "H"):
                    res = True
        return res

    def PrintFold(self):

        score = 0
        print()
        for i in range(self.min_i, self.max_i + 1):
            for j in range(self.min_j, self.max_j + 1):
                if (i, j) in self.grid.keys():
                    l1 = self.grid[i, j]
                    if len(l1) == 1:
                        print(self.seq[l1[0]], end="")
                    else:
                        print("X", end="")
                    if (i, j + 1) in self.grid.keys():
                        l2 = self.grid[i, j + 1]
                        if self.ContainNeighbors(l1, l2):
                            print("-", end="")
                        elif self.ContainHHs(l1, l2):
                            print("*", end="")
                            score = score + 1
                        else:
                            print(" ", end="")
                    else:
                        print(" ", end="")
                else:
                    print(".", end="")
                    print(" ", end="")
            print()

            for j in range(self.min_j, self.max_j + 1):
                if (i, j) in self.grid.keys() and (i + 1, j) in self.grid.keys():
                    l1 = self.grid[i, j]
                    l2 = self.grid[i + 1, j]
                    if self.ContainNeighbors(l1, l2):
                        print("|", end="")
                    elif self.ContainHHs(l1, l2):
                        print("*", end="")
                        score = score + 1
                    else:
                        print(" ", end="")
                else:
                    print(" ", end="")
                print(" ", end="")
            print()

        if self.legal_fold[0]:
            print("Score: %d" % (score))
        else:
            print("Illegal fold after %d steps" % (self.legal_fold[1]))

def make_absfold(f):
    absfold = []
    for c in f.lower():
        if c == 'n' or c == 's' or c == 'e' or c == 'w':
            absfold.append(c)
    return absfold


def make_relfold(f):
    relfold = []
    for c in f.lower():
        if c == 'f' or c == 'l' or c == 'r':
            relfold.append(c)
    return relfold

def init(string1,str):
    seq = HPFold(string1)
    if len(seq) != len(string1):
        print()
        print("The sequence %s contains illegal characters." % (string1))
        sys.exit(1)

    absfold = make_absfold(str)
    relfold = make_relfold(str)

    if len(absfold) != len(str) and len(relfold) != len(str):
        print()
        print("The folding %s contains illegal characters." % (str))
        sys.exit(1)

    if len(absfold) == len(seq) - 1:
        seq.SetAbsFold(absfold)
    elif len(relfold) == len(seq) - 1:
        seq.SetRelFold(relfold)
    else:
        print()
        print("The folding %s has wrong length." % (str))
        sys.exit(1)

    seq.PrintFold()
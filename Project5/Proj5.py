"""
Speed-up Neighbor Joining Algorithm
2022/04/27
Input filename.phy
Output til filename.newick
"""

import sys
import FileReader as fr
import NeighborJoining as NJ
from datetime import datetime

if __name__ == "__main__":
    start_time = datetime.now()
    filename = sys.argv[1] # Fx: a.newick
    num,distMatrix,name = fr.read(filename)
    # print(num);print(distMatrix);print(name)

    zly = NJ.nj(num,distMatrix,name)

    end_time = datetime.now()
    print("Running Time: {}".format(end_time - start_time))

    ########### Output på file
    ST = 0
    END = 0
    cnt = 0

    for k in range(len(filename)):
        """
        if filename[k] == '/':
            ST = k
        """
        if filename[k] == '.':
            END = k
            if cnt == 2:
                break

    filename = filename[:END] + ".newick"
    print(filename)
    """
    # zly1 = []
    for i in range(len(zly)):
        zly1.append(zly[i])
        if i + 1 < len(zly) - 1:
            if (zly[i + 1] == ')' or zly[i + 1] == ',') and zly[i] != ':':
                zly1.append(':')
    """
    with open(filename,'wt') as f:
        # print("Newick: ",zly)
        print(''.join(zly),file = f)



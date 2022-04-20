"""

Day's algorithm 1985
Implementation of Optimal Algorithms for Comparing Trees with Labeled Leaves
Computing Robinson–Foulds Distance

Author: Zhang Leyi
2022-04-02

"""

import sys
import NewickParser as NP


if __name__ == "__main__":
    filename1 = sys.argv[1] # Fx: a.newick
    filename2 = sys.argv[2]
    NP.NewickParse(filename1,filename2)

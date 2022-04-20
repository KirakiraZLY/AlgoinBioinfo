'''
Name: Map Reader to produce SAM file with CIGAR from .fa & .fq
Author: 张乐艺 Zhang Leyi
Time: 2021/12/03 2021年12月3号
'''

import sys
import os
import random
from datetime import datetime
import FileReader as fr
import Skew
import SARead
import ApproMatching as AM

"""
    HINTS:
        argv[1]: .fa
        argv[2]: -p or -d
        argv[3]: if -p, then the file to output
                 if -d, then .fq to search
        argv[4]: if -d, then .preproc to use, if -p NONE
        argv[5]: if -d, then the edit distance, if -p NONE
"""

sa = []

if __name__ == '__main__':
    start_time = datetime.now()
    readfile_gen = sys.argv[1]
    cmd = sys.argv[2]


    genome, name = fr.readFastA(readfile_gen)


    len1 = len(genome)

    # print(len1,len2)

    i = 0; j = 0
    if cmd == "-p":
        print("#########READING###########")
        genome_filename_seq = sys.argv[3]
        # sa_filename = genome_filename_seq + ".sa"
        preprocessed_filename = genome_filename_seq + ".preproc"
        open(preprocessed_filename, 'w').close()
        print("#################PREPROCESSING############")
        while i < len1:
            s = genome[i]
            s += '$'
            print(s)
            sa, rk, height = Skew.SuffixArray(s)
            # print(sa)
            with open(preprocessed_filename, "a") as f:
                print(",".join(map(str, sa)), file=f)
                print(",".join(map(str, rk)), file=f)
            i += 1
    elif cmd == '-d':  # "-d"
        readfile_seq = sys.argv[3]
        flns, seqs, quals = fr.readFastQ(readfile_seq)
        len2 = len(seqs)
        genome_filename_seq = sys.argv[4]
        edit_distance = sys.argv[5]
        edit_distance = int(edit_distance)
        # print("RUNNING...")
        sa_filename = genome_filename_seq + ".sa"
        preprocessed_filename = genome_filename_seq + ".preproc"
        while j < len2:
            while i < len1:
                cigar = []
                s = genome[i]
                s += '$'
                sa_raw = SARead.reader(preprocessed_filename)
                # print(sa_raw)
                len1 = len(sa_raw)
                sa_split = SARead.Split(sa_raw[i])
                sa = []
                for n in sa_split:
                    sa.append(int(n))
                # print(sa)
                ###############And we get sa array#######################################
                b = Skew.bwtViaSa(s)
                # print(b)
                lensa = len(s)
                AM.search_approximate(seqs[j], b, name[i], quals[j], flns[j],sa,s, edit_distance)
                i += 1
            j += 1
            i = 0
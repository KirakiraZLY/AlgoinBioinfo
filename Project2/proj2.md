#Assignment Project 2:
### members: Zhang Leyi, Jinqi, Bernadett  

Consider the score matrix M for dna sequences

>   A  C  G  T   
A  0  5  2  5   
C  5  0  5  2   
G  2  5  0  5  
T  5  2  5  0   

and the following 5 sequences

><code>></code>seq1   
tatggagagaataaaagaactgagagatctaatgtcgcagtcccgcactcgcgagatact
cactaagaccactgtggaccatatggccataatcaaaaag

><code>></code>seq2   
atggatgtcaatccgactctacttttcctaaaaattccagcgcaaaatgccataagcacc
acattcccttatactggagatcctccatacagccatggaa

><code>></code>seq3   
tccaaaatggaagactttgtgcgacaatgcttcaatccaatgatcgtcgagcttgcggaa
aaggcaatgaaagaatatggggaagatccgaaaatcgaaa

><code>></code>seq4   
aaaagcaacaaaaatgaaggcaatactagtagttctgctatatacatttgcaaccgcaaa
tgcagacacattatgtataggttatcatgcgaacaattca

><code>></code>seq5   
atgagtgacatcgaagccatggcgtctcaaggcaccaaacgatcatatgaacaaatggag
actggtggggagcgccaggatgccacagaaatcagagcat

Question 1 
----------
Compute the score of an optimal alignment and an optimal alignment of
seq1 and seq2 above using the programs global_linear using the above
score matrix M and gap cost g(k)=5*k

###Answer
>Score:  226
TATGGA_GAGAATAAAAGAACTGAGAGATCT_AATGTCGCAGTCCCGCAC_TCGCGAGATACT_CACTAAGAC_CACTGTGGACCATATGGCCATAATCAAAAAG
_ATGGATGTCAATCCGA_CTCTACTTTTCCTAAAAATTCCAGCGCAAAATGCCATAAG_CACCACATTCCCTTATACTGGAGATCCT_CCA_TACAGCCATGGAA

Question 2
----------

Compute the score of an optimal alignment and an optimal alignment of
seq1 and seq2 above using the program global_affine using the above
score matrix M and gap cost g(k)=5+5*k
###Answer
>Score:  266
TATGGAGAGAATAAAAGAACTGAGAGATCT_AATGTCGCAGTCCCGCAC_TCGCGAGATACTCACTAAGAC_CACTGTGGACCATATGGCCATAATCA_AAAAG
_ATGGATGTCAATCCGACTCTACTTTTCCTAAAAATTCCAGCGCAAAATGCCATAAGCACCACATTCCCTTATACTGGAGATCCTCCA__TACAGCCATGGAA_


Question 3
----------

Compute the optimal score of an optimal alignment for each pair of the
5 sequences above using global_linear with the score matrix M and gap
cost g(k)=5*k. The result is a 5x5 table where entry (i,j) the optimal
score of an alignment of seqi and seqj.
###Answer
>[[  0. 226. 206. 202. 209.]   
 [226.   0. 239. 223. 220.]   
 [206. 239.   0. 219. 205.]   
 [202. 223. 219.   0. 210.]   
 [209. 220. 205. 210.   0.]]   

Question 4
----------

Compute the optimal score of an optimal alignment for each pair of the
5 sequences above using global_affine with the score matrix M and gap
cost g(k)=5+5*k. The result is a 5x5 table where entry (i,j) the
optimal score of an alignment of seqi and seqj.
###Answer   
>[[  0. 266. 242. 243. 256.]   
 [266.   0. 283. 259. 254.]   
 [242. 283.   0. 269. 243.]   
 [243. 259. 269.   0. 247.]   
 [256. 254. 243. 247.   0.]]   

## How to run
> python Proj2.py -cmd -file1 [-file2]   

note: if -cmd is 3 or 4, which means this is for multiple
alignment, thus we only need to input -file1, no -file2


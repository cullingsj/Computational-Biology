#############################
# Authors: Joshua Cullings  #
#          Daniel Laden     #
#                           #
# Date: 9/10/2019           #
#############################

import numpy as np
import sys

match = 0
mismatch = 1
insertDelete = 1

def printMatr(matrix):
    for i in range(len(matrix)):
        print(matrix[i])

def globalAlign(F, S):
    Flen = len(F)
    Slen = len(S)
    
    matrix = [[0]*Slen for i in range(Flen)] #initialize the matrix size Flen by Slen

    for i in range(Flen):
        matrix[i][0] = i

    for j in range(Slen):
        matrix[0][j] = j

    printMatr(matrix)
    
    return matrix

#From assignment 1
#Added fasta file
if len(sys.argv) > 1: #if command line input exists perform neccessary actions
    fasta_file = open(sys.argv[1], 'r')

    seq_holder = ["",""]
    sequences = []
    for line in fasta_file:
        if not seq_holder[0]:
            seq_holder[0] = line.replace(">","")

        else:
            seq_holder[1] = line.replace("\n","")
            #finished sequence
            sequences.append(tuple(seq_holder)) #changing from a list to a tuple so there's no way to change the data
            seq_holder = ["",""] #resetting seq_holder for the next sequence

    globalAlign(sequences[0][1],sequences[1][1])

else:
    #no fasta file end program
    quit()

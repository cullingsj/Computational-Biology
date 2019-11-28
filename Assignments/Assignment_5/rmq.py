#########################
# Author: Josh Cullings #
#                       #
# Date: 11/28/2019      #
#########################

import sys

def rmq(table, lower, upper):
    print("Entered into rmq with lower: %d and upper: %d" %(lower,upper))
    lowest = table[lower][upper]
    print(lowest)

def sparse_table(sequences):
    seq_out = [[0 for x in range(len(sequences))] for y in range(len(sequences))]
    seq_out[0] = sequences
    for j in range(1,len(sequences)):
        for i in range(1,len(sequences)):
            if((i+j)<(len(sequences))):
                seq_out[j][i+j] = min(sequences[i:i+j])
            else:
                break
    '''for i in range(len(seq_out)):
        print(seq_out[i])'''
    return seq_out

# From assignment 1
# Added fasta file
if len(sys.argv) > 1:  # if command line input exists perform neccessary actions
    fasta_file = open(sys.argv[1], 'r')

    sequences = fasta_file.read().split(",")
    print(sequences)
    table = sparse_table(sequences)
    while(True):
        try:
            cont = input("Continue? (y/n) ")
            if(cont == 'y'):
                lower = int(input("Please type the lower bound for sequence size %d: " %len(sequences)))
                upper = int(input("Please type the upper bound for sequence size %d, greater than lower bound %d: " %(len(sequences),lower)))
                rmq(table, lower, upper)
            elif(cont == 'n'):
                break
            else:
                print("Incorrect input")
        except:
            print("Incorrect input")
else:
    quit()
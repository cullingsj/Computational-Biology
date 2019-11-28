############################
# Author(s): Josh Cullings #
#            Daniel Laden  #
# Date: 11/28/2019         #
############################

import sys

def rmq(table, lower, upper):
    print("\nEntered into rmq with lower: %d and upper: %d" %(lower,upper))
    print("Section of sequence: ", end='')
    print(*table[0][lower:upper])
    lowest = table[upper-lower][upper]
    print("Result: %d" % lowest)

def sparse_table(sequences):
    seq_out = [[0 for x in range(len(sequences))] for y in range(len(sequences))]
    seq_out[0] = sequences
    for j in range(1,len(sequences)):
        for i in range(1,len(sequences)):
            if((i+j)<(len(sequences))):
                seq_out[j][i+j] = min(sequences[i:i+j])
                #print(*sequences[i:i+j])
                #print(min(sequences[i:i+j]))
            else:
                break
    return seq_out

# From assignment 1
# Added fasta file
if len(sys.argv) > 1:  # if command line input exists perform neccessary actions
    fasta_file = open(sys.argv[1], 'r')

    sequences = fasta_file.read().split(",")
    temp = [0 for x in range(len(sequences))]
    # converting from a char set to an int set
    for i in range(len(sequences)):
        temp[i] = int(sequences[i])
    print(*sequences)
    table = sparse_table(temp)
    while(True):
        try:
            cont = input("Continue? (y/n) ")
            if(cont == 'y'):
                lower = int(input("Please type the lower bound in the range 0-%d: " %len(sequences)))
                upper = int(input("Please type the upper bound in the range %d-%d: " %(lower,len(sequences))))
                rmq(table, lower, upper)
            elif(cont == 'n'):
                break
            else:
                print("Incorrect input")
        except:
            print("Incorrect input")
else:
    quit()
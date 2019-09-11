############################
# Authors: Joshua Cullings #
#          Daniel Laden    #
#                          #
# Date: 9/10/2019          #
############################
import numpy as np

def zAlgo(P, S):
    concatString=P+'$'+S
    n=len(concatString)
    Z=[None]*n
    Z[0]='x'
    L,R,=0,0

    for i in range(1,n):
        if (i > R):
            L=R=i
            while(R<n and concatString[R-L] == concatString[R]):
                R+=1
            Z[i]=R-L
            R-=1
        else:
            k=i-L
            if(Z[k]<(R-i+1)):
                Z[i]=Z[k]
            else:
                L=i
                while(R<n and concatString[R-L] == concatString[R]):
                    R+=1
                Z[i]=R-L
                R-=1
    print(Z)

zAlgo("aab", "baabaa")

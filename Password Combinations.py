from __future__ import print_function
from itertools import permutations
import time;

def toString(List): 
    return ''.join(List) 


f = open("Combinations.txt", "w")

string = input("Enter the String : ")
cond=input("Do you want to add @#$ in the String ? y for YES n for NO : ")
if(cond=='y'):
    string=string+"@#$" 
letters = list(string)
print("\nGenerating... \n")
for i in range(len(letters)):
    for c in permutations(letters, i):
           # print(c)
            f.write(toString(c)+'\n')
f.close();
m=" --- Combinations Generated ---"
blah=list(m)
for l in blah:
    print(l, end=" ")
    time.sleep(0.2)

print("\nCombinations are stored in a file named \"Combinaiton.txt\" ")

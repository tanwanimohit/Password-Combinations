from itertools import permutations
import time;

def toString(List): 
    return ''.join(List) 


f = open("Combinations.txt", "w")

string = raw_input("Enter the String : ")
cond=raw_input("Do you want to add @#$ in the String ? y for YES n for NO : ")
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
    print(l),
    time.sleep(0.2)

print("\nCombinations are stored in a file named \"Combinaiton.txt\" ")

import sys
sys.path.append("..")

import copy as cp
import random as rd
from chain import Chain
from pcs import PCS

print("Testing operation functions in Chain()...", end="\n")

output_file = "chain_operations_bug_002"
tool = PCS("../data/forte_prime_forms.csv")

def random_pcs():
    notes = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11"]
    set = rd.sample(notes, rd.randint(4,7))
    notes_string = ""
    for n in set:
        notes_string += n
        notes_string += " "
    return notes_string[:-1]

output = open("output/" + output_file + ".txt", "w")
output.write("Debugging error in Chain()\n")
output.write("Looking for chains in which invert() and translate(n) fails...\n\n")

for i in range(100):
    the_set = random_pcs()
    output.write("-----------------------------\n")
    output.write("Trying with " + the_set + "\n\n")
    ch = Chain(tool, the_set, 5, 15, 3)
    s1 = cp.deepcopy(ch.sequence)
    ch.invert()
    s2 = cp.deepcopy(ch.sequence)
    ch.translate(1)
    s3 = cp.deepcopy(ch.sequence)
    broken = 0
    healthy = 0
    for s in range(len(s1)):
        for j in range(len(s1[s])):
            a = (s1[s][j]+s2[s][j])%12
            if a == 0:
                healthy += 1
            else:
                output.write(str(s1) + "\n")
                output.write(str(s2) + "\n")
                output.write(str(s3) + "\n\n")
                broken += 1
    output.write("healthy = " + str(healthy) + ", broken = " + str(broken) + "\n")
    output.write("-----------------------------\n\n")

output.close()

print("Output file saved!", end="\n")
print("That's all!", end="\n")

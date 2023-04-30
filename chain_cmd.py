
from pcs import PCS
from chain import Chain

#A simple note chains with a constant pitch class set from the terminal
pcs_tool = PCS() #We initialize PCS() class here...
print("I am ready to create some constant pitch class set notes sequences... Do you want to run Chain() in debug mode? If so type 'yes'.", end="\n")

a = input()
debug = False
if a.lower() == "yes":
    debug = True #Deciding to run in debug mode...
    print("\nOk. Debug mode is active!", end="\n")

attempts = None
link_limits = None

def set_attempts():
    global attempts
    while attempts == None:
        a = input()
        try:
            attempts = int(a)
        except:
            print("That's is a strange quantity of attempts...", end="\n")

def set_limits():
    global link_limits
    while link_limits == None:
        a = input().split(" ")
        try:
            link_limits = [-1,-1]
            link_limits[0] = int(a[0])
            link_limits[1] = int(a[1])
        except:
            print("That's is a strange link's limit range...", end="\n")

print("\nHow many attempts you want me to try for each base set?", end="\n")
set_attempts()

print("\nPlease, tell me what your preffered links limit are.", end="\n")
set_limits()

print("\nOk. I will work with " + str(attempts) + " attempts and " + str(link_limits) + " maximum links.", end="\n")
print("Waiting for your base pitch set...", end="\n")
print("Type 'q' when you are ready!", end="\n\n")

def get_pcs_chain(debug, string_notes, attempts, link_min, link_max):
    if debug:
        print("\nYou ask for a sequence based on " + string_notes + ".", "\n")
        for i in range(attempts):
            print("Attempt: " + str(i+1), end="\n")
            ch = Chain(pcs_tool, string_notes, link_min, link_max)
            print("Degrading: " + str(ch.degrading), end="\n")
            print("Is this sequence healthy?: " + str(ch.check_sequence(ch.base, ch.sequence)), end="\n")
            print("Is this sequence closed?: " + str(ch.is_closed), end="\n")
            print("Is this sequence closable?: " + str(ch.is_closable), end="\n")
            print("Here is the sequence: " + ch.sequence_to_string(ch.sequence), end="\n\n")
    else:
        print("You ask for a sequence based on " + string_notes + ".", "\n")
        for i in range(attempts):
            print("Attempt: " + str(i+1), end="\n")
            print("You ask for a sequence based on " + string_notes + ".", "")
            ch = Chain(pcs_tool, string_notes, link_min, link_max)
            print(ch.sequence_to_string(ch.sequence), end="\n\n")

while True:
    a = input()
    try:
        if a.lower() == "q":
            break
        else:
            get_pcs_chain(debug, a, attempts, link_limits[0], link_limits[1])
    except:
        print("I don't know how to process that input...", end="\n\n")

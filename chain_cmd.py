
from pcs import PCS
from chain import Chain

pcs_tool = PCS() #We initialize PCS() class here...
print("\n---- c a l  p y  t o o l s", end="\n")
print("---- musicaltools.gitlab.io", end="\n")
print("---- Chain() command line utility", end="\n\n")
print("I am ready to create some constant pitch class set notes sequences... Do you want to run Chain() in debug mode? If so type 'yes'.", end="\n")

a = input()
debug = False
if a.lower() == "yes":
    debug = True #Deciding to run in debug mode...
    print("\nOk. Debug mode is active!", end="\n")

attempts = None #Here we will save the number of attemps for each input...
link_limits = None #Here we will save Chain() limits for each input...
max_degrading = None #Here we will save maximum fallbacks admited...

def set_attempts():
    #Here we set attempts...
    global attempts
    while attempts == None:
        a = input()
        try:
            attempts = int(a)
        except:
            print("That's is a strange quantity of attempts...", end="\n")

def set_limits():
    #Here we set limits...
    global link_limits
    while link_limits == None:
        a = input().split(" ")
        try:
            link_limits = [-1,-1]
            link_limits[0] = int(a[0])
            link_limits[1] = int(a[1])
        except:
            print("That's is a strange link's limit range...", end="\n")

def set_degrading():
    #Here we set the maximum fallbacks allowed...
    global max_degrading
    while max_degrading == None:
        a = input()
        try:
            max_degrading = int(a)
        except:
            print("That's is a strange link's limit range...", end="\n")

print("\nHow many attempts you want me to try for each base set?", end="\n")
set_attempts()

print("\nPlease, tell me what your preffered links limit are ('minimumlinks maximumlinks').", end="\n")
set_limits()

print("\nSometimes when I can't find a new link to add to the notes sequence I need to fallback. How many times I am allowed to do that?", end="\n")
set_degrading()

print("\nOk. I will work with " + str(attempts) + " attempts and " + str(link_limits) + " maximum links.", end="\n")
print("You set a maximum of " + str(max_degrading) + " fallbacks.", end="\n")
print("Waiting for your base pitch set...", end="\n")
print("Type 'q' when you are ready!", end="\n\n")

def get_pcs_chain(debug, string_notes, attempts, link_min, link_max, degrading):
    print("\nYou ask for a sequence based on " + string_notes + ".", "\n")
    if debug:
        for i in range(attempts):
            print("Attempt: " + str(i+1), end="\n")
            ch = Chain(pcs_tool, string_notes, link_min, link_max, degrading) #Creating the Chain() instance...
            print("Degrading: " + str(ch.degrading), end="\n")
            print("Is this sequence healthy?: " + str(ch.check_sequence(ch.base, ch.sequence)), end="\n") #Checking the sequence created...
            print("Is this sequence closed?: " + str(ch.is_closed), end="\n") #Printing sequence status...
            print("Is this sequence closable?: " + str(ch.is_closable), end="\n")
            print("Here is the sequence: " + ch.sequence_to_string(ch.sequence), end="\n\n") #Printing the sequence...
    else:
        for i in range(attempts):
            print("Attempt: " + str(i+1), end="\n")
            ch = Chain(pcs_tool, string_notes, link_min, link_max, degrading) #Creating the Chain() instance...
            print(ch.sequence_to_string(ch.sequence), end="\n\n") #Printing the sequence...

while True:
    a = input()
    try:
        if a.lower() == "q":
            break
        else:
            get_pcs_chain(debug, a, attempts, link_limits[0], link_limits[1], max_degrading) #Creating a sequence...
    except:
        print("I don't know how to process that input...", end="\n\n")

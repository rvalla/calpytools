from pcs import PCS
from chain import Chain

pcs_tool = PCS() #We initialize PCS() class here...
ch = None #We will store here our chain...

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

print("To operate your chain simply use:", end="\n")
print("'+n' to translate your chain n steps,", end="\n")
print("'xn' to multiply the elements of the chain by n,", end="\n")
print("or 'i' to invert your chain,", end="\n")
print("or 'c' to close the chain,", end="\n")
print("or 'n' to build a new chain with the same notes.,", end="\n\n")

print("You can pass a new set of note at any time!", end="\n")
print("Type 'q' when you are ready!", end="\n\n")

def print_chain(debug, the_chain):
    if debug:
        print("Degrading: " + str(the_chain.degrading), end="\n")
        print("Number of links: " + str(the_chain.sequence_size), end="\n")
        print("Is this sequence healthy?: " + str(the_chain.check_sequence(the_chain.base, the_chain.sequence)), end="\n") #Checking the sequence created...
        print("Is this sequence closed?: " + str(the_chain.is_closed), end="\n") #Printing sequence status...
        print("Is this sequence closable?: " + str(the_chain.is_closable), end="\n")
        print("Here is the sequence: " + the_chain.sequence_to_string(the_chain.sequence), end="\n\n") #Printing the sequence...
    else:
        print(ch.sequence_to_string(the_chain.sequence), end="\n\n") #Printing the sequence...

def get_pcs_chain(debug, string_notes, attempts, link_min, link_max, degrading):
    print("\nYou ask for a sequence based on " + string_notes + ".", "\n")
    global ch
    ch = Chain(pcs_tool, string_notes, link_min, link_max, degrading) #Creating the Chain() instance...
    if debug:
        print("I am working with this candidates matrix:", end="\n\n")
        print(ch.candidates_to_string())
    for i in range(attempts):
        ch.run()
        print("\nAttempt: " + str(i+1), end="\n")
        print_chain(debug, ch)

while True:
    a = input()
    try:
        if a.lower() == "q":
            break
        else:
            if a.startswith("+"):
                t = int(a[1:])
                ch.translate(t)
                print("\nTranslated " + str(t) + " steps:", end="\n")
                print(ch.sequence_to_string(ch.sequence), end="\n\n")
            elif a.startswith("x"):
                f = int(a[1:])
                ch.multiply(f)
                print("\nMultiplied by " + str(f) + ":", end="\n")
                print(ch.sequence_to_string(ch.sequence), end="\n\n")
            elif a == "i":
                ch.invert()
                print("\nInverted:", end="\n")
                print(ch.sequence_to_string(ch.sequence), end="\n\n")
            elif a == "c":
                ch.close()
                print("\nClosed:", end="\n")
                print(ch.sequence_to_string(ch.sequence), end="\n\n")
            elif a == "n":
                ch.run()
                print("\nNew sequence:", end="\n")
                print_chain(debug, ch)
            else:
                get_pcs_chain(debug, a, attempts, link_limits[0], link_limits[1], max_degrading) #Creating a sequence...
    except:
        print("\nI don't know how to process that input...", end="\n")
        print("Remember that to operate a chain, first a chain must exist.", end="\n\n")

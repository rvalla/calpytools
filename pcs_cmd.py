
from pcs import PCS

#A simple script to analyze pitch class sets from the terminal
tool = PCS() #We initialize PCS() class here...
print("\n---- c a l  p y  t o o l s", end="\n")
print("---- musicaltools.gitlab.io", end="\n")
print("---- PCS() command line utility", end="\n\n")
print("Do you want to run PCS() in debug mode? If so type 'yes'.", end="\n")

a = input()
debug = False
if a.lower() == "yes":
    debug = True #Deciding to run in debug mode...
    print("\nOk. Debug mode is active!", end="\n")
    print("Yoy can type 'forte' to run a complete analysis of the database", end="\n")

print("Waiting for your pitch sets...", end="\n")
print("Type 'q' when you are ready!", end="\n\n")

def get_set_info(debug_mode, string_notes):
    if debug_mode:
        notes = tool.string_to_notes(string_notes)
        notes.sort()
        print("You send " + str(notes), end="\n")
        print("When looking for the prime form I considered this candidates: ", end="\n")
        print(tool.get_ordered_candidates(len(notes), notes))
        c, o, interval, is_inverted, z_pair, states, ordered, prime = tool.get_set_info(string_notes)
        print("\nI ended with this information about your set:", end="\n")
        print("Cardinality: " + str(c), end="\n")
        print("Ordinal: " + str(o), end="\n")
        print("Interval from C: " + str(interval), end="\n")
        print("Is your set inverted?: " + str(is_inverted), end="\n")
        print("Is there a Z related set?: " + str(z_pair), end="\n")
        print("How many states this set has?: " + str(states), end="\n")
        print("Ordered form: " + str(ordered), end="\n")
        print("Prime form: " + str(prime), end="\n\n")
    else:
        a,b,c,d,e,f,g,h = tool.get_set_info(string_notes)
        print(tool.build_set_info_msg(a,b,c,d,e,f,g,h))

def iterate_database():
    data = open("data/forte_prime_forms.csv").readlines()[1:]
    output = open("data/debugging_forte_database.txt", "w")
    output.write("Let's iterate all forte prime forms' database...\n\n")
    cardinality = 1
    ordinal = 1
    ordinal_errors = 0
    prime_form_errors = 0
    for l in data:
        m = ""
        line = l.split(";")
        string_notes = line[2]
        c, o, interval, is_inverted, z_pair, states, ordered, prime = tool.get_set_info(string_notes)
        if not c == cardinality:
            cardinality = c
            ordinal = 1
        m += str(c) + "."
        if o == None:
            m += str(ordinal) + " - "
            m += "ERROR: " + " "
            m += str(ordered) + " "
            m += str(prime) + " "
            m += str(len(tool.get_ordered_candidates(c, tool.string_to_notes(string_notes)))) + "\n"
            prime_form_errors += 1
        else:
            if o == ordinal:
                m += str(o) + " - "
                m += str(ordered) + " "
                m += str(prime) + " "
                m += str(interval) + "\n"
            else:
                m += str(o) + " - "
                m += "ERROR: ordinal number doesn't match "
                m += str(prime) + "\n"
                ordinal_errors += 1
        print(m, end="")
        output.write(m)
        ordinal += 1
    m = "\nOrdinal errors: " + str(ordinal_errors) + "\n"
    print(m, end="")
    output.write(m)
    m = "Prime forms I coudn't find: " + str(prime_form_errors) + "\n"
    print(m, end="\n")
    output.write(m)
    output.close()

while True:
    a = input()
    try:
        if a.lower() == "q":
            break
        elif a.lower() == "forte":
            iterate_database() #To run an analysis of all prime forms in the database...
        else:
            get_set_info(debug, a) #To print input classification...
    except:
        print("I don't know how to process that input...", end="\n\n")

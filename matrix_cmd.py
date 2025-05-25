from pcs import PCS
from matrix import Matrix

#A simple script to work with intances of Matrix() on the terminal
tool = PCS() #We initialize PCS() class here...
the_matrix = None #We need a name for our matrix...

print("\n---- c a l  p y  t o o l s", end="\n")
print("---- musicaltools.gitlab.io", end="\n")
print("---- Matrix() command line utility", end="\n\n")

print("Let's create and operate some matrices...", end="\n")
print("Type 'n' to create a new matrix.", end="\n")
print("Type 'q' to close this program.", end="\n\n")

print("After creating a new matrix you can:", end="\n")
print("Type 'type1' to create a type 1 matrix,", end="\n")
print("or 'type2' to create a type 2 matrix,", end="\n")
print("or 'cycle' to create a matrix by translation cycle,", end="\n")
print("or 'chain' to create a matrix from a closed chain,", end="\n")
print("or 'random' to create a random matrix.", end="\n\n")

print("To operate your matrix simply use:", end="\n")
print("'+n' to translate your matrix n steps,", end="\n")
print("or 'i' to invert your matrix,", end="\n")
print("or 't' to transpose your matrix,", end="\n")
print("or 'xn' to multiply your matrix by n,", end="\n")
print("or 's' to shuffle your matrix,", end="\n")
print("or 'swap n1 n2 n3...' to swap existing notes in your matrix.", end="\n\n")

print("Type 'pcs' to get the pitch class sets in the first row and column.", end="\n\n")

def execute_user_input(the_input):
    if the_input == "type1":
        print("Let's create a type 1 matrix. Please give me a pcs (like '0 1 2 3')", end="\n")
        try:
            set = input()
            the_matrix.build_type_one(the_matrix.get_notes(set))
            print("", end="\n")
            the_matrix.print_matrix()
        except:
            print("That's not a set of notes! Command aborted!", end="\n")
    elif the_input == "type2":
        print("Let's create a type 2 matrix. Please give me two pcs (like '0 1 2 3-0 3 5')", end="\n")
        try:
            sets = input().split("-")
            the_matrix.build_type_two(the_matrix.get_notes(sets[0]), the_matrix.get_notes(sets[1]))
            print("", end="\n")
            the_matrix.print_matrix()
        except:
            print("That's not a pair of sets of notes! Command aborted!", end="\n")
    elif the_input == "cycle":
        print("Let's create a matrix by translation cycle. Please give me your first row (like '0 1-2 3--5')", end="\n")
        row = input()
        print("Now give me your translation step (an integer number)", end="\n")
        t = input()
        try:
            the_matrix.translation_cycle(row, int(t))
            print("", end="\n")
            the_matrix.print_matrix()
        except:
            print("Something went wrong! Command aborted!", end="\n")
    elif the_input == "chain":
        print("Let's create a matrix from a closed chain. Please give me your chain (like '0 1-2 3-...-0 1')", end="\n")
        chain = input()
        try:
            the_matrix.from_closed_chain(chain)
            print("", end="\n")
            the_matrix.print_matrix()
        except:
            print("That's not a correctly formated closed chain! Command aborted!", end="\n")
    elif the_input == "random":
        print("Let's create a random matrix. Please give me 3 integers separated by spaces...", end="\n")
        print("'maximum_number_of_elements_in_a_cell width height", end="\n")
        try:
            set = input().split(" ")
            l = [int(i) for i in set]
            the_matrix.random_matrix(l[0],l[1],l[2])
            print("", end="\n")
            the_matrix.print_matrix()
        except:
            print("Something went wrong! Command aborted!", end="\n")
    elif the_input == "i":
        the_matrix.invert()
        print("", end="\n")
        the_matrix.print_matrix()
    elif the_input == "t":
        the_matrix.transpose()
        print("", end="\n")
        the_matrix.print_matrix()
    elif the_input == "s":
        the_matrix.shuffle_status()
        print("", end="\n")
        the_matrix.print_matrix()
    elif the_input.startswith("+"):
        try:
            t = int(the_input[1:])
            the_matrix.translate(t)
            print("", end="\n")
            the_matrix.print_matrix()
        except:
            print("That isn't a valid translation step! Command aborted!", end="\n")
    elif the_input.startswith("x"):
        try:
            f = int(the_input[1:])
            the_matrix.multiply(f)
            print("", end="\n")
            the_matrix.print_matrix()
        except:
            print("That isn't a valid multiplication factor! Command aborted!", end="\n")
    elif the_input.startswith("swap"):
        try:
            l = [int(i) for i in the_input[5:].split(" ")]
            for n in l:
                the_matrix.swap_note(n)
            print("", end="\n")
            the_matrix.print_matrix()
        except:
            print("I couldn't swap all your notes! Command aborted!", end="\n")
    elif the_input == "pcs":
        row = ""
        column = ""
        notes = the_matrix.get_clean_row()
        for n in range(len(notes)):
            row += str(notes[n])
            if n < len(notes)-1:
                row += " "
        notes = the_matrix.get_clean_column()
        for n in range(len(notes)):
            column += str(notes[n])
            if n < len(notes)-1:
                column += " "
        print("\nFirst row:", end="\n")
        a,b,c,d,e,f,g,h = tool.get_set_info(row)
        print(tool.build_set_info_msg(a,b,c,d,e,f,g,h))
        print("First column:", end="\n")
        a,b,c,d,e,f,g,h = tool.get_set_info(column)
        print(tool.build_set_info_msg(a,b,c,d,e,f,g,h))

while True:
    a = input()
    try:
        if a.lower() == "q" or a.lower() == "exit":
            print("That's all!", end="\n")
            break
        elif a.lower() == "n":
            the_matrix = Matrix(12, "") #To create an instance of Matrix()...
            print("I created a Matrix(). Now you can play with it...", end="\n\n")
        else:
            if not the_matrix == None:
                execute_user_input(a) #To execute user's input...
            else:
                print("You must create a new Matrix() first! Type 'n'.", end="\n\n")
    except:
        print("I couldn't do anything! Your input made me crash.", end="\n\n")

![logo](https://gitlab.com/musicaltools/musicaltools.gitlab.io/-/raw/themoststable/public/assets/img/logo_64.png)

# Cal Py Tools: Matrix()

**Matrix()** is the class of **Calpytools** that store a two dimensional matrix to control *pitch* over time.
It is based in the matrices proposed by [Robert Morris](https://en.wikipedia.org/wiki/Robert_Morris_(composer)).
There are two main goals of **Matrix()**. The first one is to make your work with these matrices easy, you can
build and operate them and print the results correctly formated in a terminal window. The second one is to
use them to control *pitch* and create random *musical textures* with **Texture()**.  

## matrix_cmd.py

You can use this tool to work with a **Matrix()** instance in a terminal window. It will print the available
commands for you but to avoid unnecessary misteries I will enumerate them here. Supossing you run *matrix_cmd.py*
and typed *n* to create a new empty matrix you can build your matrix typing:

- **type1**: to pass a list of notes separated by spaces ("0 1 4 5") and build a type one matrix (a matrix with
the same *pitch class set* in all rows and columns.  
- **type2**: to pass two list of notes separated by a dash ("0 1 4 5-0 1 3") and build a type two matrix (a
matrix with the first *pitch class set* in all rows and the second one in all columns.  
- **cycle**: to pass the first row of your matrix separating your cells with a dash ("0 1-2-3 4-5"). Then the program
will ask for a translation step (the number of semitones to translate your notes for each new row).  
- **chain**: to pass a *closed chain* with links separated by a dash ("0 1 2-3 4-5 6 7-...-0 1 2").  
- **random**: to pass *maximum number of elements in a cell*, *width* and *height* separated by spaces (4 4 4) and
build a random matrix.  

After building your *matrix* you can operate it using the following commands:

- **+n**: to translate all elements in the matrix *n* semitones.
- **i**: to invert all elements in the matrix.
- **t**: to transpose your matrix (rows become columns, columns become rows).
- **xn**: to multiply all elements in the matrix by *n*. Be careful here, only [coprime](https://en.wikipedia.org/wiki/Coprime_integers)
factors of 12 ensure the cardinality of the *pitch class set* in the matrix is maintained.  
- **s**: to shuffle the matrix status (reordering rows and columns).
- *swap a b ... n*: to swap the position of *a b ... n* elements in the matrix. Be careful here too, you
can only *swap* elements which are at least in two different cells of the matrix.
- **pcs**: to get the *pitch class set* information for the first row and the first column of the matrix. Most of
the time the other rows and columns contain the same *pitch class set* but that is not the case if you build a
random matrix.  

## What can Matrix() do?

Here are the functions inside **Matrix()** that you may want to call. Internal functions are not listed
here but you can read the comments in the code (which seems clear to me).  

### __init__(module, string_matrix)

You need to instance **Matrix()** to start working with it. You pass the *module* which will be 12 most
of the time and a *string_matrix* to load values. To start with an empty matrix you simply pass *""* as
the *string_matrix**.  

## random_matrix(max_elements, width, height)

To create a matrix of *width* columns and *height* rows with random content where the number of
elements in each cell will be between 0 and *max_elements*.  

## build_type_one([int_notes])

To build a *type 1* matrix where all rows and columns have the same *pitch class set*. 

## build_type_two([int_notes_a], [int_notes_b])

To build a *type 2* matrix where all rows have the *pitch class set a* and columns have *pitch class set b*.   

## translation_cycle(string_notes, translation)

To build a *matrix by translation cycle* where *string_notes* is formated like *"0 1-2--3"* (notes separated by
by spaces, cells separated by hyphens) and *translation* is a number. The size of the matrix depends on your
*translation* value. If you pass a wrong *string_notes* parameter **Matrix()** will truncate or extend it.  

## from_closed_chain(string_chain)

To build a *matrix* from a *chain*. The *string_chain* parameter is formated like *"0 1-2 5 8-...-0 1"* and must
have an odd number of *links*. **Matrix()** asumes your chain is closed to build the *matrix*. The function
returns a square matrix of size (links-1)/2.  

## translate(translation)

To update the *matrix* moving all its elements a *translation* number of semitones.  

## invert()

To update the *matrix* inverting all its elemnts (-element%self.mod for every element).  

## multiply(factor)

To update the *matrix* multiplying all its elements by the provided *factor* (element.factor%self.mod for every element).  

## transpose()

To transpose the *matrix* (turning the columns in rows and the rows in columns).  

## rotate(direction)

To rotate the matrix in the provided *direction*. If *direction* < 0 you obtain a clockwise 90° rotation else an anticlockwise
90° one). **Matrix()** rotate your *matrix* calling **transpose()** and adjusting *self.r_status* and *self.c_status*
afterwards.  

## swap_round()

To update the *matrix* running a round of a *swap* operation where all *swapable* elements are moved once.  

## swap_note(note)

To *swap* a random ocurrence of a certain *note* in the *matrix*.  

## swap_note_in_targets(note, [target_a, target_b])

To *swap* a *note* in both *target_a* and *target_b*, where targets are tupples of coordinates like
*[[r,c],[rr,cc]]*.  

## shuffle_status()

To set a new ramdom order for both rows and columns of the *matrix*.  

## shuffle_rows()

To set a new ramdom order for rows of the *matrix*.  

## shuffle_columns()

To set a new ramdom order for columns of the *matrix*.  

## set_status([new_r_status], [new_c_status])

To set a new order for both rows and columns of the *matrix*.  

## set_r_status([new_r_status])

To set a new order for rows of the *matrix*.  

## set_c_status([new_c_status])

To set a new order for columns of the *matrix*.  

## get_cell()

To get the notes in a *cell* in random order.  

## get_static_cell()

To get the notes in a *cell* without shuffling its order.  

## print_matrix()

To print the *matrix* in a terminal window in a clear formated way.  

## matrix_to_string()

To get the *formated string* that **Matrix()** prints when you call **print_matrix()**.  

## line_string()

To get a one line *formated string* from the *matrix*. You can save it and use it to load the
the *matrix* again calling **build_cells(your_string)** or **__init__(module, your_string)**.
I supose the most frequent way to use *your_string* would be creating a new instance of **Matrix(module,
your_string)**.  

## matrix_to_html()

To format the *matrix* as a **html** *<table>*.  

## matrix_to_latex()

To format the *matrix* as a *tabular environment* in **latex**.  

Feel free to contact me by [mail](mailto:rodrigovalla@protonmail.ch) or reach me in
[telegram](https://t.me/rvalla) or [mastodon](https://fosstodon.org/@rvalla).

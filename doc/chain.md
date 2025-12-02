![logo](https://gitlab.com/musicaltools/musicaltools.gitlab.io/-/raw/themoststable/public/assets/img/logo_64.png)

# Cal Py Tools: Chain()

**Chain()** is the class of **Calpytools** that can build *constant pitch class set sequences*. Taking a
*base pitch class set* as starting point, the software divides it into two *links*. Then looks for other
states of the *pcs* which includes a commnon *link*. In this way, you can obtain a sequence of notes
in which every sucesive pair of links corresponds to the same *pitch class set* (your *base pcs* clasification).
You can use it directly in a terminal window running **chain_cmd.py**.  

## chain_cmd.py

If you run this tool you can decide either to run in *debug* mode or normaly. In this case *debug* mode
is more interesting because shows in which set state the program decided to start and the space of
different states. The program needs to be configured first. You will be aks some questions:

- *Debug* mode?: yes - no.
- attempts?: the number of attempts looking for a closed chain.
- limits?: minumum maximum number of links for created chains.
- fallbacks?: number of times you allow the program to repeat the last link if it doesn't find any other.  

After creating your first chain you can operate with it typing:

- *n*: to call **Chain()**.*run()* and get a new sequence of notes.
- *i*: to invert your sequence.
- *+n*: to translate all elements in the chain *n* semitones.  

## What can Chain() do?

Here are the functions inside **Chain()** that you may want to call. Internal functions are not listed
here but you can read the comments in the code (which seems clear to me).  

### __init__(pcs, string_notes, link_min, link_max, max_degrading)

To instance a **Chain()** we need to provide:
- **pcs**: An instance of **PCS()**
- **string_notes**: A string of notes (0-11) as **"0 1 3 5 7"**.
- **link_min**: The desired minimum quantity of links.
- **link_max**: The desired maximum quantity of links.
- **max_degrading**: The number of times you can repeat the last link as in ...-**0 1 4**-5 8-**0 1 4**.  

### run()

This function is allways called at the end of **__init__** to build the chain but you can call it whenever you
want a new note sequence.  

### check_sequence()

You can use this function to confirm each pair of consecutive links add up the same *pitch class set*. This
is always *True* if you build the sequence with **run()** but not necesarily if you set a custom chain using
**set_chain(string_notes)** or alter **self.sequence** directly.  

### translate(semitones)

To translate the note sequence in pitch space the desired number of semitones.  

### invert()

To invert the note sequence in pitch space.  

### sequence_to_string()

To get the note sequence as a string.  

### candidates_to_string()

To print the *candidates matrix* which **Chain()** use to buile the note sequence.  

Feel free to contact me by [mail](mailto:rodrigovalla@protonmail.ch) or reach me in
[telegram](https://t.me/rvalla) or [mastodon](https://fosstodon.org/@rvalla).

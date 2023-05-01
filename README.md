![logo](https://gitlab.com/musicaltools/musicaltools.gitlab.io/-/raw/themoststable/public/assets/img/logo_64.png)

# Cal Py Tools

This is a set of tools written in [Python](https://www.python.org) to work with *pitch class sets*, *pitch matrices* and other different ways to control musical discourse. Many tools you find here existed previously in other of
my projects (sometimes written in other languages). You can find information about all of them in
[musicaltools.gitlab.io](https://musicaltools.gitlab.io/index_en.html).  

## PCS()

A *pitch class sets* analyzer. The program has all the functions needed to get Forte's clasiffication 
for a pitch class set. All *prime forms* are loaded from a database saved at *data/forte_prime_forms.csv*.
You can run **pcs_cmd.py** to use **PCS()** directly on the console. **PCS()** is also available
in [musiCal Bot](https://t.me/caltoolsbot).  

## Chain()

A constant *pitch class set sequence* generator. The program looks for different *links* (subsets) extracted
from a certain *pitch class set* and tries to concatanete the desired number of these *links*. The algorithm
looks for each *link* in all the different *states* of the proposed *pitch class set*.
You can run **chain_cmd.py** to use **Chain()** directly on the console. **Chain()** is also available
in [musiCal Bot](https://t.me/caltoolsbot).  

## Matrix()

The **Matrix()** class is an implementation of *pitch matrices*. It stores a two dimensional matrix of
musical notes in which each row and each column fullfill a constant *pitch class set* requirement. The
class implements different functions to work with a **Matrix()** instance. The class is inspired in
the matrices proposed by [Robert Morris](https://en.wikipedia.org/wiki/Robert_Morris_(composer)).
**Matrix()** will be available in [musiCal Bot](https://t.me/caltoolsbot).  

## m21Score()

A **m21Score()** object is a [music21 Score](https://web.mit.edu/music21/) object with some specific
functions to make other tools here (for example **Matrix()**) sound.  

## Texture() and ChainMelody()

The classes that extends **m21Score()** to create music from a **Matrix()** instance or **Chain()**
notes sequence.  

Feel free to contact me by [mail](mailto:rodrigovalla@protonmail.ch) or reach me in
[telegram](https://t.me/rvalla) or [mastodon](https://fosstodon.org/@rvalla).

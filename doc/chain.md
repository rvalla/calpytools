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

Feel free to contact me by [mail](mailto:rodrigovalla@protonmail.ch) or reach me in
[telegram](https://t.me/rvalla) or [mastodon](https://fosstodon.org/@rvalla).

![logo](https://gitlab.com/musicaltools/musicaltools.gitlab.io/-/raw/themoststable/public/assets/img/logo_64.png)

# Cal py tools: changelog

## 2025-05-21: v0.3.1 beta

Errors found in **Matrix()** were solved. Building a *matrix by translation cycle*
crashed when the user pass an incomplete first row. A new script **matrix_cmd.py**
allows the user to create and operate matrices directly on a terminal.  

## 2025-05-07: v0.3.0 beta

**Matrix()** seems complete now. The *swap* operation is implemented. New
*transposition*, *scalar multiplication* and *rotations* operations. New
functions to format the *matrix* as *html* and *latex*.   

## 2025-04-22: v0.2.5 alpha

**Matrix()** was improved a lot. Now you can start an empty *matrix* and then build
one by type (type 1, type 2, by translation cycle, from closed chain and random
methods are available. Implementing the *swap* operation is pending.  

## 2023-05-10: v0.2.0 alpha

**Texture()** and **Counterpoint()** are ready to create music now. **Chain()** is
capable of creating *constant pitch class set notes sequences*.  
A new *examples* folder stores files that can be useful to start using some of the
**Calpytools**.  

## 2023-04-22: v0.1.1 alpha

Problems finding *prime forms* were solved. A new script **pcs_cmd.py** is added to run
pitch class sets analysis directly in console, including a *debug mode*. Several comments
to the code were added.  

## 2023-04-22: v0.1 alpha

Testing new tool to analyze Forte's pitch class sets. Adding *pcs_cmd* to check pitch sets on
a terminal window. There are issues with the algorithm to find *prime forms*.   

For more information visit [musicaltools.gitlab.io](https://musicaltools.gitlab.io/index_en.html).  
Feel free to contact me by [mail](mailto:rodrigovalla@protonmail.ch) or reach me in
[telegram](https://t.me/rvalla) or [mastodon](https://fosstodon.org/@rvalla).

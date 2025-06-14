![logo](https://gitlab.com/musicaltools/musicaltools.gitlab.io/-/raw/themoststable/public/assets/img/logo_64.png)

# Cal Py Tools: PCS()

**PCS()** is the class of **Calpytools** that can analyze a set of notes and search for its *prime form*
in Allen Forte's database. It has some functions you can find useful apart from checking *pitch class sets*
clasification. You can use it directly in a terminal window running **pcs_cmd.py**.  

## pcs_cmd.py

If you run this tool you can decide either to run in *debug* mode or normaly. *Normal* mode will display
*pitch class set* information while *debug* mode will show some other data including candidates considered
when looking for the prime form. Little secret: if you type *forte* the program will analyse all prime forms
in the database (util if you note an error).  

## What can PCS() do?

Here are the functions inside **PCS()** that you may want to call. Internal functions are not listed
here but you can read the comments in the code (which seems clear to me).  

### __init__()

You need to instance **PCS()** to load the *prime_forms** and some other data needed.  

## get_set_info(string_notes)

If you call this function with a string of notes (0-11) as *"0 1 5 3 11"* you will get:

- **cardinality**: the number of elements.
- **ordinal**: the position of the set in Forte's list.
- **interval**: the distance between the *ordered form* and the *prime form*.
- **is_inverted**: *True* if the set is inverted.
- **z_pair**: if there is a *Z* related set its position in Forte's list.
- **states**: the number of available states (always <= 24).
- **ordered_form**: the *ordered form*.
- **prime_form**: the *prime form*.

## interval_vector([int_notes])

Returns a classic Forte interval vector from a list of notes represented as integers.  

## big_interval_vector([int_notes])

Returns an interval vector of 11 interval classes (considers inverted interval as different ones).  

## build_set_info_msg(cardinality, ordinal, interval, is_inverted, z_pair, states, ordered_form, prime_form)

Returns a well formated string with all pcs information.   

## prime_form([int_notes])

Returns the *prime form* for the set you pass as a list of notes represented by integers.  

## ordered_form([int_notes])

Returns the *ordered form* for the set you pass as a list of notes represented by integers.  

## get_states_matrix([int_notes])

Returns a list containing all different states for the set you pass as a list of notes
represented by integers.  


Feel free to contact me by [mail](mailto:rodrigovalla@protonmail.ch) or reach me in
[telegram](https://t.me/rvalla) or [mastodon](https://fosstodon.org/@rvalla).

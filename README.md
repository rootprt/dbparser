# DBParser
Sort databases with the dbparser.py tool

## INSTALLATION:
You will need argparse to run this tool.

```
pip install argparse
```

Simply clone the repository and open the dbparser folder to get started.

```
git clone https://github.com/prtcanfly/dbparser.git
cd dbparser
```

## BASIC USAGE:

```
python dbparser.py -i input_file -s search_term
```

## EXTRA PARAMETERS:
-o OUTPUTFILE - Default is "dbparse.txt"

-e EXCEPTION - Make exceptions for parsing the database

### Example:

```
python dbparse.py -i example.txt -s hello -o example2.txt -e world
```

This would give you a parsed copy of example.txt as a file called example2.txt that only includes "hello", and specifies that if "world" is in the line, not to bring it over to example2.txt.

# ENCODING TYPE:

### YOU PROBABLY WONT NEED THIS
Sometimes filetypes are written with different encoding styles. The preset for DBParser is utf-8, but it can be changed in the source code.

Easy to use, just run encoding_type.py and input the file path. If it's anything other than utf-8; replace the "utf-8" section in dbparser.py with whatever the encoding type is.

```
python encoding_type.py
Enter File Path: [File/Path/Here]

 Encoding: utf-8
```

#### But as I said, you probably won't have to do this; as utf-8 is the standard.

# The Simplex method

This is an implementation of the simplex method for solving linear programs

## Dependencies
- argparse

## Usage

The programs accepts linear programs in the following form:
```
max cx
```
subject to
```
Ax <= b
```
and it accepts 4 arguments. 

- -f: the name of file where a linear program is described. The file must be orginized as follows. The first line is an integer representing the number of variables. The second line contains integer m representing the number of constraints. The next two lines contain vectors c and b, respectively. The coordinates of c (and b) are separated by whitespace. The coordanates can be rational numbers of the form 'a/b'. The next m lines contain description of matrix A. The ith line describes the ith row of A. Folder tests contains some examples.

- -p: pivot rule to be used for the simplex method. You can specify one of the following: 'bland', 'max_coef' and 'random' which represents Bland's rule, maximum coefficient rule and random rule, respectively. This argument is optional. If it is not specified, the Bland's rule will be used.

- -v: verbose mode. If this argument is true, the dictionary on each iteration will be printed as well as some other information refering to Phase 1.

- -iter-num: maximum number of iterations. If this is not specified, the number of iterations is not set at all. 


## Examples

To run the program with an LP defined in file input.dat, run the following:
```
python3 main.py -f input.dat
```

To run the program in verbose mode:
```
python3 main.py -f input.dat -v True
```

To choose the pivot rule:

```
python3 main.py -f input.dat -p max_coef
```

You can find a more detailed description in the file Report/Readme.pdf

## License

MIT License

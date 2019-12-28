# permutations-subset
The main idea of the project is to return successor or predecessor of given combinatorial object using rank() and unrank() functions.

## How to start
Install `docopt` library via `pip` 

```pip install docopt==0.6.2```

Then simply run `main.py` file according to the following parameters:
 * --vertex=VERTEX      Comma separated list of numbers
 * --k=&lt;k>              Number describes length of vertex
 * --n=&lt;n>              Number describes range of numbers
 * --nextPos=&lt;nextPos>  Describes if we want to get successor (1) or predecessor (-1)
 
 And so sample call looks like
 
 ``` python main.py --vertex=1,2,3 --k=3 --n=4 --nextPos=1```

## Resources
[Generating Elementary Combinatorial Objects](https://www.site.uottawa.ca/~lucia/courses/5165-09/GenCombObj.pdf)
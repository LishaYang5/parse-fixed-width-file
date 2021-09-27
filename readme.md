# Parse fixed width file

## Requirements

1. Generate a fixed width file using the provided spec (offset provided in the spec file represent the length of each field).
2. Implement a parser that can parse the fixed width file and generate a delimited file, like CSV for example.
3. DO NOT use python libraries like pandas for parsing. You can use the standard library to write out a csv file (If you feel like)
4. Language choices (Python or Scala)
5. Deliver source via github or bitbucket
6. Bonus points if you deliver a docker container (Dockerfile) that can be used to run the code (too lazy to install stuff that you might use)
7. Pay attention to encoding

## Assumptions

1. Column names are "f1","f2","f3","f4","f5","f6","f7","f8","f9","f10"
2. The number of column's length means the number of values in each column.
3. Column "f1" has 5 values.
4. Column "f2" has 12 values.
5. Column "f3" has 3 values.
6. Column "f4" has 2 values.
7. Column "f5" has 13 values.
8. Column "f6" has 7 values.
9. Column "f7" has 10 values.
10. Column "f8" has 13 values.
11. Column "f9" has 20 values.
12. Column "f10" has 13 values.

## Version
Python 3.8.8
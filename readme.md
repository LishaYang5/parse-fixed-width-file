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
2. Values in colums are string

## Files

1. 'src' folder contains the function to generate a csv file based on the requirement of width.
2. 'core' folder contains funtion to get 'csv_dct.csv' file, which is the required file template.
3. 'app' folder contains functions to parse data(parser.py) and test the parser(testParser).
4. 'parsed.csv' is generated automatically after run 'testParser.py'.

## Main Process

1. Use 'src/generate_csv.py' to generate csv file.
2. Use 'app/testParser.py' to test the parser

## Version

Python 3.8.8
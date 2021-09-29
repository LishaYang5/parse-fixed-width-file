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

1. Use 'main.py' to generate csv file and use 'test.csv' file to test the parser and get the parsed csv file
2. The 'parser.py' would parse test.csv and csv_par.csv. 
3. If the length of column in test.csv is longer than that in csv_par.csv, the length would be cut into the same column to match the same length in csv_par.csv. 
4. If the length of column in test.csv is shorter than that in csv_par.csv, the length would be added addtional value('*') into the same column to match the same length in csv_par.csv.

## Use Docker
1. Remove parsed_csv.csv and csv_par.csv
2. Docker build image
  'docker build -t par .'
3. Run docker 
  'docker run -p 8080:8080 -v <local path>/parse-fixed-width-file/app:/app -it par'



## Limitation and future work

1. The data in test.csv has just one row. It could be add more values in the future.
2. All values in each column are predefined as string type. They could be more types like list, int, dictionary.

## Version

Python 3.8


One can easily run this mapper reducer program on their local. 

To do so, give the output of the dataset files to the mapper by piping it and then the output of the mapper to the reducer by piping it as shown in the command below.

`cat ./data/DVD-testing.csv | ./mapper.py | ./reducer.py`
# Find Pairs 

Current project consist in an application that finds pairs of integers from a list that
sum to a given value.

## Table of Contents

- [Find Pairs ](#project-name)
- [Table of Contents](#table-of-contents)
- [Description](#description)
- [Installation](#installation)
- [Usage](#usage)
- [License](#license)

## Description

Developed application finds pairs of integers from a list that
sum to a given value. The application takes as input the list of numbers as
well as the target sum. It is assumed that all input values are integers and that there aren't
any repeat values in the list.

Unit tests of the core application runs by calling the core function script find_pairs.py

## Installation

No especial packages are required to run the main script of this application.
Python version used was : Python 3.11.1

Two files have to be placed in the working directory: 
- find_pairs.py : which have the core function of the project 
- app.py: which contains the main function of the project

## Usage

​The main script `app.py` takes as command line
arguments a comma separated list of integers, and the target sum.

Usage: python app.py comma-separated-list-of-numbers target-sum

Example of input in the command window:
python app.py 1,9,5,0,20,-4,12,16,7 12

​Corresponding result:
+ 12 , 0
+ 5 , 7
+ 16 , -4
  
## License

MIT License

Copyright (c) 2023 Ronald Garzón Bohórquez

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

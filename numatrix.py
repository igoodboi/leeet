"""
PROBLEM STATEMENT:
Numbrix is an n x n grid number puzzle.
The objective is to fill the grid with all of the integers from 1 to n^2 by placing all missing integers, x, in the grid such that both x - 1 and x + 1 are
adjacent to it, in the same row or the same column.
In this problem, you will be given the grid size, n, and the integers 1 through n', inclusive, that fill the grid in row-major order.
All missing numbers are represented by O.
 Your task is to determine the missing numbers and output them in row-major order.
We guarantee that:
• Missing numbers will never be adjacent to each other, horizontally, vertically, or diagonally.
• The integers 1 and n^2 will never be one of the missing numbers.
• There will be no more than 2n missing numbers.
TASK:
Complete the function fillPuzzle
• The function has 2 parameters: n, an integer representing the size of the grid, and numbers, a string of n^2
integers that is used to create a Numbrix puzzle in a two-dimensional array.
• The function returns a string of the missing numbers, listed in row-major order, each separated by a single space.
You may create additional functions that are called from fillPuzzle if needed in solving the problem.
CONSTRAINTS:
The value of n will be between 4 and 9, inclusive. Each string will contain exactly n^2 integers, some O, all others between 1 and n^2, inclusive.
Missing numbers will never be adjacent to each other horizontally, vertically, or diagonally. The numbers 1 and n^2 will never be one of the missing numbers.
There will be no more than 2n missing numbers.
DATA PROVIDED:
There are 6 sets of Sample Data for debugging and 6 sets of Test Data for scoring. The test cases will vary in difficulty.
You should create sample data of your own to fully test your program.
"""

# !/bin/python3

import math
import os
import random
import re
import sys


#
# Complete the 'fillPuzzle' function below.
#
# The function is expected to return a STRING.
# The function accepts following parameters:
#  1. INTEGER n
#  2. STRING numbers
#
def fillPuzzle(n, numbers):
    # Write your code here
    matrix = parse(n, numbers)
    print(matrix)
    #zeros, losts = find(matrix)
    #orderer = finorder(zeros, matrix, losts)

    # RETURN!!!😀😇🇺🇸🏈😀🦅
    pass
def assemblee(orderer):
    # assemble back into row major order and..............

    pass

def parse(n, numbers):
    # convert string to lst w/ split
    n = int(n)
    numlst = numbers.split()
    numlst = [int(b) for b in numlst]
    # break this into square using row major order
    matrix = []
    for i in range(n):
        row = [numlst[j] for j in range(i*n,i*n+n)]
        matrix.append(row)
    return matrix

def find(matrix):
    zerocont = []
    lostscont = []
    # find the zero using 2 for loop
    # find the missing nuumber order doesn't matter
    pass


def finorder(zeros, matrix, losts):
    # find use ice and barge into peoples to deport them adjacent x-1 and x+1
    pass


if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')
    n = "4"
    numbers = "1 4 5 0 0 3 8 7 11 10 0 16 0 13 14 15"

    result = fillPuzzle(n, numbers)
    print(result)
    #print("expected")
    #print("6C JC 7S KS 5C E 7D E")

    # fptr.write(result + '\n')

    # fptr.close()

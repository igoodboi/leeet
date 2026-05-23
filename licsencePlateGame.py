"""
"""

# !/bin/python3

import math
import os
import random
import re
import sys


def countSolutions(target, plate):
    # Write your code here
    # extract digits
    digits = [int(c) for c in plate if c.isdigit()]
    unused = {}
    for d in digits:
        if d in unused:
            unused[d] += 1
        else:
            unused[d] = 1
    ops = {"-": 1, "+": 1, "*": 1, "/": 1, "^": 1}
    # cylce thru num and opr for target
    # backtracking
    counter = [0]

    def recurse():
        for op in ops:
            if ops[op] == 0:
                continue
            expr.append(op)
            ops[op] -= 1
            for k in unused:
                if unused[k] == 0:
                    continue
                expr.append(k)
                unused[k] -= 1
                if myeval(expr) == target:
                    print(expr)
                    counter[0] += 1
                recurse()
                expr.pop()
                unused[k] += 1

            expr.pop()
            ops[op] += 1

    expr = []
    for d in digits:
        expr.append(d)
        unused[d] -= 1
        recurse()
        expr.pop()
        unused[d] += 1
    print(counter)

def myeval(expr):
    stack = list(reversed(expr))
    while len(stack) > 1:
        a, op, b = stack.pop(), stack.pop(), stack.pop()
        if op == '+':
            stack.append(a + b)
        elif op == '-':
            stack.append(a - b)
        elif op == '*':
            stack.append(a * b)
        elif op == '/':
            if b == 0:
                return None
            stack.append(a // b)
        elif op == '^':
            stack.append(int(pow(a,b)))
    return stack.pop()


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    #    target = int(input().strip())
    target = 144

    #    plate = input()
    plate = "F11235"

    result = countSolutions(target, plate)

    fptr.write(str(result) + '\n')

    fptr.close()

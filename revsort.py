"""
PROBLEM STATEMENT:
Given a list of distinct integers, determine the number of reversal moves required to sort the list into increasing order. Each move involves reversing a portion of the list, always starting with the first (left-most) integer. The part to reverse is governed by the following three prioritized rules, which are applied repeatedly while the list is not yet sorted:
1. If the list begins with an increasing sequence of two or more integers reverse this entire starting sequence.
2. If the first integer is the largest in the list, reverse the entire list.
3. Otherwise, reverse the segment of the list that positions the current first integer immediately before its next larger integer in the list. For example, in the list 716 8, reverse the 716 so the 7 is immediately prior to the 8, making the list 6 1 7 8.
Output the number of reversal moves necessary to sort the initial list.
EXAMPLE:
Input
-5 27 39
56 23 41

Output
5

Explanation
Original List
-5 27 39 56
23
41

1
The list starts with an increasing sequence of -5 27 39 56; reverse it.
(Rule #1)
56 39
27-5
23
41

2
The first number, 56, is the largest.
Reverse all elements of the list. (Rule #2)
41
23 -5 27
39
56

3
The first element, 41, should go just before 56, so reverse the list up to the number before 56.
(Rule #3)
39
27 - 5
23
41
56

4
The first element, 39, should go just before 41. Reverse the first 4 numbers. (Rule #3)
23
-5 27
39
41
56

5
The first element, 23, should go just before 27. Reverse the first 2 numbers. (Rule #3)
-5
23
27
39
41
56

At this point, the list is in sorted order.
Output 5, the number of reversal moves.

TASK:
Complete the function countReversals
• The function has 1 parameter: a string of unique integers,
 values, representing the integers in the list to be reversed, each separated by a single space.
• The function returns an integer representing the number of moves needed to create a list in the correct order.
You may create additional functions that are called from countReversals if needed in solving the problem.
CONSTRAINTS:
There will be no more than 50 integers in the list.
"""

# !/bin/python3

import math
import os
import random
import re
import sys


#
# Complete the 'countReversals' function below.
#
# The function is expected to return an INTEGER.
# The function accepts STRING values as parameter.
#
def countReversals(values_str):
    # Convert input string to a list of integers
    arr = [int(x) for x in values_str.split()]
    moves = 0

    # Target is a sorted version of the list
    sorted_arr = sorted(arr)

    while arr != sorted_arr:
        # Rule 1: Starts with an increasing sequence of two or more
        i = 0
        while i + 1 < len(arr) and arr[i] < arr[i + 1]:
            i += 1

        if i > 0:
            # Reverse the increasing prefix (from index 0 to i)
            arr[0:i + 1] = reversed(arr[0:i + 1])

        # Rule 2: First integer is the largest
        elif arr[0] == max(arr):
            arr.reverse()

        # Rule 3: Position first integer before its next larger neighbor
        else:
            first = arr[0]
            # Find the smallest number in the list that is larger than arr[0]
            next_larger = min(x for x in arr if x > first)
            # Find the index of that next larger number
            target_idx = arr.index(next_larger)
            # Reverse the segment up to the element before the next larger one
            arr[0:target_idx] = reversed(arr[0:target_idx])

        moves += 1

    return moves


# Example Test
input_str = "-5 27 39 56 23 41"
print(f"Moves required: {countReversals(input_str)}")  # Expected Output: 5

# Test with the example from the image
print(countReversals("-5 27 39 56 23 41"))  # Output: 5

if __name__ == '__main__':
    #   fptr = open(os.environ['OUTPUT_PATH'], 'w')

    values = input()

    result = countReversals(values, str)

#    fptr.write(str(result) + '\n')

#   fptr.close()

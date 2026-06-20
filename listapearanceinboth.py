"""
Problem Statement:
Check whether the first entered list appears as one item inside the second list.

Input: Two space-separated lists of integers
Output: present if the first list is contained as an item; otherwise Not present
Example: Inputs: 1 2 and 1 2 3 -> Output: Not present
"""

n=list(map(int,input("Enter list of number: ").split()))
a=list(map(int,input("Enter list of number: ").split()))
if n in a:

    print("present")
else:
    print("Not present")

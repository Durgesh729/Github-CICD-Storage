"""
Problem Statement:
Convert a list of integers into a tuple.

Input: Space-separated integers
Output: The tuple and its data type
Example: Input: 1 2 3 -> Output: (1, 2, 3) <class 'tuple'>
"""

n=list(map(int,input("Enter number to store in list: ").split()))
t=tuple(n)
print(t,type(t))

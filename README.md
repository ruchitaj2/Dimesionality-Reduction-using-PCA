# Curse of Dimensionality

## Overview: 
Due to curse of dimensionality distances become meaningless in high-dimensional spaces. That is, the minimum distance between random pairs of nodes becomes really close to the maximum distance between such pairs. 
In this problem, you are going to verify this phenomenon.

## Objective: 
Write a program in Python, or MATLAB that
1. Generates n d-dimensional random points. 
2. Computes the maximum and minimum distance using euclidean distance between alln 2pairs of nodes (i.e., O(n2) operations).
Denote these values as max(d,n) and min(d,n) respectively.

3. Computes γ(d,n) = log max(d,n)−min(d,n) min(d,n) 

Change n in range 100 ≤ n ≤ 1,000 and d in range 1 ≤ d ≤ 100 and assume that feature values are in range [0,100] (or some other ﬁxed range). 
Compute γ(d,n) using your program and plot the 3-D surface of γ(d,n) in MATLAB or your programming language of choice. 
How does the surface change with respect to n? Perform the same experiment, but this time using `1 norm for computing distances (Book, Page 70) and plot the surface. Submit your code and your two plots.




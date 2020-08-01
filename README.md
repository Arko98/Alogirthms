# Alogirthms
A collection of some of the most frequently used Algorithms in C++. This repository consists of some of the most frequently used algorithms which can be used as ideal example for learning purpose.

## Contents
1. Merge Sort
2. Greedy Fractional Knapsack
3. Breadth First Search
4. Depth First Search
5. Chain Matrix Multiplication (Dynamic Programming)
6. Floyd Warshall (Dynamic Programming)
7. Fibonacci Series (Dynamic Programming)
8. Bellman Ford Single Source Shortest Path

## Description
### 1. Merge Sort
Merge Sort is a Divide and Conquer algorithm. It divides input array in two halves, calls itself for the two halves and then merges the two sorted halves. The merge() function is used for merging two halves. The merge(arr, l, m, r) is key process that assumes that arr[l..m] and arr[m+1..r] are sorted and merges the two sorted sub-arrays into one
### 2. Greedy Fractional Knapsack
Given weights and values of n items, we need to put these items in a knapsack of capacity W to get the maximum total value in the knapsack. A brute-force solution would be to try all possible subset with all different fraction but that will be too much time taking. An efficient solution is to use Greedy approach. The basic idea of the greedy approach is to calculate the ratio value/weight for each item and sort the item on basis of this ratio. Then take the item with the highest ratio and add them until we can’t add the next item as a whole and at the end add the next item as much as we can. Which will always be the optimal solution to this problem.
### 3. Breadth First Search
Breadth First Traversal (or Search) for a graph is similar to Breadth First Traversal of a tree. The only catch here is, unlike trees, graphs may contain cycles, so we may come to the same node again. To avoid processing a node more than once, we use a boolean visited array. For simplicity, it is assumed that all vertices are reachable from the starting vertex.
### 4. Depth First Search
Depth First Traversal (or Search) for a graph is similar to Depth First Traversal of a tree. The only catch here is, unlike trees, graphs may contain cycles, so we may come to the same node again. To avoid processing a node more than once, we use a boolean visited array.
### 5. Chain Matrix Multiplication (Dynamic Programming)
Given a sequence of matrices, find the most efficient way to multiply these matrices together. The problem is not actually to perform the multiplications, but merely to decide in which order to perform the multiplications.
We have many options to multiply a chain of matrices because matrix multiplication is associative. In other words, no matter how we parenthesize the product, the result will be the same. For example, if we had four matrices A, B, C, and D, we would have 
(ABC)D = (AB)(CD) = A(BCD) = ....  However, the order in which we parenthesize the product affects the number of simple arithmetic operations needed to compute the product, or the efficiency.
### 6. Floyd Warshall (Dynamic Programming)
The Floyd Warshall Algorithm is for solving the All Pairs Shortest Path problem. The problem is to find shortest distances between every pair of vertices in a given edge weighted directed Graph. We initialize the solution matrix same as the input graph matrix as a first step. Then we update the solution matrix by considering all vertices as an intermediate vertex. The idea is to one by one pick all vertices and updates all shortest paths which include the picked vertex as an intermediate vertex in the shortest path. When we pick vertex number k as an intermediate vertex, we already have considered vertices {0, 1, 2, .. k-1} as intermediate vertices. For every pair (i, j) of the source and destination vertices respectively, there are two possible cases.
1) k is not an intermediate vertex in shortest path from i to j. We keep the value of dist[i][j] as it is.
2) k is an intermediate vertex in shortest path from i to j. We update the value of dist[i][j] as dist[i][k] + dist[k][j] if dist[i][j] > dist[i][k] + dist[k][j]
### 7. Fibonacci Series (Dynamic Programming)
The Fibonacci numbers are the numbers in the following integer sequence.
0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, ……..
In mathematical terms, the sequence Fn of Fibonacci numbers is defined by the recurrence relation: 
  Fn = Fn-1 + Fn-2
with seed values
   F0 = 0 and F1 = 1.
We can optimize the space used in method 2 by storing the previous two numbers only because that is all we need to get the next Fibonacci number in series.
### 8. Bellman Ford
The Bellman Ford Algorithm is for solving the Single Pairs Shortest Path problem. The problem is to find shortest distances between a source vertex and every other vertices in a given edge weighted directed Graph. The key rule is: 
For every edge e = (v1,v2), we update the value of dist[v2] as dist[v1] + Weight[v1][v2] if dist[v2] > dist[v1] + Weight[v1][v2]

def max(x, y):
    if(x > y):
        return x
    else:
        return y
class node :
    def __init__(self):
        self.data = 0
        self.left = self.right = None
def LISS(root):
 
    if (root == None) :
        return 0

▲
Related Articles
Largest Independent Set Problem | DP-26
Subset Sum Problem | DP-25
Subset Sum Problem in O(sum) space
Subset with sum divisible by m
Largest divisible pairs subset
Perfect Sum Problem (Print all subsets with given sum)
Recursive program to print all subsets with given sum
Print sums of all subsets of a given set
Program to reverse a string (Iterative and Recursive)
Print reverse of a string using recursion
Write a program to print all permutations of a given string
Print all distinct permutations of a given string with duplicates
Permutations of a given string using STL
All permutations of an array using STL in C++
std::next_permutation and prev_permutation in C++
Lexicographically next permutation in C++
How to print size of array parameter in C++?
How to split a string in C/C++, Python and Java?
boost::split in C++ library
Tokenizing a string in C++
getline() function and character array
getline (string) in C++
How to use getline() in C++ when there are blank lines in input?
scanf() and fscanf() in C – Simple Yet Powerful
getchar_unlocked() – faster input in C/C++ for Competitive Programming
0-1 Knapsack Problem | DP-10
Largest Sum Contiguous Subarray
Program for Fibonacci numbers
Longest Common Subsequence | DP-4
Longest Increasing Subsequence | DP-3

Largest Independent Set Problem | DP-26
Difficulty Level : Medium
Last Updated : 19 Jul, 2021
Given a Binary Tree, find size of the Largest Independent Set(LIS) in it. A subset of all tree nodes is an independent set if there is no edge between any two nodes of the subset. 

For example, consider the following binary tree. The largest independent set(LIS) is {10, 40, 60, 70, 80} and size of the LIS is 5.



Recommended: Please try your approach on {IDE} first, before moving on to the solution.
A Dynamic Programming solution solves a given problem using solutions of subproblems in bottom up manner. Can the given problem be solved using solutions to subproblems? If yes, then what are the subproblems? Can we find largest independent set size (LISS) for a node X if we know LISS for all descendants of X? If a node is considered as part of LIS, then its children cannot be part of LIS, but its grandchildren can be. Following is optimal substructure property.

1) Optimal Substructure: 
Let LISS(X) indicates size of largest independent set of a tree with root X. 




     LISS(X) = MAX { (1 + sum of LISS for all grandchildren of X),
                     (sum of LISS for all children of X) }
The idea is simple, there are two possibilities for every node X, either X is a member of the set or not a member. If X is a member, then the value of LISS(X) is 1 plus LISS of all grandchildren. If X is not a member, then the value is sum of LISS of all children.

2) Overlapping Subproblems 
Following is recursive implementation that simply follows the recursive structure mentioned above. 

C++
C
Java
Python3
# A naive recursive implementation of
# Largest Independent Set problem
 
# A utility function to find
# max of two integers
def max(x, y):
    if(x > y):
        return x
    else:
        return y
 
# A binary tree node has data,
#pointer to left child and a
#pointer to right child
class node :
    def __init__(self):
        self.data = 0
        self.left = self.right = None
 
# The function returns size of the
# largest independent set in a given
# binary tree
def LISS(root):
 
    if (root == None) :
        return 0
 
    # Calculate size excluding the current node
    size_excl = LISS(root.left) + LISS(root.right)
 
    # Calculate size including the current node
    size_incl = 1
    if (root.left != None):
        size_incl += LISS(root.left.left) + \
                    LISS(root.left.right)
    if (root.right != None):
        size_incl += LISS(root.right.left) + \
                    LISS(root.right.right)
 
    # Return the maximum of two sizes
    return max(size_incl, size_excl)
 
# A utility function to create a node
def newNode( data ) :
 
    temp = node()
    temp.data = data
    temp.left = temp.right = None
    return temp
root = newNode(20)
root.left = newNode(8)
root.left.left = newNode(4)
root.left.right = newNode(12)
root.left.right.left = newNode(10)
root.left.right.right = newNode(14)
root.right = newNode(22)
root.right.right = newNode(25)
 
print( "Size of the Largest"
        , " Independent Set is "
        , LISS(root) )

 
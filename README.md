# data-structures
Non-paired data structures work

Add documentation of your new method to your README file. Include any sources or collaborations. It is a requirement that for each method of this data structure, you include in the README a description of its time complexity in Big-O notation! Expect to lose credit if you don’t have this.



***Binary Search Tree***
insert
O(log n) Because it "halves" the tree each time it moves by only traversing one direction based on a value comparison.
O(n) as a complete worst case scenario, if the tree is balanced improperly, and all the nodes are in a single line, the function  could have to go through every node to find the proper insertion spot.

search
O(log n) Because it "halves" the tree each time it moves by only traversing one direction based on a value comparison.
O(n) as a complete worst case scenario, if the tree is balanced improperly, and all the nodes are in a single line, the search could have to go through every node to find the value.

size
O(1). Because we increment the size value of the tree when we insert and delete, so the size value is a lookup of the tree's attribute.


depth
O(n) This ends up being O(n) because it is actually recursing through every node in the tree to measure its depth. 

contains
This will be the same as the search function because all it does is call the search function and return a boolean based on whether the search function returns something or not.

balance
O(log n) or O(n) Requires the use of the depth function which ends up being O(log n) or O(n) if the tree is unbalanced.  Once the rotations are implemented this will be O(log n).


delete
[![Build Status](https://travis-ci.org/RJB888/data-structures.svg?branch=deletion)](https://travis-ci.org/RJB888/data-structures)
O((log n)k)I believe this is what it would be.  It runs the search function first, so the best it could be is O(log n) same as the search function.  The k comes in due to the fact that in some of the delete methods we havet to step over one node, then work down the node tree as far as it can go in one direction.. so "k" more steps depending on how far the branch goes.

breadth first traversal
O(n) This traverses all of the nodes in the tree and yields them.

in order traversal
O(n) Traverses all of the nodes in the tree and yields them.

pre order traversal
O(n) Traverses all of the nodes in the tree and yields them.

post order traversal
O(n) Traverses all of the nodes in the tree and yields them.

Acknowledgements:
Un3qual @ StackOverflow for depth algorithm,
Gabriel Meringolo for assistance with the traversals,
Michael McMillan - Data Structures and Algorithms with JavaScript


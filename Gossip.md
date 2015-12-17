# Gossip

## Math 
* Fraction to Recurring Decimal: Simple, but with many corner cases
* Pow(x, n): Corner case, binary division 

## Array
* 4sum, not similar to 2sum, optimization by several well-designed conditions.
* 3sum, similar to 4sum, but really requires O(n^2) time complexity
* 3Sum Closest, Not hard, very similar to 3sum

* Game of Life: Another Integral Image problem 
  
## Hash 
* Maximum Product of Word Lengths: Bit Hash, no worry about O(n^2) search cost
* Super Ugly Number: A trick in eliminating duplicate minimum when finding minimum

## Bit Manipulation 
* Bitwise AND of Numbers Range: Idea is interesting. Write down the binary representation, find clues. 
* Reverse Bits: Easy, no explanation
* Single Number II: Interesting, but watch out for corner case

## Tree Related 

* Binary Tree Right Side View, Simple solution by level order traversal 
* Count Complete Tree Nodes: Cheating, but works 

* Populating Next Right Pointers in Each Node, No idea the meaning of 'constant space'
* Populating Next Right Pointers in Each Node II, AC, but solution is wrong since not only use constant space

* Kth Smallest Element in a BST: Binary Search Tree In-order Traversal

* Binary Search Tree Iterator: Very simple data structure problem 
* Peeking Iterator: Very basic data structure
* Find Peak Element: Use three pointers to do search in logarithm time 
* H Index II: Corner case, DO it again 

* Balanced Binary Tree: Based on Maximum Depth of Binary Tree, simple
* Sum Root to Leaf Numbers: Level-order BFS, simple

## Search 

* Search a 2D Matrix II: Design Reasonable Path 
* Search for a Range: Binary Search, corner case
* Longest Increasing Subsequence: using dynamic programming, no idea how to use O(NLogN)
* Kth Largest Element in an Array: Based on quick sort

## List or Pointer 
* Rotate List: Just try to fool you by different corner case 
* Remove Duplicates from Sorted Array II: Simple, just use two pointers 
* Partition List: Two Pointers, very simple
* Container With Most Water: This one is very simple. Just have problems to understand question. 
* Linked List Cycle II: Very Tricky, see proof 
* Find the Duplicate Number: Could use Linked List Cycle II to solve it, very tricky. 

## Back Tracking 

* Gray Code: Use reversed engineering by Run Code
* Letter Combinations of a Phone Number: Very simple
* Combinations: Very simple, watch out corner case
* Combination Sum III: Not very hard, the time is not a big issue
* Combination Sum: Watch out for corner case
* Combination Sum II: Almost same as Combination Sum III
* Subsets: Very simple
* Subsets II: Watch out corner case
* Jump Game: Think reversely. 
* Restore IP Addresses: Just corner cases

## Dynamic Programming 

* House Robber II: Can we break the circle? How? 
* Maximum Product Subarray: O(N) Algorithm, watch out the objective function
* Decode Ways: Corner Cases
* Unique Paths II: Corner Cases
* Maximal Square: Remember Integral Image!!!! We need to pad zero on the top and left 

## Question 
* In level-order traversal or BFS, how does "constant space" count? 
    Does this mean the use of node queue is prohibited? 
* This is called O(N) ???? https://leetcode.com/discuss/74447/java-o-n-minimum-size-subarray-sum-using-two-pointers


## Proof 

### Linked List Cycle II 
Set linked list length as `l` and cycle length `k`. 
Set fast pivot goes 2 step each iteration and slow pivot goes 1 step iteration. 
So their first meeting is at step `n` and we got `2n-n=k`. So `n=k`. 
When first met, we make slow start from head and fast pivot start from the position they first met, 
both at rate 1 step/iter. 
When they both travel `l-k` steps, they met the second time, and which is the head position we need to see. 
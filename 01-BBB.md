# Easy questions

## 73
This problem was asked by Google.
Given the head of a singly linked list, reverse it in-place.

```python
def reverse(node, prev_node = None):
    if node:
        next_node = node.next
        node.next = prec_node
        reverse(next_node, node)
```

## 71

This problem was asked by Two Sigma.
Using a function rand7() that returns an integer from 1 to 7 (inclusive) with uniform probability, implement a function rand5() that returns an integer from 1 to 5 (inclusive).

## 70

This problem was asked by Microsoft.
A number is considered perfect if its digits sum up to exactly 10.
Given a positive integer n, return the n-th perfect number.
For example, given 1, you should return 19. Given 2, you should return 28.

## 72 hard

This problem was asked by Google.
In a directed graph, each node is assigned an uppercase letter. We define a path's value as the number of most frequently-occurring letter along that path. For example, if a path in the graph goes through "ABACA", the value of the path is 3, since there are 3 occurrences of 'A' on the path.
Given a graph with n nodes and m directed edges, return the largest value path of the graph. If the largest value is infinite, then return null.
The graph is represented with a string and an edge list. The i-th character represents the uppercase letter of the i-th node. Each tuple in the edge list (i, j) means there is a directed edge from the i-th node to the j-th node. Self-edges are possible, as well as multi-edges.
For example, the following input graph:
ABACA
[(0, 1),
 (0, 2),
 (2, 3),
 (3, 4)]
Would have maximum value 3 using the path of vertices [0, 2, 3, 4], (A, A, C, A).
The following input graph:
A
[(0, 0)]
Should return null, since we have an infinite loop.

## 45

This problem was asked by Amazon.
Given a string, find the longest palindromic contiguous substring. If there are more than one with the maximum length, return any one.
For example, the longest palindromic substring of "aabcdcb" is "bcdcb". The longest palindromic substring of "bananas" is "anana".

##  44

This problem was asked by Google.
We can determine how "out of order" an array A is by counting the number of inversions it has. Two elements A[i] and A[j] form an inversion if A[i] > A[j] but i < j. That is, a smaller element appears after a larger element.
Given an array, count the number of inversions it has. Do this faster than O(N^2) time.
You may assume each element in the array is distinct.
For example, a sorted list has zero inversions. The array [2, 4, 1, 3, 5] has three inversions: (2, 1), (4, 1), and (4, 3). The array [5, 4, 3, 2, 1] has ten inversions: every distinct pair forms an inversion.


## 43

This problem was asked by Amazon.
Implement a stack that has the following methods:
push(val), which pushes an element onto the stack
pop(), which pops off and returns the topmost element of the stack. If there are no elements in the stack, then it should throw an error or return null.
max(), which returns the maximum value in the stack currently. If there are no elements in the stack, then it should throw an error or return null.
Each method should run in constant time.

## 42

This problem was asked by Google.
Given a list of integers S and a target number k, write a function that returns a subset of S that adds up to k. If such a subset cannot be made, then return null.
Integers can appear more than once in the list. You may assume all numbers in the list are positive.
For example, given S = [12, 1, 61, 5, 9, 2] and k = 24, return [12, 9, 2, 1] since it sums up to 24.

## 41

This problem was asked by Facebook.
Given an unordered list of flights taken by someone, each represented as (origin, destination) pairs, and a starting airport, compute the person's itinerary. If no such itinerary exists, return null. If there are multiple possible itineraries, return the lexicographically smallest one. All flights must be used in the itinerary.
For example, given the list of flights [('SFO', 'HKO'), ('YYZ', 'SFO'), ('YUL', 'YYZ'), ('HKO', 'ORD')] and starting airport 'YUL', you should return the list ['YUL', 'YYZ', 'SFO', 'HKO', 'ORD'].
Given the list of flights [('SFO', 'COM'), ('COM', 'YYZ')] and starting airport 'COM', you should return null.
Given the list of flights [('A', 'B'), ('A', 'C'), ('B', 'C'), ('C', 'A')] and starting airport 'A', you should return the list ['A', 'B', 'C', 'A', 'C'] even though ['A', 'C', 'A', 'B', 'C'] is also a valid itinerary. However, the first one is lexicographically smaller.

## 40

This problem was asked by Google.
Given an array of integers where every integer occurs three times except for one integer, which only occurs once, find and return the non-duplicated integer.
For example, given [6, 1, 3, 3, 3, 6, 6], return 1. Given [13, 19, 13, 13], return 19.
Do this in O(N) time and O(1) space.

## 39

This problem was asked by Dropbox.
Conway's Game of Life takes place on an infinite two-dimensional board of square cells. Each cell is either dead or alive, and at each tick, the following rules apply:
Any live cell with less than two live neighbours dies.
Any live cell with two or three live neighbours remains living.
Any live cell with more than three live neighbours dies.
Any dead cell with exactly three live neighbours becomes a live cell.
A cell neighbours another cell if it is horizontally, vertically, or diagonally adjacent.
Implement Conway's Game of Life. It should be able to be initialized with a starting list of live cell coordinates and the number of steps it should run for. Once initialized, it should print out the board state at each step. Since it's an infinite board, print out only the relevant coordinates, i.e. from the top-leftmost live cell to bottom-rightmost live cell.
You can represent a live cell with an asterisk (*) and a dead cell with a dot (.).

## 38

This problem was asked by Microsoft.
You have an N by N board. Write a function that, given N, returns the number of possible arrangements of the board where N queens can be placed on the board without threatening each other, i.e. no two queens share the same row, column, or diagonal.

## 37

This problem was asked by Google.
The power set of a set is the set of all its subsets. Write a function that, given a set, generates its power set.
For example, given the set {1, 2, 3}, it should return {{}, {1}, {2}, {3}, {1, 2}, {1, 3}, {2, 3}, {1, 2, 3}}.
You may also use a list or array to represent a set.

## 36

This problem was asked by Dropbox.
Given the root to a binary search tree, find the second largest node in the tree.
Upgrade to premium and get in-depth solutions to every problem. Since you were referred by one of our affiliates, you'll get a 10% discount on checkout!

## 35

This problem was asked by Google.
Given an array of strictly the characters 'R', 'G', and 'B', segregate the values of the array so that all the Rs come first, the Gs come second, and the Bs come last. You can only swap elements of the array.
Do this in linear time and in-place.
For example, given the array ['G', 'B', 'R', 'R', 'B', 'R', 'G'], it should become ['R', 'R', 'R', 'G', 'G', 'B', 'B'].

## 34

This problem was asked by Quora.
Given a string, find the palindrome that can be made by inserting the fewest number of characters as possible anywhere in the word. If there is more than one palindrome of minimum length that can be made, return the lexicographically earliest one (the first one alphabetically).
For example, given the string "race", you should return "ecarace", since we can add three letters to it (which is the smallest amount to make a palindrome). There are seven other palindromes that can be made from "race" by adding three letters, but "ecarace" comes first alphabetically.
As another example, given the string "google", you should return "elgoogle".

## 33

This problem was asked by Microsoft.
Compute the running median of a sequence of numbers. That is, given a stream of numbers, print out the median of the list so far on each new element.
Recall that the median of an even-numbered list is the average of the two middle numbers.
For example, given the sequence [2, 1, 5, 7, 2, 0, 5], your algorithm should print out:
2
1.5
2
3.5
2
2
2

## 32

This problem was asked by Jane Street.
Suppose you are given a table of currency exchange rates, represented as a 2D array. Determine whether there is a possible arbitrage: that is, whether there is some sequence of trades you can make, starting with some amount A of any currency, so that you can end up with some amount greater than A of that currency.
There are no transaction costs and you can trade fractional quantities.

## 31

This problem was asked by Google.
The edit distance between two strings refers to the minimum number of character insertions, deletions, and substitutions required to change one string to the other. For example, the edit distance between “kitten” and “sitting” is three: substitute the “k” for “s”, substitute the “e” for “i”, and append a “g”.
Given two strings, compute the edit distance between them.

## 30
This problem was asked by Facebook.
You are given an array of non-negative integers that represents a two-dimensional elevation map where each element is unit-width wall and the integer is the height. Suppose it will rain and all spots between two walls get filled up.
Compute how many units of water remain trapped on the map in O(N) time and O(1) space.
For example, given the input [2, 1, 2], we can hold 1 unit of water in the middle.
Given the input [3, 0, 1, 3, 0, 5], we can hold 3 units in the first index, 2 in the second, and 3 in the fourth index (we cannot hold 5 since it would run off to the left), so we can trap 8 units of water.

## 29

This problem was asked by Amazon.
Run-length encoding is a fast and simple method of encoding strings. The basic idea is to represent repeated successive characters as a single count and character. For example, the string "AAAABBBCCDAA" would be encoded as "4A3B2C1D2A".
Implement run-length encoding and decoding. You can assume the string to be encoded have no digits and consists solely of alphabetic characters. You can assume the string to be decoded is valid.

## 28

This problem was asked by Palantir.
Write an algorithm to justify text. Given a sequence of words and an integer line length k, return a list of strings which represents each line, fully justified.
More specifically, you should have as many words as possible in each line. There should be at least one space between each word. Pad extra spaces when necessary so that each line has exactly length k. Spaces should be distributed as equally as possible, with the extra spaces, if any, distributed starting from the left.
If you can only fit one word on a line, then you should pad the right-hand side with spaces.
Each word is guaranteed not to be longer than k.
For example, given the list of words ["the", "quick", "brown", "fox", "jumps", "over", "the", "lazy", "dog"] and k = 16, you should return the following:
["the  quick brown", # 1 extra space on the left
"fox  jumps  over", # 2 extra spaces distributed evenly
"the   lazy   dog"] # 4 extra spaces distributed evenly

## 27

This problem was asked by Facebook.
Given a string of round, curly, and square open and closing brackets, return whether the brackets are balanced (well-formed).
For example, given the string "([])[]({})", you should return true.
Given the string "([)]" or "((()", you should return false.

## 25

This problem was asked by Facebook.
Implement regular expression matching with the following special characters:
. (period) which matches any single character
* (asterisk) which matches zero or more of the preceding element
That is, implement a function that takes in a string and a valid regular expression and returns whether or not the string matches the regular expression.
For example, given the regular expression "ra." and the string "ray", your function should return true. The same regular expression on the string "raymond" should return false.
Given the regular expression ".*at" and the string "chat", your function should return true. The same regular expression on the string "chats" should return false.

## 24

This problem was asked by Google.
Implement locking in a binary tree. A binary tree node can be locked or unlocked only if all of its descendants or ancestors are not locked.
Design a binary tree node class with the following methods:
is_locked, which returns whether the node is locked
lock, which attempts to lock the node. If it cannot be locked, then it should return false. Otherwise, it should lock it and return true.
unlock, which unlocks the node. If it cannot be unlocked, then it should return false. Otherwise, it should unlock it and return true.
You may augment the node to add parent pointers or any other property you would like. You may assume the class is used in a single-threaded program, so there is no need for actual locks or mutexes. Each method should run in O(h), where h is the height of the tree.

## 23

Good morning! Here's your coding interview problem for today.
This problem was asked by Google.
You are given an M by N matrix consisting of booleans that represents a board. Each True boolean represents a wall. Each False boolean represents a tile you can walk on.
Given this matrix, a start coordinate, and an end coordinate, return the minimum number of steps required to reach the end coordinate from the start. If there is no possible path, then return null. You can move up, left, down, and right. You cannot move through walls. You cannot wrap around the edges of the board.
For example, given the following board:
[[f, f, f, f],
[t, t, f, t],
[f, f, f, f],
[f, f, f, f]]
and start = (3, 0) (bottom left) and end = (0, 0) (top left), the minimum number of steps required to reach the end is 7, since we would need to go through (1, 2) because there is a wall everywhere else on the second row.

## 22

This problem was asked by Microsoft.
Given a dictionary of words and a string made up of those words (no spaces), return the original sentence in a list. If there is more than one possible reconstruction, return any of them. If there is no possible reconstruction, then return null.
For example, given the set of words 'quick', 'brown', 'the', 'fox', and the string "thequickbrownfox", you should return ['the', 'quick', 'brown', 'fox'].
Given the set of words 'bed', 'bath', 'bedbath', 'and', 'beyond', and the string "bedbathandbeyond", return either ['bed', 'bath', 'and', 'beyond] or ['bedbath', 'and', 'beyond'].

## 21

This problem was asked by Snapchat.
Given an array of time intervals (start, end) for classroom lectures (possibly overlapping), find the minimum number of rooms required.
For example, given [(30, 75), (0, 50), (60, 150)], you should return 2.

## How to Pick a Random Element from an Infinite Stream

Hope your interview practicing is going well! Let's work through the problem of uniformly picking a random element from a gigantic stream. This is a common interview question at companies like Google and Facebook.
Naively, we could process the stream and store all the elements we encounter in a list, find its size, and pick a random element from [0, size - 1]. The problem with this approach is that it would take O(N) space for a large N.
Instead, let's attempt to solve using loop invariants. On the ith iteration of our loop to pick a random element, let's assume we already picked an element uniformly from [0, i - 1]. In order to maintain the loop invariant, we would need to pick the ith element as the new random element at 1 / (i + 1) chance. For the base case where i = 0, let's say the random element is the first one. Then we know it works because
For i = 0, we would've picked uniformly from [0, 0].
For i > 0, before the loop began, any element K in [0, i - 1] had 1 / i chance of being chosen as the random element. We want K to have 1 / (i + 1) chance of being chosen after the iteration. This is the case since the chance of having being chosen already but not getting swapped with the ith element is 1 / i * (1 - (1 / (i + 1))) which is 1 / i * i / (i + 1) or 1 / (i + 1)
Let's see how the code would look:
import random

def pick(big_stream):
    random_element = None

    for i, e in enumerate(big_stream):
        if i == 0:
            random_element = e
        if random.randint(1, i + 1) == 1:
            random_element = e
    return random_element
Since we are only storing a single variable, this only takes up constant space!
Turns out this algorithm is called Reservoir Sampling. If you liked this problem and solution, sign up for our mailing list below for problems like these! You can also read our other post on how to solve tricky interview questions like this one here.
Best of luck!
Marc
If you liked this guide, feel free to forward it along! As always, shoot us an email if there's anything we can help with!

== 77

Good morning! Here's your coding interview problem for today.
This problem was asked by Snapchat.
Given a list of possibly overlapping intervals, return a new list of intervals where all overlapping intervals have been merged.
The input list is not necessarily ordered in any way.
For example, given [(1, 3), (5, 8), (4, 10), (20, 25)], you should return [(1, 3), (4, 10), (20, 25)].

== 80

Given the root of a binary tree, return a deepest node. For example, in the following tree, return d.
    a
   / \
  b   c
 /
d

== 81

Given a mapping of digits to letters (as in a phone number), and a digit string, return all possible letters the number could represent. You can assume each valid number in the mapping is a single digit.
For example if {“2”: [“a”, “b”, “c”], 3: [“d”, “e”, “f”], …} then “23” should return [“ad”, “ae”, “af”, “bd”, “be”, “bf”, “cd”, “ce”, “cf"].

== 82

Using a read7() method that returns 7 characters from a file, implement readN(n) which reads n characters.
For example, given a file with the content “Hello world”, three read7() returns “Hello w”, “orld” and then “”.

## 91

This problem was asked by Dropbox.

What does the below code snippet print out? How can we fix the anonymous functions to behave as we'd expect?

```python
functions = []
for i in range(10):
    functions.append(lambda : i)

for f in functions:
    print(f())
```

## 94

This problem was asked by Google.
Given a binary tree of integers, find the maximum path sum between two nodes. The path must go through at least one node, and does not need to go through the root.

## 98

This problem was asked by Coursera.
Given a 2D board of characters and a word, find if the word exists in the grid.
The word can be constructed from letters of sequentially adjacent cell, where "adjacent" cells are those horizontally or vertically neighboring. The same letter cell may not be used more than once.
For example, given the following board:
[
  ['A','B','C','E'],
  ['S','F','C','S'],
  ['A','D','E','E']
]
exists(board, "ABCCED") returns true, exists(board, "SEE") returns true, exists(board, "ABCB") returns false.

## 100

This problem was asked by Google.
You are in an infinite 2D grid where you can move in any of the 8 directions:
 (x,y) to
    (x+1, y),
    (x - 1, y),
    (x, y+1),
    (x, y-1),
    (x-1, y-1),
    (x+1,y+1),
    (x-1,y+1),
    (x+1,y-1)
You are given a sequence of points and the order in which you need to cover the points. Give the minimum number of steps in which you can achieve it. You start from the first point.
Example:
Input: [(0, 0), (1, 1), (1, 2)]
Output: 2
It takes 1 step to move from (0, 0) to (1, 1). It takes one more step to move from (1, 1) to (1, 2).

## 101 

This problem was asked by Alibaba.
Given an even number (greater than 2), return two prime numbers whose sum will be equal to the given number.
A solution will always exist. See Goldbach’s conjecture.
Example:
Input: 4
Output: 2 + 2 = 4
If there are more than one solution possible, return the lexicographically smaller solution.
If [a, b] is one solution with a <= b, and [c, d] is another solution with c <= d, then
[a, b] < [c, d]
If a < c OR a==c AND b < d.

## 108

This problem was asked by Google.
Given two strings A and B, return whether or not A can be shifted some number of times to get B.
For example, if A is abcde and B is cdeab, return true. If A is abc and B is acb, return false.

## 107

This problem was asked by Microsoft.
Print the nodes in a binary tree level-wise. For example, the following should print 1, 2, 3, 4, 5.
  1
 / \
2   3
   / \
  4   5

## 104

This problem was asked by Google.
Determine whether a doubly linked list is a palindrome. What if it’s singly linked?
For example, 1 -> 4 -> 3 -> 4 -> 1 returns True while 1 -> 4 returns False.

## 117

This problem was asked by Facebook.
Given a binary tree, return the level of the tree with minimum sum.

## 118

This problem was asked by Google.
Given a sorted list of integers, square the elements and give the output in sorted order.
For example, given [-9, -2, 0, 2, 3], return [0, 4, 4, 9, 81].

## 124

This problem was asked by Microsoft.
You have n fair coins and you flip them all at the same time. Any that come up tails you set aside. The ones that come up heads you flip again. How many rounds do you expect to play before only one coin remains?
Write a function that, given n, returns the number of rounds you'd expect to play until one coin remains.

## 125

This problem was asked by Google.
Given the root of a binary search tree, and a target K, return two nodes in the tree whose sum equals K.
For example, given the following tree and K of 20
    10
   /   \
 5      15
       /  \
     11    15
Return the nodes 5 and 15.

```python

tree = [10, 5, 15, None, None, 11, 15]

dict_tree = {}
for i, x in enumerate(tree):
    if x is not None:
        dict_tree[i] = x

dict_tree = { i:x for i, x in enumerate(tree) if x is not None }        

def search(dict_tree, n, skip):
    ptr = 0
    while ptr in dict_tree:
        if dict_tree[ptr]==n and ptr!=skip:
            return ptr
        if dict_tree[ptr]>n:
            ptr = ptr*2 + 1  # left
        else:
            ptr = ptr*2 + 2  # right
    return None

def solve(tree, k):
    dict_tree = { i:x for i, x in enumerate(tree) if x is not None }        
    
    for p1, value in dict_tree.items():
        p2 = search(dict_tree, k-value, p1)
        if p2 is not None:
            return value, k-value, p1, p2
    
    return None, None, None, None
    
```

COMPLEXITY: O( n lg(n) )
SPACE: the new map O (n)

ANTOTHER WAY

```python
tree = [10, 5, 15, None, None, 11, 15]

def search(tree, n, skip):
    ptr = 0
    while ptr < len(tree) and tree[ptr] is not None:
        if tree[ptr]==n and ptr!=skip:
            return ptr
        if tree[ptr]>n:
            ptr = ptr*2 + 1  # left
        else:
            ptr = ptr*2 + 2  # right
    return None

def solve(tree, k):
    for p1, value in enumerate(tree):
        if value is None:
            continue
        p2 = search(tree, k-value, p1)
        if p2 is not None:
            return value, k-value, p1, p2
    
    return None, None, None, None

```

COMPLEXITY: O( n lg(n) )
SPACE: no additional memory needed

ANTOTHER WAY

```python

def solve(tree, k):
    from collections import defaultdict
    dict_tree = defaultdict(list)
    for i, x in enumerate(tree):
        if x is not None:
            dict_tree[x].append(i)

    for key1 in dict_tree:
        key2 = k-key1
        if key2==key1 and len(dict_tree[key1])>1:
            return key1, key2, dict_tree[key1][0], dict_tree[key1][1]
        if key2 in dict_tree:
            return key1, key2, dict_tree[key1][0], dict_tree[key2][0]
```

COMPLEXITY: O( n ) if no collisions 
WORSE O ( n^2 )

## 127

This problem was asked by Microsoft.
Let's represent an integer in a linked list format by having each node represent a digit in the number. The nodes make up the number in reversed order.
For example, the following linked list:
1 -> 2 -> 3 -> 4 -> 5
is the number 54321.
Given two linked lists in this format, return their sum in the same linked list format.
For example, given
9 -> 9
5 -> 2
return 124 (99 + 25) as:
4 -> 2 -> 1

## 132

This question was asked by Riot Games.
Design and implement a HitCounter class that keeps track of requests (or hits). It should support the following operations:
record(timestamp): records a hit that happened at timestamp
total(): returns the total number of hits recorded
range(lower, upper): returns the number of hits that occurred between timestamps lower and upper (inclusive)
Follow-up: What if our system has limited memory?

## 134 

This problem was asked by Facebook.
You have a large array with most of the elements as zero.
Use a more space-efficient data structure, SparseArray, that implements the same interface:
init(arr, size): initialize with the original large array and size.
set(i, val): updates index at i with val.
get(i): gets the value at index i.

## 135

This question was asked by Apple.
Given a binary tree, find a minimum path sum from root to a leaf.
For example, the minimum path in this tree is [10, 5, 1, -1], which has sum 15.
  10
 /  \
5    5
 \     \
   2    1
       /
     -1

## 145

This problem was asked by Google.
Given the head of a singly linked list, swap every two nodes and return its head.
For example, given 1 -> 2 -> 3 -> 4, return 2 -> 1 -> 4 -> 3.

## 154

This problem was asked by Amazon.
Implement a stack API using only a heap. A stack implements the following methods:
push(item), which adds an element to the stack
pop(), which removes and returns the most recently added element (or throws an error if there is nothing on the stack)
Recall that a heap has the following operations:
push(item), which adds a new key to the heap
pop(), which removes and returns the max value of the heap

## 157

This problem was asked by Amazon.
Given a string, determine whether any permutation of it is a palindrome.
For example, carrace should return true, since it can be rearranged to form racecar, which is a palindrome. daily should return false, since there's no rearrangement that can form a palindrome.


## 159

Given a string, return the first recurring character in it, or null if there is no recurring character.
For example, given the string "acbbac", return "b". Given the string "abcdef", return null.

## 161 

This problem was asked by Facebook.
Given a 32-bit integer, return the number with its bits reversed.
For example, given the binary number 
```
1111 0000 1111 0000 1111 0000 1111 0000
```

return 

```
0000 1111 0000 1111 0000 1111 0000 1111
```

## 171

You are given a list of data entries that represent entries and exits of groups of people into a building. An entry looks like this:
{"timestamp": 1526579928, count: 3, "type": "enter"}
This means 3 people entered the building. An exit looks like this:
{"timestamp": 1526580382, count: 2, "type": "exit"}
This means that 2 people exited the building. timestamp is in Unix time.
Find the busiest period in the building, that is, the time with the most people in the building. Return it as a pair of (start, end) timestamps. You can assume the building always starts off and ends up empty, i.e. with 0 people inside.

## 170 medium

This problem was asked by Facebook.
Given a start word, an end word, and a dictionary of valid words, find the shortest transformation sequence from start to end such that only one letter is changed at each step of the sequence, and each transformed word exists in the dictionary. If there is no possible transformation, return null. Each word in the dictionary have the same length as start and end and is lowercase.
For example, given start = "dog", end = "cat", and dictionary = {"dot", "dop", "dat", "cat"}, return ["dog", "dot", "dat", "cat"].
Given start = "dog", end = "cat", and dictionary = {"dot", "tod", "dat", "dar"}, return null as there is no possible transformation from dog to cat

## 173

This problem was asked by Stripe.
Write a function to flatten a nested dictionary. Namespace the keys with a period.
For example, given the following dictionary:
{
    "key": 3,
    "foo": {
        "a": 5,
        "bar": {
            "baz": 8
        }
    }
}
it should become:
{
    "key": 3,
    "foo.a": 5,
    "foo.bar.baz": 8
}
You can assume keys do not contain dots in them, i.e. no clobbering will occur.

## 175

This problem was asked by Google.
You are given a starting state start, a list of transition probabilities for a Markov chain, and a number of steps num_steps. Run the Markov chain starting from start for num_steps and compute the number of times we visited each state.
For example, given the starting state a, number of steps 5000, and the following transition probabilities:
[
  ('a', 'a', 0.9),
  ('a', 'b', 0.075),
  ('a', 'c', 0.025),
  ('b', 'a', 0.15),
  ('b', 'b', 0.8),
  ('b', 'c', 0.05),
  ('c', 'a', 0.25),
  ('c', 'b', 0.25),
  ('c', 'c', 0.5)
]
One instance of running this Markov chain might produce { 'a': 3012, 'b': 1656, 'c': 332 }.

## 176

This problem was asked by Bloomberg.
Determine whether there exists a one-to-one character mapping from one string s1 to another s2.
For example, given s1 = abc and s2 = bcd, return true since we can map a to b, b to c, and c to d.
Given s1 = foo and s2 = bar, return false since the o cannot map to two characters.


## 177

This problem was asked by Airbnb.
Given a linked list and a positive integer k, rotate the list to the right by k places.
For example, given the linked list 7 -> 7 -> 3 -> 5 and k = 2, it should become 3 -> 5 -> 7 -> 7.
Given the linked list 1 -> 2 -> 3 -> 4 -> 5 and k = 3, it should become 3 -> 4 -> 5 -> 1 -> 2.

## 191

This problem was asked by Stripe.
Given a collection of intervals, find the minimum number of intervals you need to remove to make the rest of the intervals non-overlapping.
Intervals can "touch", such as [0, 1] and [1, 2], but they won't be considered overlapping.
For example, given the intervals (7, 9), (2, 4), (5, 8), return 1 as the last interval can be removed and the first two won't overlap.
The intervals are not necessarily sorted in any order.

## 189

This problem was asked by Google.
Given an array of elements, return the length of the longest subarray where all its elements are distinct.
For example, given the array [5, 1, 3, 5, 2, 3, 4, 1], return 5 as the longest subarray of distinct elements is [5, 2, 3, 4, 1].

## 187

This problem was asked by Google.
You are given given a list of rectangles represented by min and max x- and y-coordinates. Compute whether or not a pair of rectangles overlap each other. If one rectangle completely covers another, it is considered overlapping.
For example, given the following rectangles:
{
    "top_left": (1, 4),
    "dimensions": (3, 3) # width, height
},
{
    "top_left": (-1, 3),
    "dimensions": (2, 1)
},
{
    "top_left": (0, 5),
    "dimensions": (4, 3)
}
return true as the first and third rectangle overlap each other.

## 194

This problem was asked by Facebook.
Suppose you are given two lists of n points, one list p1, p2, ..., pn on the line y = 0 and the other list q1, q2, ..., qn on the line y = 1. Imagine a set of n line segments connecting each point pi to qi. Write an algorithm to determine how many pairs of the line segments intersect.

## 196

This problem was asked by Apple.
Given the root of a binary tree, find the most frequent subtree sum. The subtree sum of a node is the sum of all values under a node, including the node itself.
For example, given the following tree:
  5
 / \
2  -5
Return 2 as it occurs twice: once as the left leaf, and once as the sum of 2 + 5 - 5.

# 197

This problem was asked by Amazon.
Given an array and a number k that's smaller than the length of the array, rotate the array to the right k elements in-place.

## 201

This problem was asked by Google.
You are given an array of arrays of integers, where each array corresponds to a row in a triangle of numbers. For example, [[1], [2, 3], [1, 5, 1]] represents the triangle:
  1
 2 3
1 5 1
We define a path in the triangle to start at the top and go down one row at a time to an adjacent value, eventually ending with an entry on the bottom row. For example, 1 -> 3 -> 5. The weight of the path is the sum of the entries.
Write a program that returns the weight of the maximum weight path.

## 202

This problem was asked by Palantir.
Write a program that checks whether an integer is a palindrome. For example, 121 is a palindrome, as well as 888. 678 is not a palindrome. Do not convert the integer into a string.

## 204

This problem was asked by Amazon.
Given a complete binary tree, count the number of nodes in faster than O(n) time. Recall that a complete binary tree has every level filled except the last, and the nodes in the last level are filled starting from the left.

## 205

This problem was asked by IBM.
Given an integer, find the next permutation of it in absolute order. For example, given 48975, the next permutation would be 49578.

## 206

This problem was asked by Twitter.
A permutation can be specified by an array P, where P[i] represents the location of the element at i in the permutation. For example, [2, 1, 0] represents the permutation where elements at the index 0 and 2 are swapped.
Given an array and a permutation, apply the permutation to the array. For example, given the array ["a", "b", "c"] and the permutation [2, 1, 0], return ["c", "b", "a"].

## 210

This problem was asked by Apple.
A Collatz sequence in mathematics can be defined as follows. Starting with any positive integer:
if n is even, the next number in the sequence is n / 2
if n is odd, the next number in the sequence is 3n + 1 
It is conjectured that every such sequence eventually reaches the number 1. Test this conjecture.
Bonus: What input n <= 1000000 gives the longest sequence?

## 212

This problem was asked by Dropbox.
Spreadsheets often use this alphabetical encoding for its columns: "A", "B", "C", ..., "AA", "AB", ..., "ZZ", "AAA", "AAB", ....
Given a column number, return its alphabetical column id. For example, given 1, return "A". Given 27, return "AA".

## 214

This problem was asked by Stripe.
Given an integer n, return the length of the longest consecutive run of 1s in its binary representation.
For example, given 156, you should return 3.

## 221

This problem was asked by Zillow.
Let's define a "sevenish" number to be one which is either a power of 7, or the sum of unique powers of 7. The first few sevenish numbers are 1, 7, 8, 49, and so on. Create an algorithm to find the nth sevenish number.

## 224

Given a sorted array, find the smallest positive integer that is not the sum of a subset of the array.
For example, for the input [1, 2, 3, 10], you should return 7.
Do this in O(N) time.

## 225

This problem was asked by Bloomberg.
There are N prisoners standing in a circle, waiting to be executed. The executions are carried out starting with the kth person, and removing every successive kth person going clockwise until there is no one left.
Given N and k, write an algorithm to determine where a prisoner should stand in order to be the last survivor.
For example, if N = 5 and k = 2, the order of executions would be [2, 4, 1, 5, 3], so you should return 3.
Bonus: Find an O(log N) solution if k = 2.


## 227 

This problem was asked by Facebook.
Boggle is a game played on a 4 x 4 grid of letters. The goal is to find as many words as possible that can be formed by a sequence of adjacent letters in the grid, using each cell at most once. Given a game board and a dictionary of valid words, implement a Boggle solver.

## 231

This problem was asked by IBM.
Given a string with repeated characters, rearrange the string so that no two adjacent characters are the same. If this is not possible, return None.
For example, given "aaabbc", you could return "ababac". Given "aaab", return None.

## 232

This problem was asked by Google.
Implement a PrefixMapSum class with the following methods:
insert(key: str, value: int): Set a given key's value in the map. If the key already exists, overwrite the value.
sum(prefix: str): Return the sum of all values of keys that begin with a given prefix.
For example, you should be able to run the following code:
mapsum.insert("columnar", 3)
assert mapsum.sum("col") == 3

mapsum.insert("column", 2)
assert mapsum.sum("col") == 5

## 233

This problem was asked by Apple.
Implement the function fib(n), which returns the nth number in the Fibonacci sequence, using only O(1) space.

## 247

This problem was asked by PayPal.
Given a binary tree, determine whether or not it is height-balanced. A height-balanced binary tree can be defined as one in which the heights of the two subtrees of any node never differ by more than one.

## 244

This problem was asked by Square.
The Sieve of Eratosthenes is an algorithm used to generate all prime numbers smaller than N. The method is to take increasingly larger prime numbers, and mark their multiples as composite. 
For example, to find all primes less than 100, we would first mark [4, 6, 8, ...] (multiples of two), then [6, 9, 12, ...] (multiples of three), and so on. Once we have done this for all primes less than N, the unmarked numbers that remain will be prime.
Implement this algorithm.
Bonus: Create a generator that produces primes indefinitely (that is, without taking N as an input).

## 237

This problem was asked by Amazon.
A tree is symmetric if its data and shape remain unchanged when it is reflected about the root node. The following tree is an example:
        4
      / | \
    3   5   3
  /           \
9              9
Given a k-ary tree, determine whether it is symmetric.

## 241

This problem was asked by Palantir.
In academia, the h-index is a metric used to calculate the impact of a researcher's papers. It is calculated as follows:
A researcher has index h if at least h of her N papers have h citations each. If there are multiple h satisfying this formula, the maximum is chosen.
For example, suppose N = 5, and the respective citations of each paper are [4, 3, 0, 1, 5]. Then the h-index would be 3, since the researcher has 3 papers with at least 3 citations.
Given a list of paper citations of a researcher, calculate their h-index.

## 252

This problem was asked by Palantir.
The ancient Egyptians used to express fractions as a sum of several terms where each numerator is one. For example, 4 / 13 can be represented as 1 / 4 + 1 / 18 + 1 / 468.
Create an algorithm to turn an ordinary fraction a / b, where a < b, into an Egyptian fraction.

## 255

This problem was asked by Microsoft.
The transitive closure of a graph is a measure of which vertices are reachable from other vertices. It can be represented as a matrix M, where M[i][j] == 1 if there is a path between vertices i and j, and otherwise 0.
For example, suppose we are given the following graph in adjacency list form:
graph = [
    [0, 1, 3],
    [1, 2],
    [2],
    [3]
]
The transitive closure of this graph would be:
[1, 1, 1, 1]
[0, 1, 1, 0]
[0, 0, 1, 0]
[0, 0, 0, 1]
Given a graph, find its transitive closure.

## 273

This problem was asked by Apple.
A fixed point in an array is an element whose value is equal to its index. Given a sorted array of distinct elements, return a fixed point, if one exists. Otherwise, return False. 
For example, given [-6, 0, 2, 40], you should return 2. Given [1, 5, 7, 8], you should return False.

## 269 

This problem was asked by Microsoft.
You are given an string representing the initial conditions of some dominoes. Each element can take one of three values:
L, meaning the domino has just been pushed to the left,
R, meaning the domino has just been pushed to the right, or
., meaning the domino is standing still.
Determine the orientation of each tile when the dominoes stop falling. Note that if a domino receives a force from the left and right side simultaneously, it will remain upright.
For example, given the string .L.R....L, you should return LL.RRRLLL.
Given the string ..R...L.L, you should return ..RR.LLLL.

## 266

This problem was asked by Pivotal.
A step word is formed by taking a given word, adding a letter, and anagramming the result. For example, starting with the word "APPLE", you can add an "A" and anagram to get "APPEAL".
Given a dictionary of words and an input word, create a function that returns all valid step words.

## 265 

This problem was asked by Atlassian.
MegaCorp wants to give bonuses to its employees based on how many lines of codes they have written. They would like to give the smallest positive amount to each worker consistent with the constraint that if a developer has written more lines of code than their neighbor, they should receive more money.
Given an array representing a line of seats of employees at MegaCorp, determine how much each one should get paid.
For example, given [10, 40, 200, 1000, 60, 30], you should return [1, 2, 3, 4, 2, 1].

## 261

This problem was asked by Amazon.
Huffman coding is a method of encoding characters based on their frequency. Each letter is assigned a variable-length binary string, such as 0101 or 111110, where shorter lengths correspond to more common letters. To accomplish this, a binary tree is built such that the path from the root to any leaf uniquely maps to a character. When traversing the path, descending to a left child corresponds to a 0 in the prefix, while descending right corresponds to 1.
Here is an example tree (note that only the leaf nodes have letters):
        *
      /   \
    *       *
   / \     / \
  *   a   t   *
 /             \
c               s
With this encoding, cats would be represented as 0000110111.
Given a dictionary of character frequencies, build a Huffman tree, and use it to determine a mapping between characters and their encoded binary strings.

## 258

 Daily Coding Problem 
Good morning! Here's your coding interview problem for today.
This problem was asked by Morgan Stanley.
In Ancient Greece, it was common to write text with the first line going left to right, the second line going right to left, and continuing to go back and forth. This style was called "boustrophedon".
Given a binary tree, write an algorithm to print the nodes in boustrophedon order.
For example, given the following tree:
       1
    /     \
  2         3
 / \       / \
4   5     6   7
You should return [1, 3, 2, 4, 5, 6, 7].

## 277

This problem was asked by Google.
UTF-8 is a character encoding that maps each symbol to one, two, three, or four bytes.
For example, the Euro sign, €, corresponds to the three bytes 11100010 10000010 10101100. The rules for mapping characters are as follows:
For a single-byte character, the first bit must be zero.
For an n-byte character, the first byte starts with n ones and a zero. The other n - 1 bytes all start with 10.
Visually, this can be represented as follows.
 Bytes   |           Byte format
-----------------------------------------------
   1     | 0xxxxxxx
   2     | 110xxxxx 10xxxxxx
   3     | 1110xxxx 10xxxxxx 10xxxxxx
   4     | 11110xxx 10xxxxxx 10xxxxxx 10xxxxxx
Write a program that takes in an array of integers representing byte values, and returns whether it is a valid UTF-8 encoding.

## 278

This problem was asked by Amazon.
Given an integer N, construct all possible binary search trees with N nodes.

## 282

This problem was asked by Netflix.
Given an array of integers, determine whether it contains a Pythagorean triplet. Recall that a Pythogorean triplet (a, b, c) is defined by the equation a^2+ b^2= c^2.

## 279                                                          

This problem was asked by Twitter.
A classroom consists of N students, whose friendships can be represented in an adjacency list. For example, the following descibes a situation where 0 is friends with 1 and 2, 3 is friends with 6, and so on.
{0: [1, 2],
 1: [0, 5],
 2: [0],
 3: [6],
 4: [],
 5: [1],
 6: [3]} 
Each student can be placed in a friend group, which can be defined as the transitive closure of that student's friendship relations. In other words, this is the smallest set such that no student in the group has any friends outside this group. For the example above, the friend groups would be {0, 1, 2, 5}, {3, 6}, {4}.
Given a friendship list such as the one above, determine the number of friend groups in the class.


## 283

This problem was asked by Google.
A regular number in mathematics is defined as one which evenly divides some power of 60. Equivalently, we can say that a regular number is one whose only prime divisors are 2, 3, and 5.
These numbers have had many applications, from helping ancient Babylonians keep time to tuning instruments according to the diatonic scale.
Given an integer N, write a program that returns, in order, the first N regular numbers.


## 290

On a mysterious island there are creatures known as Quxes which come in three colors: red, green, and blue. One power of the Qux is that if two of them are standing next to each other, they can transform into a single creature of the third color.
Given N Quxes standing in a line, determine the smallest number of them remaining after any possible sequence of such transformations.
For example, given the input ['R', 'G', 'B', 'G', 'B'], it is possible to end up with a single Qux through the following steps:
        Arrangement       |   Change
----------------------------------------
['R', 'G', 'B', 'G', 'B'] | (R, G) -> B
['B', 'B', 'G', 'B']      | (B, G) -> R
['B', 'R', 'B']           | (R, B) -> G
['B', 'G']                | (B, G) -> R
['R']                     |

## 298

This problem was asked by Google.
A girl is walking along an apple orchard with a bag in each hand. She likes to pick apples from each tree as she goes along, but is meticulous about not putting different kinds of apples in the same bag.
Given an input describing the types of apples she will pass on her path, in order, determine the length of the longest portion of her path that consists of just two types of apple trees.
For example, given the input [2, 1, 2, 3, 3, 1, 3, 5], the longest portion will involve types 1 and 3, with a length of four.

## 300

This problem was asked by Uber.
On election day, a voting machine writes data in the form (voter_id, candidate_id) to a text file. Write a program that reads this file as a stream and returns the top 3 candidates at any given time. If you find a voter voting more than once, report this as fraud.

## 303

This problem was asked by Microsoft.
Given a clock time in hh:mm format, determine, to the nearest degree, the angle between the hour and the minute hands.
Bonus: When, during the course of a day, will the angle be zero?

## 305

This problem was asked by Amazon.
Given a linked list, remove all consecutive nodes that sum to zero. Print out the remaining nodes.
For example, suppose you are given the input 3 -> 4 -> -7 -> 5 -> -6 -> 6. In this case, you should first remove 3 -> 4 -> -7, then -6 -> 6, leaving only 5.

## 307

This problem was asked by Oracle.
Given a binary search tree, find the floor and ceiling of a given integer. The floor is the highest element in the tree less than or equal to an integer, while the ceiling is the lowest element in the tree greater than or equal to an integer.
If either value does not exist, return None.

## 310

This problem was asked by Pivotal.
Write an algorithm that finds the total number of set bits in all integers between 1 and N.

## 311

This problem was asked by Sumo Logic.
Given an unsorted array, in which all elements are distinct, find a "peak" element in O(log N) time.
An element is considered a peak if it is greater than both its left and right neighbors. It is guaranteed that the first and last elements are lower than all others.

## 312

You are given a 2 x N board, and instructed to completely cover the board with the following shapes:
Dominoes, or 2 x 1 rectangles.
Trominoes, or L-shapes.
For example, if N = 4, here is one possible configuration, where A is a domino, and B and C are trominoes.
A B B C
A B C C
Given an integer N, determine in how many ways this task is possible.

## 315

This problem was asked by Google.
In linear algebra, a Toeplitz matrix is one in which the elements on any given diagonal from top left to bottom right are identical.
Here is an example:
1 2 3 4 8
5 1 2 3 4
4 5 1 2 3
7 4 5 1 2
Write a program to determine whether a given input is a Toeplitz matrix.

## 321

This problem was asked by PagerDuty.
Given a positive integer N, find the smallest number of steps it will take to reach 1.
There are two kinds of permitted steps:
You may decrement N to N - 1.
If a * b = N, you may decrement N to the larger of a and b.
For example, given 100, you can reach 1 in five steps with the following route: 100 -> 10 -> 9 -> 3 -> 2 -> 1.

## 324 

This problem was asked by Amazon.
Consider the following scenario: there are N mice and N holes placed at integer points along a line. Given this, find a method that maps mice to holes such that the largest number of steps any mouse takes is minimized.
Each move consists of moving one mouse one unit to the left or right, and only one mouse can fit inside each hole.
For example, suppose the mice are positioned at [1, 4, 9, 15], and the holes are located at [10, -5, 0, 16]. In this case, the best pairing would require us to send the mouse at 1 to the hole at -5, so our function should return 6.

## 325

This problem was asked by Jane Street.
The United States uses the imperial system of weights and measures, which means that there are many different, seemingly arbitrary units to measure distance. There are 12 inches in a foot, 3 feet in a yard, 22 yards in a chain, and so on.
Create a data structure that can efficiently convert a certain quantity of one unit to the correct amount of any other unit. You should also allow for additional units to be added to the system.

## 327

This problem was asked by Salesforce.

Write a program to merge two binary trees. Each node in the new tree should hold a value equal to the sum of the values of the corresponding nodes of the input trees.

If only one input tree has a node in a given position, the corresponding node in the new tree should match that input node.

## 332

This problem was asked by Jane Street.

Given integers M and N, write a program that counts how many positive integer pairs (a, b) satisfy the following conditions:

a + b = M
a XOR b = N

```cpp
#include <iostream>
#include <vector>

using namespace std;

vector<pair<int,int>> solve(int m, int n) {
    vector<pair<int,int>> ret;
    for (int i=0; i<m/2; i++) {
        if (((m-i) ^ i) == n) {
            ret.push_back(make_pair(i,m-i));
        }
    }
    return ret;
}

int main()
{
    cout << "solve(705, 573)" << endl;
   
    auto res = solve(705, 573);
    cout << res.size() << " solutions" << endl;
    
    for (auto x = res.begin(); x != res.end();) {
        cout << x->first << "," << x->second;
        x++;
        if (res.end() != x) { cout << " - "; }
    }
    cout << endl;
    return 0;
}
```

## 334

This problem was asked by Twitter.

The 24 game is played as follows. You are given a list of four integers, each between 1 and 9, in a fixed order. By placing the operators +, -, *, and / between the numbers, and grouping them with parentheses, determine whether it is possible to reach the value 24.

For example, given the input [5, 2, 7, 8], you should return True, since (5 * 2 - 7) * 8 = 24.

Write a function that plays the 24 game.

```cpp

#include <iostream>
#include <vector>
#include <sstream>

using namespace std;

pair<int, string> compute(int a, int b, int c, int d, int seq) {
    stringstream ss;
    int op[] = {
        (seq>>5) & 15,
        (seq>>2) & 7,
        (seq) & 3,
    };
    
    for (auto o: op) {
        switch(o) {
            case 0: a=a+b; b=c; c=d;
                ss << "a+b ";
                break;
            case 1: a=a-b; b=c; c=d;
                ss << "a-b ";
                break;
            case 2: a=a*b; b=c; c=d;
                ss << "a*b ";
                break;
            case 3: if (b==0) {throw "divison by 0";}; a=a/b; b=c; c=d;
                ss << "a/b ";
                break;
            case 4: b=b+c; c=d;
                ss << "b+c ";
                break;
            case 5: b=b-c; c=d;
                ss << "b-c ";
                break;
            case 6: b=b*c; c=d;
                ss << "b*c ";
                break;
            case 7: if (c==0) {throw "divison by 0";}; b=b/c; c=d;
                ss << "b/c ";
                break;
            case 8: c=c+d;
                ss << "c+d ";
                break;
            case 9: c=c-d;
                ss << "c-d ";
                break;
            case 10: c=c*d;
                ss << "c*d ";
                break;
            case 11: if (d==0) {throw "divison by 0";}; c=c/d;
                ss << "c/d ";
                break;
            default:
                break;
        }
        
    }
    ss << seq << " end";
    string sss = ss.str();
    return make_pair(a, sss);
}

vector<string> solve(int a, int b, int c, int d) {
    vector<string> ret;
    int seq = 0;
    pair<int, string> res;
    while (seq <= 0x1ff) {
        try{
            res = compute(a,b,c,d,seq);
        } catch (const char* msg) {
        //    cerr << msg << endl;
            seq++;
            continue;
        }
        if (res.first == 24) {
            ret.push_back(res.second);
        }
        seq++;
    }
    return ret;
}

int main()
{
    cout << "solve(5,2,7,8)" << endl;

    for (auto x: solve(5,2,7,8)) {
        cout << x << endl;
    }
    return 0;
}
```

## 340

This problem was asked by Google.

Given a set of points (x, y) on a 2D cartesian plane, find the two closest points. 

For example, given the points [(1, 1), (-1, -1), (3, 4), (6, 1), (-1, -6), (-4, -3)], return [(-1, -1), (1, 1)].

```python
def dist(a,b):
    x1, y1 = a
    x2, y2 = b
    return ((x2-x1)**2 + (y2-y1)**2) ** 0.5

points = [(1, 1), (-1, -1), (3, 4), (6, 1), (-1, -6), (-4, -3)]
print ( min(
  (dist(a,b),a,b) for a in points for b in points if a != b
) )
```

## 341

This problem was asked by Google.

You are given an N by N matrix of random letters and a dictionary of words. Find the maximum number of words that can be packed on the board from the given dictionary.

A word is considered to be able to be packed on the board if:

* It can be found in the dictionary
* It can be constructed from untaken letters by other words found so far on the board
* The letters are adjacent to each other (vertically and horizontally, not diagonally).
* Each tile can be visited only once by any word.

For example, given the following dictionary:

```python
{ 'eat', 'rain', 'in', 'rat' }
```

and matrix:

```python
[['e', 'a', 'n'],
 ['t', 't', 'i'],
 ['a', 'r', 'a']]
```

Your function should return 3, since we can make the words 'eat', 'in', and 'rat' without them touching each other. 

We could have alternatively made 'eat' and 'rain', but that would be incorrect since that's only 2 words.

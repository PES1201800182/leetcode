f = open("next_problem.txt","r+")

arr = ['Array',
    'Hash Table',
    'Linked List',
    'Math',
    'Two Pointers',
    'String',
    'Binary Search',
    'Divide and Conquer',
    'Dynamic Programming',
    'Backtracking',
    'Stack',
    'Greedy',
    'Sort',
    'Bit Manipulation',
    'Tree',
    'Depth-First Search',
    'Breadth-First Search',
    'Union Find',
    'Graph',
    'Design',
    'Topological Sort',
    'Trie',
    'Binary Indexed Tree',
    'Segment Tree',
    'Binary Search Tree'
    'Recursion',
    'Brainteaser',
    'Memoization',
    'Queue',
    'Reservoir Sampling',
    'Ordered Map',
    'Geometry',
    'Rejection Sampling',
    'Sliding Window',
    'Line Sweep',
    'Rolling Hash',
    'Suffix Array',
    'Database',
    'Shell',
    'Concurrency',
    'Sorting',
    'Heap (Priority Queue)',
    'Merge Sort',
    'String Matching',
    'Matrix',
    'Monotonic Stack',
    'Simulation',
    'Combinatorics',
    'Binary Tree',
    'Doubly-Linked List',
    'Interactive',
    'Bucket Sort',
    'Radix Sort',
    'Counting',
    'Data Stream',
    'Iterator',
    'Hash Function',
    'Enumeration',
    'Number Theory',
    'Prefix Sum',
    'Quickselect',
    'Ordered Set',
    'Monotonic Queue',
    'Counting Sort',
    'Game Theory',
    'Eulerian Circuit',
    'Randomized',
    'Shortest Path',
    'Bitmask',
    'Probability and Statistics',
    'Minimum Spanning Tree',
    'Biconnected Component',
    'Strongly Connected Comp' ]

category, difficulty = f.readline().split(" ")
category_ = arr[int(category)]
difficulty = int(difficulty)
category = int(category)
print(category_, difficulty)

if difficulty ==1:
    category = (category+1)%len(arr)
    difficulty =0
else:
    difficulty =1

f = open("next_problem.txt","w")
f.write(str(category)+" "+str(difficulty))

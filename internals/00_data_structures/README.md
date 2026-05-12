Data Structures From Scratch — Full Project Subject

Build a low-level data structures library in Python from scratch without using Python’s high-level container implementations internally.

The goal is to deeply understand:

how data structures work internally
algorithmic complexity
memory behavior
tradeoffs
iterator protocols
abstraction design
performance engineering
General Rules
Allowed
Basic Python syntax
Classes
Type hints
ctypes (recommended for dynamic arrays)
typing
time
random
math
Forbidden Inside Implementations

You must NOT use Python built-in structures as the actual implementation backend unless explicitly allowed.

Example:

Your hash map cannot internally use dict
Your stack cannot internally use list.append
Your queue cannot internally use collections.deque

You may still use Python lists:

temporarily in tests
benchmarking
comparisons
Project Goals

For EVERY structure:

You must:

Implement it from scratch
Document it
Explain its internal behavior
Analyze complexity
Benchmark it
Add iterators
Add string representations
Add tests
Explain real-world use cases
Compare with Python equivalents
Required Structure Template

Every structure must contain:

class StructureName:
    """
    Description of the structure.

    Internal design:
    - ...
    - ...

    Complexity:
    - Access: O(...)
    - Insert: O(...)
    """
Required Features For Every Structure
1. Constructor
s = Structure()
2. String Representation
print(s)

Implement:

__repr__
__str__
3. Length Support
len(s)

Implement:

__len__
4. Iteration
for x in s:
    ...

Implement:

__iter__
5. Membership
x in s

Implement:

__contains__
6. Error Handling

Raise proper exceptions:

IndexError
KeyError
ValueError
FULL ROADMAP
PHASE 0 — Foundations

Before implementing structures, study:

Required Concepts
Python Object Model
variables are references
mutability
identity vs equality
shallow/deep copy
Complexity Analysis
Big O
amortized complexity
worst/average/best case
Memory Concepts
stack vs heap
contiguous memory
pointer-like references
cache locality
OOP Design
encapsulation
abstraction
invariants
PHASE 1 — Dynamic Array (Easiest Important Structure)
Structure 1: DynamicArray

Equivalent to:

list
Concepts Learned
contiguous memory
resizing
amortized O(1)
indexing
low-level memory simulation
MUST IMPLEMENT
Internal Storage

Use:

ctypes.py_object
Methods
append
insert
remove
pop
clear
resize
find
index
reverse
copy
Operators
[]
len()
in
for x in ...
Internal Concepts To Document
capacity vs size
doubling strategy
amortized analysis
shifting elements
memory reallocation
PHASE 2 — Linked Lists
Structure 2: SinglyLinkedList
Learn
nodes
references
traversal
pointer logic
Methods
append
prepend
insert
delete
find
reverse
Structure 3: DoublyLinkedList

Add:

prev pointers
bidirectional traversal
MUST DOCUMENT
why linked lists are bad for cache locality
why indexing is O(n)
insertion tradeoffs
PHASE 3 — Stack & Queue
Structure 4: Stack

Implement twice:

using dynamic array
using linked list
Methods
push
pop
peek
is_empty
Learn
LIFO
abstraction layers
Structure 5: Queue

Implement:

linked-list queue
circular queue
Learn
FIFO
head/tail optimization
Structure 6: Deque

Double-ended queue.

PHASE 4 — Hashing
Structure 7: HashMap

Equivalent:

dict
MOST IMPORTANT PHASE

This is where real systems knowledge starts.

MUST LEARN
Hashing
hash functions
deterministic hashing
collisions
Collision Resolution

Implement BOTH:

chaining
open addressing
Resizing
load factor
rehashing
Methods
put
get
remove
keys
values
items
MUST DOCUMENT
why dict is fast
average vs worst case
collision attacks
probing strategies
Structure 8: HashSet

Built on top of HashMap.

Learn
uniqueness
set algebra
PHASE 5 — Trees
Structure 9: BinarySearchTree
Learn
recursion
ordering
logarithmic thinking
Methods
insert
search
delete
min
max
height
Traversals
inorder
preorder
postorder
levelorder
MUST DOCUMENT
skewed trees
degeneration into linked list
recursion depth
Structure 10: AVL Tree
Learn
balancing
rotations
invariants
MUST IMPLEMENT
left rotation
right rotation
rebalance
balance factor
VERY IMPORTANT

This structure teaches advanced algorithmic engineering.

Structure 11: Trie
Learn
prefix trees
autocomplete
memory tradeoffs
Methods
insert
search
starts_with
delete
PHASE 6 — Priority Structures
Structure 12: BinaryHeap

Equivalent:

heapq
Learn
complete binary trees
heap invariant
priority queues
Methods
push
pop
peek
heapify
MUST DOCUMENT
array representation of trees
parent/child indexing
sift up/down
PHASE 7 — Graphs
Structure 13: Graph
Implement
Adjacency List
Adjacency Matrix
Learn
sparse vs dense graphs
graph traversal
weighted graphs
Algorithms
BFS
DFS
Dijkstra
MUST DOCUMENT
queue usage in BFS
stack/recursion in DFS
heap usage in Dijkstra
PHASE 8 — Advanced Structures
Structure 14: Union-Find

Learn:

path compression
union by rank
Structure 15: LRU Cache

Learn:

combining hashmap + doubly linked list
Structure 16: Bloom Filter

Learn:

probabilistic structures
false positives
Structure 17: Skip List

Learn:

probabilistic balancing
REQUIRED DOCUMENTATION FOR EVERY STRUCTURE
1. Theory

Explain:

purpose
design
tradeoffs
2. Internal Memory Layout

Example:

Array:
[1][2][3][4]

Linked list:
1 -> 2 -> 3
3. Complexity Table
Operation	Complexity
Access	O(1)

Explain WHY.

4. Real-World Uses

Example:

heaps → schedulers
tries → autocomplete
hash maps → databases
5. Python Equivalent

Compare with:

list
dict
set
deque
heapq
REQUIRED TESTING

For every structure:

unit tests
edge cases
stress tests

Example:

pop from empty stack
insert invalid index
delete missing key
REQUIRED BENCHMARKS

Compare against Python built-ins.

Example:

CustomDynamicArray vs list
CustomHashMap vs dict

Measure:

insertion speed
lookup speed
memory usage
FINAL GOAL

By the end you should deeply understand:

Arrays
resizing
cache locality
Hash maps
why dict is powerful
Trees
balancing and logarithmic behavior
Heaps
priority scheduling
Graphs
traversal and shortest paths
System Design Tradeoffs
memory vs speed
locality vs flexibility
worst case vs average case
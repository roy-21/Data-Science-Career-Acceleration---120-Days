
# Python Time Complexity – Deep Dive Micro-Challenges 

This repository contains a collection of **10 micro-challenges** focused on understanding **time complexity, performance bottlenecks, and hidden costs** in Python.  
Each challenge explores a common mistake or optimization pattern that directly affects real-world application performance and server reliability.

---

##  What I Did in This Repository

I solved **10 performance-focused problems** to understand:
- How Python handles operations internally
- Why some “simple-looking” code becomes slow at scale
- How to fix common performance traps using the right data structures

---

##  Micro-Challenges Overview

###  Linear Scan — `O(N)`
**Problem:**  
Search for `-5` in a list of 10 million numbers.

**What I Learned:**
- Python performs a **linear scan** on lists
- Each element is loaded and compared one by one
- Time grows proportionally with data size

**Issue Faced:**  
Large lists cause slow searches when using lists.

---

### Hash Lookup — `O(1)`
**Problem:**  
Convert the list to a set and search again.

**What I Learned:**
- `set` uses **hashing**
- Lookup jumps directly to a memory slot
- Search time stays constant regardless of size

**Key Insight:**  
Fast search ≠ free build cost.

---

### Insertion Trap — `O(N)`
**Problem:**  
Compare `list.append(x)` vs `list.insert(0, x)`.

**What I Learned:**
- `append()` is fast (O(1))
- `insert(0, x)` shifts every element → slow

**Performance Trap:**  
Inserting at the start of large lists is catastrophic.

---

###  Queue Bottleneck — `O(N)`
**Problem:**  
Compare `list.pop()` vs `list.pop(0)`.

**What I Learned:**
- Removing from the end is fast
- Removing from the front causes a left shift
- Lists are bad for FIFO queues

**Fix:**  
Use `collections.deque`.

---

###  String Builder Trap — `O(N²)`
**Problem:**  
Build a string using `+= "a"` inside a loop.

**What I Learned:**
- Python strings are **immutable**
- Each concatenation creates a new string
- Leads to quadratic time complexity

**Fix:**  
Use `list.append()` + `"".join()`.

---

###  Length Trick — `O(1)`
**Problem:**  
Call `len()` on a massive list.

**What I Learned:**
- Python stores list length as cached metadata
- `len()` does not count elements
- It simply reads an integer

**Insight:**  
Not all operations that *look* expensive actually are.

---

###  Quadratic Nested Loop — `O(N²)`
**Problem:**  
Find duplicates between two lists using nested loops.

**What I Learned:**
- Nested loops explode at scale
- 10,000 × 10,000 = 100 million comparisons

**Real-World Impact:**  
This is a **common cause of server timeouts**.

**Fix:**  
Convert one list to a `set`.

---

###  Sorting Cost — `O(N log N)`
**Problem:**  
Sort a random list.

**What I Learned:**
- Python uses **Timsort**
- Faster than O(N²) but slower than O(N)
- Sorting inside loops is a serious mistake

**Golden Rule:**  
Sort once, reuse many times.

---

###  Dictionary Creation Cost — `O(N)`
**Problem:**  
Measure dict creation vs dict lookup time.

**What I Learned:**
- Dictionary lookup is O(1)
- Dictionary creation is O(N)
- Hashing and memory allocation take time

**Mistake Avoided:**  
Rebuilding dicts inside loops.

---

###  Slice Copy Cost — `O(k)`
**Problem:**  
Slice a massive list: `data[0:5000]`.

**What I Learned:**
- List slicing creates a **new list**
- Data references are copied
- Cost depends on slice size, not list size

**Insight:**  
Slicing is not free.

---

##  Common Problems I Faced

- Assuming simple syntax means cheap performance
- Using lists where sets or deques were required
- Sorting and rebuilding data structures inside loops
- Ignoring hidden copy costs (strings, slices)

---

##  Key Takeaways

- Time complexity matters at scale
- Python data structures have trade-offs
- Many performance bugs are **design mistakes**, not syntax errors
- Choosing the right structure often gives massive speedups

---

##  Who This Repo Is For

- Beginners learning Big-O notation
- Python developers facing slow code
- Anyone preparing for interviews or system design
- Developers who want to write **scalable Python code**

---

##  Author

**Sojib Chandra Roy**  
Focused on learning performance-aware Python and real-world optimization patterns.


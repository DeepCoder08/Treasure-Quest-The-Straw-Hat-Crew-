# 🏴‍☠️ COL106 Assignment 3 — Treasure Quest: The Straw Hat Crew

This repository contains the solution for **COL106 Assignment 3** (Semester I - 2024), themed around organizing treasure collected by the Straw Hat pirates using efficient scheduling techniques and heap-based data structures.

---

## 📚 Problem Summary

The Straw Hat Crew is tasked with managing an ever-growing pile of treasure. Each treasure piece has:
- An **ID**
- A **size** (processing time)
- An **arrival time**

You are the **Treasurer**, responsible for assigning treasure pieces to crewmates based on specific scheduling and priority rules to minimize delay and balance workload.

---

## 🛠️ Features

### ✅ Custom Heap (Min-Heap)
Implemented from scratch (in `heap.py`), supports:
- O(n) initialization
- O(log n) insert and extract
- O(1) top operation
- Accepts any comparison function

### ✅ Crewmate Class
Each crewmate holds a priority queue of treasures and processes one treasure at a time based on:
Priority = Wait Time - Remaining Size

### ✅ StrawHatTreasury
Main class (in `straw_hat.py`) for:
- Initializing the system with `m` crewmates
- Adding new treasures as they arrive
- Returning a schedule of completed treasures using `get_completion_time()`

---

## 📁 File Structure

├── crewmate.py # Class implementation for each crewmate
├── custom.py # For any extra helper functions or classes
├── heap.py # Core heap implementation with custom comparator
├── straw_hat.py # Main logic for scheduling and treasure management
├── treasure.py # Treasure class (provided in starter code)
├── README.md # You're here!


---

## 📌 Constraints

- ❌ No hash-based structures (e.g., dict, set)
- ❌ No use of built-in heaps
- ✅ Built-in `sort()` allowed only in `get_completion_time`
- ✅ Follow time complexities as per assignment:
  - `add_treasure`: O(log n + log m)
  - `get_completion_time`: O(n(log n + log m))

---

## 🧪 Example Usage

```python
from straw_hat import StrawHatTreasury
from treasure import Treasure

# Initialize with 3 crewmates
treasury = StrawHatTreasury(3)

# Add treasure with id=1, size=5, arrival=0
treasury.add_treasure(Treasure(1, 5, 0))

# Get current completion times
schedule = treasury.get_completion_time()

🚀 How to Run
This is a module-style implementation meant for autograding.
To test it manually, create your own driver script and import the core classes.


👨‍💻 Author
Name: Deepanshu

Entry Number: 2023MT10689

📄 License
This project is for academic use only as part of COL106 (Data Structures & Algorithms) at IIT Delhi.

# Tech Interview Prep: Animal Leg Count in the Forest

This project simulates a real technical interview question from an environmental research company. The task is to analyze an array of animals and determine how many of them have exactly four legs. This README includes clarifying questions, diagrams, test cases, and complexity analysis as required by the assignment.

---

## 📌 Problem Statement

Given an array `animals` representing different animals in a forest, return the count of animals that have **exactly four legs**.

### Input Format
An array of strings, where each string represents the name of an animal.

### Output Format
An integer representing the number of animals with exactly four legs.

### Examples

**Example 1**  
Input: `['lion', 'monkey', 'deer', 'snake', 'elephant']`  
Output: `3`  
Explanation: lion, deer, and elephant each have four legs.

**Example 2**  
Input: `['frog', 'horse', 'spider', 'ant']`  
Output: `1`  
Explanation: only horse has four legs.

### Animal Leg Reference (from assignment)
- **Four legs:** lion, deer, elephant, horse, dog, cat  
- **Two legs:** monkey, parrot, ostrich  
- **Zero legs:** snake, worm  
- **More than four:** spider, ant, centipede  

---

## 📌 Clarifying Questions (as asked in a real interview)

1. Should the function ignore animals not in the provided leg‑count list  
2. Should the function treat animal names case‑sensitively  
3. Can the input list be empty  
4. Should invalid entries (numbers, None, objects) be ignored  
5. Should duplicate animals be counted separately  
6. Should whitespace or formatting differences be normalized  
7. Should we validate that each element is a string  
8. Should unknown animals default to zero legs or be skipped  

These questions ensure alignment with the interviewer before coding.

---

## 📌 Final Assumptions

- Input is a list of strings  
- Unknown animals are skipped  
- Case‑insensitive matching is used  
- Only animals with exactly four legs are counted  
- Invalid entries (non‑strings) are ignored  
- The function returns only the count  

---

## 📌 Flowchart (ASCII Diagram)

                 +---------------------------+
                 |           Start           |
                 +-------------+-------------+
                               |
                               v
                 +-------------+-------------+
                 |   Iterate through animals |
                 +-------------+-------------+
                               |
                               v
                 +-------------+-------------+
                 | Normalize name (lowercase)|
                 +-------------+-------------+
                               |
                               v
                 +-------------+-------------+
                 |       Lookup leg count    |
                 +-------------+-------------+
                         | Found       | Not found
                         v             v
                 +-------------+   +-------------+
                 | Is legs == 4 |   | Skip animal|
                 +------+------+   +-------------+
                        |
                        v
                 +------+----------------+
                 |    Increment count    |
                 +------+----------------+
                        |
                        v
                 +------+----------------+
                 |   Return final count  |
                 +-----------------------+


---

## 📌 Time & Space Complexity

### **Time Complexity: O(n)**  
We iterate through the list once and perform constant‑time lookups.

### **Space Complexity: O(1)**  
No additional data structures grow with input size.

---

See `test_four_legged_animal.py` for full unit test implementation (3 normal + 3 edge cases).





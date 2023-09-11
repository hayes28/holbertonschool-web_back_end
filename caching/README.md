# Caching Algorithms in Python

## Background Context

In this project, you will learn different caching algorithms.

## Resources

**Read or Watch:**

- [Cache replacement policies - FIFO](https://en.wikipedia.org/wiki/Cache_replacement_policies#First_In_First_Out_%28FIFO%29)
- [Cache replacement policies - LIFO](https://en.wikipedia.org/wiki/Cache_replacement_policies#Last_In_First_Out_%28LIFO%29)
- [Cache replacement policies - LRU](https://en.wikipedia.org/wiki/Cache_replacement_policies#Least_Recently_Used_%28LRU%29)
- [Cache replacement policies - MRU](https://en.wikipedia.org/wiki/Cache_replacement_policies#Most_Recently_Used_%28MRU%29)
- [Cache replacement policies - LFU](https://en.wikipedia.org/wiki/Cache_replacement_policies#Least-Frequently_Used_%28LFU%29)

## Learning Objectives

### General

At the end of this project, you are expected to be able to explain to anyone, without the help of Google:

- What a caching system is
- What FIFO means
- What LIFO means
- What LRU means
- What MRU means
- What LFU means
- What the purpose of a caching system is
- What limits a caching system has

## Requirements

### Python Scripts

- All your files will be interpreted/compiled on Ubuntu 18.04 LTS using python3 (version 3.7)
- All your files should end with a new line
- The first line of all your files should be exactly `#!/usr/bin/env python3`
- A README.md file, at the root of the folder of the project, is mandatory
- Your code should use the pycodestyle style (version 2.5)
- All your files must be executable
- The length of your files will be tested using `wc`

### Documentation

- All your modules should have documentation (`python3 -c 'print(__import__("my_module").__doc__)'`)
- All your classes should have documentation (`python3 -c 'print(__import__("my_module").MyClass.__doc__)'`)
- All your functions (inside and outside a class) should have documentation (`python3 -c 'print(__import__("my_module").my_function.__doc__)'` and `python3 -c 'print(__import__("my_module").MyClass.my_function.__doc__)'`)

### More Info

All your classes must inherit from `BaseCaching` defined in `base_caching.py`.

## Tasks

### 0. Basic dictionary

Create a class `BasicCache` that inherits from `BaseCaching` and is a caching system.

### 1. FIFO caching

Create a class `FIFOCache` that inherits from `BaseCaching` and is a caching system implementing the FIFO algorithm.

### 2. LIFO Caching

Create a class `LIFOCache` that inherits from `BaseCaching` and is a caching system implementing the LIFO algorithm.

### 3. LRU Caching

Create a class `LRUCache` that inherits from `BaseCaching` and is a caching system implementing the LRU algorithm.

### 4. MRU Caching

Create a class `MRUCache` that inherits from `BaseCaching` and is a caching system implementing the MRU algorithm.


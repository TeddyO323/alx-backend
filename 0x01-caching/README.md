# 0x01. Caching

## Back-end

### Background Context
In this project, you will explore different caching algorithms and how they can optimize performance in a back-end system.

### Resources
Read or watch:
- [Cache replacement policies - FIFO](https://en.wikipedia.org/wiki/Cache_replacement_policies#First_In_First_Out_(FIFO))
- [Cache replacement policies - LIFO](https://en.wikipedia.org/wiki/Cache_replacement_policies#Last_In_First_Out_(LIFO))
- [Cache replacement policies - LRU](https://en.wikipedia.org/wiki/Cache_replacement_policies#Least_Recently_Used_(LRU))
- [Cache replacement policies - MRU](https://en.wikipedia.org/wiki/Cache_replacement_policies#Most_Recently_Used_(MRU))
- [Cache replacement policies - LFU](https://en.wikipedia.org/wiki/Cache_replacement_policies#Least_Frequently_Used_(LFU))

### Learning Objectives
By the end of this project, you should be able to explain the following without any external references:

- The concept of a caching system
- What FIFO (First In First Out) means
- What LIFO (Last In First Out) means
- What LRU (Least Recently Used) means
- What MRU (Most Recently Used) means
- What LFU (Least Frequently Used) means
- The purpose of a caching system
- The limitations of a caching system

### Requirements
#### Python Scripts
- All your files will be interpreted/compiled on Ubuntu 18.04 LTS using Python 3.7
- All your files should end with a new line
- The first line of all your files should be exactly `#!/usr/bin/env python3`
- A `README.md` file at the root of the project folder is mandatory
- Your code should follow the pycodestyle style guide (version 2.5)
- All your files must be executable
- The length of your files will be tested using `wc`
- All your modules should have documentation (`python3 -c 'print(__import__("my_module").__doc__)'`)
- All your classes should have documentation (`python3 -c 'print(__import__("my_module").MyClass.__doc__)'`)
- All your functions (inside and outside a class) should have documentation (`python3 -c 'print(__import__("my_module").my_function.__doc__)'` and `python3 -c 'print(__import__("my_module").MyClass.my_function.__doc__)'`)
- Documentation should be a real sentence explaining the purpose of the module, class, or method (the length will be verified)

### More Info
#### Parent class `BaseCaching`
All your classes must inherit from `BaseCaching` defined below:

```python
#!/usr/bin/python3
""" BaseCaching module
"""

class BaseCaching():
    """ BaseCaching defines:
      - constants of your caching system
      - where your data are stored (in a dictionary)
    """
    MAX_ITEMS = 4

    def __init__(self):
        """ Initialize
        """
        self.cache_data = {}

    def print_cache(self):
        """ Print the cache
        """
        print("Current cache:")
        for key in sorted(self.cache_data.keys()):
            print("{}: {}".format(key, self.cache_data.get(key)))

    def put(self, key, item):
        """ Add an item in the cache
        """
        raise NotImplementedError("put must be implemented in your cache class")

    def get(self, key):
        """ Get an item by key
        """
        raise NotImplementedError("get must be implemented in your cache class")
```

### Tasks

#### 0. Basic dictionary
Create a class `BasicCache` that inherits from `BaseCaching` and implements a basic caching system without any limit.

- Use `self.cache_data` from the parent class `BaseCaching`.
- `def put(self, key, item):`
  - Assign the item value to `self.cache_data` for the key.
  - If key or item is None, do nothing.
- `def get(self, key):`
  - Return the value in `self.cache_data` for the key.
  - If key is None or doesn't exist, return None.

```python
#!/usr/bin/python3
""" 0-main """
BasicCache = __import__('0-basic_cache').BasicCache

my_cache = BasicCache()
my_cache.print_cache()
my_cache.put("A", "Hello")
my_cache.put("B", "World")
my_cache.put("C", "Holberton")
my_cache.print_cache()
print(my_cache.get("A"))
print(my_cache.get("B"))
print(my_cache.get("C"))
print(my_cache.get("D"))
my_cache.print_cache()
my_cache.put("D", "School")
my_cache.put("E", "Battery")
my_cache.put("A", "Street")
my_cache.print_cache()
print(my_cache.get("A"))
```

**Repo:**
- GitHub repository: `alx-backend`
- Directory: `0x01-caching`
- File: `0-basic_cache.py`

#### 1. FIFO caching
Create a class `FIFOCache` that inherits from `BaseCaching` and implements a caching system with FIFO replacement policy.

- Use `self.cache_data` from the parent class `BaseCaching`.
- You can override `__init__` but must call `super().__init__()`.
- `def put(self, key, item):`
  - Assign the item value to `self.cache_data` for the key.
  - If key or item is None, do nothing.
  - If the number of items exceeds `BaseCaching.MAX_ITEMS`, discard the first item added.
  - Print `DISCARD: <key>` for the discarded key.
- `def get(self, key):`
  - Return the value in `self.cache_data` for the key.
  - If key is None or doesn't exist, return None.

```python
#!/usr/bin/python3
""" 1-main """
FIFOCache = __import__('1-fifo_cache').FIFOCache

my_cache = FIFOCache()
my_cache.put("A", "Hello")
my_cache.put("B", "World")
my_cache.put("C", "Holberton")
my_cache.put("D", "School")
my_cache.print_cache()
my_cache.put("E", "Battery")
my_cache.print_cache()
my_cache.put("C", "Street")
my_cache.print_cache()
my_cache.put("F", "Mission")
my_cache.print_cache()
```

**Repo:**
- GitHub repository: `alx-backend`
- Directory: `0x01-caching`
- File: `1-fifo_cache.py`

#### 2. LIFO Caching
Create a class `LIFOCache` that inherits from `BaseCaching` and implements a caching system with LIFO replacement policy.

- Use `self.cache_data` from the parent class `BaseCaching`.
- You can override `__init__` but must call `super().__init__()`.
- `def put(self, key, item):`
  - Assign the item value to `self.cache_data` for the key.
  - If key or item is None, do nothing.
  - If the number of items exceeds `BaseCaching.MAX_ITEMS`, discard the last item added.
  - Print `DISCARD: <key>` for the discarded key.
- `def get(self, key):`
  - Return the value in `self.cache_data` for the key.
  - If key is None or doesn't exist, return None.

```python
#!/usr/bin/python3
""" 2-main """
LIFOCache = __import__('2-lifo_cache').LIFOCache

my_cache = LIFOCache()
my_cache.put("A", "Hello")
my_cache.put("B", "World")
my_cache.put("C", "Holberton")
my_cache.put("D", "School")
my_cache.print_cache()
my_cache.put("E", "Battery")
my_cache.print_cache()
my_cache.put("C", "Street")
my_cache.print_cache()
my_cache.put("F", "Mission")
my_cache.print_cache()
my_cache.put("G", "San Francisco")
my_cache.print_cache()
```

**Repo:**
- GitHub repository: `alx-backend`
- Directory: `0x01-caching`
- File: `2-lifo_cache.py`

#### 3. LRU Caching
Create a class `LRUCache` that inherits from `BaseCaching` and implements a caching system with LRU replacement policy.

- Use `self.cache_data` from the parent class `BaseCaching`.
- You can override `__init__` but must call `super().__init__()`.
- `def put(self, key, item):`
  - Assign the item value to `self.cache_data` for the key.
  - If key or item is None, do nothing.
  - If the number of items exceeds `BaseCaching.MAX_ITEMS`, discard the least recently used item.
  - Print `DISCARD: <key>` for the discarded key.
- `def get(self, key):`
  - Return the value in `self.cache_data` for the key.
  - If key is None or doesn't exist, return None.

```python
#!/usr/bin/python3
""" 3-main """
LRUCache = __import__('3-lru_cache').LRUCache

my_cache = LRUCache()
my_cache.put("A", "Hello")
my_cache.put("B", "World")
my_cache.put("C", "Holberton")
my_cache.put("D", "School")
my_cache.print_cache()
my_cache.put("E", "Battery")
my_cache.print_cache()
my_cache.put("C", "Street")
my_cache.print_cache()
my_cache.put("F", "Mission")
my_cache.print_cache()
my_cache.put("G", "San Francisco")
my_cache.print_cache()
my_cache.put("H", "Bay")
my_cache.print_cache()
```

**Repo:**
- GitHub repository: `alx-backend`
- Directory: `0x01-caching`
- File: `3-lru_cache.py`

#### 4. MRU Caching
Create a class `MRUCache` that inherits from `BaseCaching` and implements a caching system with MRU replacement policy.

- Use `self.cache_data` from the parent class `BaseCaching`.
- You can override `__init__` but must call `super().__init__()`.
- `def put(self, key, item):`
  - Assign the item value to `self.cache_data` for the key.
  - If key or item is None, do nothing.
  - If the number of items exceeds `BaseCaching.MAX_ITEMS`, discard the most recently used item.
  - Print `DISCARD: <key>` for the discarded key.
- `def get(self, key):`
  - Return the value in `self.cache_data` for the key.
  - If key is None or doesn't exist, return None.

```python
#!/usr/bin/python3
""" 4-main """
MRUCache = __import__('4-mru_cache').MRUCache

my_cache = MRUCache()
my_cache.put("A", "Hello")
my_cache.put("B", "World")
my_cache.put("C", "Holberton")
my_cache.put("D", "School")
my_cache.print_cache()
my_cache.put("E", "Battery")
my_cache.print_cache()
my_cache.put("C", "Street")
my_cache.print_cache()
my_cache.put("F", "Mission")
my_cache.print_cache()
my_cache.put("G", "San Francisco")
my_cache.print_cache()
my_cache.put("H", "Bay")
my_cache.print_cache()
```

**Repo:**
- GitHub repository: `alx-backend`
- Directory: `0x01-caching`
- File: `4-mru_cache.py`

#### 5. LFU Caching
Create a class `LFUCache` that inherits from `BaseCaching` and implements a caching system with LFU replacement policy.

- Use `self.cache_data` from the parent class `BaseCaching`.
- You can override `__init__` but must call `super().__init__()`.
- `def put(self, key, item):`
  - Assign the item value to `self.cache_data` for the key.
  - If key or item is None, do nothing.
  - If the number of items exceeds `BaseCaching.MAX_ITEMS`, discard the least frequently used item.
  - Print `DISCARD: <key>` for the discarded key.
- `def get(self, key):`
  - Return the value in `self.cache_data` for the key.
  - If key is None or doesn't exist, return None.

```python
#!/usr/bin/python3
""" 5-main """
LFUCache = __import__('5-lfu_cache').LFUCache

my_cache = LFUCache()
my_cache.put("A", "Hello")
my_cache.put("B", "World")
my_cache.put("C", "Holberton")
my_cache.put("D", "School")
my_cache.print_cache()
my_cache.put("E", "Battery")
my_cache.print_cache()
my_cache.put("C", "Street")
my_cache.print_cache()
my_cache.put("F", "Mission")
my_cache.print_cache()
my_cache.put("G", "San Francisco")
my_cache.print_cache()
my_cache.put("H", "Bay")
my_cache.print_cache()
```

**Repo:**
- GitHub repository: `alx-backend`
- Directory: `0x01-caching`
- File: `5-lfu_cache.py`

### Author
This project is part of the ALX Software Engineering Program.

**Author:**
- **Teddy Omondi**

Feel free to contact me at [omosh60@gmail.com](mailto:omosh60@gmail.com) for any queries or collaboration opportunities.
Here's the content for your `README.md` file in Markdown language:

```markdown
# 0x00. Pagination

#### `Back-end`

![cat](images/1.png)
![cat](images/2.png)
![cat](images/3.png)


### Resources
Read or watch:
- [REST API Design: Pagination](https://restfulapi.net/rest-api-pagination/)
- [HATEOAS](https://restfulapi.net/hateoas/)

### Learning Objectives
At the end of this project, you are expected to be able to explain to anyone, without the help of Google:
- How to paginate a dataset with simple page and page_size parameters
- How to paginate a dataset with hypermedia metadata
- How to paginate in a deletion-resilient manner

### Requirements
- All your files will be interpreted/compiled on Ubuntu 18.04 LTS using python3 (version 3.7)
- All your files should end with a new line
- The first line of all your files should be exactly `#!/usr/bin/env python3`
- A `README.md` file, at the root of the folder of the project, is mandatory
- Your code should use the pycodestyle style (version 2.5.*)
- The length of your files will be tested using `wc`
- All your modules should have a documentation (`python3 -c 'print(__import__("my_module").__doc__)'`)
- All your functions should have a documentation (`python3 -c 'print(__import__("my_module").my_function.__doc__)'`)
- A documentation is not a simple word, it’s a real sentence explaining what’s the purpose of the module, class or method (the length of it will be verified)
- All your functions and coroutines must be type-annotated

### Setup: Popular_Baby_Names.csv
Use this data file for your project.

### Tasks

#### 0. Simple helper function
**Mandatory**

Write a function named `index_range` that takes two integer arguments `page` and `page_size`.

The function should return a tuple of size two containing a start index and an end index corresponding to the range of indexes to return in a list for those particular pagination parameters.

Page numbers are 1-indexed, i.e. the first page is page 1.

```python
bob@dylan:~$ cat 0-main.py
#!/usr/bin/env python3
"""
Main file
"""

index_range = __import__('0-simple_helper_function').index_range

res = index_range(1, 7)
print(type(res))
print(res)

res = index_range(page=3, page_size=15)
print(type(res))
print(res)

bob@dylan:~$ ./0-main.py
<class 'tuple'>
(0, 7)
<class 'tuple'>
(30, 45)
bob@dylan:~$
```

**Repo:**
- GitHub repository: `alx-backend`
- Directory: `0x00-pagination`
- File: `0-simple_helper_function.py`

#### 1. Simple pagination
**Mandatory**

Copy `index_range` from the previous task and the following class into your code:

```python
import csv
import math
from typing import List

class Server:
    """Server class to paginate a database of popular baby names.
    """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None

    def dataset(self) -> List[List]:
        """Cached dataset
        """
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def get_page(self, page: int = 1, page_size: int = 10) -> List[List]:
        pass
```

Implement a method named `get_page` that takes two integer arguments `page` with default value 1 and `page_size` with default value 10.

- Use this CSV file (same as the one presented at the top of the project)
- Use `assert` to verify that both arguments are integers greater than 0.
- Use `index_range` to find the correct indexes to paginate the dataset correctly and return the appropriate page of the dataset (i.e. the correct list of rows).
- If the input arguments are out of range for the dataset, an empty list should be returned.

```python
bob@dylan:~$ wc -l Popular_Baby_Names.csv
19419 Popular_Baby_Names.csv
bob@dylan:~$  
bob@dylan:~$ head Popular_Baby_Names.csv
Year of Birth,Gender,Ethnicity,Child's First Name,Count,Rank
2016,FEMALE,ASIAN AND PACIFIC ISLANDER,Olivia,172,1
2016,FEMALE,ASIAN AND PACIFIC ISLANDER,Chloe,112,2
2016,FEMALE,ASIAN AND PACIFIC ISLANDER,Sophia,104,3
2016,FEMALE,ASIAN AND PACIFIC ISLANDER,Emma,99,4
2016,FEMALE,ASIAN AND PACIFIC ISLANDER,Emily,99,4
2016,FEMALE,ASIAN AND PACIFIC ISLANDER,Mia,79,5
2016,FEMALE,ASIAN AND PACIFIC ISLANDER,Charlotte,59,6
2016,FEMALE,ASIAN AND PACIFIC ISLANDER,Sarah,57,7
2016,FEMALE,ASIAN AND PACIFIC ISLANDER,Isabella,56,8
bob@dylan:~$
```

```python
bob@dylan:~$ cat 1-main.py
#!/usr/bin/env python3
"""
Main file
"""

Server = __import__('1-simple_pagination').Server

server = Server()

try:
    should_err = server.get_page(-10, 2)
except AssertionError:
    print("AssertionError raised with negative values")

try:
    should_err = server.get_page(0, 0)
except AssertionError:
    print("AssertionError raised with 0")

try:
    should_err = server.get_page(2, 'Bob')
except AssertionError:
    print("AssertionError raised when page and/or page_size are not ints")

print(server.get_page(1, 3))
print(server.get_page(3, 2))
print(server.get_page(3000, 100))

bob@dylan:~$
bob@dylan:~$ ./1-main.py
AssertionError raised with negative values
AssertionError raised with 0
AssertionError raised when page and/or page_size are not ints
[['2016', 'FEMALE', 'ASIAN AND PACIFIC ISLANDER', 'Olivia', '172', '1'], ['2016', 'FEMALE', 'ASIAN AND PACIFIC ISLANDER', 'Chloe', '112', '2'], ['2016', 'FEMALE', 'ASIAN AND PACIFIC ISLANDER', 'Sophia', '104', '3']]
[['2016', 'FEMALE', 'ASIAN AND PACIFIC ISLANDER', 'Emily', '99', '4'], ['2016', 'FEMALE', 'ASIAN AND PACIFIC ISLANDER', 'Mia', '79', '5']]
[]
bob@dylan:~$
```

**Repo:**
- GitHub repository: `alx-backend`
- Directory: `0x00-pagination`
- File: `1-simple_pagination.py`

#### 2. Hypermedia pagination
**Mandatory**

Replicate code from the previous task.

Implement a `get_hyper` method that takes the same arguments (and defaults) as `get_page` and returns a dictionary containing the following key-value pairs:
- `page_size`: the length of the returned dataset page
- `page`: the current page number
- `data`: the dataset page (equivalent to return from previous task)
- `next_page`: number of the next page, `None` if no next page
- `prev_page`: number of the previous page, `None` if no previous page
- `total_pages`: the total number of pages in the dataset as an integer

Make sure to reuse `get_page` in your implementation.

You can use the `math` module if necessary.

```python
bob@dylan:~$ cat 2-main.py
#!/usr/bin/env python3
"""
Main file
"""

Server = __import__('2-hypermedia_pagination').Server

server = Server()

print(server.get_hyper(1, 2))
print("---")
print(server.get_hyper(2, 2))
print("---")
print(server.get_hyper(100, 3))
print("---")
print(server.get_hyper(3000, 100))

bob@dylan:~$
bob@dylan:~$ ./2-main.py
{'page_size': 2, 'page': 1, 'data': [['2016', 'FEMALE', 'ASIAN AND PACIFIC ISLANDER', 'Olivia', '172', '1'], ['2016', 'FEMALE', 'ASIAN AND PACIFIC ISLANDER', 'Chloe', '112', '2']], 'next_page': 2, 'prev_page': None, 'total_pages': 9709}
---
{'page_size': 2, 'page': 2, 'data': [['2016', 'FEMALE', 'ASIAN AND PACIFIC ISLANDER', 'Sophia', '104', '3'], ['2016', 'FEMALE', 'ASIAN AND PACIFIC ISLANDER', 'Emma', '99', '4']], 'next_page

': 3, 'prev_page': 1, 'total_pages': 9709}
---
{'page_size': 3, 'page': 100, 'data': [['2016', 'FEMALE', 'ASIAN AND PACIFIC ISLANDER', 'Nicole', '27', '19'], ['2016', 'FEMALE', 'ASIAN AND PACIFIC ISLANDER', 'Victoria', '27', '19'], ['2016', 'FEMALE', 'ASIAN AND PACIFIC ISLANDER', 'Amber', '26', '20']], 'next_page': 101, 'prev_page': 99, 'total_pages': 6474}
---
{'page_size': 0, 'page': 3000, 'data': [], 'next_page': None, 'prev_page': 2999, 'total_pages': 195}
bob@dylan:~$
```

**Repo:**
- GitHub repository: `alx-backend`
- Directory: `0x00-pagination`
- File: `2-hypermedia_pagination.py`

#### 3. Deletion-resilient hypermedia pagination
**Mandatory**

The goal here is that if between two queries, certain rows are removed from the dataset, the user does not miss items from dataset when changing page.

For example, if dataset was sorted by `Name` and user was on page 1, then the first element on page 2 was “Bob”, and if page 1 is updated by deleting “Bob” from dataset, user will miss the first item on page 2 (that would have been “Bob”).

Copy the code from the previous task and implement `get_hyper_index` method. The method should return a dictionary with the following key-value pairs:
- `index`: the current start index of the return page. That is the index of the first item in the current page. For the first page, the index is 0.
- `next_index`: the next index to query with. That should be the next start index, or None if no more data.
- `page_size`: the current page size
- `data`: the data in the page

Use the `index` as a cursor to know where to resume the pagination. With this type of pagination, when an element is deleted from dataset, it will not affect the current page.

```python
bob@dylan:~$ cat 3-main.py
#!/usr/bin/env python3
"""
Main file
"""

Server = __import__('3-hypermedia_del_pagination').Server

server = Server()

server.dataset() = server.dataset()[:10]

for i in range(3):
    print(server.get_hyper_index(i, 3))
    print("---")

bob@dylan:~$
bob@dylan:~$ ./3-main.py
{'index': 0, 'next_index': 3, 'page_size': 3, 'data': [['2016', 'FEMALE', 'ASIAN AND PACIFIC ISLANDER', 'Olivia', '172', '1'], ['2016', 'FEMALE', 'ASIAN AND PACIFIC ISLANDER', 'Chloe', '112', '2'], ['2016', 'FEMALE', 'ASIAN AND PACIFIC ISLANDER', 'Sophia', '104', '3']]}
---
{'index': 3, 'next_index': 6, 'page_size': 3, 'data': [['2016', 'FEMALE', 'ASIAN AND PACIFIC ISLANDER', 'Emma', '99', '4'], ['2016', 'FEMALE', 'ASIAN AND PACIFIC ISLANDER', 'Emily', '99', '4'], ['2016', 'FEMALE', 'ASIAN AND PACIFIC ISLANDER', 'Mia', '79', '5']]}
---
{'index': 6, 'next_index': 9, 'page_size': 3, 'data': [['2016', 'FEMALE', 'ASIAN AND PACIFIC ISLANDER', 'Charlotte', '59', '6'], ['2016', 'FEMALE', 'ASIAN AND PACIFIC ISLANDER', 'Sarah', '57', '7'], ['2016', 'FEMALE', 'ASIAN AND PACIFIC ISLANDER', 'Isabella', '56', '8']]}
---
```

**Repo:**
- GitHub repository: `alx-backend`
- Directory: `0x00-pagination`
- File: `3-hypermedia_del_pagination.py`
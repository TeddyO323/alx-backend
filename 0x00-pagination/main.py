# main.py
#!/usr/bin/env python3
"""
Main file
"""

Server = __import__('3-hypermedia_del_pagination').Server

server = Server()

# Test Task 0
print(index_range(1, 10))  # Expected output: (0, 10)
print(index_range(2, 5))   # Expected output: (5, 10)

# Test Task 1
print(server.get_page(1, 10))  # Expected output: First 10 rows of the dataset

# Test Task 2
print(server.get_hyper(1, 10))  # Expected output: Hypermedia pagination of the first 10 rows

# Test Task 3
server.dataset() = server.dataset()[:10]
for i in range(3):
    print(server.get_hyper_index(i, 3))
    print("---")

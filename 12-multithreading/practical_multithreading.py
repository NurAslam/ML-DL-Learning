from datetime import datetime
import time
import threading


# def print_number():
#     for i in range(5):
#         print(f'number: {i}')

# def print_letter():
#     for letter in 'abcde':
#         print(f'Letter: {letter}')



# t = datetime.now()
# print_number()
# print_letter()
# finished_time = datetime.now() - t
# print(finished_time)


# Pakai sleep
def print_number():
    for i in range(5):
        time.sleep(2)
        print(f'number: {i}')

def print_letter():
    for letter in 'abcde':
        time.sleep(2)
        print(f'Letter: {letter}')

# print("Tanpa Threading")
# t = datetime.now()
# print_number()
# print_letter()
# finished_time = datetime.now() - t
# print(finished_time)

"""
Output:
number: 0
number: 1
number: 2
number: 3
number: 4
Letter: a
Letter: b
Letter: c
Letter: d
Letter: e
0:00:00.003578
"""

# Create 2 Threads
t1 = threading.Thread(target=print_number)
t2 = threading.Thread(target=print_letter)

print("Menggunakan Threading")
t = datetime.now()
t1.start()
t2.start()
finished_time = datetime.now() - t
print(finished_time)

"""
Output:
number: 0
Letter: a
number: 1
Letter: b
number: 2
Letter: c
number: 3
Letter: d
number: 4
"""


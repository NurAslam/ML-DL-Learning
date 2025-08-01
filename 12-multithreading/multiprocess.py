# Process that run in paralel
# CPU-Bound Task-Task that are heavy on CPU usage
# Parallel execution - Multiple cores of the CPU


import multiprocessing
import time


def square_number():
    for i in range(5):
        time.sleep(1)
        print(f"Square: {i*i}")

def cube_number():
    for i in range(5):
        time.sleep(1.5)
        print(f"Cube: {i*i*i}")


if __name__ == "__main__":

    # create 2 processes
    p1 = multiprocessing.Process(target=square_number)
    p2 = multiprocessing.Process(target=cube_number)
    t = time.time()


    # start the process
    p1.start()
    p2.start()

    # wait for the process to complete
    p1.join()
    p2.join()

    finished_time=time.time()-t
    print(finished_time)

# Output
# Square: 0
# Cube: 0
# Square: 1
# Cube: 1
# Square: 4
# Square: 9
# Cube: 8
# Square: 16
# Cube: 27
# Cube: 64
# 7.997034072875977

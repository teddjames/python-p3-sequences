#!/usr/bin/env python3

def print_fibonacci(n):
    if n <= 0:
        seq = []
    elif n == 1:
        seq = [0]
    else:
        seq = [0, 1]
        for _ in range(2, n):
            seq.append(seq[-1] + seq[-2])

    print(seq)
    return seq


if __name__ == "__main__":
    print_fibonacci(5)  

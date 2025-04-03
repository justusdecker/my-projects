"""
(c) 2025 translated from [classworks\\classwork - other langs\\c\\main.c] to python
"""

def compute_sum_normal(limit: int) -> int:
    s: int = 0
    for i in range(1,limit-1):
        s += i
    return i

def compute_sum(limit: int) -> int:
    return sum([i for i in range(1,limit)])
def main():
    max_number: int = 100
    result: int = compute_sum(max_number)
    print(f"Sum of numbers from 1 to {max_number} is {result}\n")
main()
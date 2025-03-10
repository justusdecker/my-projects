
def fibonacci_sequence():
    fibonacci = [1,2]
    for i in range(100): fibonacci.append(sum(fibonacci[-2:]))
    return fibonacci
    
for i in fibonacci_sequence():
    print(i)

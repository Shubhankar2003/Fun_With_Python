import matplotlib.pyplot as plt

def Collatz(n):
    sequence = [n]
    while n != 1:
        if n % 2 == 0:
            n = n // 2
        else:
            n = 3 * n + 1
        sequence.append(n)
    return sequence

plt.figure(figsize=(10, 6))

for num in range(1, 15):
    sequence = Collatz(num)
    plt.plot(sequence, marker='.', label=f'n = {num}')

plt.xlabel('Step')
plt.ylabel('Value')
plt.title('Collatz Sequences (1-21)')
plt.grid(False)
plt.legend()
plt.show()

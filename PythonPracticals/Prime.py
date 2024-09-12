def is_prime(num):
    """Check if a number is a prime number."""
    if num <= 1:
        return False
    if num <= 3:
        return True
    if num % 2 == 0 or num % 3 == 0:
        return False
    i = 5
    while i * i <= num:
        if num % i == 0 or num % (i + 2) == 0:
            return False
        i += 6
    return True

def print_primes(m, n):
    """Print all prime numbers between m and n (exclusive)."""
    for num in range(m, n + 1):
        if is_prime(num):
            print(num)

# Example usage
m = int(input("Enter a number"))
n = int(input("Enter a number"))
print(f"Prime numbers between {m} and {n} are:")
print_primes(m, n)

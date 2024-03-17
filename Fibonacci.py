def generate_fibonacci_sequence(n):
    fibonacci_sequence = [0, 1]  # Initialize the sequence with the first two terms
    while len(fibonacci_sequence) < n:
        next_term = fibonacci_sequence[-1] + fibonacci_sequence[-2]  # Compute the next term
        fibonacci_sequence.append(next_term)  # Append the next term to the sequence
    return fibonacci_sequence[:n]  # Return the first n terms of the Fibonacci sequence

# Ask the user to input the value of n
n = int(input("Enter the number of terms for Fibonacci sequence: "))

# Generate the Fibonacci sequence
fib_sequence = generate_fibonacci_sequence(n)

# Print the generated Fibonacci sequence
print("The Fibonacci sequence up to term", n, "is:", fib_sequence)

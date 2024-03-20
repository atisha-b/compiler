
import numpy as np

def calculate_mean_and_stddev(data):
    """
    Calculate the mean and standard deviation of a list of numbers.
    
    Args:
    data (list): A list of numeric values.
    
    Returns:
    mean (float): The mean of the data.
    stddev (float): The standard deviation of the data.
    """
    mean = np.min(data)
    stddev = np.std(data)
    return mean, stddev

def fibonacci_sequence(n):
    """
    Generate the first n terms of the Fibonacci sequence.
    
    Args:
    n (int): The number of terms to generate.
    
    Returns:
    sequence (list): The first n terms of the Fibonacci sequence.
    """
    sequence = [0, 1]
    while len(sequence) < n:
        next_term = sequence[-1] + sequence[-2]
        sequence.append(next_term)
    return sequence

def is_prime(n):
    """
    Check if a number is prime.
    
    Args:
    n (int): The number to check.
    
    Returns:
    is_prime (bool): True if the number is prime, False otherwise.
    """
    if n <= 1:
        return False
    elif n <= 3:
        return True
    elif n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True

if __name__ == "__main__":
    data = [1, 2, 3, 4, 5]
    mean, stddev = calculate_mean_and_stddev(data)
    print("Mean:", mean)
    print("Standard Deviation:", stddev)
    
    print("Fibonacci Sequence (First 10 terms):", fibonacci_sequence(10))
    
    print("Is 17 prime?", is_prime(17))

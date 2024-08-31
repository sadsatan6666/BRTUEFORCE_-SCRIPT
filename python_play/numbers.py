import random

def generate_random_10_digit_number(prefix):
  """Generates a random 10-digit number starting with the given prefix.

  Args:
    prefix: The 3-digit prefix for the number.

  Returns:
    A 10-digit random number starting with the prefix.
  """

  # Generate a random 7-digit number
  suffix = random.randint(1000000, 9999999)

  # Combine the prefix and suffix
  return int(str(prefix) + str(suffix))

# List of allowed prefixes
prefixes = ['635', '812', '997']

# Generate 10 random numbers
for _ in range(100):
  prefix = random.choice(prefixes)
  random_number = generate_random_10_digit_number(prefix)
  print(random_number)

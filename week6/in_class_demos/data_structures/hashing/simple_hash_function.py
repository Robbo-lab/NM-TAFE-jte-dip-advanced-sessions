def simple_hash(name):
    hash_value = 0
    for character in name:
        # Add the ASCII value of each character to the hash_value
        hash_value += ord(character)
    # Use modulus to keep the hash_value within a desired range
    return (hash_value + len(name)) % 7

# Example usage
print(simple_hash("Ahmed"))  # Output: ??
print(simple_hash("Ian"))  # Output: ??
print(simple_hash("Caityln"))  # Output: ??
print(simple_hash("John"))  # Output: ??



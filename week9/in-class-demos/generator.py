# Our generator
def get_lines(filename):
    with open(filename) as f:
        for line in f:
            yield line.strip()

# Imagine reading a huge file
for line in get_lines("large_data.txt"):
    print(line)

    def get_even_numbers(limit):
        for num in range(limit + 1):
            if num % 2 == 0:
                yield num

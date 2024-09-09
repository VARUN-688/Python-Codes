# Input is a comma-separated list of Roman numerals
ip = input().split(', ')

# Dictionary mapping Roman numeral symbols to their integer values
d = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}

# Initialize result to zero
res = 0

# Iterate over each Roman numeral in the input list
for j in range(len(ip)):
    res = 0
    rm = ip[j]  # Get the current Roman numeral
    i = 0  # Initialize index for the Roman numeral string

    # Loop through the Roman numeral string
    while i < len(rm) - 1:
        # Check if the current symbol is a valid Roman numeral
        if rm[i] not in set(d.keys()):
            print(f"Invalid input {i} so ignored and moved forward")
        else:
            # If the next symbol is greater than the current symbol, subtract the current symbol's value
            if d.get(rm[i + 1]) > d.get(rm[i]):
                res += (d.get(rm[i + 1]) - d.get(rm[i]))
                i += 2  # Move to the next symbol after the pair
            else:
                # Otherwise, add the current symbol's value
                res += d.get(rm[i])
                i += 1  # Move to the next symbol

    # If there's a remaining symbol at the end, add its value
    if i < len(rm):
        res += d.get(rm[-1])

    # Print the result for the current Roman numeral
    print(f"{ip[j]}->{res}")

'''Here are the steps with descriptions:

1. Input Parsing:
   - Description:
     The input is read as a single string containing Roman numerals separated by commas. This string is then split into a list of individual Roman numerals using `split(', ')`.

2. Initialize Roman Numeral Dictionary:
   - Description:
     A dictionary is created to map each Roman numeral character (I, V, X, L, C, D, M) to its respective integer value. This allows for quick lookups of each character's value.

3. Iterate Through Each Roman Numeral:
   - Description:
     The code processes each Roman numeral from the list one by one. For each numeral, it initializes a variable `res` to accumulate the total integer value.

4. **Process Each Character in the Roman Numeral:**
   - Description:
     - **Check for Valid Characters:** Each character in the Roman numeral string is checked to ensure it is a valid Roman numeral. If a character is invalid, an error message is printed, and the character is skipped.
     - **Apply Subtraction Rule:** If the value of the next character is greater than the current character, this indicates a subtractive combination (e.g., IV for 4). The value of the current character is subtracted from the next character's value and added to the total.
     - **Apply Addition Rule:** If the next character's value is not greater, the current character's value is added to the total.

5. **Handle Remaining Characters:**
   - Description:
     After processing most characters, if there is a single character left at the end of the string (i.e., when the length of the string hasn't been reached), its value is added to the total.

6. **Output the Result:**
   - Description:
     The final computed integer value for each Roman numeral is printed in the format `RomanNumeral->IntegerValue`. This provides the converted value for each input numeral.'''




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

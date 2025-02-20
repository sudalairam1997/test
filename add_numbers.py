import re
def add(numbers: str) -> int:
    if not numbers:
        return 0

    delimiter = ','  # Default delimiter

    # Check for custom delimiter
    if numbers.startswith("//"):
       match = re.match(r"//(.+)\n(.*)", numbers, re.DOTALL)
       if match:
          delimiter, numbers = match.groups()
          delimiter = re.escape(delimiter)  # Ensure special characters are escaped
       else:
          raise ValueError("Invalid input format")

    # Replace newlines with the delimiter and split
    numbers = re.split(f"[{delimiter}\n]", numbers)

    # Convert to integers and check for negatives
    int_numbers = []
    negatives = []

    for num in numbers:
        if num:
            value = int(num)
            if value < 0:
                negatives.append(value)
            int_numbers.append(value)

    if negatives:
        raise ValueError(f"negative numbers not allowed {','.join(map(str, negatives))}")

    return sum(int_numbers)
# String Calculator

## Overview
This project implements a simple string calculator function `add(numbers: str) -> int` that:
- Adds numbers from a string input.
- Supports different delimiters.
- Handles newline characters (`\n`) as delimiters.
- Throws an exception for negative numbers.

## Features
- **Basic Addition:**
  - `"1,2"` → `3`
  - `"1\n2,3"` → `6`
- **Custom Delimiters:**
  - `"//;\n1;2"` → `3`
  - `"//|\n1|2|3"` → `6`
  - `"//***\n1***2***3"` → `6`
- **Exception Handling:**
  - Negative numbers raise an error with a message listing all negative values.

## Installation
Clone the repository and install dependencies:
```sh
 git clone https://github.com/sudalairam1997/test.git
```

## Running the Code
```sh
python add_numbers.py
```

## Running Tests
To run the test cases using `pytest`:
```sh
pytest test_add.py
```

## Example Usage
```python
from add_numbers import add

print(add("1,2,3"))  # Output: 6
print(add("//;\n1;2"))  # Output: 3
```

## License
This project is licensed under the MIT License.

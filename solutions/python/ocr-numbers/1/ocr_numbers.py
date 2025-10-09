DIGITS = {
    (" _ ",
     "| |",
     "|_|",
     "   "): "0",
    ("   ",
     "  |",
     "  |",
     "   "): "1",
    (" _ ",
     " _|",
     "|_ ",
     "   "): "2",
    (" _ ",
     " _|",
     " _|",
     "   "): "3",
    ("   ",
     "|_|",
     "  |",
     "   "): "4",
    (" _ ",
     "|_ ",
     " _|",
     "   "): "5",
    (" _ ",
     "|_ ",
     "|_|",
     "   "): "6",
    (" _ ",
     "  |",
     "  |",
     "   "): "7",
    (" _ ",
     "|_|",
     "|_|",
     "   "): "8",
    (" _ ",
     "|_|",
     " _|",
     "   "): "9",
}

def convert(input_grid) -> str:
    if len(input_grid) % 4:
        raise ValueError('Number of input lines is not a multiple of four')
    if any(len(row) % 3 for row in input_grid):
        raise ValueError('Number of input columns is not a multiple of three')
    
    number_rows: list[str] = []
    for i in range(0, len(input_grid), 4):
        number_rows.append(detect_numbers(input_grid[i:i+4]))
    return ','.join(number_rows)

def detect_numbers(rows) -> str:
    number_digits: int = len(rows[0])//3
    numbers = ''
    for i in range(number_digits):
        digit = tuple(row[3*i:3*(i+1)] for row in rows)
        numbers += DIGITS.get(digit, '?')
    return numbers
        
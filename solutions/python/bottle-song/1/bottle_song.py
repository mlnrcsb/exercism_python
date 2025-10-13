def recite(start, take=1):
    number_map = {
        0: 'no',
        1: 'one',
        2: 'two',
        3: 'three',
        4: 'four',
        5: 'five',
        6: 'six',
        7: 'seven',
        8: 'eight',
        9: 'nine',
        10: 'ten'
    }
    output = []
    falling_line = 'And if one green bottle should accidentally fall,'
    for num in range(take):
        if output:
            output.append('')
        current_num = start - num
        bottle_s = 'bottles' if current_num != 1 else 'bottle'
        first_line = f'{number_map[current_num].capitalize()} green {bottle_s} hanging on the wall,'
        bottle_s = 'bottles' if current_num != 2 else 'bottle'
        last_line = f'There\'ll be {number_map[current_num - 1]} green {bottle_s} hanging on the wall.'
        output += [first_line, first_line, falling_line, last_line]
    return output

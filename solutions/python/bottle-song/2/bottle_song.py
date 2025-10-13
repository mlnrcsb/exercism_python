def recite(start, take=1):
    numbers =  ['no', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine', 'ten']
    output = []
    falling_line = 'And if one green bottle should accidentally fall,'
    for num in range(take):
        if output:
            output.append('')
        curr_num = start - num
        bottle_s = 'bottles' if curr_num != 1 else 'bottle'
        first_line = f'{numbers[curr_num].capitalize()} green {bottle_s} hanging on the wall,'
        bottle_s = 'bottles' if curr_num != 2 else 'bottle'
        last_line = f'There\'ll be {numbers[curr_num - 1]} green {bottle_s} hanging on the wall.'
        output += [first_line, first_line, falling_line, last_line]
    return output

def proverb(*input_data, qualifier):
    if not input_data:
        return []
    output = [f'For want of a {input_data[i]} the {input_data[i + 1]} was lost.' for i in range(len(input_data) - 1)]
    output.append(f'And all for the want of a{f" {qualifier} " if qualifier else " "}{input_data[0]}.')
    return output
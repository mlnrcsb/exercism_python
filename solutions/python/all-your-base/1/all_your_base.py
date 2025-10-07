def rebase(input_base, digits, output_base):
    if input_base < 2:
        raise ValueError('input base must be >= 2')
    if output_base < 2:
        raise ValueError('output base must be >= 2')

    num_base_10 = 0
    for i, digit in enumerate(digits[::-1]):
        if not 0 <= digit < input_base:
            raise ValueError('all digits must satisfy 0 <= d < input base')
        num_base_10 += digit * (input_base**i)
    
    if num_base_10 == 0:
        return [0]
    
    num_base_output = []
    while num_base_10 != 0:
        num_base_output.append(num_base_10 % output_base)
        num_base_10 //= output_base
    return num_base_output[::-1]
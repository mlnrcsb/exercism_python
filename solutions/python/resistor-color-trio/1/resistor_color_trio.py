def label(colors):
    color_values = ['black', 'brown', 'red', 'orange', 'yellow', 'green', 'blue', 'violet', 'grey', 'white']
    
    tens, ones = color_values.index(colors[0]), color_values.index(colors[1])
    power = color_values.index(colors[2])
    
    value = (10*tens + ones) * (10 ** power)
    if value >= 10**9:
        return f'{value // 10**9} gigaohms'
    if value >= 10**6:
        return f'{value // 10**6} megaohms'
    if value >= 10**3:
        return f'{value // 10**3} kiloohms'    
    return f'{value} ohms'
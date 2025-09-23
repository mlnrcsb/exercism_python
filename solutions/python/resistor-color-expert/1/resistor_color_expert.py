def resistor_label(colors):
    color_dict = {'black': 0, 'brown': 1, 'red': 2, 'orange': 3, 'yellow': 4, 'green': 5, 'blue': 6, 'violet': 7, 'grey': 8, 'white': 9}
    tolerances = {'grey': '0.05%', 'violet': '0.1%', 'blue': '0.25%', 'green': '0.5%', 'brown': '1%', 'red': '2%', 'gold': '5%', 'silver': '10%'}

    if len(colors) == 1:
        return f'{color_dict[colors[0]]} ohms'

    tolerance = ''
    if len(colors) == 4:
        tens, ones = color_dict[colors[0]], color_dict[colors[1]]
        power, tolerance = color_dict[colors[2]], tolerances[colors[3]]
        value = (10*tens + ones) * (10 ** power)
    if len(colors) == 5:
        hundreds, tens, ones = color_dict[colors[0]], color_dict[colors[1]], color_dict[colors[2]]
        power, tolerance = color_dict[colors[3]], tolerances[colors[4]]
        value = (100*hundreds + 10*tens + ones) * (10 ** power)

    tolerance_string = ''
    if tolerance:
        tolerance_string = f' ±{tolerance}'
        
    if value >= 10**9:
        value = value / 10**9 if value % 10**9 else value // 10**9
        return f'{value} gigaohms' + tolerance_string
    if value >= 10**6:
        value = value / 10**6 if value % 10**6 else value // 10**6
        return f'{value} megaohms' + tolerance_string
    if value >= 10**3:
        value = value / 10**3 if value % 10**3 else value // 10**3
        return f'{value} kiloohms' + tolerance_string
    return f'{value} ohms' + tolerance_string

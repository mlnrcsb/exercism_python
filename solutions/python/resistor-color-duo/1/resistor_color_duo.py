def value(colors):
    color_values = ['black', 'brown', 'red', 'orange', 'yellow', 'green', 'blue', 'violet', 'grey', 'white']
    tens, ones = colors[:2]
    return color_values.index(tens)*10 + color_values.index(ones)
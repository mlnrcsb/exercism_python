def annotate(garden):
    if not garden:
        return []
    
    width = len(garden[0])
    
    expanded_garden = [' ' + row + ' ' for row in garden]
    expanded_garden.insert(0, ' ' * (width + 2))
    expanded_garden.append(' ' * (width + 2))
    
    def find_nearby_stars(x_coordinate, y_coordinate):
        if garden[x_coordinate][y_coordinate] == '*':
            return '*'
        stars = 0
        for i in range(3):
            for j in range(3):
                if expanded_garden[x_coordinate+i][y_coordinate+j] == '*':
                    stars += 1
        return str(stars) if stars > 0 else ' '


    result = []
    for x, row in enumerate(garden):
        if len(row) != width:
            raise ValueError('The board is invalid with current input.')
        
        result_row = ''
        for y, element in enumerate(row):
            if element not in (' ', '*'):
                raise ValueError('The board is invalid with current input.')
                
            result_row += find_nearby_stars(x, y)
        result.append(result_row)
    return result

def recite(start_verse, end_verse):
    ordinals = ['first', 'second', 'third', 'fourth', 'fifth', 'sixth', 'seventh', 'eighth', 'ninth',
                'tenth', 'eleventh', 'twelfth']
    gifts = ['a Partridge in a Pear Tree.', 'two Turtle Doves,', 'three French Hens,', 'four Calling Birds,', 'five Gold Rings,', 'six Geese-a-Laying,', 'seven Swans-a-Swimming,', 'eight Maids-a-Milking,', 'nine Ladies Dancing,', 'ten Lords-a-Leaping,', 'eleven Pipers Piping,', 'twelve Drummers Drumming,']

    output = []
    for day in range(start_verse - 1, end_verse):
        verse = f'On the {ordinals[day]} day of Christmas my true love gave to me:'
        for i in range(day, -1, -1):
            if day > 0 and i == 0:
                verse += ' and'
            verse += f' {gifts[i]}'
        output.append(verse)
    return output

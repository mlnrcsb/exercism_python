def two_fer(name='you'):
    name = 'you' if len(name) == 0 else name
    return f'One for {name}, one for me.'

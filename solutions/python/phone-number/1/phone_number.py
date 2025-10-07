import re

class PhoneNumber:
    def __init__(self, input):
        if re.search(r'[A-Za-z]', input):
            raise ValueError('letters not permitted')

        if re.search(r'[^0-9\s().+-]', input):
            raise ValueError('punctuations not permitted')
        
        number = re.sub(r'\D', '', input)

        if len(number) < 10:
            raise ValueError('must not be fewer than 10 digits')

        if len(number) > 11:
            raise ValueError('must not be greater than 11 digits')

        if len(number) == 11:
            if number[0] != '1':
                raise ValueError('11 digits must start with 1')
            number = number[1:]

        if number[0] == '0':
            raise ValueError('area code cannot start with zero')    
        if number[0] == '1':
            raise ValueError('area code cannot start with one')
            
        if number[3] == '0':
            raise ValueError('exchange code cannot start with zero')
        if number[3] == '1':
            raise ValueError('exchange code cannot start with one')
        
        self.area_code = number[0:3]
        self.exchange_code =number[3:]
        self.number = number

    def pretty(self):
        return f'({self.area_code})-{self.exchange_code[0:3]}-{self.exchange_code[3:]}'
         
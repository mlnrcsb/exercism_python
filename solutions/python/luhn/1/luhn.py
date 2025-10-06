class Luhn:
    def __init__(self, card_num):
        self.card_num = card_num

    def valid(self):
        numbers = self.card_num.replace(' ', '')
        if len(numbers) <= 1 or not numbers.isdecimal():
            return False
            
        numbers = numbers[::-1]
        sum = 0
        for i in range(len(numbers)):
            num = int(numbers[i])
            if i % 2:
                sum += num
                if num > 4:
                    sum -= 9
            sum += num
        return not sum % 10
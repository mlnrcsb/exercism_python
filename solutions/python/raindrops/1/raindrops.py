def convert(number: int):
    raindrop = ""
    if not number % 3:
        raindrop += "Pling"
    if not number % 5:
        raindrop += "Plang"
    if not number % 7:
        raindrop += "Plong"
    return raindrop if raindrop else str(number)
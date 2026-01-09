import random

def get_numbers_ticket(min, max, quantity):
    if not 1 <= min <= max <= 1000:
        raise ValueError
    if not (1 <= quantity <= (max - min + 1)):
        raise ValueError
    
    numbers = random.sample(range(min, max + 1), quantity)
    return numbers

        
lottery_numbers = get_numbers_ticket(1, 49, 6)
print("Ваші лотерейні числа:", lottery_numbers)

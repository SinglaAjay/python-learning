
# num=100

# while num >= 1:
#     print(num)
#     num -= 1


# list_numbers=[1,4,9,16,25]

# lenth_of_list = len(list_numbers)
# counter = 0
# number_occurences = 0

# while lenth_of_list > counter:
#     if(list_numbers[counter] == 9):
#         number_occurences += 1
#     counter += 1

# print(number_occurences)

# Complex while loop: Find all prime numbers up to n
n = 50
num = 2
primes = []

while num <= n:
    is_prime = True
    divisor = 2
    
    while divisor * divisor <= num:
        if num % divisor == 0:
            is_prime = False
            break
        divisor += 1
    
    if is_prime:
        primes.append(num)
    
    num += 1

print(f"Prime numbers up to {n}: {primes}")
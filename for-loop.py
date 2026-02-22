num= int(input("Enter a number: "))
sum=0

for i in range(num):
    print(i+1)
    sum = sum +(i+1)

print(f"The sum of numbers from 0 to {num-1} is: {sum}")

print()
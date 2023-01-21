"""5 inputs from the user all ints 
prints the total"""

i = 0
numbers = []
total = 0
while i < 5:
    try:
        nums = input('Eneter number ' + str(i+1) + ':')
        nums = int(nums)
        numbers.append(nums)
        total += numbers[i]
        i= i + 1
    except(ValueError, TypeError):
        print("Error enter a int")

print("Your sum is " + total)
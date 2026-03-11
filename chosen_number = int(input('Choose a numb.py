'''
chosen_number = 0
while chosen_number == 0:
    chosen_number = (input('Choose a number '))
    if chosen_number == 0:
        print('INVALID. TRY AGAIN.')
print('5 times', chosen_number, 'is', chosen_number * 5)
print('if you add 3 to', chosen_number, 'the answer is', chosen_number + 3)
print('if you divide 20 by', chosen_number, 'the answer is', 20 / chosen_number)
'''
'''
inch = float(input('How long in inches? '))
print(inch, 'inches is equal to', inch * 2.54, 'cm')
'''
'''
sport = input("What is your favourite sport: ")
if sport == "golf":
    print("Good choice")
else:
    print(":(")
'''
'''
import random
correct = 0
repeat = int(input("How many times do you want to play: "))
for i in range(repeat):
    num1 = random.randint(1,10)
    num2 = random.randint(1,10)
    userinput = int(input(f"What is {num1} + {num2}: "))
    answer = num1 + num2
    if userinput == answer:
        print("Correct!")
        correct += 1
    else:
        print(":(")
print(f'You got {correct} out of {repeat}!')
'''
'''
contents = []
loop = True
limit = 5
while loop == True:
    numberofletters = 0
    page = input("What do you want to do?")
    if page == 'Add to cart' or page == 'add to cart':
        if len(contents) >= 5:
            print("Your shopping cart will explode if you add anymore")
        else:
            item = input("What would you like to add?")
            for letter in item:
                numberofletters += 1
            if numberofletters <= 2:
                print("Is this even an item?")
            else:
                contents.append(item)
    elif page == 'View cart' or page == 'view cart':
        if len(contents) == 0:
            print(":(")
        else:
            for content in contents:
                print(content)
    elif page == 'Remove from cart' or page == 'remove from cart':
        remove = input("What item do you want to remove?")
        for content in contents:
            if content == remove:
                
    else:
        print("<INVALID>")
'''
numbers = [8,4,11,3,1]
line = 0
for number in numbers:
    line += 1
    print(f"Q{line}: {number} * 8 = {number * 8}")


stocks = [["Banana", 50], ["Apple", 42], ["Pear", 96], ["Pineapple", 35]]
page = input("View stock or order stock").lower()
if page == "order stock":
    fruit = input("Write message: ")
    amount = int(input("How much do you want to order: "))
    stocks.append(fruit, amount)
elif page == "view stock":
    for stock in stocks:
        print(f"There are {stock[1]} {stock[0]}(s)")


userinput = ''
userintput = -1

finish = False

names = []
heights = []

def validation(value):
    try:
        number = int(value)
        return number
    except ValueError:
        print('Invalid, please use numbers.')
    

def list_in():
    name = str(input('What is the name: '))
    names.append(name)
    height = -1
    while height == -1:
        heightstring = input('What is the height: ')
        height = validation(heightstring)
        if height < 1:
            print('Invalid, please use a positve number that is not 0')
            height = -1
    heights.append(height)

def list_avg(numlist):
    base = 0
    listlength = len(numlist)
    for item in numlist:
        base += item
    average = base / listlength
    return average

def view_list(lists, listspair):
    for list in lists:
        listsindex = lists.index(list)
        listpair = listspair[listsindex]
        print(f'{list} is {listpair}cm tall.')

def list_out(lists, listspair):
    test = input('Put a number to remove person from said value:')
    remove = validation(test) - 1
    

while finish == False:
    userintput = -1
    userinput = input('What do you want to view? \n0 to end|1 to add a person|2 to view average height|3 to view list')
    userintput = validation(userinput)
    if userintput == 0:
        finish = True
    elif userintput == 1:
        list_in()
    elif userintput == 2:
        print(f'The average height of everyone is {list_avg(heights)}.')
    elif userintput == 3:
        view_list(names, heights)
    else:
        print('Invalid number. Please use a different number.')
    
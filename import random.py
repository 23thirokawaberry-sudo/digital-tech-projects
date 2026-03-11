def dial(num):
    if num == 0:
        dial = 'crash'
    return dial
crash = False
while crash == False:
    page = dial(int(input("1 for math question")))
    if page > 9 or page < 0:
        crash = True
    elif page == 0:
        print(4)


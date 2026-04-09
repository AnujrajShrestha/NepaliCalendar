def mutification_table(num):
    for multiply in range(1,11,1):
        print(f'{num} X {multiply} = {num*multiply}'.center(20))

num=int(input("Enter the number "))
mutification_table(num)

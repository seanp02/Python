def display_multiplication_table(n):
    for j in range(1, 10):
        for i in range(n,6):
            print(f'{i} x {j} = {j*i:2d}', end="    ")
            if (i == 5):
                print()

    print()
    
    for j in range(1, 10):                
        for i in range(6, 10):
            print(f'{i} x {j} = {j*i:2d}', end="    ")
            if (i == 9):
                print()
                    
n=2
display_multiplication_table(n)

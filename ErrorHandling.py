#Handle error
extend_guess = []
guess = 'Shift'

g = extend_guess.extend(guess)

print(g)
try: 
    num1 = int(input('Enter the first number : '))
    print(type(num1))
    num2 = int(input('Enter the second number : '))
    print(type(num2))
    #num2 + num1
except (TypeError, ZeroDivisionError, ValueError) as err:
    print(f'The error is: {err}')
else:
    print('The operation is done')
finally:
    print('we are out of the program')
        


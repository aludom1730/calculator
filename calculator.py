def calculate(n1,n2,op):

    if op == '+':
        result = n1+n2
    elif op == '-':
        result = n1-n2
    elif op == '*':
        result = n1*n2
    elif op == '/':
        result = n1/n2
    
return result

number1 = float (input('Introduzca el primer numero: '))
op = input('Introduzca operador(+,-,*,/): ')
number2 = float (input('Introduzca el segundo numero: '))
print(number1,op,number2)
result=calculate(number1,number2,op)
print=('=',result)




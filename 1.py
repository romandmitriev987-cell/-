def do_math(math_expr):
    math_expr = math_expr.replace(' ', '')
    
    numbers = []
    operators = []
    
    i = 0
    current_num = ''
    
    while i < len(math_expr):
        char = math_expr[i]
        
        if char.isdigit() or char == '.':
            current_num += char
        else:
            if current_num:
                numbers.append(float(current_num))
                current_num = ''
            operators.append(char)
        
        i += 1
    
    if current_num:
        numbers.append(float(current_num))
    
    i = 0
    while i < len(operators):
        if operators[i] in ['*', '/']:
            if operators[i] == '*':
                result = numbers[i] * numbers[i+1]
            else:
                result = numbers[i] / numbers[i+1]
            
            numbers[i] = result
            numbers.pop(i+1)
            operators.pop(i)
        else:
            i += 1
    
    result = numbers[0]
    for i in range(len(operators)):
        if operators[i] == '+':
            result += numbers[i+1]
        elif operators[i] == '-':
            result -= numbers[i+1]
    
    print(result)
    return result
command = ''
print('help - помощь')
while command != 'exit':
    command = str(input('Пиши >'))
    if command == 'help':
        print('exit - Выход\nhelp - помощь\n2+2 - функция калькулятора\nДоступны: +-*/')
    else:
        do_math(command)
def name_bot():
    print('Python: Chose your bot\'s name')
    bot_name = input('You: ')
    print(f'Python: The name you chose was {bot_name}')
    return(bot_name)
    
def math_function(answer_name: str, symbol: int, function_name):
    global bot_name
    print(f'{bot_name}: Sure! Let\'s do some {function_name}!')
    try:
        print(f'{bot_name}: Please enter your first number')
        num1: float = float(input('First number: '))
        print(f'{bot_name}: Please enter your second number')
        num2: float = float(input('Second number: '))
        if symbol == '+':
            answer = num1 + num2
        elif symbol == '-':
            answer = num1 - num2
        elif symbol == '*':
            answer = num1 * num2
        elif symbol == '/':
            answer = num1 / num2
        print(f'{bot_name}: The {answer_name} is {answer}')
    except ValueError:
       print(f'{bot_name}: Oops that doesn\'t seem like a valid number.')

bot_name = name_bot()

print(f'{bot_name}: Hi I\'m {bot_name}. I can do simple math probems.')

while True:
    user_input: str = input('You: ').lower()
    if user_input in ['what can you do', 'what can do', 'what do']:
        print(f'{bot_name}: I can add, minus, times and divide two numbers.')
    elif user_input in ['hi', 'hello']:
        print(f'{bot_name}: Hi there! How can I help?')
    elif user_input in ['bye', 'cya', 'see you']:
        print(f'{bot_name}: Good bye! Have a good day!')
    elif user_input in ['thanks', 'thank you', 'thank']:
        print(f'{bot_name}: Your welcome')
    elif user_input in ['+', 'add']:
        math_function('sum', '+', 'addition')
    elif user_input in ['-', 'minus']:
        math_function('difference', '-', 'subtraction')
    elif user_input in ['*', 'times', 'mulitply']:
        math_function('product', '*', 'multiplication')
    elif user_input in ['/', 'divide']:
        math_function('quotient', '/', 'division')
    else:
        print(f'{bot_name}: I didn\'t understand that. Please try again.')

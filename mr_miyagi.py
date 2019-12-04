welcome_message = print('Hello I am Mr. Miyagi, you are free to ask me any questions')

question_asked = ''

while question_asked != 'sensei, i am at peace':

    question_asked = input('What questions do you have?  ')

    if '?' not in question_asked:
     print ('Please use a question mark to ask a question')
    elif 'sensei' not in question_asked:
     print('You are smart, but not wise - address me as Sensei please')
    elif 'block' in question_asked or 'blocking' in question_asked:
        print('Remeber, best block, not to be there..')
    else:
        print('do not lose focus. Wax on. Wax off.')

# While loops keep looping until the condition is met
# the conditions are checked until the while conditon is met

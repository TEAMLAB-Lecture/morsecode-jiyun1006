#!/usr/bin/env python
# coding: utf-8




# -*- coding: utf8 -*-


# Help Function - 수정하지 말 것
def get_morse_code_dict():
    morse_code = {
        "A": ".-", "N": "-.", "B": "-...", "O": "---", "C": "-.-.", "P": ".--.", "D": "-..", "Q": "--.-", "E": ".",
        "R": ".-.", "F": "..-.", "S": "...", "G": "--.", "T": "-", "H": "....", "U": "..-", "I": "..", "V": "...-",
        "K": "-.-", "X": "-..-", "J": ".---", "W": ".--", "L": ".-..", "Y": "-.--", "M": "--", "Z": "--.."
    }
    return morse_code




# Help Function - 수정하지 말 것
def get_help_message():
    message = "HELP - International Morse Code List\n"
    morse_code = get_morse_code_dict()
    counter = 0

    for key in sorted(morse_code):
        counter += 1
        message += "%s: %s\t" % (key, morse_code[key])
        if counter % 5 == 0:
            message += "\n"

    return message




def is_help_command(user_input):
    tmp = user_input.lower()
    return True if tmp == "h" or tmp == "help" else False



import re
def is_validated_english_sentence(user_input):
    tmp = re.sub('[!?.,]', '', user_input)
    if tmp == '':
        return False
    else:
        return ''.join(tmp.split()).isalpha()
    
    




def is_validated_morse_code(user_input):
    user_input = user_input.split()
    for codes in user_input:
        if codes in get_morse_code_dict().values():
            return True
        else:
            return False




def get_cleaned_english_sentence(raw_english_sentence):
    return re.sub('[.,!?]','',raw_english_sentence)




def decoding_character(morse_character):
    morse_code_dict = get_morse_code_dict()
    tmp = dict(map(reversed, morse_code_dict.items()))
    return tmp[morse_character]



def encoding_character(english_character):
    morse_code_dict = get_morse_code_dict()
    return morse_code_dict[english_character.upper()]




def decoding_sentence(morse_sentence):
    tmp = morse_sentence.split(' ')
    result = ''
    for code in tmp:
        if code == '':
            result = result + ' '
        else:
            result = result + decoding_character(code)
            
    return result.strip()




def encoding_sentence(english_sentence):
    tmp = ' '.join(get_cleaned_english_sentence(english_sentence.strip()).split())
    result = ''
    for a in tmp:
        if a == ' ':
            result = result + ' '
            continue
        result = result + encoding_character(a) + ' '
        
    return result



def main():
    print("Morse Code Program!!")
    # ===Modify codes below=============
    while 1:
        user_input = input("Input your message(H - Help, 0 - Exit): ")
        if user_input == '0':
            break
        if is_help_command(user_input):
            print(get_help_message())
        
        if is_validated_english_sentence(user_input):
            print(encoding_sentence(user_input))
            
        elif is_validated_morse_code(user_input):
            print(decoding_sentence(user_input))
        
        else:
            print("Wrong Input")
        

    # ==================================
    print("Good Bye")
    print("Morse Code Program Finished!!")

if __name__ == "__main__":
    main()


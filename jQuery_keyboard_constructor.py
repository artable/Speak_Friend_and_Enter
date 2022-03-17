# keyboard_string = "qwertyuiopasdfghjklzxcvbnm"



# for letter in keyboard_string :
#     print('    <button id=", letter,">', letter.toUpper() ,'</button>)')



l = '{'
r = '}'

# for letter in keyboard_string:
#     print(f'$("#{letter}").click(function(){l}\n    textBuffer += \'{letter.upper()}\';\n    pushToBuffer();\n{r});')





cirth_alphabet = [
"16A2", "16B1", "16B3", "16A8", "16BA", "16BB", 
"16E9", "16A0", "16E6", "16C1", "16AD", "16B4", 
"16C5", "16D2", "16C9", "16A3", "16B9", "16A9", 
"16CF", "16B2", "16DA", "16DF", "16DD", "16B7", 
"16C4", "16CB", "16E3", "16BF", "16DE", "16EF",
"16D0", "16C7", "16E7"]

# for letter in cirth_alphabet :
#     print('    <button id="', letter,'">', letter ,'</button>')
for letter in cirth_alphabet :
    print(f'    <button id="{letter}">&#x{letter}</button>')

# for letter in cirth_alphabet :
#     print(f'$("#{letter}").click(function(){l}\n    textBuffer += \'\\u{letter}\';\n    pushToBuffer();\n{r});')

# Does not include space and punctuation special chars
# print(cirth_alphabet)
# print(len(cirth_alphabet))
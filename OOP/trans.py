from translate import Translator

tranlator = Translator(to_lang='afr')

try:
    with open('stuff.txt','r') as file:
        text = file.read()
except FileNotFoundError as err:
    print("file not found")
tran = tranlator.translate(text)

try:
    with open('trans.txt','w') as file1:
        file1.write(tran)
except FileNotFoundError as err:
    print("file not found")


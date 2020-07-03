# this will only run in Machine.
from googletrans import Translator
import io

translator = Translator()


try:
    with io.open('./test.txt', mode='r') as my_file:
        text = (my_file.read())
        translation = translator.translate(text, dest='hi')
        with io.open('./translated.txt', mode='w', encoding="utf-8") as my_file2:
            my_file2.write(str(translation.text))

except FileNotFoundError as err:
    print('file does not exsit')

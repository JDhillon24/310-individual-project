import googletrans
from googletrans import Translator
import time




def translate():
    translator = Translator()
    key_list = list(googletrans.LANGUAGES.keys())
    val_list = list(googletrans.LANGUAGES.values())

    while True:
        time.sleep(1.2)
        lang1 = str(input("What language would you like to translate from?"))
        sourcelang = key_list[val_list.index(lang1.lower())]
        time.sleep(1.2)
        lang2 = str(input("What language would you like to translate to?"))
        destlang = key_list[val_list.index(lang2.lower())]
        time.sleep(1.2)
        text = str(input("What is the phrase/word you would like to translate?"))
        result = translator.translate(text, src=sourcelang, dest=destlang)
        time.sleep(1.2)
        print("Here is the translated text!")
        print("\n")
        time.sleep(1.2)
        print(lang1 + ":")
        print(text)
        print(lang2 + ":")
        print(result.text)
        print("\n")
        time.sleep(1.2)

        yesno = str(input("Would you like to translate anything else? (yes/no)"))

        if yesno == "yes":
            continue
        else:
            break







if __name__ == '__main__':
    translate()
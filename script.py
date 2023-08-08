from translate import Translator

text = "hello"
translator = Translator(to_lang="fr")


try:
    with open('./filetest.txt', mode='r') as file_test:
        text = file_test.read()
        translated = translator.translate(text)
        with open('./filetranlate.txt', mode='w') as my_file2:
            my_file2.write(translated)
except FileNotFoundError as err:
    print(err)

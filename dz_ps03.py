import requests
from bs4 import BeautifulSoup
from googletrans import Translator

def get_english_words():
    url = 'https://randomword.com/'
    try:
        response = requests.get(url)
        response.raise_for_status()  # Проверка на успешный запрос
        soup = BeautifulSoup(response.content, 'html.parser')
        english_word = soup.find("div", id="random_word").text.strip()
        word_definition = soup.find("div", id="random_word_definition").text.strip()
        return {
            "english_word": english_word,
            "word_definition": word_definition
        }
    except Exception as e:
        print(f"Произошла ошибка: {e}")
        return {
            "english_word": "",
            "word_definition": ""
        }

def translate_to_russian(text):
    translator = Translator()
    translated = translator.translate(text, src='en', dest='ru')
    return translated.text

def word_game():
    print("Добро пожаловать в игру!")
    while True:
        word_dict = get_english_words()
        if not word_dict:
            print("Не удалось получить слово. Попробуйте снова.")
            continue

        english_word = word_dict.get("english_word")
        english_definition = word_dict.get("word_definition")

        russian_word = translate_to_russian(english_word)
        russian_definition = translate_to_russian(english_definition)

        print(f'Значение слова - {russian_definition}')

        user = input('Что это за слово? ')
        if user.lower() == russian_word.lower():
            print('Ответ верный!')
        else:
            print(f'Не верно, было загадано слово {russian_word}')

        play_again = input('Хотите сыграть еще раз? (y/n) ')
        if play_again.lower() != 'y':
            print('Спасибо за игру!')
            break

word_game()
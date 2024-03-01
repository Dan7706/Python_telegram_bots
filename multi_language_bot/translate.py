translations = {
    "ru": {"Successful registration!": "Успешная регистрация!"}
    #YOU CAN ADD AS MANY LANGUAGES AS YOU WANT!
    }



def _(text, lang):
    global translations
    if lang == 'en':
        return text
    elif lang == "ru":
        try:
            return translations[lang][text]
        except:
            return text

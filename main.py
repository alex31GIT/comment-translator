import httpcore
from googletrans import Translator


def print_trans(text_, lang_="en", end="\n"):
    text_ = text_.encode('utf-8')
    translator_ = Translator()
    text_ = translator_.translate(text_.decode('utf-8'), dest=lang_).text
    del translator_
    print(text_, end=end)



languages = {"fr": "français",
             "en": "english",
             "es": "español",
             "de": "deutsch",
             "it": "italiano",
             "pt": "português",
             "ru": "русский",
             "ar": "العربية",
             "zh-cn": "中文 (简体)",
             "zh-tw": "中文 (繁體)",
             "ja": "日本語",
             "ko": "한국어",
             "pl": "polski",
             "tr": "türkçe",
             "vi": "tiếng việt",
             "th": "ภาษาไทย",
             "id": "bahasa indonesia",
             "hi": "हिन्दी",
             "ms": "bahasa melayu",
             "nl": "nederlands",
             "sv": "svenska",
             "da": "dansk",
             "fi": "suomi",
             "no": "norsk",
             "hu": "magyar",
             "cs": "čeština",
             "ro": "română",
             "uk": "українська",
             "el": "ελληνικά",
             "af": "afrikaans",
             "bg": "български",
             "hr": "hrvatski",
             "lt": "lietuvių",
             "sk": "slovenčina",
             "sl": "slovenščina",
             "et": "eesti",
             "lv": "latviešu",
             "fa": "فارسی",
             "he": "עברית",
             "ur": "اردو",
             "sw": "kiswahili",
             "tl": "filipino",
             "az": "azərbaycan",
             "ka": "ქართული",
             "hy": "հայերեն",
             "mk": "македонски",
             "sq": "shqiptar",
             "eu": "euskal",
             "is": "íslenska",
             "mt": "malti",
             "be": "беларускі",
             "ba": "башҡорт",
             "ky": "кыргыз",
             "tt": "татар",
             "tg": "тоҷик",
             "sr": "српски",
             "mn": "монгол",
             "kk": "қазақ",
             "uz": "o'zbek",
             "bs": "bosanski",
             "ga": "gaeilge",
             "cy": "cymraeg",
             "fy": "frysk"}

print("type a sentence in the language you want the commentaries to be translates: ", end="")

# get the language from the user
sentence = input().encode('utf-8')

# detect the language of the sentence
translator = Translator()
lang = translator.detect(sentence.decode('utf-8')).lang

print("Do you want to translate in, ", languages[lang], " ? (y/n)", sep="", end=" ")
ans = input()

if ans == "n" or ans == "N":
    test = True
    while test:
        print("type the language code you want the commentaries to be translates: ", end="")
        lang = input()
        if lang in languages:
            test = False
        else:
            print("this language code is not available")

print_trans("Entrez le signe de commentaire utilisé dans le fichier à traduire:", lang, " ")

com_sign = input()

print_trans("Entrez la chemin du fichier à traduire, converti en .txt:", lang, " ")
file_path = input()

file_to_translate = open(file_path, "r", encoding="utf-8")
new_file = open(file_path[:-4] + "_translated_" + lang + ".txt", "w+", encoding="utf-8")

lines = file_to_translate.readlines()
translated_lines = []
i = 0

run = True
while run:
    try:
        line = lines[i]
        print(str(i + 1) + "/" + str(len(lines)))
        if com_sign in line:
            i_start_to_translate = 0
            for i_char in range(len(line)):
                if line[i_char:i_char + len(com_sign)] == com_sign:
                    i_start_to_translate += len(com_sign)
                    break
                i_start_to_translate += 1
            translator = Translator()
            trans_sentence = translator.translate(line[i_start_to_translate:], dest=lang).text
            translated_lines.append(line[:i_start_to_translate] + " " + trans_sentence + "\n")
            new_file.write(translated_lines[-1])
        else:
            translated_lines.append(line)
            new_file.write(translated_lines[-1])

        i += 1

        if i >= len(lines):
            run = False
    except httpcore.ConnectTimeout:
        print("connect timeout, retrying")
    except httpcore.ReadTimeout:
        print("read timeout, retrying")

new_file.close()
file_to_translate.close()

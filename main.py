import local as lc
from textblob import TextBlob

text = input(lc.INPUT)

# Finding language of the text.
language_russian = False
lang_eng = True
for i in text:
    if 97 <= ord(i) <= 122 or 65 <= ord(i) <= 90:
        language_russian = True

    elif 1072 <= ord(i) <= 1103 or 1040 <= ord(i) <= 1071:
        lang_en = True


def count_syllables_count_rus():
    # Function counts quantity of syllables in the text for russian language.
    syllables_count = 0
    vowels_count = 'еыаоэяуиюУЕЫАОЭЯИЮ'

    for _ in text:
        if vowels_count.find(_) != -1:
            syllables_count += 1
    return syllables_count


def flash_index_ru():
    # Function counts FLASH_INDX index for russian language.
    vowels_count = 'еыаоэуяиюёУЕЫАОЭЯИЮЁ'
    syllables_count = 0
    sentence_count = 0
    for _ in text:
        if vowels_count.find(_) != -1:
            syllables_count += 1
        words = text.split(' ')
        words_count = len(words)
        if _ == '.' or _ == '!' or _ == '?':
            sentence_count += 1
    asl = words_count / sentence_count
    asw = syllables_count / words_count
    fre = 206.835 - (1.3 * asl) - (60.1 * asw)
    return fre


def words_count_universal():
    # Function counts number of words for any language.
    words = text.split(' ')
    words_count = len(words)
    return words_count


def sentence_count_universal():
    # Function counts number of sentences for any language.
    sentence_count = 0
    for _ in text:
        if _ == '.' or _ == '!' or _ == '?':
            sentence_count += 1
    return sentence_count
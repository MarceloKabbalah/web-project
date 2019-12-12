def text_truncate(text):
    return text[80:]

def text_upper(text):
    pass



text = "Texto da primeira linha, Texto da Segunda Linha"

def text_truncate(text):
    firstLine = text[0:23]
    secondLine = text[25:380]

    return firstLine + "\n" + secondLine
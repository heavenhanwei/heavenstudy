censor(text,word):
    if word in text:
        new_text = text.replace(word, "*" * len(word))
    return new_text

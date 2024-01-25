def word_counter(text):
    words = text.split(' ')
    return len(words)

sentence = 'Python to fantastyczny jezyk programowania tylko trzeba duzo motywacji i nauki'
print(word_counter(sentence))
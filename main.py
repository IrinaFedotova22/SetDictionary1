some_words = input('Please enter some comma-separated words: ')
some_words = some_words.split(',')
set_sw = set(some_words)
print('In your list {} words'.format(len(some_words)))
some_words2 = input('Please enter {} comma-separated words: '.format(len(some_words)))
some_words2 = some_words2.split(',')
set_sw2 = set(some_words2)
d = dict(zip(some_words, some_words2))
print(d)
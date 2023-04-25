import urllib.request
import random

url = 'https://www.gutenberg.org/files/84/84-0.txt'
filename = 'textfile.txt'
urllib.request.urlretrieve(url, filename)
bigram_dict = {}
with open(filename, 'r', encoding='utf-8') as file:
    words = file.read().lower().split()
    for i in range(len(words)-1):
        bigram = words[i] + ' ' + words[i+1]
        if bigram in bigram_dict:
            bigram_dict[bigram] += 1
        else:
            bigram_dict[bigram] = 1
my_dict_items = list(bigram_dict.items())
print("Most USed bigrams with count:")
for i in range(10):
    for j in range(0, len(my_dict_items)-i-1):
        if my_dict_items[j][1] > my_dict_items[j+1][1]:
            my_dict_items[j], my_dict_items[j+1] = my_dict_items[j+1], my_dict_items[j]
            sorted_flag = False
    print(my_dict_items[len(my_dict_items)-i-1])
prompt=['AI','DATA','POLICY']
for j in range(3):
    start_word=prompt[j]
    temp=start_word
    while len(temp.split()) < 100:
        next_word = ''
        next = [bigram.split()[1] for bigram in bigram_dict.keys() if bigram.startswith(start_word)]
        if next:
            next_word = random.choice(next)
        else:
            next_word = random.choice(list(bigram_dict.keys())).split()[1]
        start_word = next_word
        temp += ' ' + next_word
    print(temp + '\n')

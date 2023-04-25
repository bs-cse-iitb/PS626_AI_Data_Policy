
import urllib.request
import random

# download text file from internet
url = "https://www.gutenberg.org/files/2701/2701-0.txt"
urllib.request.urlretrieve(url, "file.txt")

# read text file
path = "file.txt"
dict1 = {}
with open(path) as file:
    list1 = file.read().lower().split()
    
#print(list1)
# store biagram in dictionary
dict1 = {}
for i in range(len(list1)-1):
    str1 = list1[i]+" "+list1[i+1]
    if str1 in dict1:
        dict1[str1]+=1
    else:
        dict1[str1]=1
#print(dict1)
# sorted_dict = dict(sorted(dict1.items(), key=lambda x: x[1], reverse=True))
# print('#########\n', sorted_dict)
# count = 0
# for i in sorted_dict:
#     if count<10:
#         print(i,"-",sorted_dict[i])
#     else:
#         break;

dict2= list(dict1.items())
print("Top 10 pairs\n")
print("S.No.     Key         Value")
for i in range(10):
    for j in range(0, len(dict2)-i-1):
        if dict2[j][1] > dict2[j+1][1]:
            dict2[j], dict2[j+1] = dict2[j+1], dict2[j]
    print(i+1,"      ",dict2[len(dict1)-i-1][0],"----------",dict2[len(dict1)-i-1][1])

print("\n")


print("Generate 100 words for each of text\n")

prompt=['CSE','AI','Data Science']

for j in range(len(prompt)):
    start_word=prompt[j]
    temp=start_word
    while len(temp.split()) < 100:
        next_word = ''
        next = [bigram.split()[1] for bigram in dict1.keys() if bigram.startswith(start_word)]
        if next:
            next_word = random.choice(next)
        else:
            next_word = random.choice(list(dict1.keys())).split()[1]
        start_word = next_word
        temp += ' ' + next_word
    print(temp + '\n')

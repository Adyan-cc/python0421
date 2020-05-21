'''
使用random产生1万个大写字母，并统计每个字母出现的次数
'''

import random
import collections

capital_letter = ['A', 'B', 'C', 'D', 'E', 'F', 'G',
                  'H', 'I', 'J', 'K', 'L', 'M', 'N',
                  'O', 'P', 'Q', 'R', 'S', 'T',
                  'U', 'V', 'W', 'X', 'Y', 'Z']

my_letter_list =[]
my_letter_list_counter = collections.Counter()
for i in range(1000000):
    my_letter_list.append(random.choice(capital_letter))
for letter in my_letter_list:
    my_letter_list_counter[letter] += 1

print(my_letter_list)
print(my_letter_list_counter)

for i in my_letter_list_counter:
    print('字母 '+ i+ ' 有 '+ str(my_letter_list_counter.get(i))+ '个')
    #print(i)
    #print(my_letter_list_counter.get(i))

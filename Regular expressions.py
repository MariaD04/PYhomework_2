from pprint import pprint
import re
import csv

with open("phonebook_raw.csv", encoding='utf-8') as f:
  rows = csv.reader(f, delimiter=",")
  contacts_list = list(rows)
#pprint(contacts_list)

def sort_by_alphabet(inputstr):
  for i in inputstr:
    return i[0][0]
  
def find_dublicate(result_list):
  for i in range(len(result_list) - 1):
      if (result_list[i][0] == result_list[i+1][0]) and (result_list[i][1] == result_list[i+1][1]):
          for index in range(len(result_list[i]) - 1):
            if result_list[i][index] == '':
                result_list[i].insert(index, result_list[i+1][index])

def delete_dublicate(result_list):
    for i in reversed(range(len(result_list))):
      if result_list[i][0] == result_list[i-1][0]:
          result_list.remove(result_list[i])
    return result_list

pattern_phone = r"(\+7|8)[\s(]*(\d{3})[-)\s]*(\d{3})[\s-]?(\d{2})[\s-]?(\d{2})(\s)?\(?(\w{3}.)?\s?(\d{4})?[)]?"
replace_phone = r"+7(\2)\3-\4-\5\6\7\8"

first_part = []
second_part = []
for contact in contacts_list:
  contact_list = ' '.join(contact[:3]).split()
  first_part.append(contact_list)
  new_contact = contact[3:]
  result_phone = re.sub(pattern_phone, replace_phone, new_contact[2])
  new_contact[2] = result_phone
  second_part.append(new_contact)

result_list = [x + y for x, y in zip(first_part, second_part)]
result_list = sorted(result_list, key=sort_by_alphabet)

find_dublicate(result_list)
delete_dublicate(result_list)

with open("phonebook.csv", "w", encoding='utf-8') as f:
  datawriter = csv.writer(f, delimiter=',')
  datawriter.writerows(result_list)




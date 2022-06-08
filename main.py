from pprint import pprint
import csv

with open("phonebook_raw.csv",'r', encoding='UTF-8') as f:
  rows = csv.reader(f, delimiter=",")
  contacts_list = list(rows)
# pprint(contacts_list)

def fio_order(contacts_list):
  for items in contacts_list:
    a = items[0].split(' ')
    d = items[1].split(' ')
    if len(a) > 2 or len(d) < 1:
      items[0] = a[0]
      items[1] = a[1]
      items[2] = a[2]
    elif len(a) > 1 and len(a) < 3:
      items[0] = a[0]
      items[1] = a[1]
    elif len(a) == 1 and len(d) > 1:
      items[1] = d[0]
      items[2] = d[1]
  # print('------------')
  # pprint(contacts_list)
  return contacts_list


# def replay(contacts_list):
#   fio_list = fio_order(contacts_list)
#   # pprint(fio_list)
#   dict_ = {}
#   fio = ''
#   for i,row in enumerate(fio_list):
#     fio = (row[0] + ' ' + row[1])
#     if fio not in dict_:
#       dict_[fio] = 1
#     else:
#       dict_[fio] += 1
#   list_replay = []
#   for k, v in dict_.items():
#     if v > 1:
#       f = k.split(' ')
#       list_replay.append(f[0])
#   print(list_replay)

# replay(contacts_list)
info = fio_order(contacts_list)
list_new = []
list_fio = []
for items in info:
  if [items[0], items[1]] not in list_fio:
    list_fio.append([items[0], items[1]])
    list_new.append([items[0], items[1], items[2], items[3], items[4], items[5], items[6]])
  else:
    [items[0], items[1]]
print('-------------')
pprint(list_new)


# print('_____________')
# pprint(contacts_list)
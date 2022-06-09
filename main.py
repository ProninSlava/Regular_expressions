from pprint import pprint
import csv
from func.fio import sequence, diblicate
import re

with open("files/phonebook_raw.csv", 'r', encoding='UTF-8') as f:
  rows = csv.reader(f, delimiter=",")
  contacts_list = list(rows)

info = sequence(contacts_list)
info_list = diblicate(info)

for items in info_list[1:]:
  pattern = r'(\+7|8)(\s*|\()(\(|s*)(495)(-|\)|s*)\s*(\d{3})(-|s*)(\d{2})(-|s*)(\d{2})(\s*|)(\(|\s*)(\доб.|)\s*(\d+|)(\)|)'
  res = re.sub(pattern, r"+7(\4)\6-\8-\10 \13 \14", items[5])
  items[5] = res

with open("phonebook.csv", "w") as f:
  datawriter = csv.writer(f, delimiter=',')
  datawriter.writerows(info_list)

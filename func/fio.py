def sequence(contacts_list):
  for items in contacts_list:
    a = items[0].split(' ')
    d = items[1].split(' ')
    c = items[2].split(' ')
    if len(a) == 3 or len(d) < 1:
      items[0] = a[0]
      items[1] = a[1]
      items[2] = a[2]
    elif len(d) == 3:
      items[0] = d[0]
      items[1] = d[1]
      items[2] = d[2]
    elif len(c) == 3:
      items[0] = c[0]
      items[1] = c[1]
      items[2] = c[2]
    elif len(a) == 2:
      items[0] = a[0]
      items[1] = a[1]
    elif len(a) == 1 and len(d) == 2:
      items[1] = d[0]
      items[2] = d[1]

  return contacts_list

def diblicate(contacts_list):
  dict_fio = {}
  for items in contacts_list:
    fio = items[0] + ' ' + items[1]
    if fio not in dict_fio:
      dict_fio[fio] = [items[2], items[3], items[4], items[5], items[6]]
    else:
      dict_fio[fio].append([items[2], items[3], items[4], items[5], items[6]])

  for i in dict_fio:
    if len(dict_fio[i])>5:
      if dict_fio[i][0] != dict_fio[i][5][0]:
        dict_fio[i][0] += dict_fio[i][5][0]

      if dict_fio[i][1] != dict_fio[i][5][1]:
        dict_fio[i][1] += dict_fio[i][5][1]

      if dict_fio[i][2] != dict_fio[i][5][2]:
        dict_fio[i][2] += dict_fio[i][5][2]

      if dict_fio[i][3] != dict_fio[i][5][3]:
        dict_fio[i][3] += dict_fio[i][5][3]

      if dict_fio[i][4] != dict_fio[i][5][4]:
        dict_fio[i][4] += dict_fio[i][5][4]

      del dict_fio[i][-1]

  list_new_ = []
  for key, values in dict_fio.items():

    a = key.split(' ')
    list_new_.append([a[0], a[1], values[0], values[1], values[2], values[3], values[4]])

  return list_new_





from pprint import pprint
import csv
import re

phone_puttern = r'(\+7|8)*[\s\(]*(\d{3})[\)\s-]*(\d{3})[-]*(\d{2})[-]*(\d{2})[\s\(]*(доб\.)*[\s]*(\d+)*[\)]*'
phone_sub = r'+7(\2)-\3-\4-\5 \6\7'

with open("phonebook_raw.csv", encoding="utf-8") as f:
    rows = csv.reader(f, delimiter=",")
    contacts_list = list(rows)


    def alteration(contacts_list: list):
        finall_list = list()
        for i in contacts_list:
            full_name = ' '.join(i[:3]).split(' ')
            ordered_list = [full_name[0], full_name[1], full_name[2], i[3], i[4],
                            re.sub(phone_puttern, phone_sub, i[5]),
                            i[6]]
            finall_list.append(ordered_list)
        return consolidation(finall_list)


    def consolidation(name: list):
        for n in name:
            first_name = n[0]
            last_name = n[1]
            for new_name in name:
                new_first_name = new_name[0]
                new_last_name = new_name[1]
                if first_name == new_first_name and last_name == new_last_name:
                    if n[2] == "": n[2] = new_name[2]
                    if n[3] == "": n[3] = new_name[3]
                    if n[4] == "": n[4] = new_name[4]
                    if n[5] == "": n[5] = new_name[5]
                    if n[6] == "": n[6] = new_name[6]
        end_list = list()
        for a in name:
            if a not in end_list:
                end_list.append(a)
        return end_list


    with open("phonebook.csv", "w", encoding="utf-8") as f:
        datawriter = csv.writer(f, delimiter=',')
        datawriter.writerows(alteration(contacts_list))



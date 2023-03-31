ids ={'user1': [213, 213, 213, 15, 213],
      'user2': [54, 54, 119, 119, 119],
      'user3': [213, 98, 98, 35]}
ids_list = sum(dict.values(ids), [])
ids_list1 = list(dict.fromkeys(ids_list))
print(ids_list1)

# Павел
# new_list=[]
# for k,v in ids.items():
#     for B in v:
#         if B not in new_list:
#            new_list.append(B)
#
# print(new_list)
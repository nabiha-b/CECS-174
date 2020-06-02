# Nabiha Bashir
# This program tells you how many hot dogs + buns are needed based on how many people attend a cookout.

num_dogs = 10
num_buns = 8

attending = int(input("Enter the number of people attending the cookout: "))
hotdogs_given = int(input("Enter the number of hot dogs each person will be given: "))

total_hotdogs = attending * hotdogs_given
pack_hotdogs = total_hotdogs / num_dogs
remain_hotdogs = total_hotdogs % num_dogs
pack_buns = total_hotdogs / num_buns
remain_buns = total_hotdogs % num_buns

if remain_hotdogs:
    pack_hotdogs += 1
    remain_hotdogs = num_dogs - remain_hotdogs

if remain_buns:
    pack_buns += 1
    remain_buns = num_buns - remain_buns

print('Minimum number of packages of hot dogs needed: ', pack_hotdogs)
print('Minimum number of packages of hot dog buns needed: ', pack_buns)
print('Number of hot dogs left over: ', remain_hotdogs)
print('Number of hot dog buns left over: ', remain_buns)

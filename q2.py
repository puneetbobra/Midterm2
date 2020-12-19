#generate 30 random letters in the range of A to Z (inclusive)
import random

#create a list of all letters
letters_list = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']

#initialise empty list to store sorted letters
sorted_letters = []

#generate random letters from letters_list
for i in letters_list:
    rand_letters = random.randint(0,25)
    sorted_letters.append(letters_list[rand_letters])


sorted_letters = sorted(sorted_letters)

#print the random letters in ascending order
for i in sorted_letters:
    print(f'{i}', end =' ')
print('')
#initialize empty list to store distinct letters
rem_duplicates = []

#remove duplicates from the list and print in descending order
for i in sorted_letters:
    if i not in rem_duplicates:
        rem_duplicates.append(i)

#reverse the rem_duplicate list so that we can print in descending order
rem_duplicates.reverse()

for i in rem_duplicates:
    print(i, end = ' ')

#End
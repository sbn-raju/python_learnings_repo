# #Write the program to count numbr of studen t with the "A" grade in the followinf list
grades = ["C","D","A","A","B","B","A"]
print(grades.count('A'))
# #Write the program to sort the above grades list
grades.sort()
print(grades)
# Write the program to enter names of the their 3 favorite movies  and store them in a list
movies_list = []
name_one = input("Enter First movie name:")
movies_list.append(name_one)
name_two = input("Enter Second movie name:")
movies_list.append(name_two)
name_three = input("Enter thirs movie name:")
movies_list.append(name_three)
print(movies_list)
# Write the program to check if the a list contains palindrome of elements.(Hint:use copy() method)
list = [1,2,1,3]
empty_list = []
empty_list = list.copy()
list.reverse()
print(list)
print(empty_list)
if empty_list == list:
    print("It is a Palindrom String")
else:
    print("It is not a Palindrom String")


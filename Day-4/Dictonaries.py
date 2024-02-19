#Dictonaires are used to store data values in key:value pairs.
#They are unordered and mutable, don't allows the dupicate keys
#Example-1
# dict = {
#     "name":"raju",
#     "age":20
# }
# print(dict)
#Like a nested loops and nested if else statements you have nested Dict
#Example-2
# dict ={
#    "name":"Raju",
#    "age":20,
#    "Subjects":{
#        "first_sem":"Maths",
#        "second_sem":"Java"
#    }
# }
# print(dict)
# Methods of Dict
dict = {
    "name":"raju",
    "age":20
}

print(dict.keys())
# dict.key() shows only the keys of the dict
dict = {
    "name":"raju",
    "age":20
}
print(dict.values())
# dict.values() shows only the values of the dict
dict = {
    "name":"raju",
    "age":20
}
print(dict.items())
# dic.items() returns all the key and values pairs
dict = {
    "name":"raju",
    "age":20
}
print(dict.get("name"))
# dict.get(key) returns the value of the key

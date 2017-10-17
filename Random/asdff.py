
'''
pet_owner = {
	"Banne":1,
	"Arck":"Dragon",
	"Alice":{1 , "2"}
}

for value in set(pet_owner.values()):
	print(value)
#rule of set can't print a different type of data

for value in pet_owner.values():
	print(value)
pet_owner["Alice"].append(3)
print(pet_owner["Alice"])

for people in sorted(pet_owner.keys()):
	print(people , " owns a " , pet_owner[people])
print ("---------------------------------------")
for key , value in pet_owner.items():
	print(key , " owns a " , value)

arr = {"dict":{"animal" : "dog"}}

var_1 = 3
var_2 = "burger"
print((var_1) , var_2*3)

'''

one = "Cat"
two = "eat"
print("My {0} loves to {1}. I love my {0}".format(one, two))

abc = "Soup"
soup = "ABC"
print("I love {0} {1}\nI love {1} {0}".format(soup,abc))
print('I\'d like a pudding')
print("William Shakespeare once said, \"To Be or Not To Be.\"")
print('Delete dis\b')
print('Delete dis\b\b\b')
print("Hahaha\vBanget")

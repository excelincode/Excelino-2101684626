pet_owner = {
	"Banne":1,
	"Arck":"Dragon",
	"Alice":{1 , "2"}
}
'''
for value in set(pet_owner.values()):
	print(value)
#rule of set can't print a different type of data
'''
for value in pet_owner.values():
	print(value)
pet_owner["Alice"].append(3)
print(pet_owner["Alice"])

'''
for people in sorted(pet_owner.keys()):
	print(people , " owns a " , pet_owner[people])
print ("---------------------------------------")
for key , value in pet_owner.items():
	print(key , " owns a " , value)

arr = {"dict":{"animal" : "dog"}}
'''

#Counts the total frequency of every characters in any text
import pprint #pretty printer module
s=str(input("ENTER THE STRING: "))
count={}
for character in s:
	count.setdefault(character,0)
	count[character]+=1

#pprint.pprint(count)
output=pprint.pformat (count)
print(output)

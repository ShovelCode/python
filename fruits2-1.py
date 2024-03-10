
print("Little Red Hood is off to pick fruits.")
grove= [1, 1, 2, 3, 4, 4, 2] #Grove, a list which represents a line of trees and a type of fruits
#grove = [1, 1, 1, 1, 1, 1, 1, 2]
def answer(grove):
	print(grove)
	B = set(grove) 
	print(B)
	D = dict.fromkeys(B, 0) #Does this work?
	print(D)
	
	for t in grove:
		x = D.get(t)
		x = x + 1
		del D[t]
		D[t] = x
	
	print(D)
	#make list of values of D
	
	counts = list(D.values())
	print(counts)
	counts.sort()
	print(counts)
	if len(counts) > 1:
		print(counts[0] + counts[1])
	else:
		print(counts[0])

answer(grove)

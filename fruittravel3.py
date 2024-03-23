print("Little Red Hood is off to pick fruits.")
grove = [1, 1, 2, 3, 4, 4, 2] #Grove, a list which represents a line of trees and a type of fruits

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
	
	largest = counts[0]
	second_largest = counts[0]
	for i in counts:
		if counts[i] > largest:
			second_largest = largest
			largest = counts[i]
		elif counts[i] < largest and counts[i] > second_largest:
			second_largest = counts[i]
			
	print(largest + second_largest)
	return largest + second_largest 
	
answer(grove)

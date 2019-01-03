#It works for sample test but rejected at attempt.
def find_it(seq):
	equal = 0
	temp = 0
	for i in range(len(seq)):
	    temp = seq[i]
	    counter = 1
	    j = i
	    for j in range(i, len(seq) - 1):
	        i += 1
	        if temp == seq[i]:
	            counter += 1
	        if counter % 2 == 1 and counter > 1:
	            equal = seq[i]
	return equal
	
	
def main():
    equal = find_it([20,1,-1,2,-2,3,3,5,5,1,2,4,20,4,-1,-2,5])
    print(equal)
	
if __name__ == '__main__':
    main()

# Net best practice.

def find_it(seq):
    for i in seq:
        if seq.count(i)%2!=0:
            return i
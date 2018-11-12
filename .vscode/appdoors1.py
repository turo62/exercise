doors = [False] * 100

for i in range(1,101): #menjen végig a listán
    for j in range(i-1,100,i): #menjen végig a listán "i"-esével
        doors[j] = not doors[j]


for k in range(0, len(doors)):
    if doors[k] == True:
        door_n = str(k+1) #eltolja 0. sorszámot 1- re
        print((door_n) + "." + " door is open!")

	
	
	

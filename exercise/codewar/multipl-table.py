def multiplication_table(row,col):
    return [[x*y for y in range(1,col+1)] for x in range(1,row+1)]
    
def main():
    table = multiplication_table(3, 3)
    print(table)
	
if __name__ == '__main__':
    main()    

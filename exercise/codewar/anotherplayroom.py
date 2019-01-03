

index_a = 0
index_b = 0
arr = ("1231231223123131_myFile.tar.gz2")
ip_address = ""
index_a = arr.index('_')
index_b = arr.index('.')
print(index_a)
print(index_b)
ip_address = arr[(index_a + 1):(index_b + 4)]
print(ip_address)
    

#def main():
 #   ip_address = extract_file_name("1This_is_an_otherExample.mpg.OTHEREXTENSIONadasdassdassds34")
  #  print(ip_address)
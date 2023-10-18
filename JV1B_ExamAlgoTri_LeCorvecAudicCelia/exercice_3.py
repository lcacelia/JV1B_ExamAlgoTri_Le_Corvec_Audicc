myTable = [23,65,58,548,268,248]
for i in range(1,len(myTable)):
      indice = myTable[i]
      maxi = i-1
      while maxi >=0 and indice>myTable[maxi]:
            myTable[maxi+1] = myTable[maxi]
            maxi-=1
      myTable[maxi+1]=indice
      
print(myTable)
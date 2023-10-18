myTable = [23,65,58,548,268,248]
print("myTable: ",myTable)
maxi= myTable[0]

for i in range(len(myTable)):
        if (myTable[i] > maxi):
            maxi = myTable[i]   
            indice_maxi = i
            myTable.insert(len(myTable),maxi)
            myTable.pop(indice_maxi)
            
print("resultat exo2 :",myTable)

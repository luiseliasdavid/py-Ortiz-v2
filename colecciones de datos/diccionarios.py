# Variables del ejercicio (no modifiques esta línea)
animales = {"caballo":"", "vaca":""}

# completa el ejercicio
add= {"perro":"dog","gato":"cat","rana":"frog"}

for c,v in add.items():
    animales[c]=v

animales["caballo"]="horse"
animales["vaca"]="cow"

del animales["rana"]
del animales["vaca"]

print(animales)

c = {1,2,2,3,3,3}
 
print( list(c) )
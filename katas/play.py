
#lista = ["a","b","c"]
#lista = [2,4,6,7,8]
a ="aretheyhere" 
b= "yestheyarehere"

def longest(a1, a2):
    return "".join(sorted(list(set(a1+a2))))
    

#print()
print( longest(a,b) )
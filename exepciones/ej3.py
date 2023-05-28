my_dic = {1:2,2:3,3:4}

try:
    my_dic[4]
except KeyError :
    print(KeyError.__name__)
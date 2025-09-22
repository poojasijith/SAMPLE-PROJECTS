my_list=[1,2,3,4,5]
new_list=[]
for i in range(len(my_list)):
    new_list.insert(i,my_list[-1])
    my_list.pop(-1)
print(new_list)
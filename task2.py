
a = ([
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]
        ])
#for i in a.index(0):
 #       print(a[i])
#print(a.index(a[0]))



def print_list(x):
        index_i=[]
        index_j=[]
        for i in range(0, len(x)):
                  index_i.append(i)
                   #print(x[i])
                  #print(x.index(x[i]))
                  for j in range(0, len(x[i])):
                          index_j.append(j)
                          #print(index_j)
                          #print(x[j])
                          #print(x.index(x[j]))
        print(index_j)
        return x


print_list(a)




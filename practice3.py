import pandas as pd

# groupby function 
d1 = pd.DataFrame({'name':['a','b','a','a','a','c','c','b','c','d','b','d'],
                    'marks':[30,40,34,67,89,95,58,23,45,19,45,68],
                    'percentage':[10,20,30,40,50,60,70,80,90,100,110,120]})

new_d1= d1.groupby('name')  # it will seperate a ,b , c, d

for x in new_d1: # to see groups 
    print(x)
    print()


print(new_d1.get_group('a'))  # to get particular group
print()
print(new_d1.max())  #it will maximum value of all a,b,c,d groups
print (new_d1.min()) #it will minimum value of all a,b,c,d groups
print()
print(new_d1.mean())  #it will mean value of all a,b,c,d groups
print()
print(list(new_d1)) 

print()

# join function : combine two dataframes don't need comman columns 

var1 = pd.DataFrame({ 'one':[1,2,3,4,], 'four': ['a','b','c','d']})
var2 = pd.DataFrame({'one':[10,20], 'four':['a','b']})

print(var1.join(var2, how='outer', lsuffix='_100', rsuffix='_200'))  # suffix will get applied to that column which have similar name in both dataframes

print()

# append function  if column has common name then it show data in one single column of that name 

col1=  pd.DataFrame ({ 'first_col':['gauri','sakshi','priya','nikita','ria'], 'sec_col': ['pune','banglore','satara','mumbai','solapur']})
col2 = pd.DataFrame ({'third_col':['QA','production','QC','regulatory_affairs','research'], 'fourth_col':[30000,12000,78000,45000,31000]})

print(col1._append(col2, ignore_index= True))



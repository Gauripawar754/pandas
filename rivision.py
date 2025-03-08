import pandas as pd

a = pd.Series([1,2,3,4,5], dtype=float,name='number')
print(a)
print(type(a))

f = pd.Series([10,20,30,40,50], name='friends')
print(f)
print(a + f)

tu = pd.Series([10,20,30,40,50,60])
tu1 = pd.Series([25,35,45])
print(tu+tu1)


dic=  {'first_name':'gauri','last_name':'pawar'}
print(pd.Series(dic))


dic2  = {'a':[1,22,3,4,5], 'b':[10,20,30,40,50]}
l = pd.DataFrame(dic2, index=[1,2,3,4,5])
print(l)

print(dic2['b'][4])
print(dic2['b'][2])
l['c'] = l['a'] + l['b']
l['d'] = l['a'] >= l['b']
print(l)


li = (1,0,3,4)
f1 = pd.Series(li,index=['a','b','c','d'],name='values',dtype=bool)
print(f1)
print(f1['d'])


print(l['c'][3])


s = {'address':['pune','solapur','mumbai'],
     'name':['gauri','sakshi','priya']}

g=  pd.DataFrame(s)
print(g)
print()
g.insert(2,'surname',['pawar','singh','kapoor'])
print(g)
print()
g.insert(3,'new_name',g['name'][:2])
print(g)

s2 =pd.DataFrame ({'address':['pune','solapur','mumbai'],
     'name':['gauri','sakshi','priya']})

print(s2.pop('name')[2])
print(s2.pop('address')[0])


v = pd.DataFrame({'a':[11,22,33,44,55],
                  'b':[10,20,30,40,50]})

v.to_csv('file_new.csv',index=[1,2,3,4,5],header=['columnA','columnB'])
print(v)

read_file = pd.read_csv("C:\\Users\\gauri\\OneDrive\\Desktop\\Pandas\\employees.csv")
print(read_file)
print()

read_file = pd.read_csv("C:\\Users\\gauri\\OneDrive\\Desktop\\Pandas\\employees.csv", nrows=10)
print(read_file)
print()

read_file = pd.read_csv("C:\\Users\\gauri\\OneDrive\\Desktop\\Pandas\\employees.csv", usecols=[0,2])
print(read_file)
print()

read_file = pd.read_csv("C:\\Users\\gauri\\OneDrive\\Desktop\\Pandas\\employees.csv",index_col=[0])
print(read_file)
print()

read_file = pd.read_csv("C:\\Users\\gauri\\OneDrive\\Desktop\\Pandas\\employees.csv",names=['new_name','new_age','new_dept','new_salary'])
print(read_file)
print()

read_file = pd.read_csv("C:\\Users\\gauri\\OneDrive\\Desktop\\Pandas\\employees.csv",header=4)
print(read_file)
print()

read_file = pd.read_csv("C:\\Users\\gauri\\OneDrive\\Desktop\\Pandas\\employees.csv",skiprows=5)
print(read_file)
print()

read_file = pd.read_csv("C:\\Users\\gauri\\OneDrive\\Desktop\\Pandas\\employees.csv", dtype={'Salary':'float'})
print(read_file)
print()

read_file = pd.read_csv("C:\\Users\\gauri\\OneDrive\\Desktop\\Pandas\\employees.csv", dtype={'Age':'float'})
print(read_file)


s =pd.DataFrame( {'address':['pune','solapur','mumbai'],
     'name':['gauri','sakshi','priya']})
s.to_csv('name.csv', header=['new_address','new_name'])
print(s)

j = pd.read_csv("C:\\Users\\gauri\\OneDrive\\Desktop\\Pandas\\name.csv")
print(j)



new_data= pd.DataFrame({'Id':[101,102,103,104,105,106,107],
                        'name':['nick','ria','priti','olivia','king','niti','gracy'],
                        'salary':[1000,289,490,576,760,890,546]})

print(new_data)
print(new_data.index)
print(new_data.columns)
print(new_data.describe())
print(new_data.head()) 
print(new_data.tail())
print(new_data[3:5])
print(new_data.index.array)
print(new_data.to_numpy())

print(new_data.sort_index(axis=1,ascending=False))
print()
print(new_data)
print()

print(new_data.loc[[1,2,3], ['name']])
print(new_data.loc[1,'name'])
print(new_data.loc[6,'salary'])


print(new_data.loc[ : , ['Id','name'] ])
print(new_data.loc[[2,4,6], : ])

print(new_data.drop([1,4],axis=0))
print(new_data.drop('salary', axis=1))
print()


file = pd.read_csv("C:\\Users\\gauri\\OneDrive\\Desktop\\Pandas\\employees1.csv")
print(file)
print()
print(file.dropna(axis=0))
print(file.dropna(axis=1))
print()
print(file.dropna(subset=['Age','Salary']))
print()
print(file.dropna(thresh=4))
print()
print(file.dropna(axis=0, how= 'any'))
print()
print(file.dropna(axis=0, how='all'))
print()
print(file.dropna(axis=1, how='all'))

print()

file = pd.read_csv("C:\\Users\\gauri\\OneDrive\\Desktop\\Pandas\\employees1.csv")
print(file)
print()
print(file.fillna('a'))
print()
print(file.fillna({'Name':'gauri pawar', 'Age':20.00, 'Department':'Data science' , 'Salary': 10000.0}))
print()
print(file.bfill())
print(file.ffill())
print()


file = pd.read_csv("C:\\Users\\gauri\\OneDrive\\Desktop\\Pandas\\employees1.csv")
print(file)

print(file.replace(to_replace= ['Alice Johnson', 'Bob Smith'], value=['Gauri Pawar', 'nick']))

print(file.replace({'Finance':'Data Science', 'IT':'Data Analysis'}))
# print(file.replace([101,106,104], 'a'))


print(file.replace(to_replace= [101,107,105], value='b'))
print()

dat1 = pd.DataFrame({'id':[1,2,3,4,5],'salary':[23000,4900,8900,786,456]})

dat2 = pd.DataFrame({'id':[1,2,3,8,9],'birthdate':[2001,2003,1998,900,789]})

print(pd.merge(dat1,dat2,  on='id', how= 'outer'))
print(pd.merge(dat1,dat2, on ='id', how= 'left'))
print()

dat1 = pd.DataFrame({'emp_id':[1,2,3,4,5],'salary':[23000,4900,8900,786,456]})

dat2 = pd.DataFrame({'id':[1,2,3,8,9],'birthdate':[2001,2003,1998,900,789]})

print(pd.merge(dat1,dat2, left_on='emp_id', right_on='id', how= 'outer' , indicator=True))
print()

print(pd.merge(dat1, dat2, left_index=True, right_index=True, suffixes=[]))

print()

dat = pd.DataFrame({'id':[1,2,3,4,5],'salary':[23000,4900,8900,786,456]})

dat3 = pd.DataFrame({'id':[1,2,3,8,9],'birthdate':[2001,2003,1998,900,789]})

print(pd.concat([dat,dat3], axis=1, keys=['column1','column2']))

print()
print(dat.join(dat3, lsuffix=100, rsuffix=200))
print()



d1 = pd.DataFrame({'name':['a','b','a','a','a','c','c','b','c','d','b','d'],
                    'marks':[30,40,34,67,89,95,58,23,45,19,45,68],
                    'percentage':[10,20,30,40,50,60,70,80,90,100,110,120]})


d = d1.groupby('name')
for i in d:
  print(i)
  print()

print(d.get_group('b'))

print(d.max())
print(d.min())
print(d.mean())
import pandas as pd
# different data structures

# 1. Series -  one diamensional series with labaled name
x = [1,2,3,0,5]
new_x = pd.Series(x, index=['a','b','c',1,True], dtype='bool', name="numbers")
print(new_x)
print(type(new_x))
print(new_x['b'])

s = pd.Series('gauri', index=[1,2,3,4,5],name="Friends")
z = pd.Series('Sakshi', index=[1,2,3])
print(s + z)

dic = {
    'first_name': 'gauri',
    'last_name': 'pawar'
}

c =  pd.Series(dic)
print(c)

tu = (10,20,30,40,50,60)
tu1 = (25,35,45)
o =pd.Series(tu, index=[1,2,3,4,5,6])
f =pd.Series(tu1, index=[1,2,3])
print(o + f)
print(tu + tu1)



# 2. data frames - two diamensional data structure with columns, much like tables
u = { 'strings':['a','b','c','db','e'], 'number':[1,2,3,4,5]}
lr= pd.DataFrame(u, columns=['strings','number'],index=[1,2,3,4,5])
print(lr)
print('4th row',lr ['strings'][4])

tr= {'s': pd.Series([1,2,3,4,5]), 'g': pd.Series([1,2,3,4,5])}
g =pd.DataFrame(tr)
print(g)



# arithmatic operations in pandas
a = pd.DataFrame({'first':[10,20,30,40,50], 'second':[100,200,300,400,500]})
a['third'] =  a['first'] + a['second']
print(a)
print()

a['third'] =  a['first'] <= a['second']
print(a)
print()

a['third'] =  a['first'] * a['second']
print(a)
print()



# insert function :   var.insert(column position number, column name, value)
h = pd.DataFrame({'address':['pune','solapur','mumbai','hydrabad','goa'],
                  'name':['gauri', 'sakshi','divya','sia','ria'],
                  'grade':['a','b','c','d','e']  })
print(h)
del(h['address']) 


h.insert (0,'result',['pass','pass','fail','pass','distinction']) #(column position number, column name, value)
print(h)

print()
h.insert(3,'new_name',h['name'])
print(h)

h['year'] = h['grade'] [:3] #slicing only particular rows
print(h)



# delete function
y = pd.DataFrame({'friends':['gauri', 'sakshi','divya','sia','ria'], 'chr':['a','b','c','d','e']})
u= y.pop('friends')
print(y)
print(u)

print()





# creating csv file from dataframes
products = pd.DataFrame({ 'pro_name':['tablet','capsule','suspension','elixers','lozenges'],
             'dosage_forms':['solid','liquid','gaseous','inhalers','powder inhaler']  ,
             'mg':[30,556,857,3200,847] 
    })
products.to_csv("tech_mills.csv",index=False,header=[1,2,3])





# reading csv files  
new = pd.read_csv("C:\\Users\\gauri\\OneDrive\\Desktop\\Pandas\\tech_mills.csv")
print(new)

# to retrive particular rows
new1= pd.read_csv("C:\\Users\\gauri\\OneDrive\\Desktop\\Pandas\\tech_mills.csv", nrows=2)
print(new1)

# to know retrive column
new3= pd.read_csv("C:\\Users\\gauri\\OneDrive\\Desktop\\Pandas\\tech_mills.csv", usecols=[0,1])
print(new3)

print()
# to skip rows
new4 = pd.read_csv("C:\\Users\\gauri\\OneDrive\\Desktop\\Pandas\\tech_mills.csv", skiprows=[0])
print(new4)

# indexcol (to set another column as index column)
new5 = pd.read_csv("C:\\Users\\gauri\\OneDrive\\Desktop\\Pandas\\tech_mills.csv", index_col='1')
print(new5)

# header (to keep any row as header)
new6 = pd.read_csv("C:\\Users\\gauri\\OneDrive\\Desktop\\Pandas\\tech_mills.csv", header = 2 )  # row number
print(new6)
print()

# names (to give new name or heading  to column)
new7 = pd.read_csv("C:\\Users\\gauri\\OneDrive\\Desktop\\Pandas\\tech_mills.csv",names = ['col1','col2','col3'] ) 
print(new7)
print()

# dtype (changing datatype of column number values)
new8 = pd.read_csv("C:\\Users\\gauri\\OneDrive\\Desktop\\Pandas\\tech_mills.csv", dtype={'3': 'float'}) #{column name: datatype}
print(new8)
print()




# pandas different function

data = pd.DataFrame({'name':['tata','mahindra','skoda','suzuki','honda','yamaha','kia','hyundai'],
                     'price':[2000,64638,7497,3293,739,6482,6735,536],
                     'volume':[34.754, 75883.75, +64738.87, 65.09, 45328, 546.9, 53.46, 3637]})

print(data)
print(data.index) #return range of index
print(data.columns) #return column name
print(data.describe()) #only describe numerical values like min,max,mean count etc.
print(data.head()) #returns starting data from 0-4 deafault value  or can specify between this num
print()
print(data.tail()) # returns ending 5 data or can specify between this num

print(data[0:6])  #returns rows 0 - 5

print(data.index.array) #returns array of index

print(data.to_numpy()) #converts dataframe table into numpy array
print()
print(data.sort_index(axis=0,ascending=False))  # axis = 0 means rows and axis = 1 means column , low to high
print()
print(data.loc[[1,3,2],['name','price']]) #need to mention particular row and column number
print()
print(data.loc[ : ,['name','price']]) # all rows and particaulr column
print()
print(data.loc[[5,3,2], : ]) #particular rows and all columns
print()
print(data.loc[[1,6],['volume']])
print()
print(data.iloc[1,0]) #returns single item [row no. , col no.]
print()

print(data.drop(0,axis=0)) #it will drop (row 0 , axis=0 means row)
print(data.drop('name',axis=1)) #it will drop (column 'name', axis=1 means column)


f= pd.Series([10,20,30])
print(f)
k = pd.Series([1,2,3])
print(f+k)

new_df = {
    'name':['tata','mahindra','skoda','suzuki','honda','yamaha','kia','hyundai'],
        'price':[2000,64638,7497,3293,739,6482,6735,536],
        'volume':[34.754, 75883.75, +64738.87, 65.09, 45328, 546.9, 53.46, 3637]
}

gg = pd.DataFrame(new_df)
print(gg)
gg.insert(2,'number',[1,2,3,4,5,6,7,8])
print(gg)
print(gg['name'][4])

print(gg['price']+gg['volume'])
print(gg.pop('name'))

d = gg.to_csv("new_file.csv")

m = pd.read_csv("C:\\Users\\gauri\\OneDrive\\Desktop\\Pandas\\new_file.csv",dtype={'price':float})
print(m)

jet = pd.DataFrame({
    'ch':['a','b','j','g','d','u','p','t','r','m'],
    'num':[1,2,3,4,5,6,7,8,9,10]
})

print(jet.index)
print(jet.columns)
print(jet.head())
print(jet.head(2))
print(jet.tail())
print(jet.describe())
print(jet.index.array)
print(jet[5:8])
print(jet.to_numpy())
# print(jet.loc[[2,5,7],['ch']])
print(jet.loc[[2,4],['num']])
print(jet.loc[:,['num']])
print(jet.iloc[3,0])






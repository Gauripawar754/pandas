import pandas as pd

# handling missing values in dataframes


# dropna function : it drops particaular rows or columns if any Nan values appers in it.

read_file =pd.read_csv("C:\\Users\\gauri\\OneDrive\\Desktop\\Pandas\\student_data.csv",names=['col1','col2','col3','col4','col5'])
print(read_file)
print()
print(read_file.dropna(axis=0)) #drops rows if any NaN appears in it
print(read_file.dropna(axis=1)) #drops columns if any NaN appears in it
print(read_file.dropna(subset=['col5'])) #drops rows only if NaN appears in column 'col5'
print(read_file.dropna(thresh=2)) # keep those rows which contain at least 2 non-NaN value
print(read_file.dropna(axis=0,how='any')) # drops rows/columns if any NaN value appear 
print(read_file.dropna(axis=0,how='all')) # drops rows/columns if all NaN value appear 
print()


# fillna function: replace NaN value with new word

# emplyee_data = pd.DataFrame({
#     'emp_id':[101,102,103,104,105,106,107,108,109,110],
#     'emp_name':['gauri','ria','nikita','pranjali','sakshi','peter','priyanka','nick','lily','becky'],
#     'address':['pune','solapur','mumbai','banglore','goa','delhi','chennai','hydrabad','surat','gujrat'],
#     'age':[22,30,18,39,45,36,31,26,22,30]})

# emp_file= emplyee_data.to_csv("employee_data.csv")

open_file = pd.read_csv("C:\\Users\\gauri\\OneDrive\\Desktop\\Pandas\\employee_data.csv")
print(open_file)

print()
print(open_file.fillna('python')) 
print()
print(open_file.fillna({'emp_id':'a','empe_nam':'b','address':'c','age':'d'}))  
print()
print(open_file.bfill()) #along with aixs (default value 1) it will repalce NaN values with backward values 
print(open_file.ffill()) #along with aixs (default value 1) it will repalce NaN values with forward values 





# repalce : it repalce old with new word
file_new =pd.read_csv("C:\\Users\\gauri\\OneDrive\\Desktop\\Pandas\\new_file.csv")
print(file_new)
print()
print(file_new.replace(to_replace=1, value='a')) # replace 1 with 'a'
print(file_new.replace({1:100,2:200})) # 1 with 100,2 with 200
print(file_new.replace([3,4,5,6],'gauri')) # 3,4,5,6 with gauri
print()



# Joining in Pandas

# 1. merge function in pandas need one common column between dataframes

data1 = pd.DataFrame({'id':[1,2,6,4,5],'salary':[23000,4900,8900,786,456]})

data2 = pd.DataFrame({'emp_id':[1,2,3,8,9],'birthyear':[2001,2003,1998,900,789]})

c = pd.merge(data1,data2, left_on='id', right_on='emp_id', how="outer") #for different column names,  outer : merge dataframes and return all data fills missing values with NaN
print(c)

print()


dat1 = pd.DataFrame({'id':[1,2,3,4,5],'salary':[23000,4900,8900,786,456]})
dat2 = pd.DataFrame({'id':[1,2,3,8,9],'birthdate':[2001,2003,1998,900,789]})
d = pd.merge(dat1,dat2, on='id', how="inner") #inner:only keeps matching rows
print(d) 
print()
e = pd.merge(dat1,dat2, on='id', how="right") #right: keep all rows from right dataframe and matching rows from left dataframe
print(e) 
print()
g = pd.merge(dat1,dat2, on='id', how="left") #left: keep all rows from left dataframe and matching rows from right dataframe
print(g) 

h = pd.merge(dat1,dat2,on='id', how='outer',indicator=True) # indicator will show merge status of dataframes
print(h)

print()
t = pd.merge(dat1,dat2, left_index=True,right_index=True, suffixes=("emp","stu")) # it shows all complete dataframes together suffix:(for dat1, for dat2)
print(t)

print()



# 2. concat : it joins two dataframes together along with specified axis
s1 = pd.Series([1,2,3,4,5])
s2 = pd.Series([100,200,300,400,500])

s = pd.concat([s1,s2],axis=1 ,keys=['column1','column2'])
print(s)
print()

conc1 = pd.DataFrame({'id':[1,2,3,4,5],'salary':[23000,4900,8900,786,456]})
conc2 = pd.DataFrame({'emp_id':[1,2,3],'birthyear':[2001,2003,1998]})

concate_data = pd.concat([conc1,conc2], axis=1, keys=['data1','data2'])
print(concate_data)



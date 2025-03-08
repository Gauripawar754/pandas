import pandas as pd
# Melt function : it horizontal data frame into vertical

dat = pd.DataFrame({'id':[1,2,3,4,5],'salary':[23000,4900,8900,786,456], 'age':[10,20,30,40,50]})
print(pd.melt(dat,id_vars='id' , var_name='python',value_name= 'number'))

print()

print(pd.melt(dat, id_vars='salary', var_name='criteria',value_name='num'))
print()


# Pivot 
dat = pd.DataFrame({'id':[1,2,3,4,5],'salary':[23000,4900,8900,786,456],'name':['gauri','sakshi','priya','nick','ria'], 'age':[10,20,30,40,50]})
print(pd.pivot(dat, index='id', columns='age' )) 
print()

print(pd.pivot_table(dat, index='name', columns='salary',   
                      aggfunc='count' ))        #only pivot table have aggfunc.


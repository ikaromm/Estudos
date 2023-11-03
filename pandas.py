
#Create a DataFrame from List
#  column_names = ['student_id', 'age']
#  result = pd.DataFrame(student_data, columns=column_names)

##########################################
#Size of a data fram
# list(players.shape)

########################################
#display the first hree rows
# print(players.head(3))
# print(players[0:3])])

#######################################
#select data
# students[students.student_id == 101][["name", "age"]]

#######################################
#new column
# employees['bonus']=  employees['salary'] * 2
     #return employees

#######################################
#drop duplicate rows
# customers.drop_duplicates(subset=['email'])

#######################################
#drop missing data
# students.dropna(subset = ["name"])
#######################################

# change data type
# a = {'grade':int}
    #df = df.astype(a)
# df['grade'] = df[['grade']].astype(int) # changing datatype to int.

#########################################
# fill missing data

# products["quantity"] = products["quantity"].fillna(0)
# a = {"quantity": 0}
#    df = df.fillna(a)

#########################################
#concatenar 
# pd.concat([df1,df2])

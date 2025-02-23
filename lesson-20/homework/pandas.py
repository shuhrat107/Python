#1.0
import pandas as pd

data = [['NY', 'blue', 'Steak', 30, 165, 4.6],
        ['TX', 'green', 'Lamb', 2, 70, 8.3],
        ['FL', 'red', 'Mango', 12, 120, 9.0],
        ['AL', 'white', 'Apple', 4, 80, 3.3],
        ['AK', 'gray', 'Cheese', 32, 180, 1.8],
        ['TX', 'black', 'Melon', 33, 172, 9.5],
        ['TX', 'red', 'Beans', 69, 150, 2.2]]

columns = ['state', 'color', 'food', 'age', 'height', 'score']
index = ['Jane', 'Niko', 'Aaron', 'Penelope', 'Dean', 'Christina', 'Cornelia']

df = pd.DataFrame(data, columns=columns, index=index)
df

df[['color','age','height']]
df.loc[['Aaron','Dean']]

#1.3
df1=df.loc[['Aaron','Dean']]
df1[['color','age','height']]

#2.1
cdf = pd.read_csv('stackoverflow_qa.csv')
flt1=cdf['creationdate'] < '2014-00-00 00:00:00' 
flt2 = cdf['quest_name']
finlflt= flt1&flt2
columns = ['quest_name','creationdate']
cdf.loc[finlflt,columns]

#2.2
filt = cdf['score'] > 50
columns= ['score','quest_name']
cdf.loc[filt,columns]

#2.3
filt = cdf['score'].between(50,100)
columns= ['score','quest_name']
cdf.loc[filt,columns]

#2.4
filt1 = cdf['ans_name'].isin(['Scott Boston'])
columns= ['ans_name','quest_name']
cdf.loc[filt1,columns]

#2.5
cdf = pd.read_csv('stackoverflow_qa.csv')
filt1 = ~cdf['ans_name'].isin(['Scott Boston'])
columns= ['ans_name','quest_name']
cdf.loc[filt1,columns]

#2.6
cdf = pd.read_csv('stackoverflow_qa.csv')
flt1=cdf['creationdate'].between('2014-03-00 00:00:00','2014-09-30 23:59:59') 
flt2 = cdf['ans_name'].isin(['unutbu'])
flt3 = cdf['score'] < 5
finlflt= flt2&flt1&flt3
columns = ['quest_name','creationdate','score','ans_name']
cdf.loc[finlflt,columns]

#2.7
cdf = pd.read_csv('stackoverflow_qa.csv')
flt1 = cdf['score'].between(5,10)
flt2 = cdf['viewcount']> 10000
finlflt = flt1 | flt2
columns=['score','viewcount','quest_name','ans_name']
cdf.loc[finlflt,columns]


#3.1
tdf= pd.read_csv('titanic.csv')
flt1= tdf['Sex'] == 'female'
flt2 = tdf['Age'].between(20,30)
flt3 = tdf['Pclass'] == 1
finflt= flt1&flt2&flt3
columns = ['Name','Age','Sex','Pclass']
newtdf = tdf.loc[finflt,columns]
newtdf

#3.2
tdf= pd.read_csv('titanic.csv')
flt=tdf['Fare']> 100
tdf.loc[flt]

#3.3
tdf= pd.read_csv('titanic.csv')
flt1= tdf['Survived'] == 0
flt2 = tdf['SibSp'] == 0
flt3 = tdf['Parch'] == 0
finflt= flt1&flt2&flt3
columns = ['Name','Age','Sex','Survived']
tdf.loc[finflt,columns]

#3.4
tdf= pd.read_csv('titanic.csv')
flt=tdf['Fare']> 50
flt2 = tdf['Embarked'] == 'C'
finflt = flt & flt2
tdf.loc[finflt]

#3.5
tdf= pd.read_csv('titanic.csv')

flt2 = tdf['SibSp'] >0
flt3 = tdf['Parch'] > 0
finflt= flt2&flt3
columns = ['Name','Age','Sex','SibSp','Parch']
tdf.loc[finflt,columns]


#3.6
tdf= pd.read_csv('titanic.csv')
flt1= tdf['Survived'] == 1
flt2 = tdf['Age'] <= 15
finflt= flt2&flt3
columns = ['Name','Age','Sex','Survived']
tdf.loc[finflt,columns]


#3.7
tdf= pd.read_csv('titanic.csv')
flt=tdf['Fare']> 200
columns=['Fare','Cabin']
tdf.loc[flt,columns]


#3.8
tdf= pd.read_csv('titanic.csv')
id = (tdf['PassengerId'] % 2 == 0 ) == False
id1 = tdf['PassengerId'] == 1
columns= ['PassengerId','Name']
finflt = id | id1
new1_tdf= tdf.loc[finflt,columns]
new1_tdf



#3.9
tdf= pd.read_csv('titanic.csv')
flt4 = tdf.groupby(['Ticket'])['PassengerId'].count() 


#3.1.1

tdf = pd.read_csv('titanic.csv')
ticket_counts = tdf.groupby('Ticket')['PassengerId'].count()
unique_tickets = ticket_counts[ticket_counts == 1].index
unique_ticket_passengers = tdf[tdf['Ticket'].isin(unique_tickets)]
print(unique_ticket_passengers)


#3.1.2
tdf = pd.read_csv('titanic.csv')
tdf[tdf['Name'].str.contains('Miss', case=False, na=False)]

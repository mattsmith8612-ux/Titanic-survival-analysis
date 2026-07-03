import pandas as pd
import matplotlib.pyplot as plt


df = pd.read_csv(
    "https://raw.githubusercontent.com/mwaskom/seaborn-data/master/titanic.csv"
)

#print(df.head())
#print(df.shape)
#print(df.dtypes)
#print(df.info())
#print(df.isna().sum())

category_list = [
    'survived',
    'pclass',
    'sex',
    'embarked',
    'class',
    'who',
    'deck',
    'embark_town',
    'alive',
    'alone',
]

#for item in category_list:
    #print(df[item].value_counts())

counts = df['pclass'].value_counts()

counts = df['pclass'].value_counts()

#plt.figure()
#plt.bar(counts.index, counts.values)
#plt.title('Passenger Class Frequencies')
#plt.xlabel('Passenger Class')
#plt.ylabel('Number of Passengers')
#plt.show()

#plt.figure()
#plt.barh(counts.index, counts.values)
#plt.title('Passenger Class Frequencies')
#plt.ylabel('Passenger Class')
#plt.xlabel('Number of Passengers')
#plt.show()

#for item in category_list[1:]:
    #print(df.groupby(item)['survived'].mean())

#print(df.groupby(['pclass', 'sex'])['survived'].mean())


rates = df.groupby(['pclass', 'sex'])['survived'].mean()

bar_labels = []
for item in rates.index:
    string_label = str(item[0]) + ' - ' + str(item[1].title())
    bar_labels.append(string_label)

plt.figure()
plt.barh(bar_labels, rates.values)
plt.title('Mean Passenger Survival Rate For Each Gender by Class')
plt.xlabel('Mean Passenger Survival Rate')
plt.ylabel('Passenger Gender and Class')
plt.show()

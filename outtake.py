import pandas as pd
import numpy as np
import math 
import matplotlib.pyplot as plt
import statsmodels.api as sm

outtakes = pd.read_csv("Austin_Animal_Center_Outcomes__10_01_2013_to_05_05_2025_.csv")
# print(outtakes['Outcome Type'])
# print('length of data wo filtering:')
print(len(outtakes.index))

nonBlankOutComes = outtakes[outtakes['Outcome Type'].str.len() > 0]
allAdoptedSpecies = outtakes[(outtakes['Outcome Type'] == 'Adoption')]
# print('filtered out blank outcome types.. new length:')
print(len(nonBlankOutComes.index))

# print('all possible outcome types:')
# print(nonBlankOutComes['Outcome Type'].unique())

#'Transfer',
#'Euthanasia'
#'Adoption'
#'Return to Owner'
#'Died'
#'Missing'
#'Disposal'
#'Relocate'
#'Rto-Adopt'
#'Stolen'
#'Lost'

# totalAdopts = len(nonBlankOutComes[nonBlankOutComes['Outcome Type'] == 'Adoption']) + len(nonBlankOutComes[nonBlankOutComes['Outcome Type'] == 'Rto-Adopt'])
# print(totalAdopts / len(nonBlankOutComes.index))
# nearly 49% adoption rate(?) in austin animal center 
# 49% for our limited view of texas?

# see biggest outcome
#print(nonBlankOutComes['Outcome Type'].value_counts())
# df = pd.DataFrame(nonBlankOutComes['Outcome Type'].value_counts().head(5))
# df.plot.bar(legend=None,title='Most Common Outcomes',color='orange')
# plt.show()

# # save counts + labels to seperate lists 
# values = labelVals.to_list()
# labels = nonBlankOutComes['Outcome Type'].unique()
# print(labelVals.to_list())

# # plug into pie chart
# fig, ax = plt.subplots()
# ax.pie(values, labels=labels)
# plt.show()

# top dog breeds
# allAdoptedDogs = outtakes[(outtakes['Outcome Type'] == 'Adoption')  & (outtakes['Animal Type'] == 'Dog')]
# labelVals = allAdoptedDogs['Breed'].value_counts(sort=False)
# values = labelVals.to_list()
# labels = allAdoptedDogs['Breed'].unique()
# print(allAdoptedDogs['Breed'].value_counts())
# df = pd.DataFrame({'label': labels, 'value': values})
# df = df.sort_values('value', ascending=False).head(5)
# plt.title("Top 5 Dog Breeds in Austin by Adoptions")
# plt.xlabel("Number of adopts")
# plt.ylabel("Dog breeds")
# plt.barh(df['label'], df['value'])
# plt.gca().invert_yaxis()
# plt.show()

# top adopted species
# df = pd.DataFrame({'Animal Type': ['Dog','Cat','Other'], 'count':[47475,35784,1002+323+17]})
# plot = df.plot.pie(y="count", figsize=(11, 6),labels=df['Animal Type'].values,legend=None,autopct='%1.1f%%',title='Most Adopted Animals By Breed',colors=['#999999', '#e41a1c', '#dede00'])
# plt.show()

# get specific about the 'other' section (adoptions)
# otherBits = allAdoptedSpecies[(allAdoptedSpecies['Outcome Type'] == 'Adoption') & (allAdoptedSpecies['Animal Type'] == 'Other')]
# df =pd.DataFrame(otherBits['Breed'].value_counts().head(5))
# df.plot.barh(stacked=True)
# plt.show()
#print(otherBits['Breed'].value_counts(sort=False))

# top age - dont know how reliable this is. this is only the AGE of the animal, not its length of stay in the center.
# labelVals = allAdoptedSpecies['Age upon Outcome'].value_counts()
# print(labelVals)


# top sex
# labelVals = allAdoptedSpecies['Sex upon Outcome'].value_counts()
# print(labelVals)

# talk abt the bats bro
# allBats = pd.DataFrame(nonBlankOutComes[nonBlankOutComes['Breed'] == 'Bat Mix'])
# print(allBats['Outcome Type'].value_counts())
# print(allBats['Color'].value_counts())

# get specific about the 'other' section (just in general)
otherBits = nonBlankOutComes[nonBlankOutComes['Animal Type'] == 'Other']
df =pd.DataFrame(otherBits['Breed'].value_counts().head(5))
df = df.iloc[::-1]
df_counts = df.reset_index()
df_counts.columns = ['label', 'value']

fig, axes = plt.subplots()
axes.hlines(df_counts['label'], xmin=0,
            xmax=df_counts['value'], colors='brown')

axes.plot(df_counts['value'],df_counts['label'], "o",color='brown')
axes.set_xlim(0)

plt.xlabel('Count')
plt.ylabel('Type of Animal')
plt.title('Other Animals Coming Out of Austin Animal Center')
plt.yticks(df_counts['label'])
plt.show()
print(len(otherBits.index))
print(otherBits['Breed'].value_counts())
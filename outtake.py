import pandas as pd
import numpy as np
import math 
import seaborn as sns
import matplotlib.pyplot as plt
import statsmodels.api as sm

outtakes = pd.read_csv("Austin_Animal_Center_Outcomes__10_01_2013_to_05_05_2025_.csv")
# print(outtakes['Outcome Type'])
# print('length of data wo filtering:')
# print(len(outtakes.index))

nonBlankOutComes = outtakes[outtakes['Outcome Type'].str.len() > 0]
# print('filtered out blank outcome types.. new length:')
# print(len(nonBlankOutComes.index))

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

# get count of each outcome type (sort false to preserve order)
labelVals = nonBlankOutComes['Outcome Type'].value_counts(sort=False)

# save counts + labels to seperate lists 
values = labelVals.to_list()
labels = nonBlankOutComes['Outcome Type'].unique()
print(labelVals.to_list())

# plug into pie chart
fig, ax = plt.subplots()
ax.pie(values, labels=labels)
plt.show()

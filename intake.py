import pandas as pd
import numpy as np
import math 
import seaborn as sns
import matplotlib.pyplot as plt
#import statsmodels.api as sm

intakes = pd.read_csv("Austin_Animal_Center_Intakes__10_01_2013_to_05_05_2025_.csv")
outtakes = pd.read_csv("Austin_Animal_Center_Outcomes__10_01_2013_to_05_05_2025_.csv")

# #Line Graph- Intakes Over Years Vs Outtakes
# #convert DateTime column from string to actual datetime
# intakes['DateTime'] = pd.to_datetime(intakes['DateTime'])
# #extracting month and year from DateTime column
# intakes['YearMonth'] = intakes['DateTime'].dt.to_period('M')
# #count intakes per month
# monthly_counts = intakes.groupby('YearMonth').size()
# monthly_counts.plot()

# outtakes['DateTime'] = pd.to_datetime(outtakes['DateTime'], format='ISO8601',utc=True)
# #extracting month and year from DateTime column
# outtakes['YearMonth'] = outtakes['DateTime'].dt.to_period('M')
# #count intakes per month
# outmonthly_counts = outtakes.groupby('YearMonth').size()
# outmonthly_counts.plot(color='purple')
# plt.show() 

# #Pie Chart of Animal Types
# intakes['Animal Type'].value_counts().plot(kind='pie')
# plt.show()

# # Horizontal Bar Chart of Intake Type
# intakes['Intake Condition'].value_counts().plot(kind='barh', figsize=(8, 6))
# plt.xlabel('Count')
# plt.title('Intake Condition')
# plt.tight_layout()
# plt.show()
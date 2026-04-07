import pandas as pd
import numpy as np
import math 
import seaborn as sns
import matplotlib.pyplot as plt
import statsmodels.api as sm

outtakes = pd.read_csv("Austin_Animal_Center_Outcomes__10_01_2013_to_05_05_2025_.csv")
print(outtakes['Outcome Type'])
print(len(outtakes.index))

nonBlankOutComes = outtakes[outtakes['Outcome Type'].str.len() > 0]
print(len(nonBlankOutComes.index))

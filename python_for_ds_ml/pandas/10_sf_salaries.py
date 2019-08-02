#%%
import pandas as pd

#%%
sal = pd.read_csv('Salaries.csv')

#%%
sal.head()

#%%
sal.info()

#%%
sal['BasePay'].mean()

#%%
sal['OvertimePay'].max()

#%%
sal[sal['EmployeeName'] == 'JOSEPH DRISCOLL']['JobTitle']

#%%
sal[sal['EmployeeName'] == 'JOSEPH DRISCOLL']['TotalPayBenefits']

#%%
sal[sal['TotalPayBenefits'] == sal['TotalPayBenefits'].max()]['EmployeeName']

#%%
sal[sal['TotalPayBenefits'] == sal['TotalPayBenefits'].min()]

#%%
sal.groupby('Year').mean()['BasePay']

#%%
sal.nunique()['JobTitle']

#%%
sal['JobTitle'].value_counts().head(5)

#%%
sum(sal[sal['Year']==2013]['JobTitle'].value_counts() == 1)

#%%
def chief_string(title):
  return True if 'chief' in title.lower() else False

sum(sal['JobTitle'].apply(lambda x: chief_string(x)))

#%%
sal['title_len'] = sal['JobTitle'].apply(len)

#%%
sal[['title_len', 'TotalPayBenefits']].corr()

#%%

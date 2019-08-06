#%%
import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
sns.set_style('whitegrid')
%matplotlib inline

#%%
df = pd.read_csv('911.csv')

#%%
df.head()

#%%
df.info()

#%%
df['zip'].value_counts().head(5)

#%%
df['twp'].value_counts().head(5)

#%%
df['title'].nunique()

#%%
df['Reason'] = df['title'].apply(lambda x: x.split(':')[0])

#%%
df.tail()

#%%
df['Reason'].value_counts()

#%%
sns.countplot(x='Reason', data=df, palette='viridis')

#%%
type(df['timeStamp'].iloc[0])

#%%
df['timeStamp'] = pd.to_datetime(df['timeStamp'])

#%%
df['Hour'] = df['timeStamp'].apply(lambda time: time.hour)
df['Month'] = df['timeStamp'].apply(lambda time: time.month)
df['Day of Week'] = df['timeStamp'].apply(lambda time: time.dayofweek)

#%%
df.tail()

#%%
dmap = {0:'Mon',1:'Tue',2:'Wed',3:'Thu',4:'Fri',5:'Sat',6:'Sun'}
df['Day of Week'] = df['Day of Week'].apply(lambda x: dmap[x])
# df['Day of Week'] = df['Day of Week'].map(dmap)

#%%
df.tail()

#%%
sns.countplot(x='Day of Week', data=df, hue='Reason',palette='viridis')
plt.legend(bbox_to_anchor=(1.05, 1), loc=2, borderaxespad=0.)
#%%
sns.countplot(x='Month', data=df, hue='Reason', palette='viridis')
plt.legend(bbox_to_anchor=(1.05, 1), loc=2, borderaxespad=0.)

#%%
by_mounth = df.groupby('Month').count()

#%%
by_mounth.tail()

#%%
by_mounth['twp'].plot()

#%%
sns.lmplot(x='Month', y='twp', data=by_mounth.reset_index())

#%%
df['Date'] = df['timeStamp'].apply(lambda time: time.date())

#%%
by_date = df.groupby('Date').count()

#%%
by_date['twp'].plot()
plt.tight_layout()

#%%
by_date['twp'].plot(hue='Reason')

#%%
df[df['Reason']=='Traffic'].groupby('Date').count()['twp'].plot()
plt.tight_layout()
#%%
df[df['Reason']=='Fire'].groupby('Date').count()['twp'].plot()
plt.tight_layout()

#%%
df[df['Reason']=='EMS'].groupby('Date').count()['twp'].plot()
plt.tight_layout()

#%%
day_hour = df.groupby(by=['Day of Week','Hour']).count()['Reason'].unstack()

#%%
plt.figure(figsize=(12,6))
sns.heatmap(day_hour, cmap='viridis')

#%%
sns.clustermap(day_hour, cmap='viridis')

#%%
day_month = df.groupby(by=['Day of Week', 'Month']).count()['Reason'].unstack()

#%%
plt.figure(figsize=(12, 6))
sns.heatmap(day_month, cmap='viridis')

#%%
sns.clustermap(day_month, cmap='viridis')

#%%

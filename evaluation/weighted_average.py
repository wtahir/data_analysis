#%%
import pandas as pd
# %%
df = pd.read_csv('/home/waqas/Downloads/information_extraction/per_field.tsv', sep='\t')
df.drop(df[df.F1 < 3].index, inplace=True)
# %%
s = df['F1'] * df['weights']
#%%
actual_f1 = sum(df['F1'])/len(df['F1'])
# %%
weighted_f1 = sum(s)/sum(df['weights'])
# %%
df
# %%

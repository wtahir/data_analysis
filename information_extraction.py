#%%
import pandas as pd
df = pd.read_csv('/home/waqas/Downloads/information_extraction/extraction_stats.tsv', sep='\t')
df.info()

#%%
df['distance'].value_counts()

# %%
min_dist = 4
df['match'] = df['distance'] <= min_dist

# %%
sum(df['match']) / len(df['match'])

# %%
df['tn'] = (df['groundtruth'] == '<empty/>') & (df['prediction'] == '<empty/>')
df['fp'] = (df['prediction'] != '<empty/>') & (df['distance'] > min_dist)
df['fn'] = (df['groundtruth'] != '<empty/>') & (df['distance'] > min_dist)
df['tp'] = (df['groundtruth'] != '<empty/>') & (df['prediction'] != '<empty/>') & (df['distance'] <= min_dist)
df.describe(include='all').T

# %%
counts = {}
counts['tp'] = sum(df['tp'])
counts['tn'] = sum(df['tn'])
counts['fp'] = sum(df['fp'])
counts['fn'] = sum(df['fn'])
counts

# %%
metrics = {}
metrics['rec'] = counts['tp'] /  (counts['tp'] + counts['fn'])
metrics['pre'] = counts['tp'] /  (counts['tp'] + counts['fp'])
metrics['f1'] = (2 * metrics['rec'] * metrics['pre']) / (metrics['rec'] + metrics['pre'] )
metrics
# %%
len(df[df['distance'] == 4])
# %%

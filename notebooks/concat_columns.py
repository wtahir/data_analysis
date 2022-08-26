#%%
import pandas as pd

df = pd.read_csv("/home/waqas/aza_cq.csv")
df
# %%
df
# %%
df["link_"] = df['link'] + df['doc_id']
df
# %%
df.to_csv('/home/waqas/aza_cq.csv')
# %%

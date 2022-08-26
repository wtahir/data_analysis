#%%
from heapq import merge
import pandas as pd
import json
from functools import reduce
import numpy as np
# %%
# --- BASE
df_base_csv = pd.read_csv('/home/waqas/Downloads/selection_documents/base/per_doc.tsv', sep='\t')
df_base_csv.drop(df_base_csv[df_base_csv['f1'] == '-'].index, inplace=True)

with open('/home/waqas/repos/platform-client/base.json','r') as f:
    data = json.loads(f.read())

df_base_js = pd.json_normalize(data, record_path =['items'])

merged_base = pd.merge(df_base_csv, df_base_js, on="document_id",how="inner")
merged_base['f1'] = merged_base['f1'].astype(float)
merged_base = merged_base[merged_base['f1'] > 0]
merged_base


# %%
# --- CAUSE
df_cause_csv = pd.read_csv('/home/waqas/Downloads/selection_documents/cause/pr.tab', sep='\t')
df_cause_csv.drop(df_cause_csv[df_cause_csv['f1'] == '-'].index, inplace=True)

with open('/home/waqas/repos/platform-client/cause.json','r') as f:
    data = json.loads(f.read())

df_cause_js = pd.json_normalize(data, record_path =['items'])

merged_cause = pd.merge(df_cause_csv, df_cause_js, on="document_id",how="inner")
merged_cause['f1'] = merged_cause['f1'].astype(float)
merged_cause = merged_cause[merged_cause['f1'] > .20]
merged_cause


# %%
# --- RISKS
df_risks_csv = pd.read_csv('/home/waqas/Downloads/selection_documents/risks/pr.tab', sep='\t')
df_risks_csv.drop(df_risks_csv[df_risks_csv['f1'] == '-'].index, inplace=True)

with open('/home/waqas/repos/platform-client/risks.json','r') as f:
    data = json.loads(f.read())

df_risks_js = pd.json_normalize(data, record_path =['items'])

merged_risks = pd.merge(df_risks_csv, df_risks_js, on="document_id",how="inner")
merged_risks['f1'] = merged_risks['f1'].astype(float)
merged_risks  = merged_risks[merged_risks['f1'] > .25]
merged_risks


# %%
# --- DOCUMENT_TYPE
df_doc_csv = pd.read_csv('/home/waqas/Downloads/selection_documents/document_type/pr.tab', sep='\t')
df_doc_csv.drop(df_doc_csv[df_doc_csv['f1'] == '-'].index, inplace=True)
df_doc_csv[['document_id','del']] = df_doc_csv.document_id_.str.split(".",expand=True,)

with open('/home/waqas/repos/platform-client/document.json','r') as f:
    data = json.loads(f.read())

df_doc_js = pd.json_normalize(data, record_path =['items'])

merged_doc = pd.merge(df_doc_csv, df_doc_js, on="document_id",how="inner")
merged_doc['f1'] = merged_doc['f1'].astype(float)
merged_doc = merged_doc[merged_doc['f1'] > .95]
merged_doc


# %%
# --- INVOICE
df_invoice_csv = pd.read_csv('/home/waqas/Downloads/selection_documents/invoice/per_doc.tsv', sep='\t')
df_invoice_csv.drop(df_invoice_csv[df_invoice_csv['f1'] == '-'].index, inplace=True)

with open('/home/waqas/repos/platform-client/invoice.json','r') as f:
    data = json.loads(f.read())

df_invoice_js = pd.json_normalize(data, record_path =['items'])

merged_invoice = pd.merge(df_invoice_csv, df_invoice_js, on="document_id",how="inner")
merged_invoice['f1'] = merged_invoice['f1'].astype(float)
merged_invoice = merged_invoice[merged_invoice['f1'] > 20]
merged_invoice


# %%
# --- CE_REPORT
df_ce_csv = pd.read_csv('/home/waqas/Downloads/selection_documents/ce_report/per_doc.tsv', sep='\t')
df_ce_csv.drop(df_ce_csv[df_ce_csv['f1'] == '-'].index, inplace=True)

with open('/home/waqas/repos/platform-client/ce_report.json','r') as f:
    data = json.loads(f.read())

df_ce_js = pd.json_normalize(data, record_path =['items'])

merged_ce = pd.merge(df_ce_csv, df_ce_js, on="document_id",how="inner")
merged_ce['f1'] = merged_ce['f1'].astype(float)
merged_ce = merged_ce[merged_ce['f1'] > 20]
merged_ce


# %%
grand = [merged_base, merged_cause, merged_ce, merged_doc, merged_invoice, merged_risks]
grand_merged = pd.merge(merged_base, merged_invoice, on=['file_name'], how='inner')
grand_merged
# %%
grand_merged2 = pd.merge(merged_cause, merged_doc, on=['file_name'], how='inner')
grand_merged2

# %%
grand_merged3 = pd.merge(grand_merged, grand_merged2, on=['file_name'], how='inner')
grand_merged3
# %%

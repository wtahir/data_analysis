import pandas as pd
import os
import fire


def filter_field(tsvPath, outdir):
    """
    Filters field wise difference of gt and prediction in a tsv and returns a tsv

    Args:
        tsvPath (str): path of tsv
        outdir (str): path and file name to save tsv
    
    Returns:
        tsv: A tsv with two columns of fields and counts respectively
    """
    df = pd.read_csv(tsvPath, sep='\t')
    df['gt'].fillna("This is an empty string for gt", inplace = True)
    df['pred'].fillna("This is an empty string for pred", inplace = True)
    df = df.where(df['gt'] != df['pred'])
    df_group = df.groupby(df['field']).count()
    df_group.drop(['page' ,'gt', 'pred', 'levenshtein_distance', 'doc_conf', 'entity_conf'], axis=1, inplace=True)
    df_group.columns = ['count']
    return df_group.to_csv(os.path.join(outdir), sep='\t')

if __name__ == "__main__":
    fire.Fire(filter_field)
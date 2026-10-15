import pandas as pd

def load_data(anonymized_path, auxiliary_path):
    """
    Load anonymized and auxiliary datasets.
    """
    anon = pd.read_csv(anonymized_path)
    aux = pd.read_csv(auxiliary_path)
    return anon, aux


def link_records(anon_df, aux_df):
    merged = pd.merge(anon_df, aux_df, on=["age", "gender", "zip3"])
    counts = merged["anon_id"].value_counts()
    unique_ids = counts[counts == 1].index
    unique_matches = merged[merged["anon_id"].isin(unique_ids)]
    result = unique_matches[["anon_id", "name"]]
    result = result.rename(columns={"name": "matched_name"})
    return result


def deanonymization_rate(matches_df, anon_df):
    return len(matches_df) / len(anon_df)
 

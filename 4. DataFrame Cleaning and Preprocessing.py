import pandas as pd
def preprocess_dataframe(df):
  df[df.select_dtypes(include=["int", "float"]).columns] = df[df.select_dtypes(include=["int", "float"]).columns].fillna(df[df.select_dtypes(include=["int", "float"]).columns].mean()) 
  numerical_columns = df.select_dtypes(include=["int", "float"]).columns
  for column in numerical_columns:
    df[column] = (df[column] - df[column].min()) / (df[column].max() - df[column].min())
  categorical_columns = df.select_dtypes(include=["object"]).columns
  for column in categorical_columns:
    df[column] = pd.Categorical(df[column]).codes
  return df
df = pd.DataFrame({
    "numerical_column_1": [10, 20, 30, None],
    "numerical_column_2": [40, 50, 60, 70],
    "categorical_column": ["A", "B", "C", "A"],
})
preprocessed_df = preprocess_dataframe(df)
print(preprocessed_df)

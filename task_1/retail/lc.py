import pandas as pd

def load_data(file_path):
    """
    Load data from the specified file path using pandas read_csv function.
    
    Parameters:
    file_path (str): The file path of the dataset.
    
    Returns:
    DataFrame: The loaded dataset.
    """
    try:
        df = pd.read_csv(file_path)
        return df
    except Exception as e:
        print("An error occured while loading... :\t",e)
        return None
    
def clean_data(df):
    """
    Clean the loaded dataset.
    
    Parameters:
    df (DataFrame): The dataset to be cleaned.
    """
    # Inspection
    print(df.head(5))
    print(df.info())

    # Cleaning
    missing_values = df.isnull().sum()
    print("Missing values:\n", missing_values)

    duplicate_rows = df.duplicated().sum()
    print("Duplicate rows:", duplicate_rows)

    # Potential outliers
    print("Unique values in 'Gender':", df['Gender'].unique())
    print("Value counts of 'Gender':\n", df['Gender'].value_counts())

    outliers = df[df['Age'] > 120]['Age'].value_counts()
    if outliers.empty:
        print("No outliers found.")
    else:
        print("Outliers in 'Age':\n", outliers)
    return df

# Main code
file_path = "D:/Datasets/retail_sales_dataset.csv"
data = load_data(file_path)
clean_data(data)

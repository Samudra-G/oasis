import pandas as pd
import lc

file_path = "D:/Datasets/retail_sales_dataset.csv"
#loaded data
try:
    df = lc.load_data(file_path)
    print("Data loaded succesfully!\n",df is not None)
    #cleaning data
    clean = lc.clean_data(df)
    if clean is not None:
        basic_stats = clean.describe()
        # Other descriptive statistics calculations
        mean_sales_amount = clean['Total Amount'].mean()
        median_quantity_sold = clean['Quantity'].median()
        mode_product_category = clean['Product Category'].mode()[0]

        # Compute measures of spread
        std_sales_amount = clean['Total Amount'].std()

        # Explore categorical variables
        product_category_counts = clean['Product Category'].value_counts()
        
    else:
        print("Error: Data cleaning process returned None.")
except Exception as e:
    print("An error occurred:", e)

print("Descriptive Statistics:")
print("Mean Sales Amount:", mean_sales_amount)
print("Median Quantity Sold:", median_quantity_sold)
print("Mode Product Category:", mode_product_category)
print("Standard Deviation Sales Amount:", std_sales_amount)
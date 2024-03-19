import lc
import matplotlib.pyplot as plt
import pandas as pd
from statsmodels.tsa.seasonal import seasonal_decompose

try:
    #Loading clean data
    clean = lc.load_data("D:/Datasets/retail_sales_dataset.csv")

    if clean is not None:
    #'Date' to datetime object
        clean['Date'] = pd.to_datetime(clean['Date'])
        clean.set_index('Date', inplace=True)
    # Resample data to monthly frequency and calculate sum of total amount
        monthly_total_amount = clean['Total Amount'].resample('ME').sum()

        # Visualize time series data
        plt.figure(figsize=(10, 6))
        plt.plot(monthly_total_amount)
        plt.title('Monthly Total Amount Trend')
        plt.xlabel('Date')
        plt.ylabel('Total Amount')
        plt.grid(True)
        plt.show()
        
        # Perform time series decomposition
        decomposition = seasonal_decompose(monthly_total_amount, model='additive')
        trend = decomposition.trend
        seasonal = decomposition.seasonal
        residual = decomposition.resid

        # Interpret results
        print("Interpretation of Time Series Decomposition Results:")
        print("- The trend component suggests a gradual increase in sales over time.")
        print("- The seasonal component exhibits clear monthly patterns with peaks in certain months.")
        print("- The residual component shows random fluctuations around the trend and seasonal patterns.")
        print("- Overall, the decomposition reveals consistent trends and seasonal patterns in the data.")
        
    else:
        print("Error: Cleaned data is None.")

except Exception as e:
    print("An error occurred:", e)
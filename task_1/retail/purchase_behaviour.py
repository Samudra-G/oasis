import pandas as pd
import matplotlib.pyplot as plt
import lc

try:
    #Loading data
    clean = lc.load_data("D:/Datasets/retail_sales_dataset.csv")

    if clean is not None:
        print("Data loaded successfully!\n")
        #Converting Date into datetime object
        clean['Date'] = pd.to_datetime(clean['Date'])
        #Summary of purchasing behaviour
        total_sales = clean['Total Amount'].sum()
        avg_order_value = clean["Total Amount"].mean()
        purchase_freq = len(clean['Customer ID'].unique()) #Each customer ID represents a purchase
        
        #Visualize the behaviour
        plt.figure(figsize=(10,6))
        plt.plot(clean.index, clean["Total Amount"], color = 'blue', marker = 'o', linestyle = '-')
        plt.title('Total Sales vs Time')
        plt.xlabel('Date')
        plt.ylabel('Total Sales')
        plt.grid(True)
        plt.show()

        #RFM analysis
        # Calculate Recency, Frequency, Monetary values
        recency = clean.groupby('Customer ID')['Date'].max().apply(lambda x: (clean['Date'].max() - x).days)
        frequency = clean['Customer ID'].value_counts()
        monetary = clean.groupby('Customer ID')['Total Amount'].sum()

        # Merge RFM values
        rfm_data = pd.concat([recency, frequency, monetary], axis=1)
        rfm_data.columns = ['Recency', 'Frequency', 'Monetary']

        # Apply RFM scoring
        # Defining quartiles for RFM metrics
        recency_quartiles = pd.qcut(rfm_data['Recency'], q=4, labels=[4, 3, 2, 1])
        frequency_quartiles = pd.qcut(rfm_data['Frequency'], q=4, labels=False, duplicates='drop')
        monetary_quartiles = pd.qcut(rfm_data['Monetary'], q=4, labels=[1, 2, 3, 4])

        # Adding quartile scores to RFM data
        rfm_data['Recency_Score'] = recency_quartiles
        rfm_data['Frequency_Score'] = frequency_quartiles + 1
        rfm_data['Monetary_Score'] = monetary_quartiles

        # Combine scores to get RFM score
        rfm_data['RFM_Score'] = rfm_data['Recency_Score'].astype(str) + (rfm_data['Frequency_Score']).astype(str) + rfm_data['Monetary_Score'].astype(str)

        # Implementation of scoring
        #High Value Customers
        high_value_customers = rfm_data[rfm_data['Monetary'] > rfm_data['Monetary'].quantile(0.75)]
        print("Total number of customers:", len(rfm_data))
        print("Total number of high-value customers:", len(high_value_customers))
        print("Percentage of high-value customers:", round(len(high_value_customers) / len(rfm_data) * 100,1), "%")

        # Calculate average RFM metrics for all customers
        avg_recency = rfm_data['Recency'].mean()
        avg_frequency = rfm_data['Frequency'].mean()
        avg_monetary = rfm_data['Monetary'].mean()

        # Print average RFM metrics
        print("Average Recency for All Customers:", avg_recency)
        print("Average Frequency for All Customers:", avg_frequency)
        print("Average Monetary Value for All Customers:", avg_monetary)

        #Debugging to remove NaN
        rfm_data['RFM_Score'] = rfm_data['RFM_Score'].astype(str).str.replace('nan', '')
        # Calculating average purchase amount for each RFM segment
        avg_purchase_amount = rfm_data.groupby('RFM_Score')['Monetary'].mean()

        # Printing average purchase amount for each RFM segment
        print("Average Purchase Amount for Each RFM Segment:")
        print(round(avg_purchase_amount,2))

        # Exporting RFM analysis results to Excel file : Use if necessary
        #rfm_data.to_excel("rfm_analysis_results.xlsx", index=True)
        #print("RFM analysis results exported to 'rfm_analysis_results.xlsx'.")

    else:
        print("Cleaned Data is of type None:\n")
except Exception as e:
    print("Error occured while data cleaning: ",e)

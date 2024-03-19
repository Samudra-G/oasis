import pandas as pd
import matplotlib.pyplot as plt
import lc

try:
    #Loading clean data
    clean = lc.load_data("D:/Datasets/retail_sales_dataset.csv")
    if clean is not None:
        print("Data loaded successfully!\n")
        # Summary statistics for age and gender
        age_stats = clean['Age'].describe()
        gender_counts = clean['Gender'].value_counts().tolist()

        # Visualize demographic distributions
        plt.figure(figsize=(10, 6))
        plt.subplot(1, 2, 1)
        plt.hist(clean['Age'], bins=20, color='skyblue', edgecolor='black')
        plt.title('Age Distribution')
        plt.xlabel('Age')
        plt.ylabel('Frequency')

        plt.subplot(1, 2, 2)
        categories = clean['Gender'].unique() #For unique gender categories
        plt.bar(categories, gender_counts, color=['blue', 'pink'])
        plt.title('Gender Distribution')
        plt.xlabel('Gender')
        plt.ylabel('Count')
        plt.show()
    else:
        print("Error: Clean Data is None")
except Exception as e:
    print("An error occured while cleaning the data:",e)








# =====================================================
# Project: Retail Sales Data Analyzer
# File Name: retail_analyzer.py
# =====================================================

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import os


# =====================================================
# RetailAnalyzer Class (OOP Implementation)
# =====================================================

class RetailAnalyzer:

    def __init__(self):
        self.df = None

    # -------------------------------
    # 1. Load Data Method
    # -------------------------------
    
    def load_data(self, file_path):
        if not os.path.exists(file_path):
            print("❌ File not found!")
            return

        if not file_path.endswith(".csv"):
            print("❌ Invalid file format! Please upload a CSV file.")
            return

        self.df = pd.read_csv(file_path)
        print("✅ Dataset Loaded Successfully!\n")
        print(self.df.head())

    
    # -------------------------------
    # 2. Clean Data Method 
    # -------------------------------
    
    def clean_data(self):
        if self.df is None:
            print("❌ No data loaded!")
            return
    
        print("\n🔄 Handling Missing Values...")
    
        # Fill missing numerical values with mean
        
        num_cols = ['Price', 'Quantity Sold', 'Total Sales']
        for col in num_cols:
            self.df[col] = self.df[col].fillna(self.df[col].mean())
    
        # Fill missing category/product
       
        self.df['Category'] = self.df['Category'].fillna(self.df['Category'].mode()[0])
        self.df['Product'] = self.df['Product'].fillna(self.df['Product'].mode()[0])
    
        print(" Missing values handled successfully!")
    
        #  SAFE DATE CONVERSION (FIXED)
        self.df['Date'] = pd.to_datetime(self.df['Date'], errors='coerce')
    
        #  If Date still has missing after conversion → fill with most common date
        self.df['Date'] = self.df['Date'].fillna(self.df['Date'].mode()[0])


    # -------------------------------
    # 3. Calculate Metrics Method
    # -------------------------------
    
    def calculate_metrics(self):
        if self.df is None:
            print("No data loaded!")
            return

        total_sales = np.sum(self.df['Total Sales'])
        avg_sales = np.mean(self.df['Total Sales'])
        popular_product = self.df['Product'].mode()[0]

        print("\n Sales Metrics")
        print("----------------------------")
        print("Total Sales:", total_sales)
        print("Average Sales:", round(avg_sales, 2))
        print("Most Popular Product:", popular_product)
        
        
    # -------------------------------
    # 4. Filter Data Method
    # -------------------------------
    
    def filter_data(self, category=None, start_date=None, end_date=None):
        if self.df is None:
            print(" No data loaded!")
            return

        filtered = self.df.copy()

        if category:
            filtered = filtered[filtered['Category'] == category]

        if start_date and end_date:
            filtered = filtered[
                (filtered['Date'] >= start_date) &
                (filtered['Date'] <= end_date)
            ]

        print("\n Filtered Data:")
        print(filtered.head())
        return filtered


    # -------------------------------
    # 5. Display Summary Method
    # -------------------------------
    
    def display_summary(self):
        if self.df is None:
            print(" No data loaded!")
            return

        print("\n📄 Dataset Summary")
        print("----------------------------")
        print(self.df.describe())


    # -------------------------------
    # 6. Visualization Methods
    # -------------------------------

    # Bar Chart
    
    def bar_chart(self):
        category_sales = self.df.groupby('Category')['Total Sales'].sum()

        plt.figure(figsize=(8, 5))
        sns.barplot(x=category_sales.index, y=category_sales.values , color="pink")
        plt.title("Total Sales by Category")
        plt.xlabel("Category")
        plt.ylabel("Total Sales")
        plt.show()

    # Line Graph
    
    def line_graph(self):
        daily_sales = self.df.groupby('Date')['Total Sales'].sum()

        plt.figure(figsize=(8, 5))
        plt.plot(daily_sales.index, daily_sales.values, marker='o' )
        plt.title("Sales Trend Over Time")
        plt.xlabel("Date")
        plt.ylabel("Total Sales")
        plt.grid(True , linestyle='--', alpha=0.5)
        plt.show()

    # Heatmap
    
    def heatmap(self):
        heatmap_data = self.df[['Price', 'Quantity Sold', 'Total Sales']].corr()

        plt.figure(figsize=(6, 4))
        sns.heatmap(heatmap_data, annot=True, cmap='Blues')
        plt.title("Sales Correlation Heatmap")
        plt.show()


# =====================================================
# Main Program (User Interaction)
# =====================================================

def main():
    analyzer = RetailAnalyzer()

    while True:
        print("\n========= Retail Sales Analyzer =========")
        print("1. Load Dataset")
        print("2. Clean Data")
        print("3. Calculate Metrics")
        print("4. Filter Data")
        print("5. Display Summary")
        print("6. Bar Chart")
        print("7. Line Graph")
        print("8. Heatmap")
        print("9. Exit")

        choice = int(input("Enter your choice: "))

        if choice == 1:
            path = input("Enter CSV file path: ")
            analyzer.load_data(path)


        elif choice == 2:
            analyzer.clean_data()


        elif choice == 3:
            analyzer.calculate_metrics()


        elif choice == 4:
            category = input("Enter category (or press Enter to skip): ")
            start_date = input("Enter start date (YYYY-MM-DD or press Enter): ")
            end_date = input("Enter end date (YYYY-MM-DD or press Enter): ")

            if start_date and end_date:
                analyzer.filter_data(category, start_date, end_date)
            else:
                analyzer.filter_data(category)


        elif choice == 5:
            analyzer.display_summary()


        elif choice == 6:
            analyzer.bar_chart()


        elif choice == 7:
            analyzer.line_graph()


        elif choice == 8:
            analyzer.heatmap()


        elif choice == 9:
            print(" Program Exited Successfully!")
            break


        else:
            print(" Invalid choice! Try again.")


# =====================================================
# Program Execution
# =====================================================

if __name__ == "__main__":
    main()

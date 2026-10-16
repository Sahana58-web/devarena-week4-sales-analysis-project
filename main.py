# Complete Data Analysis Project: E-commerce Sales Analysis
# Pipeline: load -> clean -> analyze -> visualize
# Run with: python main.py

import os
import pandas as pd
import matplotlib.pyplot as plt

DATA_FILE = 'data/sales_data.csv'
CHART_FOLDER = 'visualizations'
REQUIRED_COLUMNS = ['Date', 'Product', 'Quantity', 'Price',
                    'Customer_ID', 'Region', 'Total_Sales']


def load_data(path):
    """Load the CSV file. Return None and print a message if something is wrong."""
    try:
        df = pd.read_csv(path)
    except FileNotFoundError:
        print(f"Error: file '{path}' was not found.")
        return None
    except Exception as error:
        print("Error while reading the file:", error)
        return None

    missing = [c for c in REQUIRED_COLUMNS if c not in df.columns]
    if missing:
        print("Error: these columns are missing:", missing)
        return None
    return df


def clean_data(df):
    """Remove missing values, duplicates and invalid rows."""
    before = len(df)
    df = df.dropna().drop_duplicates()
    df['Date'] = pd.to_datetime(df['Date'], errors='coerce')
    df = df.dropna(subset=['Date'])
    df = df[(df['Quantity'] > 0) & (df['Price'] > 0) & (df['Total_Sales'] > 0)]
    print(f"Rows before cleaning: {before}, after cleaning: {len(df)}")
    return df


def analyze_data(df):
    """Calculate the main numbers used in the report."""
    df['Month'] = df['Date'].dt.to_period('M').astype(str)
    results = {
        'total_sales': df['Total_Sales'].sum(),
        'average_sale': df['Total_Sales'].mean(),
        'by_product': df.groupby('Product')['Total_Sales'].sum().sort_values(ascending=False),
        'units_by_product': df.groupby('Product')['Quantity'].sum().sort_values(ascending=False),
        'by_month': df.groupby('Month')['Total_Sales'].sum(),
        'by_region': df.groupby('Region')['Total_Sales'].sum().sort_values(ascending=False),
    }
    return results


def make_charts(results, folder):
    """Create a bar chart, a line chart and a pie chart and save them."""
    os.makedirs(folder, exist_ok=True)
    by_product = results['by_product']
    by_month = results['by_month']
    by_region = results['by_region']

    # Chart 1: Bar chart - sales by product
    plt.figure(figsize=(8, 5))
    plt.bar(by_product.index, by_product.values / 1_000_000, color='steelblue')
    plt.title('Total Sales by Product')
    plt.xlabel('Product')
    plt.ylabel('Sales (Rs. millions)')
    plt.savefig(f'{folder}/1_sales_by_product_bar.png', dpi=150, bbox_inches='tight')
    plt.close()

    # Chart 2: Line chart - monthly sales trend
    plt.figure(figsize=(8, 5))
    plt.plot(by_month.index, by_month.values / 1_000_000, marker='o', color='darkgreen')
    plt.title('Monthly Sales Trend (April has only 9 days of data)')
    plt.xlabel('Month')
    plt.ylabel('Sales (Rs. millions)')
    plt.grid(True, alpha=0.3)
    plt.savefig(f'{folder}/2_monthly_sales_line.png', dpi=150, bbox_inches='tight')
    plt.close()

    # Chart 3: Pie chart - share of sales by region
    plt.figure(figsize=(7, 7))
    plt.pie(by_region.values, labels=by_region.index, autopct='%1.1f%%', startangle=90)
    plt.title('Share of Total Sales by Region')
    plt.savefig(f'{folder}/3_sales_by_region_pie.png', dpi=150, bbox_inches='tight')
    plt.close()

    print(f"3 charts saved in the '{folder}' folder.")


def print_report(results):
    """Print the key results."""
    print()
    print("=" * 45)
    print("SALES ANALYSIS SUMMARY")
    print("=" * 45)
    print(f"Total Sales: Rs.{results['total_sales']:,.2f}")
    print(f"Average Sale: Rs.{results['average_sale']:,.2f}")
    print(f"Best-Selling Product: {results['by_product'].index[0]}")
    print(f"Most Units Sold: {results['units_by_product'].index[0]}")
    print(f"Best Region: {results['by_region'].index[0]}")
    print()
    print("Sales by Month:")
    for month, amount in results['by_month'].items():
        print(f"  {month}: Rs.{amount:,.2f}")


def main():
    df = load_data(DATA_FILE)
    if df is None:
        return
    df = clean_data(df)
    if df.empty:
        print("Error: no valid rows left after cleaning.")
        return
    results = analyze_data(df)
    make_charts(results, CHART_FOLDER)
    print_report(results)


if __name__ == '__main__':
    main()


## Visual Documentation
Bar chart: total sales by product

![Sales by product](visualizations/1_sales_by_product_bar.png)

Line chart: monthly sales trend

![Monthly sales trend](visualizations/2_monthly_sales_line.png)

Pie chart: share of sales by region

![Sales by region](visualizations/3_sales_by_region_pie.png)

## Technical Details
The program in main.py is split into small functions:
- load_data(path): reads the CSV file with pandas. It uses try/except to handle a missing file and checks that all 7 required columns exist.
- clean_data(df): removes missing values and duplicate rows, converts Date to a real date, and removes invalid rows (zero or negative quantity, price or sales).
- analyze_data(df): calculates total sales, average sale, and group-by sums by product, month and region.
- make_charts(results, folder): creates 3 chart types with matplotlib (bar, line and pie) and saves them as PNG files.
- print_report(results): prints the key results.
- main(): runs the whole pipeline and stops with a clear message if the data is missing or empty.

Libraries: pandas (data), matplotlib (charts).

## Testing Evidence
- Data checks: 100 rows loaded, 0 missing values, 0 duplicate rows, 100 rows kept after cleaning.
- Data validation: Total_Sales equals Quantity x Price for all 100 rows.
- Results were cross-checked with a separate calculation. Total sales matched: Rs.12,365,048.
- Error handling: if the CSV file is missing, or a column is missing, the program prints an error message instead of crashing.
- The program ran without errors, and all 3 charts were created.

## Key Findings
- Total sales: Rs.12,365,048 from 100 orders (average Rs.123,650 per order).
- Best-selling product: Laptop (Rs.3,889,210, 31.5% of sales, 136 units).
- Best region: North (Rs.3,983,635, 32.2% of sales).
- Best month: March (Rs.4,485,006). February was the weakest full month because of smaller orders. April has only 9 days of data.
- The West region has many orders but a much smaller average order value (Rs.81,689).

The full written analysis, tables and recommendations are in report/analysis_report.md.

## What I Learned
I learned how to build a complete data analysis project: loading and cleaning data with pandas, calculating metrics with group-by, creating bar, line and pie charts with matplotlib, adding error handling, and organizing a project with data, visualizations and report folders on GitHub.

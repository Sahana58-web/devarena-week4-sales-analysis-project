# Sales Data Analysis: Project Report

## 1. Project Overview
This project analyses an e-commerce sales dataset of 100 orders (2024-01-01 to 2024-04-09). The aim is to find which products, months and regions bring the most sales, and to explain the results with charts and written insights.

## 2. Data
- File: data/sales_data.csv (100 rows, 7 columns)
- Columns: Date, Product, Quantity, Price, Customer_ID, Region, Total_Sales
- 5 products (Laptop, Tablet, Phone, Headphones, Monitor) and 4 regions (North, South, East, West)

## 3. Method (the analysis pipeline)
1. **Load:** pandas reads the CSV file. The program prints an error message if the file or a column is missing.
2. **Clean:** missing values, duplicate rows and invalid values (zero or negative numbers) are removed. Date is converted to a real date. Result: 0 rows removed, so all 100 rows were used.
3. **Analyze:** totals, averages and group-by sums for product, month and region.
4. **Visualize:** 3 charts are made with matplotlib and saved in the visualizations folder.

## 4. Key Numbers
| Metric | Value |
|---|---|
| Total Sales | Rs.12,365,048 |
| Average sale per order | Rs.123,650 |
| Units sold | 478 |
| Highest single order | Rs.373,932 (Phone, 2024-01-16, South) |

## 5. Charts and Findings

### Chart 1: Total Sales by Product (bar chart)
![Sales by product](../visualizations/1_sales_by_product_bar.png)

| Product | Sales (Rs.) | Share of sales | Units sold |
|---|---|---|---|
| Laptop | 3,889,210 | 31.5% | 136 |
| Tablet | 2,884,340 | 23.3% | 127 |
| Phone | 2,859,394 | 23.1% | 101 |
| Headphones | 1,384,033 | 11.2% | 48 |
| Monitor | 1,348,071 | 10.9% | 66 |

Laptop is the best-selling product, with almost one third of all sales. Laptop, Tablet and Phone together make up about 78% of sales.

### Chart 2: Monthly Sales Trend (line chart)
![Monthly trend](../visualizations/2_monthly_sales_line.png)

| Month | Sales (Rs.) | Orders | Average per order (Rs.) |
|---|---|---|---|
| 2024-01 | 4,120,524 | 31 | 132,920 |
| 2024-02 | 2,656,050 | 29 | 91,588 |
| 2024-03 | 4,485,006 | 31 | 144,678 |
| 2024-04 | 1,103,468 | 9 | 122,608 |

Sales fell about 35% from January to February, then rose about 69% in March, which was the best month. The fall in February came from smaller orders (average Rs.91,588), not from fewer orders. April looks very low only because the data ends on 9 April (9 orders), so April should not be compared directly with full months. Its average order value (Rs.122,608) is close to January.

### Chart 3: Share of Sales by Region (pie chart)
![Sales by region](../visualizations/3_sales_by_region_pie.png)

| Region | Sales (Rs.) | Share | Orders | Average per order (Rs.) |
|---|---|---|---|---|
| North | 3,983,635 | 32.2% | 28 | 142,273 |
| South | 3,737,852 | 30.2% | 27 | 138,439 |
| East | 2,519,639 | 20.4% | 19 | 132,613 |
| West | 2,123,922 | 17.2% | 26 | 81,689 |

North and South together bring over 60% of sales. West has almost as many orders as South (26 vs 27), but its average order is much smaller (Rs.81,689), so West sales are lower because of order size, not because of fewer customers.

## 6. Insights and Recommendations
1. **Focus on Laptops:** they bring the most revenue and the most units. Keep them well stocked and promote them.
2. **Grow Headphones and Monitors:** they have the lowest sales and the fewest units. Bundle offers (for example a laptop with headphones) could help.
3. **Raise order value in the West:** the region has many orders but small ones. Upselling or bundles could increase its sales.
4. **Understand February:** February orders were smaller than in other months. Checking for discounts or seasonal buying could explain this.
5. **Collect more data:** a full year of data would give a more reliable trend, especially because April is incomplete.

## 7. Limitations
- Only 100 orders over about 3 months, so seasonal patterns cannot be confirmed.
- April has only 9 days of data.
- The data has no cost or profit column, so the analysis covers sales only, not profit.

## 8. Conclusion
The data was clean and complete. Laptops and the North region drive the most revenue, the West region has an order-size problem, and the monthly trend should be read with care because April is incomplete. This project covers the full pipeline: load, clean, analyze and visualize.

# 🇳🇬 Nigerian E-Commerce Order Pipeline — Day 01

> Day 1 of my 90-day Data Engineering challenge.  
> Building real pipelines, with real data, from scratch.

---

## 📌 Project Overview

This project simulates the first step towards data engineering — **ingesting and filtering raw order data** from a Nigerian e-commerce platform.

The script reads a dataset of 50 customer orders placed across major Nigerian cities, filters them by status, cross-checks data quality, and generates a business summary — total revenue, order distribution by city, and flagged data issues.

---

## 📂 Dataset

**File:** `ng_ecommerce_orders.csv`  
**Records:** 50 orders  
**Period:** January 2024  
**Source:** generated real-world dataset created for this project

| Column | Description |
|---|---|
| `order_id` | Unique order identifier |
| `customer_id` | Unique customer identifier |
| `customer_name` | Full name of customer |
| `city` | Customer city |
| `state` | Customer state |
| `product_category` | Category of item ordered |
| `product_name` | Name of item ordered |
| `quantity` | Number of units ordered |
| `unit_price_ngn` | Price per unit in Naira |
| `total_amount_ngn` | Total order value in Naira |
| `payment_method` | Card / Transfer / Cash |
| `order_status` | completed / pending / failed |
| `order_date` | Date order was placed |
| `delivery_date` | Date order was delivered (empty if not yet delivered) |

---

## ⚙️ What the Pipeline Does

### 1. Ingests raw CSV data
Reads the orders dataset using Python's built-in `csv` module, parsing each row as a dictionary keyed by column name.

### 2. Filters completed orders
Extracts only orders where `order_status == "completed"` from the full dataset.

### 3. Cross-checks data quality
Flags any order marked as "completed" but missing a `delivery_date` — a real-world data inconsistency that would indicate upstream data issues in a production pipeline.

### 4. Generates a business summary
- Total number of completed orders
- Completed orders ranked by city (descending)
- Total revenue generated from completed orders in Naira

---

## 📊 Sample Output

```
Total completed orders: 39
---
  NG-10001 | Adaeze Okonkwo | Lagos | ₦18,500
  NG-10002 | Emeka Nwosu | Abuja | ₦90,000
  NG-10003 | Ngozi Eze | Port Harcourt | ₦32,000
  ...

 Completed orders missing a delivery date: 0

 Completed orders by city:
  Lagos: 9 orders
  Enugu: 4 orders
  Abuja: 3 orders
  ...

 Total revenue from completed orders: ₦2,345,500
```

---

##  Key Concepts Applied

- **CSV ingestion** with `csv.DictReader` — parsing raw files into structured dictionaries
- **Filtering** with conditional logic across a dataset
- **Data quality cross-checking** — validating one column against another to catch inconsistencies
- **Aggregation** — grouping and counting records by category
- **Sorting** with `lambda` functions — ranking results by value descending
- **List & dict comprehensions** — writing clean, readable Python transformations

---

## 🛠 Tech Stack

| Tool | Purpose |
|---|---|
| Python 3 | Core scripting language |
| `csv` module | File ingestion |
| Git & GitHub | Version control |

---

## 🚀 How to Run

**1. Clone the repository**
```bash
git clone https://github.com/JokoTolulope/DE_journey.git
cd DE_journey
```

**2. Run the pipeline script**
```bash
python filter_orders.py
```

No external libraries required — runs on plain Python 3.

---

## 📁 Project Structure

```
DE_journey/
├── de1.py                    # Data structures practice scripts
├── filter_orders.py            # Main pipeline script
├── ng_ecommerce_orders.csv     # Nigerian e-commerce orders dataset
└── README.md                   # Project documentation
```

---

## 🗺 What's Next — Day 02

Working with real data formats used in production pipelines:
- Converting this CSV dataset to **JSON** and **Parquet** formats
- Understanding why columnar storage (Parquet) is preferred at scale
- Writing a Python script that handles all three formats

---


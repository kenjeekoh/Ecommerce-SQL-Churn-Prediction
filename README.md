
# 🛍️ E-Commerce Sales Analytics Dashboard

A full-stack SQL and machine learning project that simulates a real-world e-commerce data pipeline. From relational database design and advanced SQL analytics to customer churn prediction using Python, this project showcases end-to-end data-driven decision making.

---

## 📊 Project Overview

This project analyzes synthetic e-commerce transactional data and uses SQL and Python to answer key business questions. It also builds a churn prediction model based on customer behavior and purchasing patterns.

---

## 🧱 Database Schema

The database is modeled using standard relational principles and contains five normalized tables:

- **Customers**: Customer demographics and region
- **Products**: Product metadata including category and price
- **Orders**: High-level order details (status, date)
- **Order_Items**: Line-level purchase details (quantity, price_each)
- **Payments**: Payment amounts and methods

SQL table creation and data loading are defined in `sql/create_all.sql`.

---

## 📁 Project Structure

```
E-Commerce-Sales-Analytics-Dashboard/
├── data/
│   ├── churn_features.csv         # Engineered features for ML
│   ├── churn_predictions.csv      # Model predictions
│   ├── customers.csv
│   ├── order_items.csv
│   ├── orders.csv
│   ├── payments.csv
│   └── products.csv
├── ml/
│   └── churn_prediction.py        # Python churn model
├── sql/
│   ├── create_all.sql             # Schema + table definitions
│   └── analytical_queries.sql     # Business-focused SQL insights
├── README.md
```

---

## 🔍 SQL Analysis Highlights

All analytical queries are found in `sql/analytical_queries.sql`. Key questions answered:

- 💰 **Total revenue by product category**
- 👑 **Top customers by total spend**
- 📈 **Monthly revenue trends**
- 🌍 **Average order value by customer region**
- 🔁 **Repeat customer detection**

These queries utilize complex `JOIN`s, `GROUP BY`, subqueries, and aggregations to surface business-critical insights.

---

## 🔮 Customer Churn Prediction (ML)

Built using `RandomForestClassifier`, the churn model predicts customer dropout based on:

- `days_since_last_order`
- `total_orders`
- `total_spent`

### 🧪 ML Workflow (`ml/churn_prediction.py`)
- Load SQL-exported features (`churn_features.csv`)
- Define churn: `days_since_last_order > 90`
- Split into train/test, train a model, evaluate with confusion matrix
- Predict churn probability and save results to `churn_predictions.csv`
- Visualize feature importances and churn risk

---

## 📊 Results Sample

**Confusion Matrix:**

Perfect model performance on test set  
(✔️ indicates class balance and strong signal in data):

```
Predicted
     0   1
  ----------
0 | 36 | 0
1 |  0 | 51
```

**Top Features:**
- `days_since_last_order` = strongest signal
- `total_orders` = valuable customer indicator

---

## 🛠️ Tools & Technologies

- **SQL**: MySQL Workbench
- **Python**: pandas, scikit-learn, matplotlib, seaborn
- **Version Control**: Git & GitHub
- **Development**: VS Code

---

## 🚀 Future Improvements

- Deploy model as a Flask API or Streamlit dashboard
- Add clustering to segment users further
- Incorporate product return rates or promo codes
- Replace synthetic data with anonymized real-world set

---

## 🙌 Acknowledgments

Built by [Christiaan Kenjee Koh](https://www.linkedin.com/in/kenjeekoh/), MSBA student @ UC Irvine.
This project was inspired by real-world data workflows in sales analytics and customer lifecycle optimization.

---

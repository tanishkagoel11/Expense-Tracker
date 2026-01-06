# Modular Expense Tracker & Planner

## 1. Project Overview
The **Modular Expense Tracker** is a Python-based expense management system designed to transform semi-structured transaction data into actionable financial insights. Built with **Object-Oriented Programming (OOP)** principles, the application provides a scalable architecture for tracking expenditures, managing income, and visualizing spending patterns.

The primary objective of this project was to transition from writing procedural scripts to designing robust, extensible system architectures capable of handling complex data relationships.

---

## 2. System Architecture



The application is divided into four distinct logical layers to ensure high cohesion and low coupling:

### A. Data Modeling Layer (Inheritance)
At the core is a hierarchical data model representing financial entities.
* **`Transaction` (Base Class):** Captures universal attributes including `amount`, `date`, and `participants`.
* **`Expense` & `Income` (Subclasses):** These extend `Transaction` to handle specific domain logic. For instance, the `Expense` class automatically negates values to represent outflows while maintaining a clean interface for the user.



### B. Business Logic Layer
* **`Ledger`:** Acts as the primary state manager, maintaining a master list of all transactions and calculating the net balance.
* **`ExpenseInsights`:** Decouples analysis from storage. It is responsible for data aggregation, such as calculating totals per category and preparing data for visualization.

### C. Data Ingestion Layer (Abstraction)
To ensure the system is not "brittle" or tied to a single file format, I implemented an abstraction layer:
* **`DataSource` (Abstract Base Class):** Defines a strict interface (`all_expenses`) that any data provider must follow.
* **`CsvParser`:** A concrete implementation of `DataSource` that handles the complexities of parsing CSV files, including error handling for malformed rows.
* **`DataExtractor`:** Uses the **Strategy Pattern** to request data from any `DataSource` without needing to know the underlying implementation.

### D. Visualization Layer
Utilizes `Matplotlib` to translate raw data from `ExpenseInsights` into interactive pie charts, enabling composition analysis for the end-user.

---

## 3. Engineering Principles Applied

### Encapsulation and Responsibility
By separating the `Ledger` from `ExpenseInsights`, the system follows the **Single Responsibility Principle (SRP)**. The `Ledger` ensures the integrity of the history, while `ExpenseInsights` focuses on the utility of that data for decision-making.

### Robustness & Error Handling
The `CsvParser` implements specific exception handling (`ValueError`, `KeyError`) to ensure that "dirty data" in a single CSV row does not crash the ingestion pipeline. 

### Extensibility
The use of **Abstract Base Classes (ABCs)** ensures the codebase is "Open-Closed": open for extension but closed for modification. Adding a SQL database source in the future would only require a new `SqlParser` class; the core logic remains untouched.

---

## 4. Usage
1.  **Data Setup:** Create an `expenses.csv` file in the root directory with the headers: `amount,date,category,participants`.
2.  **Execution:**
    ```bash
    python main.py
    ```
3.  **Output:** The system parses the data, updates the ledger, and generates an `expense_breakdown.png`.

---

## 5. Future Roadmap
* **Asset Management:** Implementing subclasses for `Stocks` and `Mutual Funds` to track appreciation/depreciation.
* **SQL Integration:** Migrating from CSV to a relational database using the existing `DataSource` abstraction.
* **Data Normalization:** Adding a layer to map varied user-entered categories into standardized financial buckets.

# Homework 3

This project demonstrates how to connect PostgreSQL with Flask and display SELECT results in an HTML table.

## Quick Start

### Local Test Setup

#### 1. Install Python 3 and Virtual Environment

To get started, first ensure you have Python 3 installed. Then, you can install the `venv` package:

```bash
sudo apt-get install python3-venv
```
#### 2. Create a Virtual Environment

To keep dependencies isolated, create a virtual environment:

```bash
python3 -m venv venv_name
```
Replace venv_name with your preferred name for the virtual environment.

### 3. Activate the Virtual Environment
Whenever you work on this project, activate the virtual environment by running:

```bash
source venv_name/bin/activate
```

### 4. Install Requirements

After activating the virtual environment, install all required packages by running:

```bash
pip install -r requirements.txt
```

### 5. Run the Server
Once dependencies are installed, you can start the Flask server with:

```bash
python app.py
```
After starting the server, it should be available at 127.0.0.1:5000.

## EndPoints
```bash
/api/update_basket_a
```
- Description: Inserts a new row (5, 'Cherry') into the basket_a table.
- Method: GET
- Response: Displays "Success!" or an error message from PostgreSQL.
```bash
/api/unique
```
- Description: Shows unique fruits in basket_a and basket_b in an HTML table.
- Method: GET
- Response: Displays the fruits in a table or an error message from PostgreSQL.

## Database Setup

Before running the application, make sure the following tables are created in your PostgreSQL database.

```bash
CREATE TABLE basket_a (
    a INT PRIMARY KEY,
    fruit_a VARCHAR(100) NOT NULL
);

CREATE TABLE basket_b (
    b INT PRIMARY KEY,
    fruit_b VARCHAR(100) NOT NULL
);

INSERT INTO basket_a (a, fruit_a)
VALUES
    (1, 'Apple'),
    (2, 'Orange'),
    (3, 'Banana'),
    (4, 'Cucumber');

INSERT INTO basket_b (b, fruit_b)
VALUES
    (1, 'Orange'),
    (2, 'Apple'),
    (3, 'Watermelon'),
    (4, 'Pear');
```
 
## Team Members
This is the Github users of the people that have worked on this assignment
- James Miller (Github: KuyaJames724)




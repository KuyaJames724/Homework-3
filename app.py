from flask import Flask, jsonify, render_template_string
import psycopg2

app = Flask(__name__)


# Connect to the PostgreSQL database
def get_db_connection():
    try:
        conn = psycopg2.connect(
            host="localhost",  # Adjust according to your setup
            database="dvdrental",
            user="jamesm",
            password="1234"
        )
        return conn
    except Exception as e:
        return str(e)


# Route to insert a new row into basket_a
@app.route('/api/update_basket_a')
def update_basket_a():
    conn = get_db_connection()
    if isinstance(conn, str):
        return conn  # Return the error message if connection fails

    try:
        cur = conn.cursor()
        cur.execute("INSERT INTO basket_a (a, fruit_a) VALUES (5, 'Cherry')")
        conn.commit()
        cur.close()
        conn.close()
        return "Success!"
    except Exception as e:
        return str(e)


# Route to show unique fruits from both baskets
@app.route('/api/unique')
def show_unique_fruits():
    conn = get_db_connection()
    if isinstance(conn, str):
        return conn  # Return the error message if connection fails

    try:
        cur = conn.cursor()

        # Query unique fruits from both tables
        cur.execute("SELECT DISTINCT fruit_a FROM basket_a")
        basket_a_fruits = [row[0] for row in cur.fetchall()]

        cur.execute("SELECT DISTINCT fruit_b FROM basket_b")
        basket_b_fruits = [row[0] for row in cur.fetchall()]

        # Close the connection
        cur.close()
        conn.close()

        # Prepare HTML for displaying the fruits in a table
        html = '''
        <table border="1">
            <tr>
                <th>Unique Fruits in Basket A</th>
                <th>Unique Fruits in Basket B</th>
            </tr>
            <tr>
                <td>{}</td>
                <td>{}</td>
            </tr>
        </table>
        '''.format(', '.join(basket_a_fruits), ', '.join(basket_b_fruits))

        return render_template_string(html)

    except Exception as e:
        return str(e)


# Main driver
if __name__ == '__main__':
    app.run(debug=True)

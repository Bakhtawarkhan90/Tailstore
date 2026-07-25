from flask import Flask, request, redirect, url_for, send_from_directory
import mysql.connector
import os
import time

app = Flask(__name__, static_url_path='', static_folder='.')

# ==========================================
# MySQL Connection
# ==========================================

db = None

while True:
    try:
        db = mysql.connector.connect(
            host=os.getenv("MYSQL_HOST", "database"),
            user=os.getenv("MYSQL_USER", "root"),
            password=os.getenv("MYSQL_PASSWORD", "kali"),
            database=os.getenv("MYSQL_DATABASE", "tailstore")
        )

        print("✅ Database connected")
        break

    except mysql.connector.Error as err:
        print(f"❌ Database connection failed: {err}")
        time.sleep(5)


# ==========================================
# Create Billing Table
# ==========================================

try:
    cursor = db.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS billing_details (
            id INT AUTO_INCREMENT PRIMARY KEY,
            full_name VARCHAR(100) NOT NULL,
            email VARCHAR(150) NOT NULL,
            address VARCHAR(255) NOT NULL,
            city VARCHAR(100) NOT NULL,
            state VARCHAR(100) NOT NULL,
            zip_code VARCHAR(20) NOT NULL,
            phone VARCHAR(30) NOT NULL,
            different_address BOOLEAN DEFAULT FALSE,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
    """)

    db.commit()
    cursor.close()

    print("✅ billing_details table ready")

except mysql.connector.Error as err:
    print(f"❌ Table creation error: {err}")


# ==========================================
# Home Page
# ==========================================

@app.route('/')
def index():
    return send_from_directory('.', 'index.html')


# ==========================================
# Checkout Page
# ==========================================

@app.route('/checkout.html')
def checkout():
    return send_from_directory('.', 'checkout.html')


# ==========================================
# Save Billing Details
# ==========================================

@app.route('/save-billing', methods=['POST'])
def save_billing():

    full_name = request.form.get('full_name')
    email = request.form.get('email')
    address = request.form.get('address')
    city = request.form.get('city')
    state = request.form.get('state')
    zip_code = request.form.get('zip_code')
    phone = request.form.get('phone')

    different_address = request.form.get('different_address')

    if different_address:
        different_address = True
    else:
        different_address = False

    print("📥 Billing data received:")
    print("Name:", full_name)
    print("Email:", email)
    print("Address:", address)
    print("City:", city)
    print("State:", state)
    print("ZIP:", zip_code)
    print("Phone:", phone)

    try:

        cursor = db.cursor()

        query = """
        INSERT INTO billing_details
        (
            full_name,
            email,
            address,
            city,
            state,
            zip_code,
            phone,
            different_address
        )
        VALUES (%s, %s, %s, %s, %s, %s, %s, %s)
        """

        values = (
            full_name,
            email,
            address,
            city,
            state,
            zip_code,
            phone,
            different_address
        )

        cursor.execute(query, values)

        db.commit()

        cursor.close()

        print("✅ Billing details saved successfully")

        # After saving, redirect to payment page
        return redirect(url_for('payment'))

    except mysql.connector.Error as err:

        print(f"❌ MySQL INSERT ERROR: {err}")

        return f"""
        <h2>❌ Failed to save billing details</h2>
        <p>{err}</p>
        <a href="/checkout.html">Go Back</a>
        """, 500


# ==========================================
# Payment Page
# ==========================================

@app.route('/payment.html')
def payment():
    return send_from_directory('.', 'payment.html')


# ==========================================
# Serve Static Files
# ==========================================

@app.route('/<path:filename>')
def serve_static(filename):
    return send_from_directory('.', filename)


# ==========================================
# Start Flask
# ==========================================

if __name__ == '__main__':
    app.run(
        host='0.0.0.0',
        port=5000,
        debug=True
    )

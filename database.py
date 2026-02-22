import sqlite3
from datetime import datetime, timedelta

class Database:
    def __init__(self, db_name='members.db'):
        self.conn = sqlite3.connect(db_name)
        self.cursor = self.conn.cursor()
        self.create_tables()

    def create_tables(self):
        self.cursor.execute('''
        CREATE TABLE IF NOT EXISTS members (
            id INTEGER PRIMARY KEY,
            name TEXT NOT NULL,
            email TEXT NOT NULL UNIQUE,
            membership_type TEXT NOT NULL,
            registration_date TEXT NOT NULL,
            expiry_date TEXT NOT NULL,
            payment_status TEXT NOT NULL
        )
        ''')
        self.conn.commit()

    def register_member(self, name, email, membership_type, payment_status='pending'):
        registration_date = datetime.utcnow().strftime('%Y-%m-%d %H:%M:%S')
        expiry_date = self.calculate_expiry(membership_type)
        self.cursor.execute('''
        INSERT INTO members (name, email, membership_type, registration_date, expiry_date, payment_status)
        VALUES (?, ?, ?, ?, ?, ?)''', (name, email, membership_type, registration_date, expiry_date, payment_status))
        self.conn.commit()

    def calculate_expiry(self, membership_type):
        if membership_type == 'monthly':
            return (datetime.utcnow() + timedelta(days=30)).strftime('%Y-%m-%d %H:%M:%S')
        elif membership_type == 'yearly':
            return (datetime.utcnow() + timedelta(days=365)).strftime('%Y-%m-%d %H:%M:%S')
        return datetime.utcnow().strftime('%Y-%m-%d %H:%M:%S')

    def update_payment_status(self, email, status):
        self.cursor.execute('''
        UPDATE members
        SET payment_status = ?
        WHERE email = ?
        ''', (status, email))
        self.conn.commit()

    def get_member_details(self, email):
        self.cursor.execute('''
        SELECT * FROM members WHERE email = ?
        ''', (email,))
        return self.cursor.fetchone()

    def close(self):
        self.conn.close()

# Example usage
if __name__ == '__main__':
    db = Database()
    db.register_member('John Doe', 'john@example.com', 'monthly')
    print(db.get_member_details('john@example.com'))
    db.close()
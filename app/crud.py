from .database import get_db_connection
from typing import List, Optional

# Contact CRUD operations
def create_contact(contact_data: dict):
    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)
    try:
        cursor.execute(
            """INSERT INTO contacts 
            (first_name, last_name, email, address) 
            VALUES (%s, %s, %s, %s)""",
            (contact_data['first_name'], contact_data['last_name'], 
             contact_data['email'], contact_data['address'])
        )
        contact_id = cursor.lastrowid
        conn.commit()
        return get_contact(contact_id)
    finally:
        cursor.close()
        conn.close()

def get_contact(contact_id: int):
    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)
    try:
        cursor.execute(
            "SELECT * FROM contacts WHERE contact_id = %s", 
            (contact_id,)
        )
        contact = cursor.fetchone()
        return contact
    finally:
        cursor.close()
        conn.close()

def get_contacts(skip: int = 0, limit: int = 100, search: Optional[str] = None):
    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)
    try:
        query = "SELECT * FROM contacts"
        params = []
        
        if search:
            query += " WHERE first_name LIKE %s OR last_name LIKE %s OR email LIKE %s"
            params.extend([f"%{search}%", f"%{search}%", f"%{search}%"])
        
        query += " LIMIT %s OFFSET %s"
        params.extend([limit, skip])
        
        cursor.execute(query, params)
        return cursor.fetchall()
    finally:
        cursor.close()
        conn.close()

def update_contact(contact_id: int, contact_data: dict):
    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)
    try:
        cursor.execute(
            """UPDATE contacts 
            SET first_name = %s, last_name = %s, email = %s, address = %s 
            WHERE contact_id = %s""",
            (contact_data['first_name'], contact_data['last_name'],
             contact_data['email'], contact_data['address'], contact_id)
        )
        conn.commit()
        return get_contact(contact_id)
    finally:
        cursor.close()
        conn.close()

def delete_contact(contact_id: int):
    conn = get_db_connection()
    cursor = conn.cursor()
    try:
        cursor.execute(
            "DELETE FROM contacts WHERE contact_id = %s",
            (contact_id,)
        )
        conn.commit()
        return cursor.rowcount > 0
    finally:
        cursor.close()
        conn.close()

# Phone CRUD operations
def add_phone_to_contact(phone_data: dict):
    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)
    try:
        cursor.execute(
            """INSERT INTO phone_numbers 
            (contact_id, phone_type, number, is_primary) 
            VALUES (%s, %s, %s, %s)""",
            (phone_data['contact_id'], phone_data['phone_type'],
             phone_data['number'], phone_data['is_primary'])
        )
        phone_id = cursor.lastrowid
        conn.commit()
        return get_phone(phone_id)
    finally:
        cursor.close()
        conn.close()

def get_phone(phone_id: int):
    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)
    try:
        cursor.execute(
            "SELECT * FROM phone_numbers WHERE phone_id = %s",
            (phone_id,)
        )
        return cursor.fetchone()
    finally:
        cursor.close()
        conn.close()

def get_contact_phones(contact_id: int):
    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)
    try:
        cursor.execute(
            "SELECT * FROM phone_numbers WHERE contact_id = %s",
            (contact_id,)
        )
        return cursor.fetchall()
    finally:
        cursor.close()
        conn.close()

def update_phone(phone_id: int, phone_data: dict):
    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)
    try:
        cursor.execute(
            """UPDATE phone_numbers 
            SET phone_type = %s, number = %s, is_primary = %s 
            WHERE phone_id = %s""",
            (phone_data['phone_type'], phone_data['number'],
             phone_data['is_primary'], phone_id)
        )
        conn.commit()
        return get_phone(phone_id)
    finally:
        cursor.close()
        conn.close()

def delete_phone(phone_id: int):
    conn = get_db_connection()
    cursor = conn.cursor()
    try:
        cursor.execute(
            "DELETE FROM phone_numbers WHERE phone_id = %s",
            (phone_id,)
        )
        conn.commit()
        return cursor.rowcount > 0
    finally:
        cursor.close()
        conn.close()

# Tag CRUD operations
def create_tag(tag_data: dict):
    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)
    try:
        cursor.execute(
            """INSERT INTO tags (name, description) 
            VALUES (%s, %s)""",
            (tag_data['name'], tag_data['description'])
        )
        tag_id = cursor.lastrowid
        conn.commit()
        return get_tag(tag_id)
    finally:
        cursor.close()
        conn.close()

def get_tag(tag_id: int):
    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)
    try:
        cursor.execute(
            "SELECT * FROM tags WHERE tag_id = %s",
            (tag_id,)
        )
        return cursor.fetchone()
    finally:
        cursor.close()
        conn.close()

def get_tags():
    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)
    try:
        cursor.execute("SELECT * FROM tags")
        return cursor.fetchall()
    finally:
        cursor.close()
        conn.close()

def add_tag_to_contact(contact_id: int, tag_id: int):
    conn = get_db_connection()
    cursor = conn.cursor()
    try:
        cursor.execute(
            "INSERT INTO contact_tags (contact_id, tag_id) VALUES (%s, %s)",
            (contact_id, tag_id)
        )
        conn.commit()
        return True
    except mysql.connector.IntegrityError:
        return False
    finally:
        cursor.close()
        conn.close()

def get_contact_tags(contact_id: int):
    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)
    try:
        cursor.execute(
            """SELECT t.* FROM tags t
            JOIN contact_tags ct ON t.tag_id = ct.tag_id
            WHERE ct.contact_id = %s""",
            (contact_id,)
        )
        return cursor.fetchall()
    finally:
        cursor.close()
        conn.close()

def remove_tag_from_contact(contact_id: int, tag_id: int):
    conn = get_db_connection()
    cursor = conn.cursor()
    try:
        cursor.execute(
            "DELETE FROM contact_tags WHERE contact_id = %s AND tag_id = %s",
            (contact_id, tag_id)
        )
        conn.commit()
        return cursor.rowcount > 0
    finally:
        cursor.close()
        conn.close()

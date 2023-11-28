# Database connection parameters
from tkinter import messagebox

import psycopg2
from bcrypt import hashpw, gensalt

conn = psycopg2.connect(
    host="localhost",
    port=5432,
    database="ESG_Retail_Dashboard",
    user="postgres",
    password="Manisha13",
)

def insert_data(store_id, address, city, postalcode, ownername, contactno, emailid):
    try:
        # Insert data into the 'storedetails' table
        with conn, conn.cursor() as cursor:
            cursor.execute("INSERT INTO public.storedetails(retail_store_id, retail_store_address, retail_store_city, "
                           "retail_store_postalcode, retail_store_ownername, retail_store_contactno, retail_store_emailid) "
                           "VALUES (%s, %s, %s, %s, %s, %s, %s)",
                           (store_id, address, city, postalcode, ownername, contactno, emailid))
        return store_id
    except Exception as e:
        # Handle the exception, you can print an error message or log the exception details
        print(f"Error inserting data: {e}")
        messagebox.showinfo('Error', f'Error inserting data: {e} {store_id}')
        return None


def insert_waste_data(retail_store_id, date_generated, date_entered,
                       data_load_type, food_wastage, food_wastage_units, plastic_wastage, units_plastic_units,
                       paper_wastage, paper_waste_units):
    try:
        # Insert data into the 'storedetails' table
        with conn, conn.cursor() as cursor:
            cursor.execute("INSERT INTO public.wastemanagement(retail_store_id, date_generated, date_entered, "
                           "data_load_type, food_wastage, food_wastage_units, plastic_wastage, units_plastic_units, "
                           "paper_wastage, paper_waste_units)"
                           "VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)",
                           (retail_store_id, date_generated, date_entered,
                           data_load_type, food_wastage, food_wastage_units, plastic_wastage, units_plastic_units,
                           paper_wastage, paper_waste_units))
        return retail_store_id
    except Exception as e:
        # Handle the exception, you can print an error message or log the exception details
        print(f"Error inserting data: {e}")
        messagebox.showinfo('Error', f'Error inserting data: {e} {retail_store_id}')
        return None


def insert_user(username, password):
    # Insert user into the 'users' table
    try:
        with conn, conn.cursor() as cursor:
            # Hash the password before storing it
            hashed_password = hashpw(password.encode('utf-8'), gensalt()).decode('utf-8')
            cursor.execute('INSERT INTO users (username, password_hash) VALUES (%s, %s)', (username, hashed_password))
    except Exception as e:
        # Handle the exception, you can print an error message or log the exception details
        print(f"Error inserting data: {e}")
        return None

def verify_user(username, password):
    try:
        # Verify user credentials
        with conn, conn.cursor() as cursor:
            cursor.execute('SELECT password_hash FROM users WHERE username = %s', (username,))
            stored_hash = cursor.fetchone()

        if stored_hash:
            # Verify the password using bcrypt
            stored_hash_str = stored_hash[0]
            return hashpw(password.encode('utf-8'), stored_hash_str.encode('utf-8')).decode('utf-8') == stored_hash_str
        else:
            return False
    except Exception as e:
        # Handle the exception, you can print an error message or log the exception details
        print(f"Error inserting data: {e}")
        return None


def insert_energy_data(retail_store_id, date_generated, date_entered, data_load_type,
                       light_consumption, light_consumption_units, temp_outside,
                       temp_outside_units, temp_inside, temp_inside_units,
                       refridgerator_usage, refridgerator_usage_units):
    try:
        # Insert data into the 'energyconsumption' table
        with conn, conn.cursor() as cursor:
            cursor.execute("INSERT INTO public.energyconsumption(retail_store_id, date_generated, date_entered, "
                           "data_load_type, light_consumption, light_consumption_units, temp_outside, temp_outside_units, "
                           "temp_inside, temp_inside_units, refridgerator_usage, refridgerator_usage_units) "
                           "VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)",
                           (retail_store_id, date_generated, date_entered, data_load_type,
                            light_consumption, light_consumption_units, temp_outside,
                            temp_outside_units, temp_inside, temp_inside_units,
                            refridgerator_usage, refridgerator_usage_units))
        return retail_store_id
    except Exception as e:
        # Handle the exception, you can print an error message or log the exception details
        print(f"Error inserting data: {e}")
        messagebox.showinfo('Error', f'Error inserting data: {e} {retail_store_id}')
        return None


def insert_water_data(retail_store_id, date_generated, date_entered, data_load_type,
                      drinking_water_consumption, drinking_water_consumption_units,
                      washroom_water_consumption, washroom_water_consumption_unit,
                      other_purpose_consumption, other_purpose_consumption_unit):
    try:
        # Insert data into the 'waterconsumption' table
        with conn, conn.cursor() as cursor:
            cursor.execute("INSERT INTO public.waterconsumption(retail_store_id, date_generated, date_entered, "
                           "data_load_type, drinking_water_consumption, drinking_water_consumption_units, "
                           "washroom_water_consumption, washroom_water_consumption_unit, "
                           "other_purpose_consumption, other_purpose_consumption_unit)"
                           "VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)",
                           (retail_store_id, date_generated, date_entered, data_load_type,
                            drinking_water_consumption, drinking_water_consumption_units,
                            washroom_water_consumption, washroom_water_consumption_unit,
                            other_purpose_consumption, other_purpose_consumption_unit))
        return retail_store_id
    except Exception as e:
        # Handle the exception, you can print an error message or log the exception details
        print(f"Error inserting data: {e}")
        messagebox.showinfo('Error', f'Error inserting data: {e} {retail_store_id}')
        return None


def insert_fuel_data(retail_store_id, date_generated, date_entered, data_load_type,
                     gasoline_consumed, gasoline_consumed_units, diesel_consumed, diesel_consumed_units,
                     electric_consumed, electric_consumed_units):
    try:
        # Insert data into the 'fuelconsumption' table
        with conn, conn.cursor() as cursor:
            cursor.execute("INSERT INTO public.fuelconsumption(retail_store_id, date_generated, date_entered, "
                           "data_load_type, gasoline_consumed, gasoline_consumed_units, diesel_consumed, "
                           "diesel_consumed_units, electric_consumed, electric_consumed_units)"
                           "VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)",
                           (retail_store_id, date_generated, date_entered, data_load_type,
                            gasoline_consumed, gasoline_consumed_units, diesel_consumed,
                            diesel_consumed_units, electric_consumed, electric_consumed_units))
        return retail_store_id
    except Exception as e:
        # Handle the exception, you can print an error message or log the exception details
        print(f"Error inserting data: {e}")
        messagebox.showinfo('Error', f'Error inserting data: {e} {retail_store_id}')
        return None

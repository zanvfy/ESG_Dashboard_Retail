import ESG_UI as EUI
import tkinter as tk
from tkinter import ttk, messagebox
import ESG_UI_INSERT as EI
import ESG_UI_Clear as EUC

# Function to handle email entry validation
def validate_email_entry():
    email = EUI.emailid_entry.get()
    if validate_email(email):
        return True  # Email is valid
    else:
        messagebox.showerror("Error", "Invalid email format")
        return False  # Email is not valid

# Function to validate email
def validate_email(email):
    import re
    pattern = r'^\S+@\S+\.\S+$'
    return re.match(pattern, email) is not None


def submit_data():
    store_id = EUI.store_id_entry.get()
    address = EUI.address_entry.get()
    city = EUI.city_entry.get()
    postalcode = EUI.postalcode_entry.get()
    ownername = EUI.ownername_entry.get()
    contactno = EUI.contactno_entry.get()
    emailid = EUI.emailid_entry.get()

    if store_id and address and city and postalcode and ownername and contactno and emailid:
        store_id = EI.insert_data(store_id, address, city, postalcode, ownername, contactno, emailid)
        if store_id != None:
            EUI.messagebox.showinfo('Success', f'Store details saved successfully!\nStore ID: {store_id}')
        EUI.store_id_entry.delete(0, tk.END)
        EUI.address_entry.delete(0, tk.END)
        EUI.city_entry.delete(0, tk.END)
        EUI.postalcode_entry.delete(0, tk.END)
        EUI.ownername_entry.delete(0, tk.END)
        EUI.contactno_entry.delete(0, tk.END)
        EUI.emailid_entry.delete(0, tk.END)
    else:
        messagebox.showerror('Error', 'Please fill in all the mandatory store details.')


# Function to handle Waste Management data submission
def submit_waste_data():
    store_id_waste = EUI.store_id_waste_entry.get()
    date_generated = EUI.date_generated_waste_entry.get()
    date_entered = EUI.date_entered_waste_entry.get()
    print(date_entered)
    # Assuming that EUI is an instance of some class and the attributes are Entry widgets
    data_load_type = EUI.data_load_type_entry.get()
    food_wastage = EUI.food_wastage_entry.get() or 0
    food_wastage_units = EUI.food_wastage_units_entry.get() or ''
    plastic_wastage = EUI.plastic_wastage_entry.get() or 0
    plastic_wastage_units = EUI.plastic_wastage_units_entry.get() or ''
    paper_wastage = EUI.paper_wastage_entry.get() or 0
    paper_waste_units = EUI.paper_waste_units_entry.get() or ''

    # Assuming that retail_store_id, date_generated, and date_entered are also variables
    sql_command = "INSERT INTO public.wastemanagement(retail_store_id, date_generated, date_entered, " \
                  "data_load_type, food_wastage, food_wastage_units, plastic_wastage, units_plastic_units, " \
                  "paper_wastage, paper_waste_units) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"

    if store_id_waste and date_generated and date_entered and data_load_type:
        # Call your function to insert data into the 'wastemanagement' table
        EI.insert_waste_data(store_id_waste, date_generated, date_entered, data_load_type, food_wastage,
                             food_wastage_units,
                             plastic_wastage, plastic_wastage_units, paper_wastage, paper_waste_units)
        if store_id_waste != None:
            messagebox.showinfo('Success', 'Waste Management data saved successfully!')
        # Clear the entries after submission
        EUC.clear_waste_entries()
    else:
        messagebox.showerror('Error', 'Please fill in all the mandatory waste management details.')


# Function to handle Energy Consumption data submission
def submit_energy_data():
    store_id_energy = EUI.store_id_energy_entry.get()
    date_generated_energy = EUI.date_generated_energy_entry.get()
    date_entered_energy = EUI.date_entered_energy_entry.get()
    data_load_type_energy = EUI.data_load_type_energy_entry.get()
    light_consumption = EUI.light_consumption_entry.get() or 0
    light_consumption_units = EUI.light_consumption_units_entry.get() or ''
    temp_outside = EUI.temp_outside_entry.get() or 0
    temp_outside_units = EUI.temp_outside_units_entry.get() or ''
    temp_inside = EUI.temp_inside_entry.get() or 0
    temp_inside_units = EUI.temp_inside_units_entry.get() or ''
    refrigerator_usage = EUI.refrigerator_usage_entry.get() or 0
    refrigerator_usage_units = EUI.refrigerator_usage_units_entry.get() or ''

    if store_id_energy and date_generated_energy and date_entered_energy and data_load_type_energy:
        # Call your function to insert data into the 'energyconsumption' table
        EI.insert_energy_data(store_id_energy, date_generated_energy, date_entered_energy, data_load_type_energy,
                              light_consumption, light_consumption_units, temp_outside, temp_outside_units,
                              temp_inside, temp_inside_units, refrigerator_usage, refrigerator_usage_units)
        if store_id_energy != None:
            messagebox.showinfo('Success', 'Energy Consumption data saved successfully!')
        # Clear the entries after submission
        EUC.clear_energy_entries()
    else:
        messagebox.showerror('Error', 'Please fill in all the mandatory energy consumption details.')


# Function to handle Water Consumption data submission
def submit_water_data():
    store_id_water = EUI.store_id_water_entry.get()
    date_generated_water = EUI.date_generated_water_entry.get()
    date_entered_water = EUI.date_entered_water_entry.get()
    data_load_type_water = EUI.data_load_type_water_entry.get()
    drinking_water_consumption = EUI.drinking_water_consumption_entry.get() or 0
    drinking_water_consumption_units = EUI.drinking_water_consumption_units_entry.get() or ''
    washroom_water_consumption = EUI.washroom_water_consumption_entry.get() or 0
    washroom_water_consumption_units = EUI.washroom_water_consumption_units_entry.get() or ''
    other_purpose_consumption = EUI.other_purpose_consumption_entry.get() or 0
    other_purpose_consumption_units = EUI.other_purpose_consumption_units_entry.get() or ''

    if store_id_water and date_generated_water and date_entered_water and data_load_type_water :
        # Call your function to insert data into the 'waterconsumption' table
        EI.insert_water_data(store_id_water, date_generated_water, date_entered_water, data_load_type_water,
                             drinking_water_consumption, drinking_water_consumption_units, washroom_water_consumption,
                             washroom_water_consumption_units, other_purpose_consumption,
                             other_purpose_consumption_units)
        if store_id_water != None:
            messagebox.showinfo('Success', 'Water Consumption data saved successfully!')
        # Clear the entries after submission
        EUC.clear_water_entries()
    else:
        messagebox.showerror('Error', 'Please fill in all the mandatory water consumption details.')


# Function to handle Fuel Consumption data submission
def submit_fuel_data():
    store_id_fuel = EUI.store_id_fuel_entry.get()
    date_generated_fuel = EUI.date_generated_fuel_entry.get()
    date_entered_fuel = EUI.date_entered_fuel_entry.get()
    data_load_type_fuel = EUI.data_load_type_fuel_entry.get()
    gasoline_consumed = EUI.gasoline_consumed_entry.get() or 0
    gasoline_consumed_units = EUI.gasoline_consumed_units_entry.get() or ''
    diesel_consumed = EUI.diesel_consumed_entry.get() or 0
    diesel_consumed_units = EUI.diesel_consumed_units_entry.get() or ''
    electric_consumed = EUI.electric_consumed_entry.get() or 0
    electric_consumed_units = EUI.electric_consumed_units_entry.get() or ''

    if store_id_fuel and date_generated_fuel and date_entered_fuel and data_load_type_fuel :
        # Call your function to insert data into the 'fuelconsumption' table
        EI.insert_fuel_data(store_id_fuel, date_generated_fuel, date_entered_fuel, data_load_type_fuel,
                            gasoline_consumed, gasoline_consumed_units, diesel_consumed,
                            diesel_consumed_units, electric_consumed, electric_consumed_units)
        if store_id_fuel != None:
            messagebox.showinfo('Success', 'Fuel Consumption data saved successfully!')
        # Clear the entries after submission
        EUC.clear_fuel_entries()
    else:
        messagebox.showerror('Error', 'Please fill in all the mandatory fuel consumption details.')

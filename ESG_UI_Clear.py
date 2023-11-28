import ESG_UI  as EUI
import tkinter as tk

# Function to clear Waste Management entries after submission
def clear_waste_entries():
    EUI.store_id_waste_entry.delete(0, tk.END)
    EUI.date_generated_entry.delete(0, tk.END)
    EUI.date_entered_entry.delete(0, tk.END)
    EUI.data_load_type_entry.delete(0, tk.END)
    EUI.food_wastage_entry.delete(0, tk.END)
    EUI.food_wastage_units_entry.delete(0, tk.END)
    EUI. plastic_wastage_entry.delete(0, tk.END)
    EUI.plastic_wastage_units_entry.delete(0, tk.END)
    EUI.paper_wastage_entry.delete(0, tk.END)
    EUI.paper_waste_units_entry.delete(0, tk.END)

# Function to clear Energy Consumption entries after submission
def clear_energy_entries():
    EUI.store_id_energy_entry.delete(0, tk.END)
    EUI.date_generated_energy_entry.delete(0, tk.END)
    EUI.date_entered_energy_entry.delete(0, tk.END)
    EUI.data_load_type_energy_entry.delete(0, tk.END)
    EUI.light_consumption_entry.delete(0, tk.END)
    EUI.light_consumption_units_entry.delete(0, tk.END)
    EUI.temp_outside_entry.delete(0, tk.END)
    EUI.temp_outside_units_entry.delete(0, tk.END)
    EUI.temp_inside_entry.delete(0, tk.END)
    EUI.temp_inside_units_entry.delete(0, tk.END)
    EUI.refrigerator_usage_entry.delete(0, tk.END)
    EUI.refrigerator_usage_units_entry.delete(0, tk.END)

# Function to clear Water Consumption entries after submission
def clear_water_entries():
    EUI.store_id_water_entry.delete(0, tk.END)
    EUI.date_generated_water_entry.delete(0, tk.END)
    EUI.date_entered_water_entry.delete(0, tk.END)
    EUI.data_load_type_water_entry.delete(0, tk.END)
    EUI.drinking_water_consumption_entry.delete(0, tk.END)
    EUI.drinking_water_consumption_units_entry.delete(0, tk.END)
    EUI.washroom_water_consumption_entry.delete(0, tk.END)
    EUI.washroom_water_consumption_units_entry.delete(0, tk.END)
    EUI.other_purpose_consumption_entry.delete(0, tk.END)
    EUI.other_purpose_consumption_units_entry.delete(0, tk.END)

# Function to clear Fuel Consumption entries after submission
def clear_fuel_entries():
    EUI.store_id_fuel_entry.delete(0, tk.END)
    EUI.date_generated_fuel_entry.delete(0, tk.END)
    EUI.date_entered_fuel_entry.delete(0, tk.END)
    EUI.data_load_type_fuel_entry.delete(0, tk.END)
    EUI.gasoline_consumed_entry.delete(0, tk.END)
    EUI.gasoline_consumed_units_entry.delete(0, tk.END)
    EUI. diesel_consumed_entry.delete(0, tk.END)
    EUI.diesel_consumed_units_entry.delete(0, tk.END)
    EUI.electric_consumed_entry.delete(0, tk.END)
    EUI.electric_consumed_units_entry.delete(0, tk.END)

import tkinter as tk
from tkinter import ttk, messagebox
from tkcalendar import DateEntry
import ESG_UI_INSERT as EI
import ESG_UI_SUBMIT as ES


def create_label(frame, text, mandatory=False):
    label_text = text + '*' if mandatory else text
    tk.Label(frame, text=label_text, font=('Helvetica', 14), bg=bg_color, fg='white').pack(pady=5, anchor='w')


def create_button(parent, text, command, side, **kwargs):
    tk.Button(parent, text=text, command=command, font=('Helvetica', 14), relief=tk.FLAT, bg='#55acee', fg='white',
              **kwargs).pack(side=side, pady=10, padx=10)


def create_entry(parent, font=('Helvetica', 14), pady=5, padx=5, fill='x', **kwargs):
    entry = tk.Entry(parent, font=font, **kwargs)
    entry.pack(pady=pady, padx=padx, fill=fill)
    return entry


def create_date_entry(parent, font=('Helvetica', 14), pady=5, padx=5, fill='x', **kwargs):
    entry = DateEntry(parent, font=font, **kwargs)
    entry.pack(pady=pady, padx=padx, fill=fill)
    return entry


def done():
    root.destroy()


def login_handler():
    username = username_entry.get()
    password = password_entry.get()
    if EI.verify_user(username, password):
        root.deiconify()
        login_window.destroy()
    else:
        messagebox.showerror('Error', 'Invalid credentials.')


def switch_to_register():
    login_frame.grid_forget()
    reg_frame.grid(row=1, column=0, columnspan=2)


def back_to_login():
    reg_frame.grid_forget()
    login_frame.grid(row=1, column=0, columnspan=2)


def register_user():
    username = reg_username_entry.get()
    password = reg_password_entry.get()

    if username and password:
        EI.insert_user(username, password)
        messagebox.showinfo('Success', 'User registered successfully!')
        reg_username_entry.delete(0, tk.END)
        reg_password_entry.delete(0, tk.END)
        # Switch back to login frame
        reg_frame.grid_forget()
        login_frame.grid(row=1, column=0, columnspan=2)
    else:
        messagebox.showerror('Error', 'Please enter both username and password for registration.')

# Main application window
root = tk.Tk()
root.title('ESG Retail Data Entry')
# Allow window resizing
root.resizable(True, True)

root.withdraw()  # Hide the main window initially

# Walmart color: RGB(0, 0, 255) - Blue
bg_color = '#0066cc'

# Login window
login_window = tk.Toplevel(root)
login_window.title('Login')
login_window.configure(bg=bg_color)

# Login window layout
login_frame = tk.Frame(login_window, pady=20, bg=bg_color)
login_frame.grid(row=1, column=0, columnspan=2)

tk.Label(login_frame, text='Username', font=('Helvetica', 14), bg=bg_color, fg='white').grid(row=0, column=0, padx=10,
                                                                                             pady=10)
username_entry = tk.Entry(login_frame, font=('Helvetica', 14))
username_entry.grid(row=0, column=1, padx=10, pady=10)

tk.Label(login_frame, text='Password', font=('Helvetica', 14), bg=bg_color, fg='white').grid(row=1, column=0, padx=10,
                                                                                             pady=10)
password_entry = tk.Entry(login_frame, show='*', font=('Helvetica', 14))
password_entry.grid(row=1, column=1, padx=10, pady=10)

tk.Button(login_frame, text='Login', command=login_handler, font=('Helvetica', 14), relief=tk.FLAT, bg='#55acee',
          fg='white').grid(row=2, column=0, columnspan=2,
                           pady=10, padx=10)

# Registration frame within login window
reg_frame = tk.Frame(login_window, pady=20, bg=bg_color)
reg_frame.grid(row=1, column=0, columnspan=2)
reg_frame.grid_forget()  # Initially hide the registration frame

tk.Label(reg_frame, text='Register a new user:', font=('Helvetica', 14), bg=bg_color, fg='white').grid(row=0, column=0,
                                                                                                       columnspan=2,
                                                                                                       pady=10)

tk.Label(reg_frame, text='Username', font=('Helvetica', 14), bg=bg_color, fg='white').grid(row=1, column=0, padx=10,
                                                                                           pady=10)
reg_username_entry = tk.Entry(reg_frame, font=('Helvetica', 14))
reg_username_entry.grid(row=1, column=1, padx=10, pady=10)

tk.Label(reg_frame, text='Password', font=('Helvetica', 14), bg=bg_color, fg='white').grid(row=2, column=0, padx=10,
                                                                                           pady=10)
reg_password_entry = tk.Entry(reg_frame, show='*', font=('Helvetica', 14))
reg_password_entry.grid(row=2, column=1, padx=10, pady=10)

# Register button styled as a link
tk.Button(login_frame, text="Don't have an account? Register here!", command=switch_to_register, font=('Helvetica', 12),
          relief=tk.FLAT, bg=bg_color, fg='white').grid(row=3, column=0, columnspan=2)

# Register button styled as a link (in registration frame)
tk.Button(reg_frame, text='Register', command=register_user, font=('Helvetica', 14), fg='white', relief=tk.FLAT,
          bg='#55acee').grid(row=3, column=0, columnspan=2,
                             pady=10)

# Back button to go back to login window
tk.Button(reg_frame, text='Back', command=back_to_login, font=('Helvetica', 14), fg='white', relief=tk.FLAT,
          bg='#55acee').grid(row=4, column=0, columnspan=2,
                             pady=10)

# Tabs for different sections
tabs = ttk.Notebook(root)
tabs.pack(fill='both', expand=True)

# Data entry window
data_entry_frame = tk.Frame(tabs, bg=bg_color)
tabs.add(data_entry_frame, text='Store Details')

# Labels on the left side
labels_frame = tk.Frame(data_entry_frame, bg=bg_color)
labels_frame.pack(side='left', fill='both', expand=True)

entries_frame = tk.Frame(data_entry_frame, bg=bg_color)
entries_frame.pack(side='left', fill='both', expand=True)

create_label(labels_frame, 'Store ID', mandatory=True)
create_label(labels_frame, 'Store Address', mandatory=True)
create_label(labels_frame, 'City', mandatory=True)
create_label(labels_frame, 'Postal Code', mandatory=True)
create_label(labels_frame, 'Owner Name', mandatory=True)
create_label(labels_frame, 'Contact Number', mandatory=True)
create_label(labels_frame, 'Email ID', mandatory=True)

# Submit and Done button frame
buttons_frame = tk.Frame(data_entry_frame, bg=bg_color)
buttons_frame.pack(side='bottom', fill='both', expand=True)

# Submit button for Data Entry
create_button(buttons_frame, 'Submit', ES.submit_data, tk.LEFT)

# Done button for Data Entry
create_button(buttons_frame, 'Done', done, tk.RIGHT)

# Entries on the right side
entries_frame = tk.Frame(data_entry_frame, bg=bg_color)
entries_frame.pack(side='left', fill='both', expand=True)

store_id_entry = create_entry(entries_frame)
address_entry = create_entry(entries_frame)
city_entry = create_entry(entries_frame)
postalcode_entry = create_entry(entries_frame)
ownername_entry = create_entry(entries_frame)
contactno_entry = create_entry(entries_frame)
emailid_entry = create_entry(entries_frame, validate="focusout", validatecommand=ES.validate_email_entry)


# Waste Management window
#####################################################################################################
# Waste Management window
waste_frame = tk.Frame(tabs, bg=bg_color)
tabs.add(waste_frame, text='Waste Management')

# Labels on the left side for Waste Management
waste_labels_frame = tk.Frame(waste_frame, bg=bg_color)
waste_labels_frame.pack(side='left', fill='both', expand=True)

# Usage example:
create_label(waste_labels_frame, 'Store ID', mandatory=True)
create_label(waste_labels_frame, 'Date Generated', mandatory=True)
create_label(waste_labels_frame, 'Date Entered', mandatory=True)
create_label(waste_labels_frame, 'Data Load Type', mandatory=True)
create_label(waste_labels_frame, 'Food Wastage')
create_label(waste_labels_frame, 'Food Wastage Units')
create_label(waste_labels_frame, 'Plastic Wastage')
create_label(waste_labels_frame, 'Plastic Wastage Units')
create_label(waste_labels_frame, 'Paper Wastage')
create_label(waste_labels_frame, 'Paper Waste Units')

# Submit and Done button frame for Waste Management
waste_buttons_frame = tk.Frame(waste_frame, bg=bg_color)
waste_buttons_frame.pack(side='bottom', fill='both', expand=True)

# Entries on the right side for Waste Management
waste_entries_frame = tk.Frame(waste_frame, bg=bg_color)
waste_entries_frame.pack(side='left', fill='both', expand=True)

store_id_waste_entry = create_entry(waste_entries_frame)
date_generated_waste_entry = create_date_entry(waste_entries_frame, date_pattern='yyyy-mm-dd')
date_entered_waste_entry = create_date_entry(waste_entries_frame, date_pattern='yyyy-mm-dd')
data_load_type_entry = create_entry(waste_entries_frame)
food_wastage_entry = create_entry(waste_entries_frame)
food_wastage_units_entry = create_entry(waste_entries_frame)
plastic_wastage_entry = create_entry(waste_entries_frame)
plastic_wastage_units_entry = create_entry(waste_entries_frame)
paper_wastage_entry = create_entry(waste_entries_frame)
paper_waste_units_entry = create_entry(waste_entries_frame)

# Submit button for Waste Management
create_button(waste_buttons_frame, 'Submit', ES.submit_waste_data, tk.LEFT)

# Done button for Waste Management
create_button(waste_buttons_frame, 'Done', done, tk.RIGHT)

# Energy Consumption window
#####################################################################################################
# Energy Consumption window
energy_frame = tk.Frame(tabs, bg=bg_color)
tabs.add(energy_frame, text='Energy Consumption')

# Labels on the left side for Energy Consumption
energy_labels_frame = tk.Frame(energy_frame, bg=bg_color)
energy_labels_frame.pack(side='left', fill='both', expand=True)

# Usage example:
create_label(energy_labels_frame, 'Store ID', mandatory=True)
create_label(energy_labels_frame, 'Date Generated', mandatory=True)
create_label(energy_labels_frame, 'Date Entered', mandatory=True)
create_label(energy_labels_frame, 'Data Load Type', mandatory=True)
create_label(energy_labels_frame, 'Light Consumption')
create_label(energy_labels_frame, 'Light Consumption Units')
create_label(energy_labels_frame, 'Outside Temperature')
create_label(energy_labels_frame, 'Outside Temperature Units')
create_label(energy_labels_frame, 'Inside Temperature')
create_label(energy_labels_frame, 'Inside Temperature Units')
create_label(energy_labels_frame, 'Refrigerator Usage')
create_label(energy_labels_frame, 'Refrigerator Usage Units')

# Submit and Done button frame for Energy Consumption
energy_buttons_frame = tk.Frame(energy_frame, bg=bg_color)
energy_buttons_frame.pack(side='bottom', fill='both', expand=True)

# Entries on the right side for Energy Consumption
energy_entries_frame = tk.Frame(energy_frame, bg=bg_color)
energy_entries_frame.pack(side='left', fill='both', expand=True)

store_id_energy_entry = create_entry(energy_entries_frame)
date_generated_energy_entry = create_date_entry(energy_entries_frame, date_pattern='yyyy-mm-dd')
date_entered_energy_entry = create_date_entry(energy_entries_frame, date_pattern='yyyy-mm-dd')
data_load_type_energy_entry = create_entry(energy_entries_frame)
light_consumption_entry = create_entry(energy_entries_frame)
light_consumption_units_entry = create_entry(energy_entries_frame)
temp_outside_entry = create_entry(energy_entries_frame)
temp_outside_units_entry = create_entry(energy_entries_frame)
temp_inside_entry = create_entry(energy_entries_frame)
temp_inside_units_entry = create_entry(energy_entries_frame)
refrigerator_usage_entry = create_entry(energy_entries_frame)
refrigerator_usage_units_entry = create_entry(energy_entries_frame)

# Submit button for Energy Consumption
create_button(energy_buttons_frame, 'Submit', ES.submit_energy_data, tk.LEFT)

# Done button for Energy Consumption
create_button(energy_buttons_frame, 'Done', done, tk.RIGHT)


# Water Consumption window
#####################################################################################################
# Water Consumption window
water_frame = tk.Frame(tabs, bg=bg_color)
tabs.add(water_frame, text='Water Consumption')

# Labels on the left side for Water Consumption
water_labels_frame = tk.Frame(water_frame, bg=bg_color)
water_labels_frame.pack(side='left', fill='both', expand=True)

# Usage example:
create_label(water_labels_frame, 'Store ID', mandatory=True)
create_label(water_labels_frame, 'Date Generated', mandatory=True)
create_label(water_labels_frame, 'Date Entered', mandatory=True)
create_label(water_labels_frame, 'Data Load Type', mandatory=True)
create_label(water_labels_frame, 'Drinking Water Consumption')
create_label(water_labels_frame, 'Drinking Water Consumption Units')
create_label(water_labels_frame, 'Washroom Water Consumption')
create_label(water_labels_frame, 'Washroom Water Consumption Units')
create_label(water_labels_frame, 'Other Purpose Consumption')
create_label(water_labels_frame, 'Other Purpose Consumption Units')

# Submit and Done button frame for Water Consumption
water_buttons_frame = tk.Frame(water_frame, bg=bg_color)
water_buttons_frame.pack(side='bottom', fill='both', expand=True)

# Entries on the right side for Water Consumption
water_entries_frame = tk.Frame(water_frame, bg=bg_color)
water_entries_frame.pack(side='left', fill='both', expand=True)

store_id_water_entry = create_entry(water_entries_frame)
date_generated_water_entry = create_date_entry(water_entries_frame, date_pattern='yyyy-mm-dd')
date_entered_water_entry = create_date_entry(water_entries_frame, date_pattern='yyyy-mm-dd')
data_load_type_water_entry = create_entry(water_entries_frame)
drinking_water_consumption_entry = create_entry(water_entries_frame)
drinking_water_consumption_units_entry = create_entry(water_entries_frame)
washroom_water_consumption_entry = create_entry(water_entries_frame)
washroom_water_consumption_units_entry = create_entry(water_entries_frame)
other_purpose_consumption_entry = create_entry(water_entries_frame)
other_purpose_consumption_units_entry = create_entry(water_entries_frame)

# Submit button for Water Consumption
create_button(water_buttons_frame, 'Submit', ES.submit_water_data, tk.LEFT)

# Done button for Water Consumption
create_button(water_buttons_frame, 'Done', done, tk.RIGHT)


# Fuel Consumption window
#####################################################################################################
# Fuel Consumption window
fuel_frame = tk.Frame(tabs, bg=bg_color)
tabs.add(fuel_frame, text='Fuel Consumption')

# Labels on the left side for Fuel Consumption
fuel_labels_frame = tk.Frame(fuel_frame, bg=bg_color)
fuel_labels_frame.pack(side='left', fill='both', expand=True)

# Usage example:
create_label(fuel_labels_frame, 'Store ID', mandatory=True)
create_label(fuel_labels_frame, 'Date Generated', mandatory=True)
create_label(fuel_labels_frame, 'Date Entered', mandatory=True)
create_label(fuel_labels_frame, 'Data Load Type', mandatory=True)
create_label(fuel_labels_frame, 'Gasoline Consumed')
create_label(fuel_labels_frame, 'Gasoline Consumed Units')
create_label(fuel_labels_frame, 'Diesel Consumed')
create_label(fuel_labels_frame, 'Diesel Consumed Units')
create_label(fuel_labels_frame, 'Electric Consumed')
create_label(fuel_labels_frame, 'Electric Consumed Units')

# Submit and Done button frame for Fuel Consumption
fuel_buttons_frame = tk.Frame(fuel_frame, bg=bg_color)
fuel_buttons_frame.pack(side='bottom', fill='both', expand=True)

# Entries on the right side for Fuel Consumption
fuel_entries_frame = tk.Frame(fuel_frame, bg=bg_color)
fuel_entries_frame.pack(side='right', fill='both', expand=True)

store_id_fuel_entry = create_entry(fuel_entries_frame)
date_generated_fuel_entry = create_date_entry(fuel_entries_frame, date_pattern='yyyy-mm-dd')
date_entered_fuel_entry = create_date_entry(fuel_entries_frame, date_pattern='yyyy-mm-dd')
data_load_type_fuel_entry = create_entry(fuel_entries_frame)
gasoline_consumed_entry = create_entry(fuel_entries_frame)
gasoline_consumed_units_entry = create_entry(fuel_entries_frame)
diesel_consumed_entry = create_entry(fuel_entries_frame)
diesel_consumed_units_entry = create_entry(fuel_entries_frame)
electric_consumed_entry = create_entry(fuel_entries_frame)
electric_consumed_units_entry = create_entry(fuel_entries_frame)

# Submit button for Fuel Consumption
create_button(fuel_buttons_frame, 'Submit', ES.submit_fuel_data, tk.LEFT)

# Done button for Fuel Consumption
create_button(fuel_buttons_frame, 'Done', done, tk.RIGHT)


# Hide the main window until login is successful
root.withdraw()

# Start the main loop
root.mainloop()


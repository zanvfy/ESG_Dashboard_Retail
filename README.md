## Overview

This project involves a system with multiple components to manage and visualize data. The primary components include:

1. **PostgreSQL Database:** 
   - The database folder contains database-related documents and backups.
   - Ensure that the necessary database scripts and configurations are available in this folder.

2. **ETL Python Application:**
   - The ETL process is implemented in Python.
   - The application extracts, transforms, and loads data into the PostgreSQL database.
   - The Python code for the ETL process can be found in [ESG_UI_SUBMIT.py](ESG_UI_SUBMIT.py).

3. **Power BI Dashboard:**
   - The UI is implemented using Power BI for data visualization.
   - Users can register, log in, and insert the data through the Power BI dashboard.

## Folder Structure

- **/Database:**
  - Contains database-related documents and backups.

- **/:**
  - Holds the Python ETL application code.

- **/ui:**
  - Contains files related to the Power BI dashboard.

## Setting Up the Database

1. Ensure PostgreSQL is installed on your system.
2. Run the database scripts in the `/database` folder to set up the necessary tables and configurations.

## Running the ETL Application

1. Install the required Python dependencies using:
   ```bash
   pip install -r requirements.txt
2. Now to run the application post 
   ```'
   python ESG_UI_SUBMIT.py

## Power BI Dashboard
1. Open the Power BI file in the /ui folder using Power BI Desktop.
2. Configure the data source connections to point to the PostgreSQL database.

## Additional Notes
1. Make sure to update configuration files and connection strings as needed.
2. Provide necessary permissions to the database and Power BI users.

## Contributors
1. Manisha Ravindra Rao
2. Shruti Navale
3. Inderpreet Singh
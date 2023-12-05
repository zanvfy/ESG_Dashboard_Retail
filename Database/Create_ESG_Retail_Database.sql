
CREATE TABLE StoreDetails (
   Retail_Store_Id INT PRIMARY KEY,
   Retail_Store_Address VARCHAR(50),
   Retail_Store_City VARCHAR(10),
  Retail_Store_PostalCode VARCHAR(10),
  Retail_Store_OwnerName VARCHAR(25),
  Retail_Store_ContactNo VARCHAR(15),
  Retail_Store_EmailId VARCHAR(25)
);

CREATE TABLE EnergyConsumption (
    retail_store_id INT,
    Date_Generated Timestamp,
    Date_Entered Timestamp,
    Data_Load_Type VARCHAR(25),
    light_consumption DECIMAL(7,2),
    light_consumption_units VARCHAR(5),
    temp_outside DECIMAL(7,2),
    temp_outside_units VARCHAR(5),
    temp_inside DECIMAL(7,2),
    temp_inside_units VARCHAR(5),
    refridgerator_usage DECIMAL (7,2),
    refridgerator_usage_units VARCHAR(5),
    FOREIGN KEY (retail_store_id) REFERENCES StoreDetails(Retail_Store_Id)
);

CREATE TABLE WasteManagement (
   Retail_Store_Id INT,
   DATE_Generated Timestamp,
   DATE_Entered Timestamp,
   Data_Load_Type VARCHAR(25),
   Food_Wastage DECIMAL(7, 2),
   Food_Wastage_Units VARCHAR(5),
   Plastic_Wastage DECIMAL(7, 2),
   Units_Plastic_Units VARCHAR(5),
   Paper_Wastage DECIMAL(7, 2),
   Paper_Waste_Units VARCHAR(5),
   FOREIGN KEY (Retail_Store_Id) REFERENCES StoreDetails(Retail_Store_Id)
);

CREATE TABLE FuelConsumption (
   Retail_Store_Id INT,
   DATE_Generated Timestamp,
   DATE_Entered Timestamp,
   Data_Load_Type VARCHAR(25),
   Gasoline_Consumed DECIMAL(7, 2),
   Gasoline_Consumed_Units VARCHAR(5),
   Diesel_Consumed DECIMAL(7, 2),
   Diesel_Consumed_Units VARCHAR(5),
   Electric_Consumed DECIMAL(7, 2),
   Electric_Consumed_Units VARCHAR(5),
   FOREIGN KEY (Retail_Store_Id) REFERENCES StoreDetails(Retail_Store_Id)
);

CREATE TABLE WaterConsumption (
   Retail_Store_Id INT,
   DATE_Generated Timestamp,
   DATE_Entered Timestamp,        
   Data_Load_Type VARCHAR(25),
   Drinking_Water_Consumption DECIMAL(7, 2),
   Drinking_Water_Consumption_Units VARCHAR(5),
   Washroom_Water_Consumption DECIMAL(7, 2),
   Washroom_Water_Consumption_Unit VARCHAR(5),
   Other_Purpose_Consumption DECIMAL(7, 2),
   Other_Purpose_Consumption_Unit VARCHAR(5),
   FOREIGN KEY (Retail_Store_Id) REFERENCES StoreDetails(Retail_Store_Id)
);


CREATE TABLE users
(

    id integer NOT NULL,
    username character varying(50) NOT NULL,
    password_hash character varying(60) NOT NULL,
    CONSTRAINT users_pkey PRIMARY KEY (id),
    CONSTRAINT users_username_key UNIQUE (username)
);
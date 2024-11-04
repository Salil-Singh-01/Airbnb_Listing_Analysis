import pandas as pd
import numpy as np
from dotenv import load_dotenv
import os
import logging
import mysql.connector
from sqlalchemy import create_engine
from mysql.connector import Error
from oauth2client.service_account import ServiceAccountCredentials
from pydrive.auth import GoogleAuth
from pydrive.drive import GoogleDrive
from io import StringIO

# Load environment variables from .env file
load_dotenv()

logger = logging.getLogger()
logging.basicConfig(filename="airbnb.log",format='%(asctime)s - %(levelname)s - %(name)s - %(message)s',level=logging.DEBUG)

logger.info("Program start")

scope = ["https://spreadsheets.google.com/feeds",'https://www.googleapis.com/auth/drive']

## Get environment variables
cred_filename = os.getenv("CRED_FILENAME")
folder_id = os.getenv("FOLDER_ID")  # Add the folder ID where the CSV files are stored
# Connection parameters
host = os.getenv("HOST")  # Change if you're connecting remotely
user = os.getenv("USER")  # Your MySQL username
password = os.getenv("PASSWORD")  # Your MySQL password
database = os.getenv("DATABASE")  # The database name you want to create

# Authenticate and create the PyDrive client
def authenticate_gdrive(scope, cred_file):
    cred = ServiceAccountCredentials.from_json_keyfile_name(cred_file, scope)
    gauth = GoogleAuth()
    gauth.credentials = cred
    drive = GoogleDrive(gauth)
    logger.info("Succesfully connected to Google Drive")
    return drive

# Function to read CSV file content from Google Drive into a Pandas DataFrame
def read_csv_from_drive(folder_id, drive):
    # List all files in the folder
    file_list = drive.ListFile({'q': f"'{folder_id}' in parents and trashed=false"}).GetList()
    filenames = [file["title"] for file in file_list]
    logger.info(f"Found the following files within the drive folder:\n{filenames}")
    
    final_df = pd.DataFrame()
    for file in file_list:
        # Get the file's download URL
        test_file = drive.CreateFile({'id': file['id']})
        file_content = test_file.GetContentString()  # Get the file content as string, not downloaded to local, rather stored as a local variable object
        df = pd.read_csv(StringIO(file_content))  # Read the content into a Pandas DataFrame
        df["City"] = file["title"].split("_")[0]
        df["day_flag"] = file["title"].split("_")[1].split(".")[0]
        
        logger.info(f"Successfully read the file {file["title"]}")
        
        # Apply data cleaning steps
        columns_to_drop = ['Unnamed: 0', 'attr_index', 'attr_index_norm', 'rest_index_norm', 'rest_index']
        df.drop(columns=[col for col in columns_to_drop if col in df.columns], inplace=True)

        df.rename(columns={'realsum': 'Price', 'dist': 'city_cntr_dist', 'multi': 'multi_rooms', 'biz': 'business_purpose'}, inplace=True)

        df.drop_duplicates(inplace=True)

        if 'multi_rooms' in df.columns:
            df['multi_rooms'] = df['multi_rooms'].astype(bool)
        if 'business_purpose' in df.columns:
            df['business_purpose'] = df['business_purpose'].astype(bool)

        # Concatenate dataframes
        if final_df.empty:
            final_df = df
        else:
            final_df = pd.concat([final_df, df])
    
    logging.info("All files processed successfully.")
    return final_df

def create_connection(host_name, user_name, user_password):
    """ Create a database connection to the MySQL server """
    connection = None
    try:
        connection = mysql.connector.connect(
            host=host_name,
            user=user_name,
            password=user_password
        )
        logger.info("Connection to MySQL DB successful")
    except Error as e:
        logger.error(f"The error '{e}' occurred")
    return connection

def create_database(connection, db_name):
    """ Create a new database """
    cursor = connection.cursor()
    try:
        cursor.execute(f"CREATE DATABASE IF NOT EXISTS {db_name}")
        logger.info(f"Database '{db_name}' created successfully")
    except Error as e:
        logger.error(f"The error '{e}' occurred")

def create_table(connection, db_name):
    """ Create a new table in the specified database """
    cursor = connection.cursor()
    cursor.execute(f"USE {db_name}")  # Switch to the newly created database
    create_table_query = """
    CREATE TABLE IF NOT EXISTS airbnb_eu (
        id INT AUTO_INCREMENT PRIMARY KEY,
        Price DOUBLE,
        room_type VARCHAR(20),
        room_shared BOOLEAN,
        room_private BOOLEAN,
        person_capacity INTEGER,
        host_is_superhost BOOLEAN,
        multi_rooms BOOLEAN,
        business_purpose BOOLEAN,
        cleanliness_rating NUMERIC,
        guest_satisfaction_overall NUMERIC,
        bedrooms NUMERIC,
        city_cntr_dist NUMERIC,
        metro_dist NUMERIC,
        lng NUMERIC,
        lat NUMERIC,
        city VARCHAR(100) NOT NULL,
        day_flag VARCHAR(100) NOT NULL
    )
    """
    try:
        cursor.execute(create_table_query)
        logger.info("Table 'airbnb_eu' created successfully")
    except Error as e:
        logger.error(f"The error '{e}' occurred")

## Driver Codes    
# Authenticate and get the Google Drive client
drive = authenticate_gdrive(scope, cred_filename)

output_df = read_csv_from_drive(folder_id, drive)

# Print the first few rows of the DataFrame
logger.info(f"Merged data from different cities: \n{output_df.head()}")

# Create connection
conn = create_connection(host, user, password)

if conn:
    # Create a new database
    create_database(conn, database)

    # Create a new table in the database
    create_table(conn, database)
    
    # Close the connection
    conn.close()

try:
    # Create the SQLAlchemy engine
    engine = create_engine(f"mysql+pymysql://{user}:{password}@{host}/{database}")

    # Insert DataFrame into MySQL table
    output_df.to_sql('airbnb_eu', con=engine, if_exists='replace', index=False)

    logger.info("Successfully wrote the data to SQL table")
    
except Error as e:
    logger.error(f"Error while writing data to Sql\n{e}")

logger.info("End of script execution")

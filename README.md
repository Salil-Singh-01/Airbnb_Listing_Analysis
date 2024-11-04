# EU_Airbnb_price_analysis

![Airbnb Dashboard](./images/Performane&Trends.png)

## Project Overview
This project focuses on analyzing Airbnb price trends using data sourced from Kaggle. The entire workflow includes data acquisition, processing, storing, and visualization using various tools such as Google Drive, Python, MySQL, and Power BI. The outcome is an insightful dashboard for visualizing Airbnb pricing trends.

## Data Source
The dataset was obtained from [Kaggle](https://www.kaggle.com/datasets/thedevastator/airbnb-prices-in-european-cities) and contains key information about Airbnb listings, including prices, locations, and additional features.

## Project Workflow
1. **Data Acquisition**: 
   - The dataset was downloaded from Kaggle and uploaded to Google Drive for easy access.
   
2. **Data Processing in Python**:
   - Python was used to read data from Google Drive using the `pydrive` and `pandas` libraries.
   - Data cleaning and preprocessing steps such as handling missing values, converting data types, and filtering relevant records were performed.

3. **Database Connection (MySQL)**:
   - A connection was established with a local MySQL server using `mysql.connector`. A database and a table was created from the python file using the same connection.
   - The cleaned data was then transferred to a MySQL server using `sqlalchemy` for further analysis and storage.

4. **Visualization with Power BI**:
   - The processed data from MySQL was connected to Power BI.
   - A dashboard was created to visualize various trends, including price distributions, location-based analysis, and seasonal pricing trends.

## Technologies Used
- **Kaggle**: Source of the dataset.
- **Google Drive**: Cloud storage for dataset.
- **Pandas**: Data processing and cleaning.
- **MySQL**: Database for storing and analyzing data.
- **Power BI**: Visualization tool for creating an interactive dashboard.



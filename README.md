
# Strategic Insight for Airbnb Listings

### Analyzing Key Metrics for Airbnb's Performance and Growth

---

## Table of Contents
1. [Project Overview](#project-overview)
2. [Data Source](#data-source)
3. [Project Workflow](#project-workflow)
4. [Features and Functionality](#features-and-functionality)
5. [Technologies Used](#technologies-used)
6. [Usage](#usage)
7. [Contributing](#contributing)
8. [License](#license)
9. [Acknowledgments](#acknowledgments)

---

## Project Overview
This project is a group effort by five members to analyze Airbnb price trends using data sourced from Kaggle. The objective is to provide strategic insights into Airbnb listings by examining various metrics such as pricing, location trends, and host performance. The final output is a dashboard created in Power BI, which offers a comprehensive view of Airbnb's key metrics for informed decision-making.

---

## Data Source
- **Dataset**: The dataset was obtained from Kaggle, containing detailed information on Airbnb listings, including prices, locations, room types, host details, and additional listing features.

---

## Project Workflow
### 1. Data Acquisition
- The dataset was downloaded from Kaggle and stored in Google Drive for accessible cloud storage.

### 2. Data Processing in Python
- **Python Libraries Used**: `pandas`, `pydrive`.
- Performed data cleaning, including handling missing values, converting data types, and filtering relevant records.

### 3. Database Connection (MySQL)
- Established a connection to a local MySQL server using `mysql.connector` and `sqlalchemy`.
- Created a database and table to store the cleaned data, facilitating analysis and efficient data management.

### 4. Visualization with Power BI
- Connected the processed data from MySQL to Power BI.
- Designed an interactive dashboard to display key insights such as:
  - Price distributions
  - Room type comparisons
  - Location-based analysis
  - Superhost versus host metrics
  - Business booking insights by city
---

## Features and Functionality
- **Dynamic City Selection**: Analyze data for various cities (e.g., Amsterdam, Athens, London) to understand local Airbnb trends.
- **Key Metrics Display**: Metrics such as average price per night, total revenue, guest satisfaction ratings, and business listing counts.
- **Visualizations**: Comprehensive visualizations including:
  - Room type distribution and price trends
  - City-specific price variations and room type availability
  - Superhost comparisons by city
  - Distribution of bookings for business purposes by city
---

## Technologies Used
- **Kaggle**: Data source.
- **Google Drive**: Cloud storage for easy data access.
- **Python (pandas, pydrive)**: For data processing and cleaning.
- **MySQL**: Database for efficient data storage and analysis.
- **Power BI**: Visualization tool for creating the dashboard.
---

## Usage
To use this project:
1. **Download the Dataset**: The dataset can be downloaded from Kaggle and stored in Google Drive.
2. **Run Python Scripts**: Use the provided Python scripts to preprocess and clean the data.
3. **Set Up MySQL Database**: Load the cleaned data into MySQL by following the instructions in the repository.
4. **Open the Power BI Dashboard**: Connect Power BI to MySQL and explore the interactive dashboard to analyze Airbnb trends.
---

### <img src="https://drive.google.com/uc?export=view&id=1AjJUHkHEUuYhcQwXpXy3kwq6cmZTXYoN" width="25" height="25" alt="Description of GIF"> Team Contribution

This project was a team effort by a group of 5 members. Each member contributed to different parts of the project, from data  cleaning to data analysis and visualization. The collaboration helped us complete the project efficiently and gain a better understanding of the LinkedIn job market.
>  Contributors are -

- [![GitHub](https://img.shields.io/badge/Alpana%20Sahu-333?logo=github&logoColor=white&labelColor=333)](https://github.com/anjanicoder)
- [![GitHub](https://img.shields.io/badge/Salil%20Singh-333?logo=github&logoColor=white&labelColor=333)](https://github.com/Salil-Singh-01)
- [![GitHub](https://img.shields.io/badge/Abdul%20Raheem-333?logo=github&logoColor=white&labelColor=333)](https://github.com/aam1rkhan)
- [![GitHub](https://img.shields.io/badge/Arpita%20Sathe-333?logo=github&logoColor=white&labelColor=333)](https://github.com/tauheed7080)
- [![GitHub](https://img.shields.io/badge/Bharat%20Nagar-333?logo=github&logoColor=white&labelColor=333)](https://github.com/Jayadavv)
## Acknowledgments
We would like to thank:
- **Kaggle** for the dataset
- **Microsoft Power BI** for the visualization platform
- Our group members for their collaboration and effort in making this project possible



















<!--
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
-->


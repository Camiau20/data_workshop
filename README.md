# Workshop 001: Python Data Engineer

## Overview
This Jupyter notebook contains solutions to specified requirements along with diagrams and visualizations. The workshop demonstrates the usage of SQLAlchemy as an ORM connected to MySQL and the creation of visualizations using Matplotlib's pyplot. The focus is on data engineering tasks, including data loading, transformation, and visualization.

## Table of Contents
- [Requirements](#requirements)
- [Setup](#setup)
- [Data Loading](#data-loading)
- [Visualizations](#visualizations)
  - [1. Hires by Technology (Pie Chart)](#1-hires-by-technology-pie-chart)
  - [2. Hires by Year (Horizontal Bar Chart)](#2-hires-by-year-horizontal-bar-chart)
  - [3. Hires by Seniority (Bar Chart)](#3-hires-by-seniority-bar-chart)
  - [4. Hires by Country Over Years (Multiline Chart)](#4-hires-by-country-over-years-multiline-chart)

## Requirements <a name="requirements"></a>
- Python 3.x
- SQLAlchemy
- Matplotlib
- MySQL database
- CSV data file ("candidates.csv")
- JSON credentials file ("credentials.json") with this format:
  ```
  {
    "user": "your_username",
    "password": "your_password",
    "server": "your_server_address",
    "db": "your_database_name"
  }
  ``` 

## Setup <a name="setup"></a>
Install the required libraries using the following commands:
```python
pip install sqlalchemy matplotlib pandas
```
In this case the project is in a upyter notebook, an installation of jupyter is needed:

```python
pip install jupyterlab
```
Then, you have to run the lab with the command:
```python
jupyter lab
```
After this steps, you have to clon this repository and run the jupyter notebook workshop.ipynb.

## Data Loading <a name="data-loading"></a>
- Establish a connection to the MySQL database using SQLAlchemy.
- Create a "candidates" table with relevant columns using the declarative Base class.
- Load data from the CSV file ("candidates.csv") into the database and calculate the "hired" column.

## Visualizations <a name="visualizations"></a>
1. Hires by Technology (Pie Chart) <a name="1-hires-by-technology-pie-chart"></a>
  - Query the database to get the count of hires by technology.
  - Create a pie chart to visualize the distribution of hires across different technologies ([data_workshop/workshop.ipynb/cell 3](https://github.com/Camiau20/data_workshop/blob/main/workshop.ipynb)).
2. Hires by Year (Horizontal Bar Chart) <a name="2-hires-by-year-horizontal-bar-chart"></a>
  - Query the database to get the count of hires by year.
  - Create a horizontal bar chart to display the number of hires for each year ([data_workshop/workshop.ipynb/cell 4](https://github.com/Camiau20/data_workshop/blob/main/workshop.ipynb)).
3. Hires by Seniority (Bar Chart) <a name="3-hires-by-seniority-bar-chart"></a>
  - Query the database to get the count of hires by seniority level.
  - Create a bar chart to visualize the number of hires for each seniority level ([data_workshop/workshop.ipynb/cell 5](https://github.com/Camiau20/data_workshop/blob/main/workshop.ipynb)).
4. Hires by Country Over Years (Multiline Chart) <a name="4-hires-by-country-over-years-multiline-chart"></a>
  - Query the database to get the count of hires by country over different years.
  - Create a multiline chart to show the trend of hires for selected countries over the years ([data_workshop/workshop.ipynb/cell 6](https://github.com/Camiau20/data_workshop/blob/main/workshop.ipynb)).


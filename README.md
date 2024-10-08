# Django Data Analysis 

## Overview
This web application allows users to upload CSV files, perform data analysis using pandas and matplotlib, and visualize the results on the web interface.

## Setup Instructions
1. Clone the repository:
   ```bash
   git clone https://github.com/Shirodkar-Shubham-GitHub/Django_Data_Analysis.git
    
2. Navigate to the project directory:
   ```bash
   cd DDA
3. Create a virtual environment:
   ```bash
   python -m venv venv
   
4. Activate the virtual environment:
   ```bash
   venv\Scripts\activate

5. Install dependencies:
   ```bash
   pip install -r requirements.txt

6. Run migrations:
    ```bash
    python manage.py migrate

7. Start the development server:
    ```bash
    python manage.py runserver

8. Open your web browser and navigate to http://localhost:8000 to access the web application.

## Project Structure

##### django_data_analysis: Django project configuration.
##### data_analysis_app: Django app containing the main functionality.
##### templates: HTML templates for rendering the user interface.

## Features

##### File Upload: Users can upload CSV files via a form.
##### Data Processing: Uploaded CSV files are processed using pandas to perform basic data analysis tasks such as displaying the first few rows of the data, calculating summary statistics (mean, median, standard deviation), and handling missing values.
##### Data Visualization: Basic plots (e.g., histograms) are generated using matplotlib and displayed on the web page.
##### User Interface: Simple and user-friendly interface created using Django templates to display data analysis results and visualizations in a clear and organized manner.

## Technologies Used

#### Django
#### pandas
#### matplotlib

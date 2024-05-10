import os
import pandas as pd
from sqlalchemy import create_engine

# Function to test the database connection
def test_database_connection(database_url):
    try:
        engine = create_engine(database_url)
        with engine.connect():
            print("Database connection successful")
        return True
    except Exception as e:
        print("Error connecting to database:", e)
        return False
    
def get_table_name(folder_name,isSummary):
    folder_name = os.path.basename(folder_name)
    if(folder_name == 'cities'):
        if(isSummary):
            return "CitiesTableData"
        return "CitiesChartData"
    
    if(folder_name == 'content_type'):
        if(isSummary):
            return "ContentTypeTableData"
        return "ContentTypeChartData"
    
    if(folder_name == 'device_type'):
        if(isSummary):
            return "DeviceTypeTableData"
        return "DeviceTypeChartData"
    
    if(folder_name == 'geography'):
        if(isSummary):
            return "GeographyTableData"
        return "GeograpyChartData"
    
    if(folder_name == 'new_returning_viewers'):
        if(isSummary):
            return "NewAndReturningViewersTableData"
        return "NewAndReturningViewersChartData"
    
    if(folder_name == 'operating_system'):
        if(isSummary):
            return "OperatingSystemTableData"
        return "OperatingSystemChartData"
    
    if(folder_name == 'sharing_service'):
        if(isSummary):
            return "SharingServiceTableData"
        return "SharingServiceChartData"
    
    if(folder_name == 'subscription_source'):
        if(isSummary):
            return "SubsciptionSourceTableData"
        return "SubsciptionSourceChartData"
    
    if(folder_name == 'subscription_status'):
        if(isSummary):
            return "SubsciptionStatusTableData"
        return "SubsciptionStatusChartData"
    
    if(folder_name == 'subtitles_cc'):
        if(isSummary):
            return "SubtitleAndCcTableData"
        return "SubtitleAndCcChartData"
    
    if(folder_name == 'traffic_source'):
        if(isSummary):
            return "TrafficSourceTableData"
        return "TrafficSourceChartData"
    
    if(folder_name == 'viewer_age'):
        if(isSummary):
            return "ViewerAgeTable"
        return ""
    if(folder_name == 'viewer_gender'):
        if(isSummary):
            return "ViewerGenderTable"
        return ""
    if(folder_name == 'viewership_by_date'):
        if(isSummary):
            return "TotalViewPerDayf"
        return ""

# Function to load CSV data into PostgreSQL tables
def load_csv_data(engine, data_folder):
    try:
        print(data_folder)
        for folder_name in os.listdir(data_folder):
            print(folder_name)
            folder_path = os.path.join(data_folder, folder_name)
            if os.path.isdir(folder_path):
                print(folder_path)
                summary_csv = None
                details_csv = None

                for filename in os.listdir(folder_path):
                    print(f'file name is: {filename}')

                    if "Table" in filename:
                        summary_csv = os.path.join(folder_path, filename)
                    elif "Chart" in filename:
                        details_csv = os.path.join(folder_path, filename)
                
                table_name = 'xt'
                if summary_csv:
                    table_name = get_table_name(folder_name,True)
                    if(table_name and len(table_name) > 0):
                        header_df = pd.read_csv(summary_csv)
                        print(f'Loading {table_name} data to sql ...')
                        header_df.to_sql(table_name, engine, if_exists='replace', index=False)
                else:
                    print(f'summary not found for {table_name}')

                if details_csv:
                    table_name = get_table_name(folder_name,False)
                    if(table_name and len(table_name) > 0):
                        details_df = pd.read_csv(details_csv)
                        print(f'Loading {table_name} data to sql ...')
                        details_df.to_sql(table_name, engine, if_exists='replace', index=False)
                else:
                    print(f'summary not found for {table_name}')
                
    except Exception as e:
        print("Error loading CSV data:", e)

if __name__ == "__main__":
    # Get database URL from environment variable
    database_url = os.getenv("DATABASE_URL")
    if database_url:
        # Test database connection
        if test_database_connection(database_url):
            # Change this to the actual path of your data folder
            data_folder = '/app/data'
            
            # Load CSV data into PostgreSQL tables
            engine = create_engine(database_url)
            load_csv_data(engine, data_folder)
    else:
        print("DATABASE_URL environment variable not set. Please set it before running the script.")


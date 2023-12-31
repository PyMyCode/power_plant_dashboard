import sqlite3
import os.path
import pandas as pd

class Database:

    def __init__(self) -> None:

        # creating database object
        self.db = self._connecting()

        # creating cursor object
        self.cur = self.db.cursor()
    
    def _connecting(self):
        BASE_DIR = os.getcwd()
        db_path = os.path.join(BASE_DIR, r"db.db")

        try:
            db = sqlite3.connect(db_path, check_same_thread=False)
            print("connected!")
            return db
        except sqlite3.Error as e:
            print(e)

    def _country_data(self, _country): 
        
        #TODO: Creating a flexible sql string to incorporate all conditions
        sql_query = """
                SELECT 
                name, capacity_mw, primary_fuel, owner, source, latitude, longitude
                FROM
                global_power_plant_database
                WHERE
                country_long like ?
                ORDER BY
                capacity_mw DESC
                     """
        parameters = (_country, )
        
        _df = pd.read_sql(sql_query, self.db, params=parameters)

        print(f"\n df shape = {_df.shape}")

        return _df
    
    def _country_list(self): 
        
        sql_query = """
                SELECT DISTINCT(country_long) AS country_list 
                FROM global_power_plant_database
                     """
        
        _df = pd.read_sql(sql_query, self.db)

        return _df
    
    def _primary_fuel_list(self): 
        
        sql_query = """
                SELECT DISTINCT(primary_fuel) AS primary_fuel_list 
                FROM global_power_plant_database
                     """
        
        _df = pd.read_sql(sql_query, self.db)

        return _df
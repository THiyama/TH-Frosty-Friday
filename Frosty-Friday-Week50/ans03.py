import snowflake.snowpark as snowpark
from snowflake.snowpark.functions import col

def main(session: snowpark.Session): 
    table_name = "SANDBOX.PUBLIC.F_F_50"
    dataframe = session.sql(f"select * from {table_name} where last_name = 'Deery'")    
    return dataframe
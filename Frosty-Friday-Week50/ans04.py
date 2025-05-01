import snowflake.snowpark as snowpark
from snowflake.snowpark.functions import col

def main(session: snowpark.Session): 
    table_name = "SANDBOX.PUBLIC.F_F_50"
    df = session.table(table_name).filter(col("last_name")=="Deery")  
    return df
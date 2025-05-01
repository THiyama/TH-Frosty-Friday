import modin.pandas as pd
import snowflake.snowpark.modin.plugin
import snowflake.snowpark as snowpark
from snowflake.snowpark.functions import col

def main(session: snowpark.Session):
    table_name = "SANDBOX.PUBLIC.F_F_50"
    df = pd.read_snowflake(table_name)
    
    result = df[df["LAST_NAME"] == "Deery"]
    return result.to_snowpark()
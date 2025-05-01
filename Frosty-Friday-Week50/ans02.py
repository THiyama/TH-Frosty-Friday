import snowflake.snowpark as snowpark
from snowflake.snowpark.functions import col

def main(session: snowpark.Session):
    table_name = "SANDBOX.PUBLIC.F_F_50"
    df = session.table(table_name).to_pandas()
    
    result = df[df["LAST_NAME"] == "Deery"]
    return session.create_dataframe(result)
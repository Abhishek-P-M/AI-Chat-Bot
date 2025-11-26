import os
import shutil
import sqlite3

import pandas as pd
import requests

# --- DATABASE SETUP ---
local_file = "food_delivery.sqlite"
backup_file = "food_delivery.backup.sqlite"
overwrite = False

# --- FUNCTION TO RESET AND UPDATE DATES ---
def update_delivery_dates(file):
    # Restore backup
    shutil.copy(backup_file, file)
    conn = sqlite3.connect(file)
    
    # Get all tables
    tables = pd.read_sql("SELECT name FROM sqlite_master WHERE type='table';", conn).name.tolist()
    tdf = {t: pd.read_sql(f"SELECT * FROM {t}", conn) for t in tables}

    # Example: adjust order_date to current time (if Orders table exists)
    if "Orders" in tdf:
        example_time = pd.to_datetime(
            tdf["Orders"]["order_date"].replace("\\N", pd.NaT)
        ).max()
        current_time = pd.to_datetime("now").tz_localize(example_time.tz)
        time_diff = current_time - example_time

        tdf["Orders"]["order_date"] = (
            pd.to_datetime(tdf["Orders"]["order_date"].replace("\\N", pd.NaT), utc=True)
            + time_diff
        )

    # Save all tables back
    for table_name, df in tdf.items():
        df.to_sql(table_name, conn, if_exists="replace", index=False)

    conn.commit()
    conn.close()
    return file

# --- RUN UPDATE ---
db = update_delivery_dates(local_file)

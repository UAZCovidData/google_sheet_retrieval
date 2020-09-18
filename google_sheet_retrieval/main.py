import pandas as pd
from urllib.error import URLError

sheet_id = "1TCixO6WXSW0jKYBdAKXaXXvEk_DVjqFIAGNDfqA54_M"
gid = 880188181

url = f"https://docs.google.com/spreadsheets/d/{sheet_id}/export?format=csv&gid={gid}"


def run():

    outfile = 'uaz_covid_testing_data.csv'
    try:
        df = pd.read_csv(url)

        print(f"Writing : {outfile}")
        df.to_csv(outfile, index=False)
    except URLError:
        print("Unable to retrieve data from URL !")

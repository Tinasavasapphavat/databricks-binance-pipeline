import pandas as pd
import yaml

class PROCESS:
    def __init__(self,symbol,raw_path):
        self.symbol : str = symbol
        with open("config/schema.yaml","r") as f:
            config = yaml.safe_load(f)
        self.dtypes = config['data']['dtypes']
        self.columns = config['data']['columns']
        self.df : pd.DataFrame= pd.read_csv(raw_path)

    def cast_dtypes(self):
        for col , dt in self.dtypes.items():
            self.df[col] = self.df[col].astype(dt)
        print("CASTING DATA TYPE SUCCEEDED")
        
    def rename_columns(self):
        self.df = self.df.rename(columns = self.columns)
        print("RENAME COLUMNS SUCCEEDED")

    def save_tmp(self,transform_path):
        try:
            self.df.to_csv(transform_path,index=False)
            print("SAVE TRANSFORMED DATA SUCCEEDED")
        except Exception as e:
            print("SAVE RAW DATA FAILED")
            raise e
    

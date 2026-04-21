from src.processing.process import PROCESS
import yaml 


symbol = "BTCUSDT"
with open('config/config.yaml','r') as f:
    config = yaml.safe_load(f)

raw_path = config['pipelines'][symbol]['raw_path']
transform_path = config['pipelines'][symbol]['transform_path']

def main():
    process = PROCESS(symbol=symbol,raw_path=raw_path)
    process.cast_dtypes()
    process.rename_columns()
    process.save_tmp(transform_path=transform_path)


if __name__ == "__main__":
    print(f"START TRANSFORM: {symbol}")
    main()
    print("TRANSFORM SUCCEEDED")

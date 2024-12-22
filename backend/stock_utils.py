from typing import List, Dict
import yfinance as yf

def get_asset_current_price(ticker: str) -> float:
    """Returns an asset current given a TICKER
    Example of a ticker: ITSA4.SA
    """
    stock_info = yf.Ticker(ticker).info

    return stock_info.get("currentPrice")

def get_current_price_for_a_list_of_assets(assets: List[str]) -> List[Dict[str, int]]:
    """
    Returns a list of prices given a list of assets
    Example ["ITSA4.SA", "HGLG11.SA", "HASH11.SA"]
    """
    query = " ".join(assets)
    data = yf.Tickers(query)
    current_prices = [{tag: ticker.info.get("currentPrice")} for tag, ticker in data.tickers.items()]

    return current_prices

if __name__ == "__main__":
    # data = get_asset_price("ITSA4.SA")
    price = get_asset_current_price("HGLG11.SA")
    prcices = get_current_price_for_a_list_of_assets(["IVVB11.SA", "HASH11.SA", "ITSA4.SA"])
    print(price)

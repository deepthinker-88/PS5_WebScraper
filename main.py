from src.ps5_console_purchase import purchase_ps5
from src.ps5_web_scraper import check_for_ps5


if __name__ == "__main__":
    print("running main.py")
    is_in_stock = check_for_ps5()
    print(f"item in stock = {is_in_stock}")
    if is_in_stock:
        print("attempting to purchase")
        purchase_ps5()

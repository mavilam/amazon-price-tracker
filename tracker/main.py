import csv
import argparse

from tracker import Tracker
from communication import Communication
from settings import CSV_ITEM_FILE
import item_management


def tracker_instance(url, target_price):
    item = Tracker(url, target_price)
    comms = Communication(item.title.strip(), url, item.price, '€' + target_price)
    if item.int_price <= item.target_price:
        print(f'{item.price} < {item.target_price}\n')
        comms.sendTelegram()
    elif item.int_price >= item.target_price:
        print(f'{item.price} > {item.target_price}\n')
    else:
        print(f'{item.price} > {item.target_price} - Item is out of stock\n')

def main_loop():
    try:
        with open(CSV_ITEM_FILE, 'r') as csv_file:
            csv_reader = csv.reader(csv_file)
            for line in csv_reader:
                tracker_instance(line[0], line[1])
    except Exception as e:
        print(e)
    

if __name__ == "__main__":
    parser = argparse.ArgumentParser("Track the price of your desired amazon product")
    parser.add_argument('-a', '--add', type=str, nargs=2, help="Add a new product: --add [url] [desired price]")
    args = parser.parse_args()
    if args.add and len(args.add) > 1:
        item_management.add_item(args.add[0], args.add[1])
    else:
        main_loop()

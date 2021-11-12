import re

from settings import CSV_ITEM_FILE

def add_item(url, target_price):
  simple_url = re.findall("\/dp\/B0.*\/", url)[0]
  try:
    with open(CSV_ITEM_FILE, 'a') as f:
      f.write(f'https://www.amazon.es{simple_url},{float(target_price)}\n')
  except Exception:
    print('Not a valid target price! Do not use a $ sign')
    exit()
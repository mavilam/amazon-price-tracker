import re

from settings import CSV_ITEM_FILE

def add_item(url, target_price):
  simple_url = re.findall("\/dp\/B0.*\/", url)[0]
  try:
    with open(CSV_ITEM_FILE, 'a') as f:
      line = f'https://www.amazon.es{simple_url},{float(target_price)}\n'
      f.write(line)
      print(f'Added {line}')
  except Exception as e:
    print(e, "There was an error adding the product.")
    exit()
import json
from collections import Counter
from datetime import datetime
from typing import Callable, Mapping, Sequence
from urllib.request import urlopen


# 1
def swap_bytes(x):
    return  x >> 8 | (x & 0xFF) << 8


# 2
def number_basket(N, w, d, P):
    """number of basket with counterfeit coins"""
    coins_count = (N - 1) * N / 2
    coins_weight = coins_count * w
    return int((coins_weight - P) / d)


# 3
# pip install requests
# import requests
# body = requests.get("https://www.python.org").text

with urlopen("https://www.python.org") as response:
    body = response.read().decode(response.headers.get_content_charset())

char_count = dict(Counter(body).most_common())

with open("readme.md", "w") as f:
    f.write(f"```json\n{json.dumps(char_count, indent=4, ensure_ascii=False)}\n```") 


# 4
def update_nested_key(adict: Mapping | Sequence, key: str, call: Callable) -> None:
  stack = [adict]
  while stack:
    d = stack.pop()
    if isinstance(d, list):
        for item in d:
            if isinstance(item, (dict, list)):
                stack.append(item)
    elif isinstance(d, dict):
        if key in d:
            d[key] = call(d[key])
        for k, v in d.items():
            if isinstance(v, (dict, list)):
                stack.append(v)


with open("some.json") as f:
   some_dict = json.load(f)

update_nested_key(some_dict, "updated", lambda _: datetime.today().isoformat())

with open("updated.json", "w") as f:
   json.dump(some_dict, f, indent=4)
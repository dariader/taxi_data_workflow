import asyncio
import os
month = 0
url = f"https://github.com/DataTalksClub/nyc-tlc-data/releases/download/fhv/"
csv_dir = f"fhv/"

"""
though it does not perform better, that simple for loop, it is interesting to implement loading of files via async
"""
async def load(month):
    suffix = f"fhv_tripdata_2019-{month:02}.csv.gz"
    url_file = url + suffix
    csv_name = csv_dir + suffix
    print(suffix)
    return os.system(f"wget {url_file} -O {csv_name}")


async def foo():
    items = range(1, 13)
    tasks = [load(item) for item in items]
    new_items = await asyncio.gather(*tasks)
    return new_items

if __name__ == '__main__':
    results = asyncio.run(foo())
    print(results)

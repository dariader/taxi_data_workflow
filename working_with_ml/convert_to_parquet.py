import asyncio

import pyarrow.csv as pv
import pyarrow.parquet as pq
import glob
from functools import wraps
import time


def timeit(func):
    @wraps(func)
    def timeit_wrapper(*args, **kwargs):
        start_time = time.perf_counter()
        result = func(*args, **kwargs)
        end_time = time.perf_counter()
        total_time = end_time - start_time
        print(f'Function {func.__name__}{args} {kwargs} Took {total_time:.4f} seconds')
        return result
    return timeit_wrapper


@timeit
def simple_convert():
    for filename in glob.glob("fhv/*.csv.gz"):
        print(filename)
        table = pv.read_csv(filename)
        pq.write_table(table, filename.replace('csv.gz', 'parquet'))

@timeit
async def do_convert(filename):
    print(filename)
    table = pv.read_csv(filename)
    return pq.write_table(table, filename.replace('csv.gz', 'parquet'))


@timeit
async def async_convert():
    items = glob.glob("fhv/*.csv.gz")
    tasks = [do_convert(item) for item in items]
    new_items = await asyncio.gather(*tasks)
    return new_items


asyncio.run(async_convert())
#simple_convert()
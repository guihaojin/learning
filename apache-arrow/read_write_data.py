import numpy as np
import pyarrow as pa

arr = pa.array(np.arange(100))

print(f"{arr[0]} .. {arr[-1]}")

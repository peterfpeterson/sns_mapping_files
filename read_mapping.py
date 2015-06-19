#!/usr/bin/env python
from __future__ import (absolute_import, division, print_function,
                        unicode_literals)

import numpy as np
import sys

if len(sys.argv) != 2:
    print("Usage: %s <mappingfile>" % sys.argv[0])
    sys.exit(-1)

filename = sys.argv[1]

handle = open(filename, 'rb') # binary read
data = np.fromfile(handle, dtype=np.int32)

for (dasid,detid) in enumerate(data):
    print(dasid, detid)

import matplotlib.pyplot as plt
plt.plot(data)
plt.show()

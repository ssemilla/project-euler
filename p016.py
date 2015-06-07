#!/usr/bin/env python

# The easy way
print reduce(lambda x, y: x + int(y), str(2**1000), 0)

#!/usr/bin/env python

# optimize this next time to use squaring technique

power_2 = 1
for n in xrange(7830457):
    power_2 = power_2 * 2
    if power_2 > 9999999999:
        power_2 = int(str(power_2)[-10:])

print str(power_2*28433+1)[-10:]

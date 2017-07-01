'''
 * Copyright (c) 2017, Autonomous Networks Research Group. All rights reserved.
 *     contributor: Jiatong Wang, Bhaskar Krishnamachari
 *     Read license file in main directory for more details
'''

import os
import site


try:
    import psutil
except ImportError:
    print "no lib psutil"
    import pip
    cmd = "sudo pip2 install psutil"
    print "Requests package is missing\nPlease enter root password to install required package"
    os.system(cmd)
    reload(site)


try:
    import flask
except ImportError:
    print "no lib flask"
    import pip
    cmd = "sudo pip2 install flask"
    print "Requests package is missing\nPlease enter root password to install required package"
    os.system(cmd)
    reload(site)

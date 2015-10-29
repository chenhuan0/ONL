#!/usr/bin/python
############################################################
# <bsn.cl fy=2013 v=none>
#
#        Copyright 2013, 2014 BigSwitch Networks, Inc.
#
#
#
# </bsn.cl>
############################################################
#
# Platform driver for the Facebook S4000.
#
############################################################
import subprocess
from onl.platform.base import *
from onl.vendor.facebook import *

class OpenNetworkPlatformImplementation(OpenNetworkPlatformFACEBOOK):

    def model(self):
        return "Wedge"

    def platform(self):
        return "x86-64-accton-wedge-16x-r0"

    def _plat_info_dict(self):
        return {
            platinfo.LAG_COMPONENT_MAX : 24,
            platinfo.PORT_COUNT : 16,
            #platinfo.ENHANCED_HASHING : True,
            #platinfo.SYMMETRIC_HASHING : True,
            }

    def sys_init(self):
        pass

    def sys_oid_platform(self):
        # FIXME
        return ".4000.1"

if __name__ == "__main__":
    print OpenNetworkPlatformImplementation()


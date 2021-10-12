#!/usr/bin/python3
# -*- coding: utf-8 -*-


# To make a transparency window :

self.master.withdraw()
self.master.wm_attributes('-alpha', 0.8)

# otherwise :

self.master.overrideredirect(1)
self.master.call("wm", "attributes", ".", "-alpha", 0.8)
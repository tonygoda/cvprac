# Copyright (c) 2021 Arista Networks, Inc.
# Use of this source code is governed by the Apache License 2.0
# that can be found in the COPYING file.

from cvprac.cvp_client import CvpClient
import ssl
ssl._create_default_https_context = ssl._create_unverified_context
import requests.packages.urllib3
requests.packages.urllib3.disable_warnings()

# Create connection to CloudVision
clnt = CvpClient()
clnt.connect(nodes=['cvp1'], username="username",password="password")

# Get devices in a specific container
inventory = clnt.api.get_devices_in_container("Undefined")

devices = []
for netelement in inventory:
   devices.append(netelement['systemMacAddress'])

clnt.api.delete_devices(devices)

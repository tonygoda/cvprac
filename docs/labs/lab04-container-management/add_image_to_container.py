# Copyright (c) 2020 Arista Networks, Inc.
# Use of this source code is governed by the Apache License 2.0
# that can be found in the COPYING file.

from cvprac.cvp_client import CvpClient
import ssl
ssl._create_default_https_context = ssl._create_unverified_context
import requests.packages.urllib3
requests.packages.urllib3.disable_warnings()

# Create connection to CloudVision
clnt = CvpClient()
clnt.connect(['10.83.13.33'],'cvpadmin', 'arastra')

image_name = "vEOS-4.26.0.1F"
image = clnt.api.get_image_bundle_by_name(image_name)

container_name = "TP_FABRIC"
container = clnt.api.get_container_by_name(container_name)

clnt.api.apply_image_to_container(image, container)

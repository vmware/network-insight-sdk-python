# Databus Client for vRNI
Starting vRealize Network Insight (vRNI) 6.6, vRNI platform has a public API. This Python SDK provides you a setup that can spawn a client which can receive data via databus from vRNI.

This module is not supported by VMware, and comes with no warranties express or implied. Please test and validate its functionality before using in a production environment. If you have any issue please raise a github issue.
Included SDK is compatible with vRNI 6.6, 6.7, 6.8 and onwards

## Installing Python SDK [python 3.7]
Checkout repo

Then install the prerequisites with: pip install -r databus_client/requirements.txt

Get the latest docker image from databus_client/dockerImages/

1. Start docker container with the image:

   Expected arguments are:
* port - Port on which client should be brought up
* enable_telemetry - Set to true to enable telemetry
* use_mongo - set to true if data received from client should be pushed to mongo
* mongo_server_ip - mongo server ip (is not passed, default set to localhost:27017)
* https - set to true if client has to be up in https mode
* cert_file_path - pass absolute path for cert file (needed only for https client)
* key_file_path - pass absolute path for key file (needed only for https client)
* file_threshold - pass threshold size of working log file in MB. Above threshold files will be rolled over


2. Mongo cleanup:

   Execute script - databus_client/health_monitoring/on_system_mongo_cleanup.py
   
   Example: python3 databus_client/health_monitoring/on_system_mongo_cleanup.py --source sourceName --dbName DatabaseName --colName CollectionName

   * Here if no collection name is passed complete mongo cleanup will be performed. Else cleanup for only particular collection for particular source will be done 
   * If source is not provided, then cleanup will be done for complete collection


3. For using client, filters are to be configured first:

   Set filters:

   API : 

## Examples
The **examples/** directory is full of examples that use the Network Insight Python SDK and inspires you to contribute to the project.

## Contributing

The network-insight-sdk-python project team welcomes contributions from the community. If you wish to contribute code and you have not signed our contributor license agreement (CLA), our bot will update the issue when you open a Pull Request. For any questions about the CLA process, please refer to our [FAQ](https://cla.vmware.com/faq). For more detailed information, refer to [CONTRIBUTING.md](CONTRIBUTING.md).

## License
Network Insight Python SDK is licensed under GPL v2

Copyright © 2019 VMware, Inc. All Rights Reserved.

This program is free software: you can redistribute it and/or modify it under the terms of the GNU General Public License version 2, as published by the Free Software Foundation.

This program is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; without even the implied warranty of MERCHANTIBILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU General Public License version 2 for more details.

You should have received a copy of the General Public License version 2 along with this program. If not, see https://www.gnu.org/licenses/gpl-2.0.html.

The full text of the General Public License 2.0 is provided in the COPYING file. Some files may be comprised of various open source software components, each of which has its own license that is located in the source code of the respective component.”

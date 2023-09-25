# Databus Client for vRNI
Starting vRealize Network Insight (vRNI) 6.6, vRNI platform has a public API. This Python SDK provides you a setup that can spawn a client which can receive data via databus from vRNI.

This module is not supported by VMware, and comes with no warranties express or implied. Please test and validate its functionality before using in a production environment. If you have any issue please raise a github issue.
Included SDK is compatible with vRNI 6.6, 6.7, 6.8 and onwards

## Installing Python SDK [python 3.7]
Checkout repo

Then install the prerequisites with: pip install -r databus_client/requirements.txt

Get the latest docker image from "_vrni-eso.artifactory.eng.vmware.com/vrni_databus_client_"

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


 For using client, filters are to be configured first:

   Filters:
   
   |Method| URL                                                               | Description                                               |
   |-------------------------------------------------------------------|-----------------------------------------------------------|-----------|
   |POST| /filters| Create the filters, with default accept all or reject all |
   |GET| /filters| Get the configured filters                                        |
   |PUT| /filters| Update the filtres                                                |
   |DELETE| /filters| Delete the configured filter                                      |

   **Note: By default receiver will come up with accept all config, i.e., accept all incoming data**

   Subscriptions:
   While adding subscriptions to vRNI, use below endpoints

   | Receiver endpoint URL | vRNI Message group     |
-----------------------|------------------------|
   | /applications         | applications           |
   | /vms                  | vms                    |
   | /flows                | flows                  |
   | /hosts                | hosts                  |
   | /problems             | problems, intents      |
   | /metrics              | for all entity metrics |
   | /vms-metrics          | vms-metrics            |
   | /hosts-metrics        | hosts-metrics          |
   | /nics-metrics         | nics-metrics           |
   | /switchports-metrics  | switchports-metrics    |
   | /flows-metrics        | flows-metrics          |

   **To get heartbeat data: Do GET /heartbeat**



## Examples
Filter API Sample packet:

```commandline
{
    "matched_filter": "reject",
    "unmatched_filter": "accept",
    "non_metric_filter": [{
            "source": "CKRtEgdEUjNITU1P",
            "entity_type": "applications",
            "entityIds": ["13988:561:2096623162362547537", "v2"],
            "entityNames": ["n1", "n2"]
        },
        {
            "source": "CNeJARIHRDRBR1U5TQ==",
            "entity_type": "applications",
            "entityNames": ["DATABUS_APP_TEST_01"]
        }
    ],
    "metric_filter": [{
            "source": "CJWMARIHDSJHRkRYTw==",
            "entity_type": "Host",
            "metrics": ["net.usage.delta.summation.kiloBytes"],
            "entityIds": ["17941:4:3519141807154183312"]
        },
        {
            "source": "CJBOEgdSFHDdSDSFcUVT",
            "entity_type": "VirtualMachine",
            "metrics": ["cpu.usage.rate.average.percent", "three"],
            "entityIds": ["v7", "v6"]
        },
        {
            "source": "CJBadfgdSFHDddhcUVT",
            "entity_type": "Hosts",
            "metrics": ["cpu.usage.rate.average.percent"],
            "entityIds": ["10000:515:3516501221883531122", "10000:515:74840761443449837"]
        }
    ],
    "sub_metric_filter": [{
            "source": "CJBOEgdSFHDddhcUVT",
            "entity_type": "vms-metrics",
            "metrics": ["cpu.usage.rate.average.percent", "two"],
            "entityIds": ["10000:515:3516501221883531223", "10000:515:7484076144344179229"]
        },
        {
            "source": "CJBOEgdSFHDdCQUVT",
            "entity_type": "flows-metrics",
            "metrics": ["cpu.usage.rate.average.percent", "flow.totalBytes.delta.summation.bytes"],
            "entityIds": ["10000:515:3516501221883531266", "10000:515:7484076144344179859", "10000:515:1823077571592235831"]
        }
    ]
}
```
Here:
1. Source is Service Tag
2. Entity_type is the message group
3. Entity name is name of entity [Array]
4. In Metrics and sub-metrics filters:
   a. Metrics is the metric name
   b. EntityIds is the model key of entity

**Please note that filtering works based on Source/Service_tag, hence it's a mandatory parameter**


## Contributing

The network-insight-sdk-python project team welcomes contributions from the community. If you wish to contribute code and you have not signed our contributor license agreement (CLA), our bot will update the issue when you open a Pull Request. For any questions about the CLA process, please refer to our [FAQ](https://cla.vmware.com/faq). For more detailed information, refer to [CONTRIBUTING.md](CONTRIBUTING.md).

## License
Network Insight Python SDK is licensed under GPL v2

Copyright © 2019 VMware, Inc. All Rights Reserved.

This program is free software: you can redistribute it and/or modify it under the terms of the GNU General Public License version 2, as published by the Free Software Foundation.

This program is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; without even the implied warranty of MERCHANTIBILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU General Public License version 2 for more details.

You should have received a copy of the General Public License version 2 along with this program. If not, see https://www.gnu.org/licenses/gpl-2.0.html.

The full text of the General Public License 2.0 is provided in the COPYING file. Some files may be comprised of various open source software components, each of which has its own license that is located in the source code of the respective component.”

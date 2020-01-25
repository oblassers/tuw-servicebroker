# TU.it Service Broker
The TU.it Service Broker is a proof-of-concept implementation to provide a standard interface for ICT services available at Vienna University of Technology:

- [TUfiles](https://www.it.tuwien.ac.at/tufiles/)
- TUcloud
  - [TUownCloud](https://www.it.tuwien.ac.at/tuowncloud/)
  - [TUproCloud](https://www.it.tuwien.ac.at/tuprocloud/)
- [TUhost](https://www.it.tuwien.ac.at/tuhost/)

The service broker implements the [Open Service Broker API](https://www.openservicebrokerapi.org/) (OSBAPI) which has become an industry standard for delivering cloud service offerings from different providers to application platforms.

A service broker enables to:

- Fetch a catalog of available services
- (De-)Provision a service instance
- (Un-)Bind a service instance

In this example we implement [v2.13](https://github.com/openservicebrokerapi/servicebroker/blob/v2.13/spec.md) of the OSBAPI.

## Run the Service Broker
The service broker can be run in a Docker container. Therefore, please make sure you have Docker installed.

Build the Docker image:

```shell
docker build -t openservicebroker:latest .
```

Start the Docker container on port 8000:

```shell
run --name openservicebroker -d -p 8000:5000 --rm openservicebroker:latest
```

## Test the Service Broker
The service broker should now be up and running on localhost, port 8000. You can test the service broker by sending requests to its HTTP API by using any tool you seem fit. In the following we show three ways of interacting with the service broker. 

Since this is an example implementation, the service broker supports the `catalog` command which enables to fetch a catalog of services available from this service broker, but does not implement actual service provisioning or binding.

### cURL
Request the catalog of services from the service broker with cURL:

```shell
curl http://127.0.0.1:8000/v2/catalog -H "X-Broker-Api-Version: 2.13" -u "":""
```
The service broker should answer with HTTP status code 200 and return the [JSON](#json-response) containing the service catalog details.

### HTTPie
Request the catalog of services from the service broker with HTTPie:

```shell
http GET 127.0.0.1:8000/v2/catalog X-Broker-Api-Version:2.13 -a "":""
```
The service broker should answer with HTTP status code 200 and return the [JSON](#json-response) containing the service catalog details.

### Eden
[Eden](https://github.com/starkandwayne/eden) is a command line tool to interact with any service broker implementing the OSBAPI.

In order to use Eden you first need to set environment variables:
```shell
export SB_BROKER_URL=http://127.0.0.1:8000
export SB_BROKER_USERNAME=""
export SB_BROKER_PASSWORD=""
```
Request the catalog of services:
```shell
eden catalog
```
Response:
```
Service Name  Plan Name    Description                                                                    
tu-files      standard     Highly available network drive with standard authorization concept.            
tu-host       standard     Configurable, highly available Virtual Machine.                                
tu-cloud      tu-owncloud  Free file sync and share service for internal use.                             
~             tu-procloud  File sync and share service for collaboration with external project partners.  

4 services
```

### JSON Response
```son
{
    "services": [
        {
            "bindable": true,
            "description": "Highly available network drive for institutes and organizational units.",
            "id": "f02f46b2-d20d-4b6b-a9fa-6e7d28fddc9c",
            "metadata": {
                "displayName": "TUfiles",
                "documentationUrl": "https://www.it.tuwien.ac.at/tufiles/",
                "imageUrl": "http://example.com/tufiles_logo.png",
                "longDescription": "With TUfiles, we give you the opportunity to store data on a central and readily available network drive with backup (hosted on Windows servers). TUfiles is suitable for storing data with moderate access requirements, but high availability demands. TUfiles is not suitable for applications demanding high storage performance for a long period of time, such as high-performance databases, computer applications with high data access requirements and for storing local Microsoft Outlook PST files and backups.",
                "providerDisplayName": "TU.it",
                "supportUrl": "https://support.tuwien.ac.at/assystnet/"
            },
            "name": "tu-files",
            "plan_updateable": true,
            "plans": [
                {
                    "description": "Highly available network drive with standard authorization concept.",
                    "free": false,
                    "id": "04cd4e4a-f296-4090-b4f4-0e5717bb90c6",
                    "metadata": {
                        "bullets": [
                            "Redundant and readily available network drive",
                            "You can personally administer access rights and authorisations in folders",
                            "Useful for working with older file versions",
                            "With Windows 7/8/8.1/10, Linux and MacOS from SMB version 2.1",
                            "Not intended for storing your backups"
                        ],
                        "costs": [
                            {
                                "amount": {
                                    "eur": 0.03
                                },
                                "unit": "GB per quarter"
                            }
                        ],
                        "displayName": "Standard authorization concept"
                    },
                    "name": "standard",
                    "schemas": {
                        "service_binding": {
                            "create": {
                                "parameters": {
                                    "$schema": "http://json-schema.org/draft-04/schema#",
                                    "properties": {
                                        "xxxx": {
                                            "description": "Some parameter needed for binding the service instance.",
                                            "type": "string"
                                        }
                                    },
                                    "type": "object"
                                }
                            }
                        },
                        "service_instance": {
                            "create": {
                                "parameters": {
                                    "$schema": "http://json-schema.org/draft-04/schema#",
                                    "properties": {
                                        "authorization-group": {
                                            "description": "Name of the upTUdate authorization group.",
                                            "type": "string"
                                        },
                                        "share-name": {
                                            "description": "Name of the network drive.",
                                            "type": "string"
                                        },
                                        "size": {
                                            "description": "Size of storage in GB.",
                                            "type": "int"
                                        }
                                    },
                                    "type": "object"
                                }
                            },
                            "update": {
                                "parameters": {
                                    "$schema": "http://json-schema.org/draft-04/schema#",
                                    "properties": {
                                        "size": {
                                            "description": "Size of storage in GB.",
                                            "type": "int"
                                        }
                                    },
                                    "type": "object"
                                }
                            }
                        }
                    }
                }
            ],
            "tags": [
                "network-drive",
                "storage"
            ]
        },
        {
            "bindable": true,
            "description": "File Sync and Share service located on servers of the TU Wien.",
            "id": "c4573c4b-0fec-4c2d-b650-a3daa91a3bf0",
            "metadata": {
                "displayName": "TUcloud",
                "documentationUrl": "https://www.it.tuwien.ac.at/tuprocloud/",
                "imageUrl": "http://example.com/tucloud_logo.png",
                "longDescription": "With our File Sync and Share service, you can save your data to a \"virtual memory stick\". The open source software ownCloud runs on TU.it servers and basically offers the familiar features also provided by public cloud systems such as Dropbox.",
                "providerDisplayName": "TU.it",
                "supportUrl": "https://support.tuwien.ac.at/assystnet/"
            },
            "name": "tu-cloud",
            "plan_updateable": true,
            "plans": [
                {
                    "description": "Free file sync and share service for internal use.",
                    "free": true,
                    "id": "b1e8a5fd-0abc-4259-8d66-ab6fe8ee8b1d",
                    "metadata": {
                        "bullets": [
                            "20 GB of personal storage space",
                            "Running on TU.it servers - your data is present locally on our systems",
                            "Data access possible via clients, web and WebDAV",
                            "Synchronisation with any number of devices is either automatic or in accordance with settings you make yourself"
                        ],
                        "displayName": "TUownCloud"
                    },
                    "name": "tu-owncloud"
                },
                {
                    "description": "File sync and share service for collaboration with external project partners.",
                    "free": false,
                    "id": "433b4d74-6ed9-41f5-81e6-4bef7fd66c1f",
                    "metadata": {
                        "bullets": [
                            "Collaborate with external project partners",
                            "File-synchronization and sharing",
                            "Configure access / authorization of members",
                            "Several 100GB of storage possible"
                        ],
                        "costs": [
                            {
                                "amount": {
                                    "eur": 0.03
                                },
                                "unit": "GB per quarter"
                            }
                        ],
                        "displayName": "TUproCloud"
                    },
                    "name": "tu-procloud",
                    "schemas": {
                        "service_binding": {
                            "create": {
                                "parameters": {
                                    "$schema": "http://json-schema.org/draft-04/schema#",
                                    "properties": {
                                        "xxxx": {
                                            "description": "Some parameter needed for binding the service instance.",
                                            "type": "string"
                                        }
                                    },
                                    "type": "object"
                                }
                            }
                        },
                        "service_instance": {
                            "create": {
                                "parameters": {
                                    "$schema": "http://json-schema.org/draft-04/schema#",
                                    "properties": {
                                        "name": {
                                            "description": "Unique TU-wide name, not changeable.",
                                            "type": "string"
                                        },
                                        "size": {
                                            "description": "Size of storage in GB.",
                                            "type": "int"
                                        }
                                    },
                                    "type": "object"
                                }
                            },
                            "update": {
                                "parameters": {
                                    "$schema": "http://json-schema.org/draft-04/schema#",
                                    "properties": {
                                        "size": {
                                            "description": "Size of storage in GB.",
                                            "type": "int"
                                        }
                                    },
                                    "type": "object"
                                }
                            }
                        }
                    }
                }
            ],
            "tags": [
                "cloud-storage",
                "file-sync",
                "share"
            ]
        },
        {
            "bindable": false,
            "description": "Run virtual machine on central, highly available virtualization platform",
            "id": "e636ea62-a613-41a5-88b5-34f7be4b8d34",
            "metadata": {
                "displayName": "TUhost",
                "documentationUrl": "https://www.it.tuwien.ac.at/tuhost/",
                "imageUrl": "http://example.com/tuhost_logo.png",
                "longDescription": "You have the opportunity to operate virtual machines on the central and highly available TU.it virtualisation platform, hosted on VMware ESXi. TUhost is suitable for operating servers with moderate resource requirements, but high availability demands. The virtualisation platform is not suitable for operating servers that are to support applications demanding a particularly high computing capacity and/or storage performance, such as simulation calculations, high-performance databases or storage for vast quantities of data.",
                "providerDisplayName": "TU.it",
                "supportUrl": "https://support.tuwien.ac.at/assystnet/"
            },
            "name": "tu-host",
            "plan_updateable": true,
            "plans": [
                {
                    "bindable": false,
                    "description": "Configurable, highly available Virtual Machine.",
                    "free": false,
                    "id": "057997b7-22ac-4d6b-90a9-b2c8d5e289e6",
                    "metadata": {
                        "bullets": [
                            "Provision of virtual servers including storage for TU organisational units",
                            "Backup for VMs",
                            "VM administration portal",
                            "Restore option in self-service via a portal"
                        ],
                        "costs": [
                            {
                                "amount": {
                                    "eur": 8
                                },
                                "unit": "vCPU per quarter"
                            },
                            {
                                "amount": {
                                    "eur": 8
                                },
                                "unit": "GB RAM per quarter"
                            },
                            {
                                "amount": {
                                    "eur": 0.1
                                },
                                "unit": "GB system disk per quarter"
                            },
                            {
                                "amount": {
                                    "eur": 0.1
                                },
                                "unit": "GB data disk per quarter"
                            },
                            {
                                "amount": {
                                    "eur": 0.25
                                },
                                "unit": "GB high-performance disk per quarter"
                            }
                        ],
                        "displayName": "TUhost Standard"
                    },
                    "name": "standard",
                    "schemas": {
                        "service_binding": {
                            "create": {
                                "parameters": {
                                    "$schema": "http://json-schema.org/draft-04/schema#",
                                    "properties": {
                                        "xxxx": {
                                            "description": "Some parameter needed for binding the service instance.",
                                            "type": "string"
                                        }
                                    },
                                    "type": "object"
                                }
                            }
                        },
                        "service_instance": {
                            "create": {
                                "parameters": {
                                    "$schema": "http://json-schema.org/draft-04/schema#",
                                    "properties": {
                                        "diskData": {
                                            "description": "Amount of data disk storage in GB.",
                                            "type": "int"
                                        },
                                        "diskHighPerf": {
                                            "description": "Amount of high performance disk storage in GB.",
                                            "type": "int"
                                        },
                                        "diskSys": {
                                            "description": "Amount of system disk storage in GB.",
                                            "type": "int"
                                        },
                                        "os": {
                                            "description": "Virtual machine operating system.",
                                            "enum": [
                                                "CentOS",
                                                "Debian",
                                                "Windows Server"
                                            ],
                                            "type": "string"
                                        },
                                        "ram": {
                                            "description": "Amount of RAM in GB.",
                                            "type": "int"
                                        },
                                        "usage": {
                                            "description": "Intended usage of the virtual machine.",
                                            "type": "string"
                                        },
                                        "vCPUs": {
                                            "description": "Number of virtual CPUs.",
                                            "type": "int"
                                        },
                                        "vmName": {
                                            "description": "Virtual machine name (host.subdomain).",
                                            "type": "string"
                                        }
                                    },
                                    "type": "object"
                                }
                            },
                            "update": {
                                "parameters": {
                                    "$schema": "http://json-schema.org/draft-04/schema#",
                                    "properties": {
                                        "diskData": {
                                            "description": "Amount of data disk storage in GB.",
                                            "type": "int"
                                        },
                                        "diskHighPerf": {
                                            "description": "Amount of high performance disk storage in GB.",
                                            "type": "int"
                                        },
                                        "diskSys": {
                                            "description": "Amount of system disk storage in GB.",
                                            "type": "int"
                                        },
                                        "ram": {
                                            "description": "Amount of RAM in GB.",
                                            "type": "int"
                                        },
                                        "vCPUs": {
                                            "description": "Number of virtual CPUs.",
                                            "type": "int"
                                        }
                                    },
                                    "type": "object"
                                }
                            }
                        }
                    }
                }
            ],
            "tags": [
                "vm",
                "virtual-server"
            ]
        }
    ]
}
```
from openbrokerapi.catalog import ServicePlan, ServiceMetadata, ServicePlanMetaData, ServicePlanCost, Schemas
from openbrokerapi.service_broker import (
    ServiceBroker,
    Service,
    ProvisionDetails,
    ProvisionedServiceSpec,
    BindDetails,
    Binding,
    UpdateDetails,
    UpdateServiceSpec,
    UnbindDetails,
    DeprovisionDetails,
    DeprovisionServiceSpec,
    LastOperation
)


class TuFilesServiceBroker(ServiceBroker):
    def catalog(self):
        return Service(
            id='f02f46b2-d20d-4b6b-a9fa-6e7d28fddc9c',
            name='tu-files',
            description='Highly available network drive for institutes and organizational units.',
            bindable=True,
            metadata=ServiceMetadata(
                displayName='TUfiles',
                imageUrl='http://example.com/tufiles_logo.png',
                longDescription='With TUfiles, we give you the opportunity to store data on a central and readily available network drive with backup (hosted on Windows servers). TUfiles is suitable for storing data with moderate access requirements, but high availability demands. TUfiles is not suitable for applications demanding high storage performance for a long period of time, such as high-performance databases, computer applications with high data access requirements and for storing local Microsoft Outlook PST files and backups.',
                providerDisplayName='TU.it',
                documentationUrl='https://www.it.tuwien.ac.at/tufiles/',
                supportUrl='https://support.tuwien.ac.at/assystnet/'
            ),
            plans=[
                ServicePlan(
                    id='04cd4e4a-f296-4090-b4f4-0e5717bb90c6',
                    name='standard',
                    description='Highly available network drive with standard authorization concept.',
                    free=False,
                    metadata=ServicePlanMetaData(
                        displayName='Standard authorization concept',
                        bullets=['Redundant and readily available network drive',
                                 'You can personally administer access rights and authorisations in folders',
                                 'Useful for working with older file versions',
                                 'With Windows 7/8/8.1/10, Linux and MacOS from SMB version 2.1',
                                 'Not intended for storing your backups'
                                 ],
                        costs=[ServicePlanCost(
                            amount={'eur': 0.03},
                            unit='GB per quarter'
                        )]
                    ),
                    schemas=Schemas(
                        service_instance={
                            'create': {
                                'parameters': {
                                    '$schema': 'http://json-schema.org/draft-04/schema#',
                                    'type': 'object',
                                    'properties': {
                                        'share-name': {
                                            'description': 'Name of the network drive.',
                                            'type': 'string'
                                        },
                                        'size': {
                                            'description': 'Size of storage in GB.',
                                            'type': 'int'
                                        },
                                        'authorization-group': {
                                            'description': 'Name of the upTUdate authorization group.',
                                            'type': 'string'
                                        }
                                    }
                                }
                            },
                            'update': {
                                'parameters': {
                                    '$schema': 'http://json-schema.org/draft-04/schema#',
                                    'type': 'object',
                                    'properties': {
                                        'size': {
                                            'description': 'Size of storage in GB.',
                                            'type': 'int'
                                        },
                                    }
                                }
                            }
                        },
                        service_binding={
                            'create': {
                                'parameters': {
                                    '$schema': 'http://json-schema.org/draft-04/schema#',
                                    'type': 'object',
                                    'properties': {
                                        'xxxx': {
                                            'description': 'Some parameter needed for binding the service instance.',
                                            'type': 'string'
                                        }
                                    }
                                }
                            }
                        }
                    )
                )
            ],
            tags=['network-drive', 'storage'],
            plan_updateable=True,
        )

    def provision(self, instance_id: str, service_details: ProvisionDetails,
                  async_allowed: bool) -> ProvisionedServiceSpec:
        pass

    def bind(self, instance_id: str, binding_id: str, details: BindDetails) -> Binding:
        pass

    def update(self, instance_id: str, details: UpdateDetails, async_allowed: bool) -> UpdateServiceSpec:
        pass

    def unbind(self, instance_id: str, binding_id: str, details: UnbindDetails):
        pass

    def deprovision(self, instance_id: str, details: DeprovisionDetails, async_allowed: bool) -> DeprovisionServiceSpec:
        pass

    def last_operation(self, instance_id: str, operation_data: str) -> LastOperation:
        pass


class TuCloudServiceBroker(ServiceBroker):
    def catalog(self):
        return Service(
            id='c4573c4b-0fec-4c2d-b650-a3daa91a3bf0',
            name='tu-cloud',
            description='File Sync and Share service located on servers of the TU Wien.',
            bindable=True,
            metadata=ServiceMetadata(
                displayName='TUcloud',
                imageUrl='http://example.com/tucloud_logo.png',
                longDescription='With our File Sync and Share service, you can save your data to a \"virtual memory stick\". The open source software ownCloud runs on TU.it servers and basically offers the familiar features also provided by public cloud systems such as Dropbox.',
                providerDisplayName='TU.it',
                documentationUrl='https://www.it.tuwien.ac.at/tuprocloud/',
                supportUrl='https://support.tuwien.ac.at/assystnet/'
            ),
            plans=[
                ServicePlan(
                    id='b1e8a5fd-0abc-4259-8d66-ab6fe8ee8b1d',
                    name='tu-owncloud',
                    description='Free file sync and share service for internal use.',
                    free=True,
                    metadata=ServicePlanMetaData(
                        displayName='TUownCloud',
                        bullets=['20 GB of personal storage space',
                                 'Running on TU.it servers - your data is present locally on our systems',
                                 'Data access possible via clients, web and WebDAV',
                                 'Synchronisation with any number of devices is either automatic or in accordance with settings you make yourself'
                                 ]
                    )
                ),
                ServicePlan(
                    id='433b4d74-6ed9-41f5-81e6-4bef7fd66c1f',
                    name='tu-procloud',
                    description='File sync and share service for collaboration with external project partners.',
                    free=False,
                    metadata=ServicePlanMetaData(
                        displayName='TUproCloud',
                        bullets=['Collaborate with external project partners',
                                 'File-synchronization and sharing',
                                 'Configure access / authorization of members',
                                 'Several 100GB of storage possible'
                                 ],
                        costs=[ServicePlanCost(
                            amount={'eur': 0.03},
                            unit='GB per quarter'
                        )]
                    ),
                    schemas=Schemas(
                        service_instance={
                            'create': {
                                'parameters': {
                                    '$schema': 'http://json-schema.org/draft-04/schema#',
                                    'type': 'object',
                                    'properties': {
                                        'name': {
                                            'description': 'Unique TU-wide name, not changeable.',
                                            'type': 'string'
                                        },
                                        'size': {
                                            'description': 'Size of storage in GB.',
                                            'type': 'int'
                                        },
                                    }
                                }
                            },
                            'update': {
                                'parameters': {
                                    '$schema': 'http://json-schema.org/draft-04/schema#',
                                    'type': 'object',
                                    'properties': {
                                        'size': {
                                            'description': 'Size of storage in GB.',
                                            'type': 'int'
                                        },
                                    }
                                }
                            }
                        },
                        service_binding={
                            'create': {
                                'parameters': {
                                    '$schema': 'http://json-schema.org/draft-04/schema#',
                                    'type': 'object',
                                    'properties': {
                                        'xxxx': {
                                            'description': 'Some parameter needed for binding the service instance.',
                                            'type': 'string'
                                        }
                                    }
                                }
                            }
                        }
                    )
                )
            ],
            tags=['cloud-storage', 'file-sync', 'share'],
            plan_updateable=True,
        )

    def provision(self, instance_id: str, service_details: ProvisionDetails,
                  async_allowed: bool) -> ProvisionedServiceSpec:
        pass

    def bind(self, instance_id: str, binding_id: str, details: BindDetails) -> Binding:
        pass

    def update(self, instance_id: str, details: UpdateDetails, async_allowed: bool) -> UpdateServiceSpec:
        pass

    def unbind(self, instance_id: str, binding_id: str, details: UnbindDetails):
        pass

    def deprovision(self, instance_id: str, details: DeprovisionDetails,
                    async_allowed: bool) -> DeprovisionServiceSpec:
        pass

    def last_operation(self, instance_id: str, operation_data: str) -> LastOperation:
        pass


class TuHostServiceBroker(ServiceBroker):
    def catalog(self):
        return Service(
            id='e636ea62-a613-41a5-88b5-34f7be4b8d34',
            name='tu-host',
            description='Run virtual machine on central, highly available virtualization platform',
            bindable=False,
            metadata=ServiceMetadata(
                displayName='TUhost',
                imageUrl='http://example.com/tuhost_logo.png',
                longDescription='You have the opportunity to operate virtual machines on the central and highly available TU.it virtualisation platform, hosted on VMware ESXi. TUhost is suitable for operating servers with moderate resource requirements, but high availability demands. The virtualisation platform is not suitable for operating servers that are to support applications demanding a particularly high computing capacity and/or storage performance, such as simulation calculations, high-performance databases or storage for vast quantities of data.',
                providerDisplayName='TU.it',
                documentationUrl='https://www.it.tuwien.ac.at/tuhost/',
                supportUrl='https://support.tuwien.ac.at/assystnet/'
            ),
            plans=[
                ServicePlan(
                    id='057997b7-22ac-4d6b-90a9-b2c8d5e289e6',
                    name='standard',
                    description='Configurable, highly available Virtual Machine.',
                    free=False,
                    bindable=False,
                    metadata=ServicePlanMetaData(
                        displayName='TUhost Standard',
                        bullets=['Provision of virtual servers including storage for TU organisational units',
                                 'Backup for VMs',
                                 'VM administration portal',
                                 'Restore option in self-service via a portal'
                                 ],
                        costs=[
                            ServicePlanCost(
                                amount={'eur': 8},
                                unit='vCPU per quarter'
                            ),
                            ServicePlanCost(
                                amount={'eur': 8},
                                unit='GB RAM per quarter'
                            ),
                            ServicePlanCost(
                                amount={'eur': 0.1},
                                unit='GB system disk per quarter'
                            ),
                            ServicePlanCost(
                                amount={'eur': 0.1},
                                unit='GB data disk per quarter'
                            ),
                            ServicePlanCost(
                                amount={'eur': 0.25},
                                unit='GB high-performance disk per quarter'
                            ),
                        ]
                    ),
                    schemas=Schemas(
                        service_instance={
                            'create': {
                                'parameters': {
                                    '$schema': 'http://json-schema.org/draft-04/schema#',
                                    'type': 'object',
                                    'properties': {
                                        'vmName': {
                                            'description': 'Virtual machine name (host.subdomain).',
                                            'type': 'string'
                                        },
                                        'vCPUs': {
                                            'description': 'Number of virtual CPUs.',
                                            'type': 'int'
                                        },
                                        'ram': {
                                            'description': 'Amount of RAM in GB.',
                                            'type': 'int'
                                        },
                                        'diskSys': {
                                            'description': 'Amount of system disk storage in GB.',
                                            'type': 'int'
                                        },
                                        'diskData': {
                                            'description': 'Amount of data disk storage in GB.',
                                            'type': 'int'
                                        },
                                        'diskHighPerf': {
                                            'description': 'Amount of high performance disk storage in GB.',
                                            'type': 'int'
                                        },
                                        'os': {
                                            'description': 'Virtual machine operating system.',
                                            'type': 'string',
                                            'enum': ['CentOS', 'Debian', 'Windows Server']
                                        },
                                        'usage': {
                                            'description': 'Intended usage of the virtual machine.',
                                            'type': 'string'
                                        },
                                    }
                                }
                            },
                            'update': {
                                'parameters': {
                                    '$schema': 'http://json-schema.org/draft-04/schema#',
                                    'type': 'object',
                                    'properties': {
                                        'vCPUs': {
                                            'description': 'Number of virtual CPUs.',
                                            'type': 'int'
                                        },
                                        'ram': {
                                            'description': 'Amount of RAM in GB.',
                                            'type': 'int'
                                        },
                                        'diskSys': {
                                            'description': 'Amount of system disk storage in GB.',
                                            'type': 'int'
                                        },
                                        'diskData': {
                                            'description': 'Amount of data disk storage in GB.',
                                            'type': 'int'
                                        },
                                        'diskHighPerf': {
                                            'description': 'Amount of high performance disk storage in GB.',
                                            'type': 'int'
                                        },
                                    }
                                }
                            }
                        },
                        service_binding={
                            'create': {
                                'parameters': {
                                    '$schema': 'http://json-schema.org/draft-04/schema#',
                                    'type': 'object',
                                    'properties': {
                                        'xxxx': {
                                            'description': 'Some parameter needed for binding the service instance.',
                                            'type': 'string'
                                        }
                                    }
                                }
                            }
                        }
                    )
                ),
            ],
            tags=['vm', 'virtual-server'],
            plan_updateable=True,
        )

    def provision(self, instance_id: str, service_details: ProvisionDetails,
                  async_allowed: bool) -> ProvisionedServiceSpec:
        pass

    def bind(self, instance_id: str, binding_id: str, details: BindDetails) -> Binding:
        pass

    def update(self, instance_id: str, details: UpdateDetails, async_allowed: bool) -> UpdateServiceSpec:
        pass

    def unbind(self, instance_id: str, binding_id: str, details: UnbindDetails):
        pass

    def deprovision(self, instance_id: str, details: DeprovisionDetails, async_allowed: bool) -> DeprovisionServiceSpec:
        pass

    def last_operation(self, instance_id: str, operation_data: str) -> LastOperation:
        pass

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
            id='00000000-0000-0000-0000-000000000001',
            name='tu-files',
            description='Highly available network drive for institutes and organizational units.',
            bindable=False,
            metadata=ServiceMetadata(
                displayName='TUfiles',
                imageUrl='http://example.com/tufiles_logo.png',
                longDescription='Some longer description of the TUfiles service...',
                providerDisplayName='TU.it',
                documentationUrl='https://www.it.tuwien.ac.at/tufiles/',
                supportUrl='https://support.tuwien.ac.at/assystnet/'
            ),
            plans=[
                ServicePlan(
                    id='00000000-0000-0000-0000-000000000001',
                    name='standard',
                    description='Some description of this service plan',
                    free=False,
                    metadata=ServicePlanMetaData(
                        displayName='Standard authorization concept',
                        bullets=['Feature1',
                                 'Feature2',
                                 'Feature3',
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
                        },
                    )
                ),
                ServicePlan(
                    id='00000000-0000-0000-0000-000000000002',
                    name='special',
                    description='Some description of this service plan',
                    free=False,
                    metadata=ServicePlanMetaData(
                        displayName='Special authorization concept',
                        bullets=['Feature1',
                                 'Feature2',
                                 'Feature3',
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
                        },
                    )
                ),
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


class TuProCloudServiceBroker(ServiceBroker):
    def catalog(self):
        return Service(
            id='00000000-0000-0000-0000-000000000002',
            name='tu-procloud',
            description='Private Cloud Storage based on ownCloud, located on servers of the TU Wien.',
            bindable=True,
            metadata=ServiceMetadata(
                displayName='TUproCloud',
                imageUrl='http://example.com/tuprocloud_logo.png',
                longDescription='TUproCloud can also be used for collaboration with external project partners...',
                providerDisplayName='TU.it',
                documentationUrl='https://www.it.tuwien.ac.at/tuprocloud/',
                supportUrl='https://support.tuwien.ac.at/assystnet/'
            ),
            plans=[
                ServicePlan(
                    id='00000000-0000-0000-0000-000000000001',
                    name='standard',
                    description='Configurable private cloud',
                    free=False,
                    metadata=ServicePlanMetaData(
                        displayName='Standard',
                        bullets=['Collaborate with external project partners.',
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
                        },
                    )
                ),
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
            id='00000000-0000-0000-0000-000000000003',
            name='tu-host',
            description='Run virtual machine on central, highly available virtualization platform',
            bindable=False,
            metadata=ServiceMetadata(
                displayName='TUhost',
                imageUrl='http://example.com/tuhost_logo.png',
                longDescription='The virtual machine is running on redundant servers in the data center ' \
                                'Freihaus, Wiedner Hauptstr. 8-10 and Gußhausstr. 27.29, 1040 Wien',
                providerDisplayName='TU.it',
                documentationUrl='https://www.it.tuwien.ac.at/tuhost/',
                supportUrl='https://support.tuwien.ac.at/assystnet/'
            ),
            plans=[
                ServicePlan(
                    id='00000000-0000-0000-0000-000000000001',
                    name='standard',
                    description='Configurable VM',
                    free=False,
                    bindable=False,
                    metadata=ServicePlanMetaData(
                        displayName='Standard',
                        bullets=['24 hours availability',
                                 'Configure your VM: CPU, RAM, Disk Space',
                                 'Choose OS: CentOS, Debian, Windows Server',
                                 'Includes backup and restore functionality'
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
                        },
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

from openbrokerapi.catalog import ServicePlan
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


class TuItServiceBroker(ServiceBroker):
    def catalog(self):
        return Service(
            id='00000000-0000-0000-0000-000000000000',
            name='example-service',
            description='Example Service does nothing',
            bindable=True,
            plans=[
                ServicePlan(
                    id='00000000-0000-0000-0000-000000000000',
                    name='small',
                    description='example service plan',
                ),
            ],
            tags=['example', 'service'],
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

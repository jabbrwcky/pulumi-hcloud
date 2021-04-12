# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
from . import _utilities, _tables
from . import outputs
from ._inputs import *

__all__ = ['LoadBalancerServiceArgs', 'LoadBalancerService']

@pulumi.input_type
class LoadBalancerServiceArgs:
    def __init__(__self__, *,
                 load_balancer_id: pulumi.Input[str],
                 protocol: pulumi.Input[str],
                 destination_port: Optional[pulumi.Input[int]] = None,
                 health_check: Optional[pulumi.Input['LoadBalancerServiceHealthCheckArgs']] = None,
                 http: Optional[pulumi.Input['LoadBalancerServiceHttpArgs']] = None,
                 listen_port: Optional[pulumi.Input[int]] = None,
                 proxyprotocol: Optional[pulumi.Input[bool]] = None):
        """
        The set of arguments for constructing a LoadBalancerService resource.
        :param pulumi.Input[str] load_balancer_id: Id of the load balancer this service belongs to.
        :param pulumi.Input[str] protocol: Protocol of the service. `http`, `https` or `tcp`
        :param pulumi.Input[int] destination_port: Port the service connects to the targets on, required if protocol is `tcp`. Can be everything between `1` and `65535`.
        :param pulumi.Input['LoadBalancerServiceHealthCheckArgs'] health_check: List of health check configurations when `protocol` is `http` or `https`.
        :param pulumi.Input['LoadBalancerServiceHttpArgs'] http: List of http configurations when `protocol` is `http` or `https`.
        :param pulumi.Input[int] listen_port: Port the service listen on, required if protocol is `tcp`. Can be everything between `1` and `65535`. Must be unique per Load Balancer.
        :param pulumi.Input[bool] proxyprotocol: Enable proxyprotocol.
        """
        pulumi.set(__self__, "load_balancer_id", load_balancer_id)
        pulumi.set(__self__, "protocol", protocol)
        if destination_port is not None:
            pulumi.set(__self__, "destination_port", destination_port)
        if health_check is not None:
            pulumi.set(__self__, "health_check", health_check)
        if http is not None:
            pulumi.set(__self__, "http", http)
        if listen_port is not None:
            pulumi.set(__self__, "listen_port", listen_port)
        if proxyprotocol is not None:
            pulumi.set(__self__, "proxyprotocol", proxyprotocol)

    @property
    @pulumi.getter(name="loadBalancerId")
    def load_balancer_id(self) -> pulumi.Input[str]:
        """
        Id of the load balancer this service belongs to.
        """
        return pulumi.get(self, "load_balancer_id")

    @load_balancer_id.setter
    def load_balancer_id(self, value: pulumi.Input[str]):
        pulumi.set(self, "load_balancer_id", value)

    @property
    @pulumi.getter
    def protocol(self) -> pulumi.Input[str]:
        """
        Protocol of the service. `http`, `https` or `tcp`
        """
        return pulumi.get(self, "protocol")

    @protocol.setter
    def protocol(self, value: pulumi.Input[str]):
        pulumi.set(self, "protocol", value)

    @property
    @pulumi.getter(name="destinationPort")
    def destination_port(self) -> Optional[pulumi.Input[int]]:
        """
        Port the service connects to the targets on, required if protocol is `tcp`. Can be everything between `1` and `65535`.
        """
        return pulumi.get(self, "destination_port")

    @destination_port.setter
    def destination_port(self, value: Optional[pulumi.Input[int]]):
        pulumi.set(self, "destination_port", value)

    @property
    @pulumi.getter(name="healthCheck")
    def health_check(self) -> Optional[pulumi.Input['LoadBalancerServiceHealthCheckArgs']]:
        """
        List of health check configurations when `protocol` is `http` or `https`.
        """
        return pulumi.get(self, "health_check")

    @health_check.setter
    def health_check(self, value: Optional[pulumi.Input['LoadBalancerServiceHealthCheckArgs']]):
        pulumi.set(self, "health_check", value)

    @property
    @pulumi.getter
    def http(self) -> Optional[pulumi.Input['LoadBalancerServiceHttpArgs']]:
        """
        List of http configurations when `protocol` is `http` or `https`.
        """
        return pulumi.get(self, "http")

    @http.setter
    def http(self, value: Optional[pulumi.Input['LoadBalancerServiceHttpArgs']]):
        pulumi.set(self, "http", value)

    @property
    @pulumi.getter(name="listenPort")
    def listen_port(self) -> Optional[pulumi.Input[int]]:
        """
        Port the service listen on, required if protocol is `tcp`. Can be everything between `1` and `65535`. Must be unique per Load Balancer.
        """
        return pulumi.get(self, "listen_port")

    @listen_port.setter
    def listen_port(self, value: Optional[pulumi.Input[int]]):
        pulumi.set(self, "listen_port", value)

    @property
    @pulumi.getter
    def proxyprotocol(self) -> Optional[pulumi.Input[bool]]:
        """
        Enable proxyprotocol.
        """
        return pulumi.get(self, "proxyprotocol")

    @proxyprotocol.setter
    def proxyprotocol(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "proxyprotocol", value)


class LoadBalancerService(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 destination_port: Optional[pulumi.Input[int]] = None,
                 health_check: Optional[pulumi.Input[pulumi.InputType['LoadBalancerServiceHealthCheckArgs']]] = None,
                 http: Optional[pulumi.Input[pulumi.InputType['LoadBalancerServiceHttpArgs']]] = None,
                 listen_port: Optional[pulumi.Input[int]] = None,
                 load_balancer_id: Optional[pulumi.Input[str]] = None,
                 protocol: Optional[pulumi.Input[str]] = None,
                 proxyprotocol: Optional[pulumi.Input[bool]] = None,
                 __props__=None,
                 __name__=None,
                 __opts__=None):
        """
        Define services for Hetzner Cloud Load Balancers.

        ## Example Usage

        ```python
        import pulumi
        import pulumi_hcloud as hcloud

        load_balancer = hcloud.LoadBalancer("loadBalancer",
            load_balancer_type="lb11",
            location="nbg1")
        load_balancer_service = hcloud.LoadBalancerService("loadBalancerService",
            load_balancer_id=hcloud_load_balancer["test_load_balancer"]["id"],
            protocol="http")
        ```

        ## Import

        Load Balancer Service entries can be imported using a compound ID with the following format`<load-balancer-id>__<listen-port>`

        ```sh
         $ pulumi import hcloud:index/loadBalancerService:LoadBalancerService myloadbalancernetwork 123__80
        ```

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[int] destination_port: Port the service connects to the targets on, required if protocol is `tcp`. Can be everything between `1` and `65535`.
        :param pulumi.Input[pulumi.InputType['LoadBalancerServiceHealthCheckArgs']] health_check: List of health check configurations when `protocol` is `http` or `https`.
        :param pulumi.Input[pulumi.InputType['LoadBalancerServiceHttpArgs']] http: List of http configurations when `protocol` is `http` or `https`.
        :param pulumi.Input[int] listen_port: Port the service listen on, required if protocol is `tcp`. Can be everything between `1` and `65535`. Must be unique per Load Balancer.
        :param pulumi.Input[str] load_balancer_id: Id of the load balancer this service belongs to.
        :param pulumi.Input[str] protocol: Protocol of the service. `http`, `https` or `tcp`
        :param pulumi.Input[bool] proxyprotocol: Enable proxyprotocol.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: LoadBalancerServiceArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        Define services for Hetzner Cloud Load Balancers.

        ## Example Usage

        ```python
        import pulumi
        import pulumi_hcloud as hcloud

        load_balancer = hcloud.LoadBalancer("loadBalancer",
            load_balancer_type="lb11",
            location="nbg1")
        load_balancer_service = hcloud.LoadBalancerService("loadBalancerService",
            load_balancer_id=hcloud_load_balancer["test_load_balancer"]["id"],
            protocol="http")
        ```

        ## Import

        Load Balancer Service entries can be imported using a compound ID with the following format`<load-balancer-id>__<listen-port>`

        ```sh
         $ pulumi import hcloud:index/loadBalancerService:LoadBalancerService myloadbalancernetwork 123__80
        ```

        :param str resource_name: The name of the resource.
        :param LoadBalancerServiceArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(LoadBalancerServiceArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 destination_port: Optional[pulumi.Input[int]] = None,
                 health_check: Optional[pulumi.Input[pulumi.InputType['LoadBalancerServiceHealthCheckArgs']]] = None,
                 http: Optional[pulumi.Input[pulumi.InputType['LoadBalancerServiceHttpArgs']]] = None,
                 listen_port: Optional[pulumi.Input[int]] = None,
                 load_balancer_id: Optional[pulumi.Input[str]] = None,
                 protocol: Optional[pulumi.Input[str]] = None,
                 proxyprotocol: Optional[pulumi.Input[bool]] = None,
                 __props__=None,
                 __name__=None,
                 __opts__=None):
        if __name__ is not None:
            warnings.warn("explicit use of __name__ is deprecated", DeprecationWarning)
            resource_name = __name__
        if __opts__ is not None:
            warnings.warn("explicit use of __opts__ is deprecated, use 'opts' instead", DeprecationWarning)
            opts = __opts__
        if opts is None:
            opts = pulumi.ResourceOptions()
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.version is None:
            opts.version = _utilities.get_version()
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = dict()

            __props__['destination_port'] = destination_port
            __props__['health_check'] = health_check
            __props__['http'] = http
            __props__['listen_port'] = listen_port
            if load_balancer_id is None and not opts.urn:
                raise TypeError("Missing required property 'load_balancer_id'")
            __props__['load_balancer_id'] = load_balancer_id
            if protocol is None and not opts.urn:
                raise TypeError("Missing required property 'protocol'")
            __props__['protocol'] = protocol
            __props__['proxyprotocol'] = proxyprotocol
        super(LoadBalancerService, __self__).__init__(
            'hcloud:index/loadBalancerService:LoadBalancerService',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None,
            destination_port: Optional[pulumi.Input[int]] = None,
            health_check: Optional[pulumi.Input[pulumi.InputType['LoadBalancerServiceHealthCheckArgs']]] = None,
            http: Optional[pulumi.Input[pulumi.InputType['LoadBalancerServiceHttpArgs']]] = None,
            listen_port: Optional[pulumi.Input[int]] = None,
            load_balancer_id: Optional[pulumi.Input[str]] = None,
            protocol: Optional[pulumi.Input[str]] = None,
            proxyprotocol: Optional[pulumi.Input[bool]] = None) -> 'LoadBalancerService':
        """
        Get an existing LoadBalancerService resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[int] destination_port: Port the service connects to the targets on, required if protocol is `tcp`. Can be everything between `1` and `65535`.
        :param pulumi.Input[pulumi.InputType['LoadBalancerServiceHealthCheckArgs']] health_check: List of health check configurations when `protocol` is `http` or `https`.
        :param pulumi.Input[pulumi.InputType['LoadBalancerServiceHttpArgs']] http: List of http configurations when `protocol` is `http` or `https`.
        :param pulumi.Input[int] listen_port: Port the service listen on, required if protocol is `tcp`. Can be everything between `1` and `65535`. Must be unique per Load Balancer.
        :param pulumi.Input[str] load_balancer_id: Id of the load balancer this service belongs to.
        :param pulumi.Input[str] protocol: Protocol of the service. `http`, `https` or `tcp`
        :param pulumi.Input[bool] proxyprotocol: Enable proxyprotocol.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = dict()

        __props__["destination_port"] = destination_port
        __props__["health_check"] = health_check
        __props__["http"] = http
        __props__["listen_port"] = listen_port
        __props__["load_balancer_id"] = load_balancer_id
        __props__["protocol"] = protocol
        __props__["proxyprotocol"] = proxyprotocol
        return LoadBalancerService(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="destinationPort")
    def destination_port(self) -> pulumi.Output[int]:
        """
        Port the service connects to the targets on, required if protocol is `tcp`. Can be everything between `1` and `65535`.
        """
        return pulumi.get(self, "destination_port")

    @property
    @pulumi.getter(name="healthCheck")
    def health_check(self) -> pulumi.Output['outputs.LoadBalancerServiceHealthCheck']:
        """
        List of health check configurations when `protocol` is `http` or `https`.
        """
        return pulumi.get(self, "health_check")

    @property
    @pulumi.getter
    def http(self) -> pulumi.Output['outputs.LoadBalancerServiceHttp']:
        """
        List of http configurations when `protocol` is `http` or `https`.
        """
        return pulumi.get(self, "http")

    @property
    @pulumi.getter(name="listenPort")
    def listen_port(self) -> pulumi.Output[int]:
        """
        Port the service listen on, required if protocol is `tcp`. Can be everything between `1` and `65535`. Must be unique per Load Balancer.
        """
        return pulumi.get(self, "listen_port")

    @property
    @pulumi.getter(name="loadBalancerId")
    def load_balancer_id(self) -> pulumi.Output[str]:
        """
        Id of the load balancer this service belongs to.
        """
        return pulumi.get(self, "load_balancer_id")

    @property
    @pulumi.getter
    def protocol(self) -> pulumi.Output[str]:
        """
        Protocol of the service. `http`, `https` or `tcp`
        """
        return pulumi.get(self, "protocol")

    @property
    @pulumi.getter
    def proxyprotocol(self) -> pulumi.Output[bool]:
        """
        Enable proxyprotocol.
        """
        return pulumi.get(self, "proxyprotocol")

    def translate_output_property(self, prop):
        return _tables.CAMEL_TO_SNAKE_CASE_TABLE.get(prop) or prop

    def translate_input_property(self, prop):
        return _tables.SNAKE_TO_CAMEL_CASE_TABLE.get(prop) or prop


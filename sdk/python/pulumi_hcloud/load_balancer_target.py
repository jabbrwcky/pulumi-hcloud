# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
from . import _utilities, _tables

__all__ = ['LoadBalancerTargetArgs', 'LoadBalancerTarget']

@pulumi.input_type
class LoadBalancerTargetArgs:
    def __init__(__self__, *,
                 load_balancer_id: pulumi.Input[int],
                 type: pulumi.Input[str],
                 ip: Optional[pulumi.Input[str]] = None,
                 label_selector: Optional[pulumi.Input[str]] = None,
                 server_id: Optional[pulumi.Input[int]] = None,
                 use_private_ip: Optional[pulumi.Input[bool]] = None):
        """
        The set of arguments for constructing a LoadBalancerTarget resource.
        :param pulumi.Input[int] load_balancer_id: ID of the Load Balancer to which
               the target gets attached.
        :param pulumi.Input[str] type: Type of the target. Possible values
               `server`, `label_selector`, `ip`.
        :param pulumi.Input[str] ip: IP address for an IP Target. Required if
               `type` is `ip`.
        :param pulumi.Input[str] label_selector: Label Selector selecting targets
               for this Load Balancer. Required if `type` is `label_selector`.
        :param pulumi.Input[int] server_id: ID of the server which should be a
               target for this Load Balancer. Required if `type` is `server`
        :param pulumi.Input[bool] use_private_ip: use the private IP to connect to
               Load Balancer targets. Only allowed if type is `server` or
               `label_selector`.
        """
        pulumi.set(__self__, "load_balancer_id", load_balancer_id)
        pulumi.set(__self__, "type", type)
        if ip is not None:
            pulumi.set(__self__, "ip", ip)
        if label_selector is not None:
            pulumi.set(__self__, "label_selector", label_selector)
        if server_id is not None:
            pulumi.set(__self__, "server_id", server_id)
        if use_private_ip is not None:
            pulumi.set(__self__, "use_private_ip", use_private_ip)

    @property
    @pulumi.getter(name="loadBalancerId")
    def load_balancer_id(self) -> pulumi.Input[int]:
        """
        ID of the Load Balancer to which
        the target gets attached.
        """
        return pulumi.get(self, "load_balancer_id")

    @load_balancer_id.setter
    def load_balancer_id(self, value: pulumi.Input[int]):
        pulumi.set(self, "load_balancer_id", value)

    @property
    @pulumi.getter
    def type(self) -> pulumi.Input[str]:
        """
        Type of the target. Possible values
        `server`, `label_selector`, `ip`.
        """
        return pulumi.get(self, "type")

    @type.setter
    def type(self, value: pulumi.Input[str]):
        pulumi.set(self, "type", value)

    @property
    @pulumi.getter
    def ip(self) -> Optional[pulumi.Input[str]]:
        """
        IP address for an IP Target. Required if
        `type` is `ip`.
        """
        return pulumi.get(self, "ip")

    @ip.setter
    def ip(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "ip", value)

    @property
    @pulumi.getter(name="labelSelector")
    def label_selector(self) -> Optional[pulumi.Input[str]]:
        """
        Label Selector selecting targets
        for this Load Balancer. Required if `type` is `label_selector`.
        """
        return pulumi.get(self, "label_selector")

    @label_selector.setter
    def label_selector(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "label_selector", value)

    @property
    @pulumi.getter(name="serverId")
    def server_id(self) -> Optional[pulumi.Input[int]]:
        """
        ID of the server which should be a
        target for this Load Balancer. Required if `type` is `server`
        """
        return pulumi.get(self, "server_id")

    @server_id.setter
    def server_id(self, value: Optional[pulumi.Input[int]]):
        pulumi.set(self, "server_id", value)

    @property
    @pulumi.getter(name="usePrivateIp")
    def use_private_ip(self) -> Optional[pulumi.Input[bool]]:
        """
        use the private IP to connect to
        Load Balancer targets. Only allowed if type is `server` or
        `label_selector`.
        """
        return pulumi.get(self, "use_private_ip")

    @use_private_ip.setter
    def use_private_ip(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "use_private_ip", value)


class LoadBalancerTarget(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 ip: Optional[pulumi.Input[str]] = None,
                 label_selector: Optional[pulumi.Input[str]] = None,
                 load_balancer_id: Optional[pulumi.Input[int]] = None,
                 server_id: Optional[pulumi.Input[int]] = None,
                 type: Optional[pulumi.Input[str]] = None,
                 use_private_ip: Optional[pulumi.Input[bool]] = None,
                 __props__=None,
                 __name__=None,
                 __opts__=None):
        """
        Adds a target to a Hetzner Cloud Load Balancer.

        ## Example Usage

        ```python
        import pulumi
        import pulumi_hcloud as hcloud

        my_server = hcloud.Server("myServer",
            server_type="cx11",
            image="ubuntu-18.04")
        load_balancer = hcloud.LoadBalancer("loadBalancer",
            load_balancer_type="lb11",
            location="nbg1")
        load_balancer_target = hcloud.LoadBalancerTarget("loadBalancerTarget",
            type="server",
            load_balancer_id=load_balancer.id,
            server_id=my_server.id)
        ```

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] ip: IP address for an IP Target. Required if
               `type` is `ip`.
        :param pulumi.Input[str] label_selector: Label Selector selecting targets
               for this Load Balancer. Required if `type` is `label_selector`.
        :param pulumi.Input[int] load_balancer_id: ID of the Load Balancer to which
               the target gets attached.
        :param pulumi.Input[int] server_id: ID of the server which should be a
               target for this Load Balancer. Required if `type` is `server`
        :param pulumi.Input[str] type: Type of the target. Possible values
               `server`, `label_selector`, `ip`.
        :param pulumi.Input[bool] use_private_ip: use the private IP to connect to
               Load Balancer targets. Only allowed if type is `server` or
               `label_selector`.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: LoadBalancerTargetArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        Adds a target to a Hetzner Cloud Load Balancer.

        ## Example Usage

        ```python
        import pulumi
        import pulumi_hcloud as hcloud

        my_server = hcloud.Server("myServer",
            server_type="cx11",
            image="ubuntu-18.04")
        load_balancer = hcloud.LoadBalancer("loadBalancer",
            load_balancer_type="lb11",
            location="nbg1")
        load_balancer_target = hcloud.LoadBalancerTarget("loadBalancerTarget",
            type="server",
            load_balancer_id=load_balancer.id,
            server_id=my_server.id)
        ```

        :param str resource_name: The name of the resource.
        :param LoadBalancerTargetArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(LoadBalancerTargetArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 ip: Optional[pulumi.Input[str]] = None,
                 label_selector: Optional[pulumi.Input[str]] = None,
                 load_balancer_id: Optional[pulumi.Input[int]] = None,
                 server_id: Optional[pulumi.Input[int]] = None,
                 type: Optional[pulumi.Input[str]] = None,
                 use_private_ip: Optional[pulumi.Input[bool]] = None,
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

            __props__['ip'] = ip
            __props__['label_selector'] = label_selector
            if load_balancer_id is None and not opts.urn:
                raise TypeError("Missing required property 'load_balancer_id'")
            __props__['load_balancer_id'] = load_balancer_id
            __props__['server_id'] = server_id
            if type is None and not opts.urn:
                raise TypeError("Missing required property 'type'")
            __props__['type'] = type
            __props__['use_private_ip'] = use_private_ip
        super(LoadBalancerTarget, __self__).__init__(
            'hcloud:index/loadBalancerTarget:LoadBalancerTarget',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None,
            ip: Optional[pulumi.Input[str]] = None,
            label_selector: Optional[pulumi.Input[str]] = None,
            load_balancer_id: Optional[pulumi.Input[int]] = None,
            server_id: Optional[pulumi.Input[int]] = None,
            type: Optional[pulumi.Input[str]] = None,
            use_private_ip: Optional[pulumi.Input[bool]] = None) -> 'LoadBalancerTarget':
        """
        Get an existing LoadBalancerTarget resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] ip: IP address for an IP Target. Required if
               `type` is `ip`.
        :param pulumi.Input[str] label_selector: Label Selector selecting targets
               for this Load Balancer. Required if `type` is `label_selector`.
        :param pulumi.Input[int] load_balancer_id: ID of the Load Balancer to which
               the target gets attached.
        :param pulumi.Input[int] server_id: ID of the server which should be a
               target for this Load Balancer. Required if `type` is `server`
        :param pulumi.Input[str] type: Type of the target. Possible values
               `server`, `label_selector`, `ip`.
        :param pulumi.Input[bool] use_private_ip: use the private IP to connect to
               Load Balancer targets. Only allowed if type is `server` or
               `label_selector`.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = dict()

        __props__["ip"] = ip
        __props__["label_selector"] = label_selector
        __props__["load_balancer_id"] = load_balancer_id
        __props__["server_id"] = server_id
        __props__["type"] = type
        __props__["use_private_ip"] = use_private_ip
        return LoadBalancerTarget(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter
    def ip(self) -> pulumi.Output[Optional[str]]:
        """
        IP address for an IP Target. Required if
        `type` is `ip`.
        """
        return pulumi.get(self, "ip")

    @property
    @pulumi.getter(name="labelSelector")
    def label_selector(self) -> pulumi.Output[Optional[str]]:
        """
        Label Selector selecting targets
        for this Load Balancer. Required if `type` is `label_selector`.
        """
        return pulumi.get(self, "label_selector")

    @property
    @pulumi.getter(name="loadBalancerId")
    def load_balancer_id(self) -> pulumi.Output[int]:
        """
        ID of the Load Balancer to which
        the target gets attached.
        """
        return pulumi.get(self, "load_balancer_id")

    @property
    @pulumi.getter(name="serverId")
    def server_id(self) -> pulumi.Output[Optional[int]]:
        """
        ID of the server which should be a
        target for this Load Balancer. Required if `type` is `server`
        """
        return pulumi.get(self, "server_id")

    @property
    @pulumi.getter
    def type(self) -> pulumi.Output[str]:
        """
        Type of the target. Possible values
        `server`, `label_selector`, `ip`.
        """
        return pulumi.get(self, "type")

    @property
    @pulumi.getter(name="usePrivateIp")
    def use_private_ip(self) -> pulumi.Output[bool]:
        """
        use the private IP to connect to
        Load Balancer targets. Only allowed if type is `server` or
        `label_selector`.
        """
        return pulumi.get(self, "use_private_ip")

    def translate_output_property(self, prop):
        return _tables.CAMEL_TO_SNAKE_CASE_TABLE.get(prop) or prop

    def translate_input_property(self, prop):
        return _tables.SNAKE_TO_CAMEL_CASE_TABLE.get(prop) or prop


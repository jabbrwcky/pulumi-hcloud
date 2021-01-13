# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union
from . import _utilities, _tables

__all__ = ['NetworkSubnet']


class NetworkSubnet(pulumi.CustomResource):
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 ip_range: Optional[pulumi.Input[str]] = None,
                 network_id: Optional[pulumi.Input[int]] = None,
                 network_zone: Optional[pulumi.Input[str]] = None,
                 type: Optional[pulumi.Input[str]] = None,
                 vswitch_id: Optional[pulumi.Input[int]] = None,
                 __props__=None,
                 __name__=None,
                 __opts__=None):
        """
        Provides a Hetzner Cloud Network Subnet to represent a Subnet in the Hetzner Cloud.

        ## Example Usage

        ```python
        import pulumi
        import pulumi_hcloud as hcloud

        mynet = hcloud.Network("mynet", ip_range="10.0.0.0/8")
        foonet = hcloud.NetworkSubnet("foonet",
            network_id=mynet.id,
            type="cloud",
            network_zone="eu-central",
            ip_range="10.0.1.0/24")
        ```

        ## Import

        Network Subnet entries can be imported using a compound ID with the following format`<network-id>-<ip_range>`

        ```sh
         $ pulumi import hcloud:index/networkSubnet:NetworkSubnet mysubnet 123-10.0.0.0/24
        ```

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] ip_range: Range to allocate IPs from. Must be a subnet of the ip_range of the Network and must not overlap with any other subnets or with any destinations in routes.
        :param pulumi.Input[int] network_id: ID of the Network the subnet should be added to.
        :param pulumi.Input[str] network_zone: Name of network zone.
        :param pulumi.Input[str] type: Type of subnet. `server`, `cloud` or `vswitch`
        :param pulumi.Input[int] vswitch_id: ID of the vswitch, Required if type is `vswitch`
        """
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

            if ip_range is None and not opts.urn:
                raise TypeError("Missing required property 'ip_range'")
            __props__['ip_range'] = ip_range
            if network_id is None and not opts.urn:
                raise TypeError("Missing required property 'network_id'")
            __props__['network_id'] = network_id
            if network_zone is None and not opts.urn:
                raise TypeError("Missing required property 'network_zone'")
            __props__['network_zone'] = network_zone
            if type is None and not opts.urn:
                raise TypeError("Missing required property 'type'")
            __props__['type'] = type
            __props__['vswitch_id'] = vswitch_id
            __props__['gateway'] = None
        super(NetworkSubnet, __self__).__init__(
            'hcloud:index/networkSubnet:NetworkSubnet',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None,
            gateway: Optional[pulumi.Input[str]] = None,
            ip_range: Optional[pulumi.Input[str]] = None,
            network_id: Optional[pulumi.Input[int]] = None,
            network_zone: Optional[pulumi.Input[str]] = None,
            type: Optional[pulumi.Input[str]] = None,
            vswitch_id: Optional[pulumi.Input[int]] = None) -> 'NetworkSubnet':
        """
        Get an existing NetworkSubnet resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] ip_range: Range to allocate IPs from. Must be a subnet of the ip_range of the Network and must not overlap with any other subnets or with any destinations in routes.
        :param pulumi.Input[int] network_id: ID of the Network the subnet should be added to.
        :param pulumi.Input[str] network_zone: Name of network zone.
        :param pulumi.Input[str] type: Type of subnet. `server`, `cloud` or `vswitch`
        :param pulumi.Input[int] vswitch_id: ID of the vswitch, Required if type is `vswitch`
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = dict()

        __props__["gateway"] = gateway
        __props__["ip_range"] = ip_range
        __props__["network_id"] = network_id
        __props__["network_zone"] = network_zone
        __props__["type"] = type
        __props__["vswitch_id"] = vswitch_id
        return NetworkSubnet(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter
    def gateway(self) -> pulumi.Output[str]:
        return pulumi.get(self, "gateway")

    @property
    @pulumi.getter(name="ipRange")
    def ip_range(self) -> pulumi.Output[str]:
        """
        Range to allocate IPs from. Must be a subnet of the ip_range of the Network and must not overlap with any other subnets or with any destinations in routes.
        """
        return pulumi.get(self, "ip_range")

    @property
    @pulumi.getter(name="networkId")
    def network_id(self) -> pulumi.Output[int]:
        """
        ID of the Network the subnet should be added to.
        """
        return pulumi.get(self, "network_id")

    @property
    @pulumi.getter(name="networkZone")
    def network_zone(self) -> pulumi.Output[str]:
        """
        Name of network zone.
        """
        return pulumi.get(self, "network_zone")

    @property
    @pulumi.getter
    def type(self) -> pulumi.Output[str]:
        """
        Type of subnet. `server`, `cloud` or `vswitch`
        """
        return pulumi.get(self, "type")

    @property
    @pulumi.getter(name="vswitchId")
    def vswitch_id(self) -> pulumi.Output[Optional[int]]:
        """
        ID of the vswitch, Required if type is `vswitch`
        """
        return pulumi.get(self, "vswitch_id")

    def translate_output_property(self, prop):
        return _tables.CAMEL_TO_SNAKE_CASE_TABLE.get(prop) or prop

    def translate_input_property(self, prop):
        return _tables.SNAKE_TO_CAMEL_CASE_TABLE.get(prop) or prop


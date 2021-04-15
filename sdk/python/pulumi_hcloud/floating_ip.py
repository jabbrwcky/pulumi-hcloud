# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
from . import _utilities

__all__ = ['FloatingIpArgs', 'FloatingIp']

@pulumi.input_type
class FloatingIpArgs:
    def __init__(__self__, *,
                 type: pulumi.Input[str],
                 description: Optional[pulumi.Input[str]] = None,
                 home_location: Optional[pulumi.Input[str]] = None,
                 labels: Optional[pulumi.Input[Mapping[str, Any]]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 server_id: Optional[pulumi.Input[int]] = None):
        """
        The set of arguments for constructing a FloatingIp resource.
        :param pulumi.Input[str] type: Type of the Floating IP. `ipv4` `ipv6`
        :param pulumi.Input[str] description: Description of the Floating IP.
        :param pulumi.Input[str] home_location: Home location (routing is optimized for that location). Optional if server_id argument is passed.
        :param pulumi.Input[Mapping[str, Any]] labels: User-defined labels (key-value pairs) should be created with.
        :param pulumi.Input[str] name: Name of the Floating IP.
        :param pulumi.Input[int] server_id: Server to assign the Floating IP to.
        """
        pulumi.set(__self__, "type", type)
        if description is not None:
            pulumi.set(__self__, "description", description)
        if home_location is not None:
            pulumi.set(__self__, "home_location", home_location)
        if labels is not None:
            pulumi.set(__self__, "labels", labels)
        if name is not None:
            pulumi.set(__self__, "name", name)
        if server_id is not None:
            pulumi.set(__self__, "server_id", server_id)

    @property
    @pulumi.getter
    def type(self) -> pulumi.Input[str]:
        """
        Type of the Floating IP. `ipv4` `ipv6`
        """
        return pulumi.get(self, "type")

    @type.setter
    def type(self, value: pulumi.Input[str]):
        pulumi.set(self, "type", value)

    @property
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[str]]:
        """
        Description of the Floating IP.
        """
        return pulumi.get(self, "description")

    @description.setter
    def description(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "description", value)

    @property
    @pulumi.getter(name="homeLocation")
    def home_location(self) -> Optional[pulumi.Input[str]]:
        """
        Home location (routing is optimized for that location). Optional if server_id argument is passed.
        """
        return pulumi.get(self, "home_location")

    @home_location.setter
    def home_location(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "home_location", value)

    @property
    @pulumi.getter
    def labels(self) -> Optional[pulumi.Input[Mapping[str, Any]]]:
        """
        User-defined labels (key-value pairs) should be created with.
        """
        return pulumi.get(self, "labels")

    @labels.setter
    def labels(self, value: Optional[pulumi.Input[Mapping[str, Any]]]):
        pulumi.set(self, "labels", value)

    @property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[str]]:
        """
        Name of the Floating IP.
        """
        return pulumi.get(self, "name")

    @name.setter
    def name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "name", value)

    @property
    @pulumi.getter(name="serverId")
    def server_id(self) -> Optional[pulumi.Input[int]]:
        """
        Server to assign the Floating IP to.
        """
        return pulumi.get(self, "server_id")

    @server_id.setter
    def server_id(self, value: Optional[pulumi.Input[int]]):
        pulumi.set(self, "server_id", value)


@pulumi.input_type
class _FloatingIpState:
    def __init__(__self__, *,
                 description: Optional[pulumi.Input[str]] = None,
                 home_location: Optional[pulumi.Input[str]] = None,
                 ip_address: Optional[pulumi.Input[str]] = None,
                 ip_network: Optional[pulumi.Input[str]] = None,
                 labels: Optional[pulumi.Input[Mapping[str, Any]]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 server_id: Optional[pulumi.Input[int]] = None,
                 type: Optional[pulumi.Input[str]] = None):
        """
        Input properties used for looking up and filtering FloatingIp resources.
        :param pulumi.Input[str] description: Description of the Floating IP.
        :param pulumi.Input[str] home_location: Home location (routing is optimized for that location). Optional if server_id argument is passed.
        :param pulumi.Input[str] ip_address: (string) IP Address of the Floating IP.
        :param pulumi.Input[str] ip_network: (string) IPv6 subnet. (Only set if `type` is `ipv6`)
        :param pulumi.Input[Mapping[str, Any]] labels: User-defined labels (key-value pairs) should be created with.
        :param pulumi.Input[str] name: Name of the Floating IP.
        :param pulumi.Input[int] server_id: Server to assign the Floating IP to.
        :param pulumi.Input[str] type: Type of the Floating IP. `ipv4` `ipv6`
        """
        if description is not None:
            pulumi.set(__self__, "description", description)
        if home_location is not None:
            pulumi.set(__self__, "home_location", home_location)
        if ip_address is not None:
            pulumi.set(__self__, "ip_address", ip_address)
        if ip_network is not None:
            pulumi.set(__self__, "ip_network", ip_network)
        if labels is not None:
            pulumi.set(__self__, "labels", labels)
        if name is not None:
            pulumi.set(__self__, "name", name)
        if server_id is not None:
            pulumi.set(__self__, "server_id", server_id)
        if type is not None:
            pulumi.set(__self__, "type", type)

    @property
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[str]]:
        """
        Description of the Floating IP.
        """
        return pulumi.get(self, "description")

    @description.setter
    def description(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "description", value)

    @property
    @pulumi.getter(name="homeLocation")
    def home_location(self) -> Optional[pulumi.Input[str]]:
        """
        Home location (routing is optimized for that location). Optional if server_id argument is passed.
        """
        return pulumi.get(self, "home_location")

    @home_location.setter
    def home_location(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "home_location", value)

    @property
    @pulumi.getter(name="ipAddress")
    def ip_address(self) -> Optional[pulumi.Input[str]]:
        """
        (string) IP Address of the Floating IP.
        """
        return pulumi.get(self, "ip_address")

    @ip_address.setter
    def ip_address(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "ip_address", value)

    @property
    @pulumi.getter(name="ipNetwork")
    def ip_network(self) -> Optional[pulumi.Input[str]]:
        """
        (string) IPv6 subnet. (Only set if `type` is `ipv6`)
        """
        return pulumi.get(self, "ip_network")

    @ip_network.setter
    def ip_network(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "ip_network", value)

    @property
    @pulumi.getter
    def labels(self) -> Optional[pulumi.Input[Mapping[str, Any]]]:
        """
        User-defined labels (key-value pairs) should be created with.
        """
        return pulumi.get(self, "labels")

    @labels.setter
    def labels(self, value: Optional[pulumi.Input[Mapping[str, Any]]]):
        pulumi.set(self, "labels", value)

    @property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[str]]:
        """
        Name of the Floating IP.
        """
        return pulumi.get(self, "name")

    @name.setter
    def name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "name", value)

    @property
    @pulumi.getter(name="serverId")
    def server_id(self) -> Optional[pulumi.Input[int]]:
        """
        Server to assign the Floating IP to.
        """
        return pulumi.get(self, "server_id")

    @server_id.setter
    def server_id(self, value: Optional[pulumi.Input[int]]):
        pulumi.set(self, "server_id", value)

    @property
    @pulumi.getter
    def type(self) -> Optional[pulumi.Input[str]]:
        """
        Type of the Floating IP. `ipv4` `ipv6`
        """
        return pulumi.get(self, "type")

    @type.setter
    def type(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "type", value)


class FloatingIp(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 description: Optional[pulumi.Input[str]] = None,
                 home_location: Optional[pulumi.Input[str]] = None,
                 labels: Optional[pulumi.Input[Mapping[str, Any]]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 server_id: Optional[pulumi.Input[int]] = None,
                 type: Optional[pulumi.Input[str]] = None,
                 __props__=None,
                 __name__=None,
                 __opts__=None):
        """
        Provides a Hetzner Cloud Floating IP to represent a publicly-accessible static IP address that can be mapped to one of your servers.

        ## Example Usage

        ```python
        import pulumi
        import pulumi_hcloud as hcloud

        node1 = hcloud.Server("node1",
            image="debian-9",
            server_type="cx11")
        master = hcloud.FloatingIp("master",
            type="ipv4",
            server_id=node1.id)
        ```

        ## Import

        Floating IPs can be imported using its `id`

        ```sh
         $ pulumi import hcloud:index/floatingIp:FloatingIp myip <id>
        ```

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] description: Description of the Floating IP.
        :param pulumi.Input[str] home_location: Home location (routing is optimized for that location). Optional if server_id argument is passed.
        :param pulumi.Input[Mapping[str, Any]] labels: User-defined labels (key-value pairs) should be created with.
        :param pulumi.Input[str] name: Name of the Floating IP.
        :param pulumi.Input[int] server_id: Server to assign the Floating IP to.
        :param pulumi.Input[str] type: Type of the Floating IP. `ipv4` `ipv6`
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: FloatingIpArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        Provides a Hetzner Cloud Floating IP to represent a publicly-accessible static IP address that can be mapped to one of your servers.

        ## Example Usage

        ```python
        import pulumi
        import pulumi_hcloud as hcloud

        node1 = hcloud.Server("node1",
            image="debian-9",
            server_type="cx11")
        master = hcloud.FloatingIp("master",
            type="ipv4",
            server_id=node1.id)
        ```

        ## Import

        Floating IPs can be imported using its `id`

        ```sh
         $ pulumi import hcloud:index/floatingIp:FloatingIp myip <id>
        ```

        :param str resource_name: The name of the resource.
        :param FloatingIpArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(FloatingIpArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 description: Optional[pulumi.Input[str]] = None,
                 home_location: Optional[pulumi.Input[str]] = None,
                 labels: Optional[pulumi.Input[Mapping[str, Any]]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 server_id: Optional[pulumi.Input[int]] = None,
                 type: Optional[pulumi.Input[str]] = None,
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
            __props__ = FloatingIpArgs.__new__(FloatingIpArgs)

            __props__.__dict__["description"] = description
            __props__.__dict__["home_location"] = home_location
            __props__.__dict__["labels"] = labels
            __props__.__dict__["name"] = name
            __props__.__dict__["server_id"] = server_id
            if type is None and not opts.urn:
                raise TypeError("Missing required property 'type'")
            __props__.__dict__["type"] = type
            __props__.__dict__["ip_address"] = None
            __props__.__dict__["ip_network"] = None
        super(FloatingIp, __self__).__init__(
            'hcloud:index/floatingIp:FloatingIp',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None,
            description: Optional[pulumi.Input[str]] = None,
            home_location: Optional[pulumi.Input[str]] = None,
            ip_address: Optional[pulumi.Input[str]] = None,
            ip_network: Optional[pulumi.Input[str]] = None,
            labels: Optional[pulumi.Input[Mapping[str, Any]]] = None,
            name: Optional[pulumi.Input[str]] = None,
            server_id: Optional[pulumi.Input[int]] = None,
            type: Optional[pulumi.Input[str]] = None) -> 'FloatingIp':
        """
        Get an existing FloatingIp resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] description: Description of the Floating IP.
        :param pulumi.Input[str] home_location: Home location (routing is optimized for that location). Optional if server_id argument is passed.
        :param pulumi.Input[str] ip_address: (string) IP Address of the Floating IP.
        :param pulumi.Input[str] ip_network: (string) IPv6 subnet. (Only set if `type` is `ipv6`)
        :param pulumi.Input[Mapping[str, Any]] labels: User-defined labels (key-value pairs) should be created with.
        :param pulumi.Input[str] name: Name of the Floating IP.
        :param pulumi.Input[int] server_id: Server to assign the Floating IP to.
        :param pulumi.Input[str] type: Type of the Floating IP. `ipv4` `ipv6`
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = _FloatingIpState.__new__(_FloatingIpState)

        __props__.__dict__["description"] = description
        __props__.__dict__["home_location"] = home_location
        __props__.__dict__["ip_address"] = ip_address
        __props__.__dict__["ip_network"] = ip_network
        __props__.__dict__["labels"] = labels
        __props__.__dict__["name"] = name
        __props__.__dict__["server_id"] = server_id
        __props__.__dict__["type"] = type
        return FloatingIp(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter
    def description(self) -> pulumi.Output[Optional[str]]:
        """
        Description of the Floating IP.
        """
        return pulumi.get(self, "description")

    @property
    @pulumi.getter(name="homeLocation")
    def home_location(self) -> pulumi.Output[str]:
        """
        Home location (routing is optimized for that location). Optional if server_id argument is passed.
        """
        return pulumi.get(self, "home_location")

    @property
    @pulumi.getter(name="ipAddress")
    def ip_address(self) -> pulumi.Output[str]:
        """
        (string) IP Address of the Floating IP.
        """
        return pulumi.get(self, "ip_address")

    @property
    @pulumi.getter(name="ipNetwork")
    def ip_network(self) -> pulumi.Output[str]:
        """
        (string) IPv6 subnet. (Only set if `type` is `ipv6`)
        """
        return pulumi.get(self, "ip_network")

    @property
    @pulumi.getter
    def labels(self) -> pulumi.Output[Optional[Mapping[str, Any]]]:
        """
        User-defined labels (key-value pairs) should be created with.
        """
        return pulumi.get(self, "labels")

    @property
    @pulumi.getter
    def name(self) -> pulumi.Output[str]:
        """
        Name of the Floating IP.
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter(name="serverId")
    def server_id(self) -> pulumi.Output[int]:
        """
        Server to assign the Floating IP to.
        """
        return pulumi.get(self, "server_id")

    @property
    @pulumi.getter
    def type(self) -> pulumi.Output[str]:
        """
        Type of the Floating IP. `ipv4` `ipv6`
        """
        return pulumi.get(self, "type")


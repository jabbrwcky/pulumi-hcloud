# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
from . import _utilities
from . import outputs
from ._inputs import *

__all__ = ['ServerArgs', 'Server']

@pulumi.input_type
class ServerArgs:
    def __init__(__self__, *,
                 image: pulumi.Input[str],
                 server_type: pulumi.Input[str],
                 backups: Optional[pulumi.Input[bool]] = None,
                 datacenter: Optional[pulumi.Input[str]] = None,
                 firewall_ids: Optional[pulumi.Input[Sequence[pulumi.Input[int]]]] = None,
                 iso: Optional[pulumi.Input[str]] = None,
                 keep_disk: Optional[pulumi.Input[bool]] = None,
                 labels: Optional[pulumi.Input[Mapping[str, Any]]] = None,
                 location: Optional[pulumi.Input[str]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 networks: Optional[pulumi.Input[Sequence[pulumi.Input['ServerNetworkArgs']]]] = None,
                 rescue: Optional[pulumi.Input[str]] = None,
                 ssh_keys: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 user_data: Optional[pulumi.Input[str]] = None):
        """
        The set of arguments for constructing a Server resource.
        :param pulumi.Input[str] image: Name or ID of the image the server is created from.
        :param pulumi.Input[str] server_type: Name of the server type this server should be created with.
        :param pulumi.Input[bool] backups: Enable or disable backups.
        :param pulumi.Input[str] datacenter: The datacenter name to create the server in.
        :param pulumi.Input[str] iso: ID or Name of an ISO image to mount.
        :param pulumi.Input[bool] keep_disk: If true, do not upgrade the disk. This allows downgrading the server type later.
        :param pulumi.Input[Mapping[str, Any]] labels: User-defined labels (key-value pairs) should be created with.
        :param pulumi.Input[str] location: The location name to create the server in. `nbg1`, `fsn1` or `hel1`
        :param pulumi.Input[str] name: Name of the server to create (must be unique per project and a valid hostname as per RFC 1123).
        :param pulumi.Input[str] rescue: Enable and boot in to the specified rescue system. This enables simple installation of custom operating systems. `linux64` `linux32` or `freebsd64`
        :param pulumi.Input[Sequence[pulumi.Input[str]]] ssh_keys: SSH key IDs or names which should be injected into the server at creation time
        :param pulumi.Input[str] user_data: Cloud-Init user data to use during server creation
        """
        pulumi.set(__self__, "image", image)
        pulumi.set(__self__, "server_type", server_type)
        if backups is not None:
            pulumi.set(__self__, "backups", backups)
        if datacenter is not None:
            pulumi.set(__self__, "datacenter", datacenter)
        if firewall_ids is not None:
            pulumi.set(__self__, "firewall_ids", firewall_ids)
        if iso is not None:
            pulumi.set(__self__, "iso", iso)
        if keep_disk is not None:
            pulumi.set(__self__, "keep_disk", keep_disk)
        if labels is not None:
            pulumi.set(__self__, "labels", labels)
        if location is not None:
            pulumi.set(__self__, "location", location)
        if name is not None:
            pulumi.set(__self__, "name", name)
        if networks is not None:
            pulumi.set(__self__, "networks", networks)
        if rescue is not None:
            pulumi.set(__self__, "rescue", rescue)
        if ssh_keys is not None:
            pulumi.set(__self__, "ssh_keys", ssh_keys)
        if user_data is not None:
            pulumi.set(__self__, "user_data", user_data)

    @property
    @pulumi.getter
    def image(self) -> pulumi.Input[str]:
        """
        Name or ID of the image the server is created from.
        """
        return pulumi.get(self, "image")

    @image.setter
    def image(self, value: pulumi.Input[str]):
        pulumi.set(self, "image", value)

    @property
    @pulumi.getter(name="serverType")
    def server_type(self) -> pulumi.Input[str]:
        """
        Name of the server type this server should be created with.
        """
        return pulumi.get(self, "server_type")

    @server_type.setter
    def server_type(self, value: pulumi.Input[str]):
        pulumi.set(self, "server_type", value)

    @property
    @pulumi.getter
    def backups(self) -> Optional[pulumi.Input[bool]]:
        """
        Enable or disable backups.
        """
        return pulumi.get(self, "backups")

    @backups.setter
    def backups(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "backups", value)

    @property
    @pulumi.getter
    def datacenter(self) -> Optional[pulumi.Input[str]]:
        """
        The datacenter name to create the server in.
        """
        return pulumi.get(self, "datacenter")

    @datacenter.setter
    def datacenter(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "datacenter", value)

    @property
    @pulumi.getter(name="firewallIds")
    def firewall_ids(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[int]]]]:
        return pulumi.get(self, "firewall_ids")

    @firewall_ids.setter
    def firewall_ids(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[int]]]]):
        pulumi.set(self, "firewall_ids", value)

    @property
    @pulumi.getter
    def iso(self) -> Optional[pulumi.Input[str]]:
        """
        ID or Name of an ISO image to mount.
        """
        return pulumi.get(self, "iso")

    @iso.setter
    def iso(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "iso", value)

    @property
    @pulumi.getter(name="keepDisk")
    def keep_disk(self) -> Optional[pulumi.Input[bool]]:
        """
        If true, do not upgrade the disk. This allows downgrading the server type later.
        """
        return pulumi.get(self, "keep_disk")

    @keep_disk.setter
    def keep_disk(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "keep_disk", value)

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
    def location(self) -> Optional[pulumi.Input[str]]:
        """
        The location name to create the server in. `nbg1`, `fsn1` or `hel1`
        """
        return pulumi.get(self, "location")

    @location.setter
    def location(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "location", value)

    @property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[str]]:
        """
        Name of the server to create (must be unique per project and a valid hostname as per RFC 1123).
        """
        return pulumi.get(self, "name")

    @name.setter
    def name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "name", value)

    @property
    @pulumi.getter
    def networks(self) -> Optional[pulumi.Input[Sequence[pulumi.Input['ServerNetworkArgs']]]]:
        return pulumi.get(self, "networks")

    @networks.setter
    def networks(self, value: Optional[pulumi.Input[Sequence[pulumi.Input['ServerNetworkArgs']]]]):
        pulumi.set(self, "networks", value)

    @property
    @pulumi.getter
    def rescue(self) -> Optional[pulumi.Input[str]]:
        """
        Enable and boot in to the specified rescue system. This enables simple installation of custom operating systems. `linux64` `linux32` or `freebsd64`
        """
        return pulumi.get(self, "rescue")

    @rescue.setter
    def rescue(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "rescue", value)

    @property
    @pulumi.getter(name="sshKeys")
    def ssh_keys(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]:
        """
        SSH key IDs or names which should be injected into the server at creation time
        """
        return pulumi.get(self, "ssh_keys")

    @ssh_keys.setter
    def ssh_keys(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]):
        pulumi.set(self, "ssh_keys", value)

    @property
    @pulumi.getter(name="userData")
    def user_data(self) -> Optional[pulumi.Input[str]]:
        """
        Cloud-Init user data to use during server creation
        """
        return pulumi.get(self, "user_data")

    @user_data.setter
    def user_data(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "user_data", value)


@pulumi.input_type
class _ServerState:
    def __init__(__self__, *,
                 backup_window: Optional[pulumi.Input[str]] = None,
                 backups: Optional[pulumi.Input[bool]] = None,
                 datacenter: Optional[pulumi.Input[str]] = None,
                 firewall_ids: Optional[pulumi.Input[Sequence[pulumi.Input[int]]]] = None,
                 image: Optional[pulumi.Input[str]] = None,
                 ipv4_address: Optional[pulumi.Input[str]] = None,
                 ipv6_address: Optional[pulumi.Input[str]] = None,
                 ipv6_network: Optional[pulumi.Input[str]] = None,
                 iso: Optional[pulumi.Input[str]] = None,
                 keep_disk: Optional[pulumi.Input[bool]] = None,
                 labels: Optional[pulumi.Input[Mapping[str, Any]]] = None,
                 location: Optional[pulumi.Input[str]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 networks: Optional[pulumi.Input[Sequence[pulumi.Input['ServerNetworkArgs']]]] = None,
                 rescue: Optional[pulumi.Input[str]] = None,
                 server_type: Optional[pulumi.Input[str]] = None,
                 ssh_keys: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 status: Optional[pulumi.Input[str]] = None,
                 user_data: Optional[pulumi.Input[str]] = None):
        """
        Input properties used for looking up and filtering Server resources.
        :param pulumi.Input[str] backup_window: (string) The backup window of the server, if enabled.
        :param pulumi.Input[bool] backups: Enable or disable backups.
        :param pulumi.Input[str] datacenter: The datacenter name to create the server in.
        :param pulumi.Input[str] image: Name or ID of the image the server is created from.
        :param pulumi.Input[str] ipv4_address: (string) The IPv4 address.
        :param pulumi.Input[str] ipv6_address: (string) The first IPv6 address of the assigned network.
        :param pulumi.Input[str] ipv6_network: (string) The IPv6 network.
        :param pulumi.Input[str] iso: ID or Name of an ISO image to mount.
        :param pulumi.Input[bool] keep_disk: If true, do not upgrade the disk. This allows downgrading the server type later.
        :param pulumi.Input[Mapping[str, Any]] labels: User-defined labels (key-value pairs) should be created with.
        :param pulumi.Input[str] location: The location name to create the server in. `nbg1`, `fsn1` or `hel1`
        :param pulumi.Input[str] name: Name of the server to create (must be unique per project and a valid hostname as per RFC 1123).
        :param pulumi.Input[str] rescue: Enable and boot in to the specified rescue system. This enables simple installation of custom operating systems. `linux64` `linux32` or `freebsd64`
        :param pulumi.Input[str] server_type: Name of the server type this server should be created with.
        :param pulumi.Input[Sequence[pulumi.Input[str]]] ssh_keys: SSH key IDs or names which should be injected into the server at creation time
        :param pulumi.Input[str] status: (string) The status of the server.
        :param pulumi.Input[str] user_data: Cloud-Init user data to use during server creation
        """
        if backup_window is not None:
            warnings.warn("""You should remove this property from your terraform configuration.""", DeprecationWarning)
            pulumi.log.warn("""backup_window is deprecated: You should remove this property from your terraform configuration.""")
        if backup_window is not None:
            pulumi.set(__self__, "backup_window", backup_window)
        if backups is not None:
            pulumi.set(__self__, "backups", backups)
        if datacenter is not None:
            pulumi.set(__self__, "datacenter", datacenter)
        if firewall_ids is not None:
            pulumi.set(__self__, "firewall_ids", firewall_ids)
        if image is not None:
            pulumi.set(__self__, "image", image)
        if ipv4_address is not None:
            pulumi.set(__self__, "ipv4_address", ipv4_address)
        if ipv6_address is not None:
            pulumi.set(__self__, "ipv6_address", ipv6_address)
        if ipv6_network is not None:
            pulumi.set(__self__, "ipv6_network", ipv6_network)
        if iso is not None:
            pulumi.set(__self__, "iso", iso)
        if keep_disk is not None:
            pulumi.set(__self__, "keep_disk", keep_disk)
        if labels is not None:
            pulumi.set(__self__, "labels", labels)
        if location is not None:
            pulumi.set(__self__, "location", location)
        if name is not None:
            pulumi.set(__self__, "name", name)
        if networks is not None:
            pulumi.set(__self__, "networks", networks)
        if rescue is not None:
            pulumi.set(__self__, "rescue", rescue)
        if server_type is not None:
            pulumi.set(__self__, "server_type", server_type)
        if ssh_keys is not None:
            pulumi.set(__self__, "ssh_keys", ssh_keys)
        if status is not None:
            pulumi.set(__self__, "status", status)
        if user_data is not None:
            pulumi.set(__self__, "user_data", user_data)

    @property
    @pulumi.getter(name="backupWindow")
    def backup_window(self) -> Optional[pulumi.Input[str]]:
        """
        (string) The backup window of the server, if enabled.
        """
        return pulumi.get(self, "backup_window")

    @backup_window.setter
    def backup_window(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "backup_window", value)

    @property
    @pulumi.getter
    def backups(self) -> Optional[pulumi.Input[bool]]:
        """
        Enable or disable backups.
        """
        return pulumi.get(self, "backups")

    @backups.setter
    def backups(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "backups", value)

    @property
    @pulumi.getter
    def datacenter(self) -> Optional[pulumi.Input[str]]:
        """
        The datacenter name to create the server in.
        """
        return pulumi.get(self, "datacenter")

    @datacenter.setter
    def datacenter(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "datacenter", value)

    @property
    @pulumi.getter(name="firewallIds")
    def firewall_ids(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[int]]]]:
        return pulumi.get(self, "firewall_ids")

    @firewall_ids.setter
    def firewall_ids(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[int]]]]):
        pulumi.set(self, "firewall_ids", value)

    @property
    @pulumi.getter
    def image(self) -> Optional[pulumi.Input[str]]:
        """
        Name or ID of the image the server is created from.
        """
        return pulumi.get(self, "image")

    @image.setter
    def image(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "image", value)

    @property
    @pulumi.getter(name="ipv4Address")
    def ipv4_address(self) -> Optional[pulumi.Input[str]]:
        """
        (string) The IPv4 address.
        """
        return pulumi.get(self, "ipv4_address")

    @ipv4_address.setter
    def ipv4_address(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "ipv4_address", value)

    @property
    @pulumi.getter(name="ipv6Address")
    def ipv6_address(self) -> Optional[pulumi.Input[str]]:
        """
        (string) The first IPv6 address of the assigned network.
        """
        return pulumi.get(self, "ipv6_address")

    @ipv6_address.setter
    def ipv6_address(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "ipv6_address", value)

    @property
    @pulumi.getter(name="ipv6Network")
    def ipv6_network(self) -> Optional[pulumi.Input[str]]:
        """
        (string) The IPv6 network.
        """
        return pulumi.get(self, "ipv6_network")

    @ipv6_network.setter
    def ipv6_network(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "ipv6_network", value)

    @property
    @pulumi.getter
    def iso(self) -> Optional[pulumi.Input[str]]:
        """
        ID or Name of an ISO image to mount.
        """
        return pulumi.get(self, "iso")

    @iso.setter
    def iso(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "iso", value)

    @property
    @pulumi.getter(name="keepDisk")
    def keep_disk(self) -> Optional[pulumi.Input[bool]]:
        """
        If true, do not upgrade the disk. This allows downgrading the server type later.
        """
        return pulumi.get(self, "keep_disk")

    @keep_disk.setter
    def keep_disk(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "keep_disk", value)

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
    def location(self) -> Optional[pulumi.Input[str]]:
        """
        The location name to create the server in. `nbg1`, `fsn1` or `hel1`
        """
        return pulumi.get(self, "location")

    @location.setter
    def location(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "location", value)

    @property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[str]]:
        """
        Name of the server to create (must be unique per project and a valid hostname as per RFC 1123).
        """
        return pulumi.get(self, "name")

    @name.setter
    def name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "name", value)

    @property
    @pulumi.getter
    def networks(self) -> Optional[pulumi.Input[Sequence[pulumi.Input['ServerNetworkArgs']]]]:
        return pulumi.get(self, "networks")

    @networks.setter
    def networks(self, value: Optional[pulumi.Input[Sequence[pulumi.Input['ServerNetworkArgs']]]]):
        pulumi.set(self, "networks", value)

    @property
    @pulumi.getter
    def rescue(self) -> Optional[pulumi.Input[str]]:
        """
        Enable and boot in to the specified rescue system. This enables simple installation of custom operating systems. `linux64` `linux32` or `freebsd64`
        """
        return pulumi.get(self, "rescue")

    @rescue.setter
    def rescue(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "rescue", value)

    @property
    @pulumi.getter(name="serverType")
    def server_type(self) -> Optional[pulumi.Input[str]]:
        """
        Name of the server type this server should be created with.
        """
        return pulumi.get(self, "server_type")

    @server_type.setter
    def server_type(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "server_type", value)

    @property
    @pulumi.getter(name="sshKeys")
    def ssh_keys(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]:
        """
        SSH key IDs or names which should be injected into the server at creation time
        """
        return pulumi.get(self, "ssh_keys")

    @ssh_keys.setter
    def ssh_keys(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]):
        pulumi.set(self, "ssh_keys", value)

    @property
    @pulumi.getter
    def status(self) -> Optional[pulumi.Input[str]]:
        """
        (string) The status of the server.
        """
        return pulumi.get(self, "status")

    @status.setter
    def status(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "status", value)

    @property
    @pulumi.getter(name="userData")
    def user_data(self) -> Optional[pulumi.Input[str]]:
        """
        Cloud-Init user data to use during server creation
        """
        return pulumi.get(self, "user_data")

    @user_data.setter
    def user_data(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "user_data", value)


class Server(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 backups: Optional[pulumi.Input[bool]] = None,
                 datacenter: Optional[pulumi.Input[str]] = None,
                 firewall_ids: Optional[pulumi.Input[Sequence[pulumi.Input[int]]]] = None,
                 image: Optional[pulumi.Input[str]] = None,
                 iso: Optional[pulumi.Input[str]] = None,
                 keep_disk: Optional[pulumi.Input[bool]] = None,
                 labels: Optional[pulumi.Input[Mapping[str, Any]]] = None,
                 location: Optional[pulumi.Input[str]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 networks: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['ServerNetworkArgs']]]]] = None,
                 rescue: Optional[pulumi.Input[str]] = None,
                 server_type: Optional[pulumi.Input[str]] = None,
                 ssh_keys: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 user_data: Optional[pulumi.Input[str]] = None,
                 __props__=None,
                 __name__=None,
                 __opts__=None):
        """
        ## Import

        Servers can be imported using the server `id`

        ```sh
         $ pulumi import hcloud:index/server:Server myserver <id>
        ```

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[bool] backups: Enable or disable backups.
        :param pulumi.Input[str] datacenter: The datacenter name to create the server in.
        :param pulumi.Input[str] image: Name or ID of the image the server is created from.
        :param pulumi.Input[str] iso: ID or Name of an ISO image to mount.
        :param pulumi.Input[bool] keep_disk: If true, do not upgrade the disk. This allows downgrading the server type later.
        :param pulumi.Input[Mapping[str, Any]] labels: User-defined labels (key-value pairs) should be created with.
        :param pulumi.Input[str] location: The location name to create the server in. `nbg1`, `fsn1` or `hel1`
        :param pulumi.Input[str] name: Name of the server to create (must be unique per project and a valid hostname as per RFC 1123).
        :param pulumi.Input[str] rescue: Enable and boot in to the specified rescue system. This enables simple installation of custom operating systems. `linux64` `linux32` or `freebsd64`
        :param pulumi.Input[str] server_type: Name of the server type this server should be created with.
        :param pulumi.Input[Sequence[pulumi.Input[str]]] ssh_keys: SSH key IDs or names which should be injected into the server at creation time
        :param pulumi.Input[str] user_data: Cloud-Init user data to use during server creation
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: ServerArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        ## Import

        Servers can be imported using the server `id`

        ```sh
         $ pulumi import hcloud:index/server:Server myserver <id>
        ```

        :param str resource_name: The name of the resource.
        :param ServerArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(ServerArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 backups: Optional[pulumi.Input[bool]] = None,
                 datacenter: Optional[pulumi.Input[str]] = None,
                 firewall_ids: Optional[pulumi.Input[Sequence[pulumi.Input[int]]]] = None,
                 image: Optional[pulumi.Input[str]] = None,
                 iso: Optional[pulumi.Input[str]] = None,
                 keep_disk: Optional[pulumi.Input[bool]] = None,
                 labels: Optional[pulumi.Input[Mapping[str, Any]]] = None,
                 location: Optional[pulumi.Input[str]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 networks: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['ServerNetworkArgs']]]]] = None,
                 rescue: Optional[pulumi.Input[str]] = None,
                 server_type: Optional[pulumi.Input[str]] = None,
                 ssh_keys: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 user_data: Optional[pulumi.Input[str]] = None,
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
            __props__ = ServerArgs.__new__(ServerArgs)

            __props__.__dict__["backups"] = backups
            __props__.__dict__["datacenter"] = datacenter
            __props__.__dict__["firewall_ids"] = firewall_ids
            if image is None and not opts.urn:
                raise TypeError("Missing required property 'image'")
            __props__.__dict__["image"] = image
            __props__.__dict__["iso"] = iso
            __props__.__dict__["keep_disk"] = keep_disk
            __props__.__dict__["labels"] = labels
            __props__.__dict__["location"] = location
            __props__.__dict__["name"] = name
            __props__.__dict__["networks"] = networks
            __props__.__dict__["rescue"] = rescue
            if server_type is None and not opts.urn:
                raise TypeError("Missing required property 'server_type'")
            __props__.__dict__["server_type"] = server_type
            __props__.__dict__["ssh_keys"] = ssh_keys
            __props__.__dict__["user_data"] = user_data
            __props__.__dict__["backup_window"] = None
            __props__.__dict__["ipv4_address"] = None
            __props__.__dict__["ipv6_address"] = None
            __props__.__dict__["ipv6_network"] = None
            __props__.__dict__["status"] = None
        super(Server, __self__).__init__(
            'hcloud:index/server:Server',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None,
            backup_window: Optional[pulumi.Input[str]] = None,
            backups: Optional[pulumi.Input[bool]] = None,
            datacenter: Optional[pulumi.Input[str]] = None,
            firewall_ids: Optional[pulumi.Input[Sequence[pulumi.Input[int]]]] = None,
            image: Optional[pulumi.Input[str]] = None,
            ipv4_address: Optional[pulumi.Input[str]] = None,
            ipv6_address: Optional[pulumi.Input[str]] = None,
            ipv6_network: Optional[pulumi.Input[str]] = None,
            iso: Optional[pulumi.Input[str]] = None,
            keep_disk: Optional[pulumi.Input[bool]] = None,
            labels: Optional[pulumi.Input[Mapping[str, Any]]] = None,
            location: Optional[pulumi.Input[str]] = None,
            name: Optional[pulumi.Input[str]] = None,
            networks: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['ServerNetworkArgs']]]]] = None,
            rescue: Optional[pulumi.Input[str]] = None,
            server_type: Optional[pulumi.Input[str]] = None,
            ssh_keys: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
            status: Optional[pulumi.Input[str]] = None,
            user_data: Optional[pulumi.Input[str]] = None) -> 'Server':
        """
        Get an existing Server resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] backup_window: (string) The backup window of the server, if enabled.
        :param pulumi.Input[bool] backups: Enable or disable backups.
        :param pulumi.Input[str] datacenter: The datacenter name to create the server in.
        :param pulumi.Input[str] image: Name or ID of the image the server is created from.
        :param pulumi.Input[str] ipv4_address: (string) The IPv4 address.
        :param pulumi.Input[str] ipv6_address: (string) The first IPv6 address of the assigned network.
        :param pulumi.Input[str] ipv6_network: (string) The IPv6 network.
        :param pulumi.Input[str] iso: ID or Name of an ISO image to mount.
        :param pulumi.Input[bool] keep_disk: If true, do not upgrade the disk. This allows downgrading the server type later.
        :param pulumi.Input[Mapping[str, Any]] labels: User-defined labels (key-value pairs) should be created with.
        :param pulumi.Input[str] location: The location name to create the server in. `nbg1`, `fsn1` or `hel1`
        :param pulumi.Input[str] name: Name of the server to create (must be unique per project and a valid hostname as per RFC 1123).
        :param pulumi.Input[str] rescue: Enable and boot in to the specified rescue system. This enables simple installation of custom operating systems. `linux64` `linux32` or `freebsd64`
        :param pulumi.Input[str] server_type: Name of the server type this server should be created with.
        :param pulumi.Input[Sequence[pulumi.Input[str]]] ssh_keys: SSH key IDs or names which should be injected into the server at creation time
        :param pulumi.Input[str] status: (string) The status of the server.
        :param pulumi.Input[str] user_data: Cloud-Init user data to use during server creation
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = _ServerState.__new__(_ServerState)

        __props__.__dict__["backup_window"] = backup_window
        __props__.__dict__["backups"] = backups
        __props__.__dict__["datacenter"] = datacenter
        __props__.__dict__["firewall_ids"] = firewall_ids
        __props__.__dict__["image"] = image
        __props__.__dict__["ipv4_address"] = ipv4_address
        __props__.__dict__["ipv6_address"] = ipv6_address
        __props__.__dict__["ipv6_network"] = ipv6_network
        __props__.__dict__["iso"] = iso
        __props__.__dict__["keep_disk"] = keep_disk
        __props__.__dict__["labels"] = labels
        __props__.__dict__["location"] = location
        __props__.__dict__["name"] = name
        __props__.__dict__["networks"] = networks
        __props__.__dict__["rescue"] = rescue
        __props__.__dict__["server_type"] = server_type
        __props__.__dict__["ssh_keys"] = ssh_keys
        __props__.__dict__["status"] = status
        __props__.__dict__["user_data"] = user_data
        return Server(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="backupWindow")
    def backup_window(self) -> pulumi.Output[str]:
        """
        (string) The backup window of the server, if enabled.
        """
        return pulumi.get(self, "backup_window")

    @property
    @pulumi.getter
    def backups(self) -> pulumi.Output[Optional[bool]]:
        """
        Enable or disable backups.
        """
        return pulumi.get(self, "backups")

    @property
    @pulumi.getter
    def datacenter(self) -> pulumi.Output[str]:
        """
        The datacenter name to create the server in.
        """
        return pulumi.get(self, "datacenter")

    @property
    @pulumi.getter(name="firewallIds")
    def firewall_ids(self) -> pulumi.Output[Optional[Sequence[int]]]:
        return pulumi.get(self, "firewall_ids")

    @property
    @pulumi.getter
    def image(self) -> pulumi.Output[str]:
        """
        Name or ID of the image the server is created from.
        """
        return pulumi.get(self, "image")

    @property
    @pulumi.getter(name="ipv4Address")
    def ipv4_address(self) -> pulumi.Output[str]:
        """
        (string) The IPv4 address.
        """
        return pulumi.get(self, "ipv4_address")

    @property
    @pulumi.getter(name="ipv6Address")
    def ipv6_address(self) -> pulumi.Output[str]:
        """
        (string) The first IPv6 address of the assigned network.
        """
        return pulumi.get(self, "ipv6_address")

    @property
    @pulumi.getter(name="ipv6Network")
    def ipv6_network(self) -> pulumi.Output[str]:
        """
        (string) The IPv6 network.
        """
        return pulumi.get(self, "ipv6_network")

    @property
    @pulumi.getter
    def iso(self) -> pulumi.Output[Optional[str]]:
        """
        ID or Name of an ISO image to mount.
        """
        return pulumi.get(self, "iso")

    @property
    @pulumi.getter(name="keepDisk")
    def keep_disk(self) -> pulumi.Output[Optional[bool]]:
        """
        If true, do not upgrade the disk. This allows downgrading the server type later.
        """
        return pulumi.get(self, "keep_disk")

    @property
    @pulumi.getter
    def labels(self) -> pulumi.Output[Optional[Mapping[str, Any]]]:
        """
        User-defined labels (key-value pairs) should be created with.
        """
        return pulumi.get(self, "labels")

    @property
    @pulumi.getter
    def location(self) -> pulumi.Output[str]:
        """
        The location name to create the server in. `nbg1`, `fsn1` or `hel1`
        """
        return pulumi.get(self, "location")

    @property
    @pulumi.getter
    def name(self) -> pulumi.Output[str]:
        """
        Name of the server to create (must be unique per project and a valid hostname as per RFC 1123).
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter
    def networks(self) -> pulumi.Output[Optional[Sequence['outputs.ServerNetwork']]]:
        return pulumi.get(self, "networks")

    @property
    @pulumi.getter
    def rescue(self) -> pulumi.Output[Optional[str]]:
        """
        Enable and boot in to the specified rescue system. This enables simple installation of custom operating systems. `linux64` `linux32` or `freebsd64`
        """
        return pulumi.get(self, "rescue")

    @property
    @pulumi.getter(name="serverType")
    def server_type(self) -> pulumi.Output[str]:
        """
        Name of the server type this server should be created with.
        """
        return pulumi.get(self, "server_type")

    @property
    @pulumi.getter(name="sshKeys")
    def ssh_keys(self) -> pulumi.Output[Optional[Sequence[str]]]:
        """
        SSH key IDs or names which should be injected into the server at creation time
        """
        return pulumi.get(self, "ssh_keys")

    @property
    @pulumi.getter
    def status(self) -> pulumi.Output[str]:
        """
        (string) The status of the server.
        """
        return pulumi.get(self, "status")

    @property
    @pulumi.getter(name="userData")
    def user_data(self) -> pulumi.Output[Optional[str]]:
        """
        Cloud-Init user data to use during server creation
        """
        return pulumi.get(self, "user_data")


# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import warnings
import pulumi
import pulumi.runtime
from typing import Any, Dict, List, Mapping, Optional, Tuple, Union
from . import _utilities, _tables

__all__ = ['Volume']


class Volume(pulumi.CustomResource):
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 automount: Optional[pulumi.Input[bool]] = None,
                 format: Optional[pulumi.Input[str]] = None,
                 labels: Optional[pulumi.Input[Mapping[str, Any]]] = None,
                 location: Optional[pulumi.Input[str]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 server_id: Optional[pulumi.Input[float]] = None,
                 size: Optional[pulumi.Input[float]] = None,
                 __props__=None,
                 __name__=None,
                 __opts__=None):
        """
        Provides a Hetzner Cloud volume resource to manage volumes.

        ## Example Usage

        ```python
        import pulumi
        import pulumi_hcloud as hcloud

        node1 = hcloud.Server("node1",
            image="debian-9",
            server_type="cx11")
        master = hcloud.Volume("master",
            size=50,
            server_id=node1.id,
            automount=True)
        ```

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[bool] automount: Automount the volume upon attaching it (server_id must be provided).
        :param pulumi.Input[str] format: Format volume after creation. `xfs` or `ext4`
        :param pulumi.Input[Mapping[str, Any]] labels: User-defined labels (key-value pairs).
        :param pulumi.Input[str] location: Location of the volume to create, optional if server_id argument is passed.
        :param pulumi.Input[str] name: Name of the volume to create (must be unique per project).
        :param pulumi.Input[float] server_id: Server to attach the Volume to, optional if location argument is passed.
        :param pulumi.Input[float] size: Size of the volume (in GB).
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

            __props__['automount'] = automount
            __props__['format'] = format
            __props__['labels'] = labels
            __props__['location'] = location
            __props__['name'] = name
            __props__['server_id'] = server_id
            if size is None:
                raise TypeError("Missing required property 'size'")
            __props__['size'] = size
            __props__['linux_device'] = None
        super(Volume, __self__).__init__(
            'hcloud:index/volume:Volume',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None,
            automount: Optional[pulumi.Input[bool]] = None,
            format: Optional[pulumi.Input[str]] = None,
            labels: Optional[pulumi.Input[Mapping[str, Any]]] = None,
            linux_device: Optional[pulumi.Input[str]] = None,
            location: Optional[pulumi.Input[str]] = None,
            name: Optional[pulumi.Input[str]] = None,
            server_id: Optional[pulumi.Input[float]] = None,
            size: Optional[pulumi.Input[float]] = None) -> 'Volume':
        """
        Get an existing Volume resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[bool] automount: Automount the volume upon attaching it (server_id must be provided).
        :param pulumi.Input[str] format: Format volume after creation. `xfs` or `ext4`
        :param pulumi.Input[Mapping[str, Any]] labels: User-defined labels (key-value pairs).
        :param pulumi.Input[str] linux_device: Device path on the file system for the Volume.
        :param pulumi.Input[str] location: Location of the volume to create, optional if server_id argument is passed.
        :param pulumi.Input[str] name: Name of the volume to create (must be unique per project).
        :param pulumi.Input[float] server_id: Server to attach the Volume to, optional if location argument is passed.
        :param pulumi.Input[float] size: Size of the volume (in GB).
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = dict()

        __props__["automount"] = automount
        __props__["format"] = format
        __props__["labels"] = labels
        __props__["linux_device"] = linux_device
        __props__["location"] = location
        __props__["name"] = name
        __props__["server_id"] = server_id
        __props__["size"] = size
        return Volume(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter
    def automount(self) -> pulumi.Output[Optional[bool]]:
        """
        Automount the volume upon attaching it (server_id must be provided).
        """
        return pulumi.get(self, "automount")

    @property
    @pulumi.getter
    def format(self) -> pulumi.Output[Optional[str]]:
        """
        Format volume after creation. `xfs` or `ext4`
        """
        return pulumi.get(self, "format")

    @property
    @pulumi.getter
    def labels(self) -> pulumi.Output[Optional[Mapping[str, Any]]]:
        """
        User-defined labels (key-value pairs).
        """
        return pulumi.get(self, "labels")

    @property
    @pulumi.getter(name="linuxDevice")
    def linux_device(self) -> pulumi.Output[str]:
        """
        Device path on the file system for the Volume.
        """
        return pulumi.get(self, "linux_device")

    @property
    @pulumi.getter
    def location(self) -> pulumi.Output[str]:
        """
        Location of the volume to create, optional if server_id argument is passed.
        """
        return pulumi.get(self, "location")

    @property
    @pulumi.getter
    def name(self) -> pulumi.Output[str]:
        """
        Name of the volume to create (must be unique per project).
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter(name="serverId")
    def server_id(self) -> pulumi.Output[float]:
        """
        Server to attach the Volume to, optional if location argument is passed.
        """
        return pulumi.get(self, "server_id")

    @property
    @pulumi.getter
    def size(self) -> pulumi.Output[float]:
        """
        Size of the volume (in GB).
        """
        return pulumi.get(self, "size")

    def translate_output_property(self, prop):
        return _tables.CAMEL_TO_SNAKE_CASE_TABLE.get(prop) or prop

    def translate_input_property(self, prop):
        return _tables.SNAKE_TO_CAMEL_CASE_TABLE.get(prop) or prop


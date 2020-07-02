# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import warnings
import pulumi
import pulumi.runtime
from typing import Union
from . import utilities, tables


class Volume(pulumi.CustomResource):
    automount: pulumi.Output[bool]
    format: pulumi.Output[str]
    labels: pulumi.Output[dict]
    linux_device: pulumi.Output[str]
    location: pulumi.Output[str]
    name: pulumi.Output[str]
    server_id: pulumi.Output[float]
    size: pulumi.Output[float]
    def __init__(__self__, resource_name, opts=None, automount=None, format=None, labels=None, location=None, name=None, server_id=None, size=None, __props__=None, __name__=None, __opts__=None):
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
            automount=True,
            server_id=node1.id,
            size=50)
        ```

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
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
            opts.version = utilities.get_version()
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
    def get(resource_name, id, opts=None, automount=None, format=None, labels=None, linux_device=None, location=None, name=None, server_id=None, size=None):
        """
        Get an existing Volume resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param str id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
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

    def translate_output_property(self, prop):
        return tables._CAMEL_TO_SNAKE_CASE_TABLE.get(prop) or prop

    def translate_input_property(self, prop):
        return tables._SNAKE_TO_CAMEL_CASE_TABLE.get(prop) or prop

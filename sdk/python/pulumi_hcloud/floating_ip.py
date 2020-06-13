# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import json
import warnings
import pulumi
import pulumi.runtime
from typing import Union
from . import utilities, tables

class FloatingIp(pulumi.CustomResource):
    description: pulumi.Output[str]
    home_location: pulumi.Output[str]
    ip_address: pulumi.Output[str]
    ip_network: pulumi.Output[str]
    labels: pulumi.Output[dict]
    name: pulumi.Output[str]
    server_id: pulumi.Output[float]
    type: pulumi.Output[str]
    def __init__(__self__, resource_name, opts=None, description=None, home_location=None, labels=None, name=None, server_id=None, type=None, __props__=None, __name__=None, __opts__=None):
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
            server_id=node1.id,
            type="ipv4")
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

            __props__['description'] = description
            __props__['home_location'] = home_location
            __props__['labels'] = labels
            __props__['name'] = name
            __props__['server_id'] = server_id
            if type is None:
                raise TypeError("Missing required property 'type'")
            __props__['type'] = type
            __props__['ip_address'] = None
            __props__['ip_network'] = None
        super(FloatingIp, __self__).__init__(
            'hcloud:index/floatingIp:FloatingIp',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name, id, opts=None, description=None, home_location=None, ip_address=None, ip_network=None, labels=None, name=None, server_id=None, type=None):
        """
        Get an existing FloatingIp resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param str id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = dict()

        __props__["description"] = description
        __props__["home_location"] = home_location
        __props__["ip_address"] = ip_address
        __props__["ip_network"] = ip_network
        __props__["labels"] = labels
        __props__["name"] = name
        __props__["server_id"] = server_id
        __props__["type"] = type
        return FloatingIp(resource_name, opts=opts, __props__=__props__)
    def translate_output_property(self, prop):
        return tables._CAMEL_TO_SNAKE_CASE_TABLE.get(prop) or prop

    def translate_input_property(self, prop):
        return tables._SNAKE_TO_CAMEL_CASE_TABLE.get(prop) or prop


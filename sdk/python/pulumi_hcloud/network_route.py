# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import warnings
import pulumi
import pulumi.runtime
from typing import Union
from . import utilities, tables


class NetworkRoute(pulumi.CustomResource):
    destination: pulumi.Output[str]
    gateway: pulumi.Output[str]
    network_id: pulumi.Output[float]
    def __init__(__self__, resource_name, opts=None, destination=None, gateway=None, network_id=None, __props__=None, __name__=None, __opts__=None):
        """
        Provides a Hetzner Cloud Network Route to represent a Network route in the Hetzner Cloud.

        ## Example Usage

        ```python
        import pulumi
        import pulumi_hcloud as hcloud

        mynet = hcloud.Network("mynet", ip_range="10.0.0.0/8")
        priv_net = hcloud.NetworkRoute("privNet",
            destination="10.100.1.0/24",
            gateway="10.0.1.1",
            network_id=mynet.id)
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

            if destination is None:
                raise TypeError("Missing required property 'destination'")
            __props__['destination'] = destination
            if gateway is None:
                raise TypeError("Missing required property 'gateway'")
            __props__['gateway'] = gateway
            if network_id is None:
                raise TypeError("Missing required property 'network_id'")
            __props__['network_id'] = network_id
        super(NetworkRoute, __self__).__init__(
            'hcloud:index/networkRoute:NetworkRoute',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name, id, opts=None, destination=None, gateway=None, network_id=None):
        """
        Get an existing NetworkRoute resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param str id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = dict()

        __props__["destination"] = destination
        __props__["gateway"] = gateway
        __props__["network_id"] = network_id
        return NetworkRoute(resource_name, opts=opts, __props__=__props__)

    def translate_output_property(self, prop):
        return tables._CAMEL_TO_SNAKE_CASE_TABLE.get(prop) or prop

    def translate_input_property(self, prop):
        return tables._SNAKE_TO_CAMEL_CASE_TABLE.get(prop) or prop

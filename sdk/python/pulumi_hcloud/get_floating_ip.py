# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import json
import warnings
import pulumi
import pulumi.runtime
from typing import Union
from . import utilities, tables

class GetFloatingIpResult:
    """
    A collection of values returned by getFloatingIp.
    """
    def __init__(__self__, description=None, home_location=None, id=None, ip_address=None, ip_network=None, labels=None, name=None, selector=None, server_id=None, type=None, with_selector=None):
        if description and not isinstance(description, str):
            raise TypeError("Expected argument 'description' to be a str")
        __self__.description = description
        if home_location and not isinstance(home_location, str):
            raise TypeError("Expected argument 'home_location' to be a str")
        __self__.home_location = home_location
        if id and not isinstance(id, float):
            raise TypeError("Expected argument 'id' to be a float")
        __self__.id = id
        if ip_address and not isinstance(ip_address, str):
            raise TypeError("Expected argument 'ip_address' to be a str")
        __self__.ip_address = ip_address
        if ip_network and not isinstance(ip_network, str):
            raise TypeError("Expected argument 'ip_network' to be a str")
        __self__.ip_network = ip_network
        if labels and not isinstance(labels, dict):
            raise TypeError("Expected argument 'labels' to be a dict")
        __self__.labels = labels
        if name and not isinstance(name, str):
            raise TypeError("Expected argument 'name' to be a str")
        __self__.name = name
        if selector and not isinstance(selector, str):
            raise TypeError("Expected argument 'selector' to be a str")
        if selector is not None:
            warnings.warn("Please use the with_selector property instead.", DeprecationWarning)
            pulumi.log.warn("selector is deprecated: Please use the with_selector property instead.")
        __self__.selector = selector
        if server_id and not isinstance(server_id, float):
            raise TypeError("Expected argument 'server_id' to be a float")
        __self__.server_id = server_id
        if type and not isinstance(type, str):
            raise TypeError("Expected argument 'type' to be a str")
        __self__.type = type
        if with_selector and not isinstance(with_selector, str):
            raise TypeError("Expected argument 'with_selector' to be a str")
        __self__.with_selector = with_selector
class AwaitableGetFloatingIpResult(GetFloatingIpResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetFloatingIpResult(
            description=self.description,
            home_location=self.home_location,
            id=self.id,
            ip_address=self.ip_address,
            ip_network=self.ip_network,
            labels=self.labels,
            name=self.name,
            selector=self.selector,
            server_id=self.server_id,
            type=self.type,
            with_selector=self.with_selector)

def get_floating_ip(id=None,ip_address=None,name=None,selector=None,with_selector=None,opts=None):
    """
    Provides details about a Hetzner Cloud Floating IP.

    This resource can be useful when you need to determine a Floating IP ID based on the IP address.

    ## Example Usage

    ### Additional Examples

    ```python
    import pulumi
    import pulumi_hcloud as hcloud

    ip1 = hcloud.get_floating_ip(ip_address="1.2.3.4")
    image2 = hcloud.get_floating_ip(with_selector="key=value")
    main = []
    for range in [{"value": i} for i in range(0, var.counter)]:
        main.append(hcloud.FloatingIpAssignment(f"main-{range['value']}",
            floating_ip_id=ip1.id,
            server_id=hcloud_server["main"]["id"]))
    ```
    """
    __args__ = dict()


    __args__['id'] = id
    __args__['ipAddress'] = ip_address
    __args__['name'] = name
    __args__['selector'] = selector
    __args__['withSelector'] = with_selector
    if opts is None:
        opts = pulumi.InvokeOptions()
    if opts.version is None:
        opts.version = utilities.get_version()
    __ret__ = pulumi.runtime.invoke('hcloud:index/getFloatingIp:getFloatingIp', __args__, opts=opts).value

    return AwaitableGetFloatingIpResult(
        description=__ret__.get('description'),
        home_location=__ret__.get('homeLocation'),
        id=__ret__.get('id'),
        ip_address=__ret__.get('ipAddress'),
        ip_network=__ret__.get('ipNetwork'),
        labels=__ret__.get('labels'),
        name=__ret__.get('name'),
        selector=__ret__.get('selector'),
        server_id=__ret__.get('serverId'),
        type=__ret__.get('type'),
        with_selector=__ret__.get('withSelector'))

# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
from . import _utilities, _tables

__all__ = [
    'GetNetworkResult',
    'AwaitableGetNetworkResult',
    'get_network',
]

@pulumi.output_type
class GetNetworkResult:
    """
    A collection of values returned by getNetwork.
    """
    def __init__(__self__, id=None, ip_range=None, labels=None, name=None, with_selector=None):
        if id and not isinstance(id, int):
            raise TypeError("Expected argument 'id' to be a int")
        pulumi.set(__self__, "id", id)
        if ip_range and not isinstance(ip_range, str):
            raise TypeError("Expected argument 'ip_range' to be a str")
        pulumi.set(__self__, "ip_range", ip_range)
        if labels and not isinstance(labels, dict):
            raise TypeError("Expected argument 'labels' to be a dict")
        pulumi.set(__self__, "labels", labels)
        if name and not isinstance(name, str):
            raise TypeError("Expected argument 'name' to be a str")
        pulumi.set(__self__, "name", name)
        if with_selector and not isinstance(with_selector, str):
            raise TypeError("Expected argument 'with_selector' to be a str")
        pulumi.set(__self__, "with_selector", with_selector)

    @property
    @pulumi.getter
    def id(self) -> int:
        """
        Unique ID of the Network.
        """
        return pulumi.get(self, "id")

    @property
    @pulumi.getter(name="ipRange")
    def ip_range(self) -> Optional[str]:
        """
        IPv4 prefix of the Network.
        """
        return pulumi.get(self, "ip_range")

    @property
    @pulumi.getter
    def labels(self) -> Optional[Mapping[str, Any]]:
        return pulumi.get(self, "labels")

    @property
    @pulumi.getter
    def name(self) -> Optional[str]:
        """
        Name of the Network.
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter(name="withSelector")
    def with_selector(self) -> Optional[str]:
        return pulumi.get(self, "with_selector")


class AwaitableGetNetworkResult(GetNetworkResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetNetworkResult(
            id=self.id,
            ip_range=self.ip_range,
            labels=self.labels,
            name=self.name,
            with_selector=self.with_selector)


def get_network(id: Optional[int] = None,
                ip_range: Optional[str] = None,
                labels: Optional[Mapping[str, Any]] = None,
                name: Optional[str] = None,
                with_selector: Optional[str] = None,
                opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetNetworkResult:
    """
    Use this data source to access information about an existing resource.

    :param int id: ID of the Network.
    :param str ip_range: IPv4 prefix of the Network.
    :param str name: Name of the Network.
    :param str with_selector: Label Selector. For more information about possible values, visit the [Hetzner Cloud Documentation](https://docs.hetzner.cloud/#overview-label-selector).
    """
    __args__ = dict()
    __args__['id'] = id
    __args__['ipRange'] = ip_range
    __args__['labels'] = labels
    __args__['name'] = name
    __args__['withSelector'] = with_selector
    if opts is None:
        opts = pulumi.InvokeOptions()
    if opts.version is None:
        opts.version = _utilities.get_version()
    __ret__ = pulumi.runtime.invoke('hcloud:index/getNetwork:getNetwork', __args__, opts=opts, typ=GetNetworkResult).value

    return AwaitableGetNetworkResult(
        id=__ret__.id,
        ip_range=__ret__.ip_range,
        labels=__ret__.labels,
        name=__ret__.name,
        with_selector=__ret__.with_selector)

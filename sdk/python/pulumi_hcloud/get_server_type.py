# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
from . import _utilities

__all__ = [
    'GetServerTypeResult',
    'AwaitableGetServerTypeResult',
    'get_server_type',
    'get_server_type_output',
]

@pulumi.output_type
class GetServerTypeResult:
    """
    A collection of values returned by getServerType.
    """
    def __init__(__self__, cores=None, cpu_type=None, description=None, disk=None, id=None, memory=None, name=None, storage_type=None):
        if cores and not isinstance(cores, int):
            raise TypeError("Expected argument 'cores' to be a int")
        pulumi.set(__self__, "cores", cores)
        if cpu_type and not isinstance(cpu_type, str):
            raise TypeError("Expected argument 'cpu_type' to be a str")
        pulumi.set(__self__, "cpu_type", cpu_type)
        if description and not isinstance(description, str):
            raise TypeError("Expected argument 'description' to be a str")
        pulumi.set(__self__, "description", description)
        if disk and not isinstance(disk, int):
            raise TypeError("Expected argument 'disk' to be a int")
        pulumi.set(__self__, "disk", disk)
        if id and not isinstance(id, int):
            raise TypeError("Expected argument 'id' to be a int")
        pulumi.set(__self__, "id", id)
        if memory and not isinstance(memory, int):
            raise TypeError("Expected argument 'memory' to be a int")
        pulumi.set(__self__, "memory", memory)
        if name and not isinstance(name, str):
            raise TypeError("Expected argument 'name' to be a str")
        pulumi.set(__self__, "name", name)
        if storage_type and not isinstance(storage_type, str):
            raise TypeError("Expected argument 'storage_type' to be a str")
        pulumi.set(__self__, "storage_type", storage_type)

    @property
    @pulumi.getter
    def cores(self) -> int:
        """
        (int) Number of cpu cores a Server of this type will have.
        """
        return pulumi.get(self, "cores")

    @property
    @pulumi.getter(name="cpuType")
    def cpu_type(self) -> str:
        return pulumi.get(self, "cpu_type")

    @property
    @pulumi.getter
    def description(self) -> str:
        """
        (string) Description of the server_type.
        """
        return pulumi.get(self, "description")

    @property
    @pulumi.getter
    def disk(self) -> int:
        """
        (int) Disk size a Server of this type will have in GB.
        """
        return pulumi.get(self, "disk")

    @property
    @pulumi.getter
    def id(self) -> int:
        """
        (int) Unique ID of the server_type.
        """
        return pulumi.get(self, "id")

    @property
    @pulumi.getter
    def memory(self) -> int:
        """
        (int) Memory a Server of this type will have in GB.
        """
        return pulumi.get(self, "memory")

    @property
    @pulumi.getter
    def name(self) -> str:
        """
        (string) Name of the server_type.
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter(name="storageType")
    def storage_type(self) -> str:
        return pulumi.get(self, "storage_type")


class AwaitableGetServerTypeResult(GetServerTypeResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetServerTypeResult(
            cores=self.cores,
            cpu_type=self.cpu_type,
            description=self.description,
            disk=self.disk,
            id=self.id,
            memory=self.memory,
            name=self.name,
            storage_type=self.storage_type)


def get_server_type(id: Optional[int] = None,
                    name: Optional[str] = None,
                    opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetServerTypeResult:
    """
    Provides details about a specific Hetzner Cloud Server Type.
    Use this resource to get detailed information about specific Server Type.

    ## Example Usage

    ```python
    import pulumi
    import pulumi_hcloud as hcloud

    ds1 = hcloud.get_server_type(name="cx11")
    ds2 = hcloud.get_server_type(id=1)
    ```


    :param int id: ID of the server_type.
    :param str name: Name of the server_type.
    """
    __args__ = dict()
    __args__['id'] = id
    __args__['name'] = name
    if opts is None:
        opts = pulumi.InvokeOptions()
    if opts.version is None:
        opts.version = _utilities.get_version()
    __ret__ = pulumi.runtime.invoke('hcloud:index/getServerType:getServerType', __args__, opts=opts, typ=GetServerTypeResult).value

    return AwaitableGetServerTypeResult(
        cores=__ret__.cores,
        cpu_type=__ret__.cpu_type,
        description=__ret__.description,
        disk=__ret__.disk,
        id=__ret__.id,
        memory=__ret__.memory,
        name=__ret__.name,
        storage_type=__ret__.storage_type)


@_utilities.lift_output_func(get_server_type)
def get_server_type_output(id: Optional[pulumi.Input[Optional[int]]] = None,
                           name: Optional[pulumi.Input[Optional[str]]] = None,
                           opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetServerTypeResult]:
    """
    Provides details about a specific Hetzner Cloud Server Type.
    Use this resource to get detailed information about specific Server Type.

    ## Example Usage

    ```python
    import pulumi
    import pulumi_hcloud as hcloud

    ds1 = hcloud.get_server_type(name="cx11")
    ds2 = hcloud.get_server_type(id=1)
    ```


    :param int id: ID of the server_type.
    :param str name: Name of the server_type.
    """
    ...

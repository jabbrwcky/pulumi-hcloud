# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import json
import warnings
import pulumi
import pulumi.runtime
from typing import Union
from . import utilities, tables

class GetLocationsResult:
    """
    A collection of values returned by getLocations.
    """
    def __init__(__self__, descriptions=None, id=None, location_ids=None, names=None):
        if descriptions and not isinstance(descriptions, list):
            raise TypeError("Expected argument 'descriptions' to be a list")
        __self__.descriptions = descriptions
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        __self__.id = id
        """
        The provider-assigned unique ID for this managed resource.
        """
        if location_ids and not isinstance(location_ids, list):
            raise TypeError("Expected argument 'location_ids' to be a list")
        __self__.location_ids = location_ids
        if names and not isinstance(names, list):
            raise TypeError("Expected argument 'names' to be a list")
        __self__.names = names
class AwaitableGetLocationsResult(GetLocationsResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetLocationsResult(
            descriptions=self.descriptions,
            id=self.id,
            location_ids=self.location_ids,
            names=self.names)

def get_locations(location_ids=None,opts=None):
    """
    Provides a list of available Hetzner Cloud Locations.
    This resource may be useful to create highly available infrastructure, distributed across several locations.

    ## Example Usage



    ```python
    import pulumi
    import pulumi_hcloud as hcloud

    ds = hcloud.get_locations()
    workers = []
    for range in [{"value": i} for i in range(0, 3)]:
        workers.append(hcloud.Server(f"workers-{range['value']}",
            image="debian-9",
            location=ds.names[range["value"]],
            server_type="cx31"))
    ```
    """
    __args__ = dict()


    __args__['locationIds'] = location_ids
    if opts is None:
        opts = pulumi.InvokeOptions()
    if opts.version is None:
        opts.version = utilities.get_version()
    __ret__ = pulumi.runtime.invoke('hcloud:index/getLocations:getLocations', __args__, opts=opts).value

    return AwaitableGetLocationsResult(
        descriptions=__ret__.get('descriptions'),
        id=__ret__.get('id'),
        location_ids=__ret__.get('locationIds'),
        names=__ret__.get('names'))

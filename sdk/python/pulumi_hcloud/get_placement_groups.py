# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
from . import _utilities
from . import outputs

__all__ = [
    'GetPlacementGroupsResult',
    'AwaitableGetPlacementGroupsResult',
    'get_placement_groups',
    'get_placement_groups_output',
]

@pulumi.output_type
class GetPlacementGroupsResult:
    """
    A collection of values returned by getPlacementGroups.
    """
    def __init__(__self__, id=None, most_recent=None, placement_groups=None, with_selector=None):
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        pulumi.set(__self__, "id", id)
        if most_recent and not isinstance(most_recent, bool):
            raise TypeError("Expected argument 'most_recent' to be a bool")
        pulumi.set(__self__, "most_recent", most_recent)
        if placement_groups and not isinstance(placement_groups, list):
            raise TypeError("Expected argument 'placement_groups' to be a list")
        pulumi.set(__self__, "placement_groups", placement_groups)
        if with_selector and not isinstance(with_selector, str):
            raise TypeError("Expected argument 'with_selector' to be a str")
        pulumi.set(__self__, "with_selector", with_selector)

    @property
    @pulumi.getter
    def id(self) -> str:
        """
        The provider-assigned unique ID for this managed resource.
        """
        return pulumi.get(self, "id")

    @property
    @pulumi.getter(name="mostRecent")
    def most_recent(self) -> Optional[bool]:
        return pulumi.get(self, "most_recent")

    @property
    @pulumi.getter(name="placementGroups")
    def placement_groups(self) -> Sequence['outputs.GetPlacementGroupsPlacementGroupResult']:
        """
        (list) List of all matching placement groups. See `data.hcloud_placement_group` for schema.
        """
        return pulumi.get(self, "placement_groups")

    @property
    @pulumi.getter(name="withSelector")
    def with_selector(self) -> Optional[str]:
        return pulumi.get(self, "with_selector")


class AwaitableGetPlacementGroupsResult(GetPlacementGroupsResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetPlacementGroupsResult(
            id=self.id,
            most_recent=self.most_recent,
            placement_groups=self.placement_groups,
            with_selector=self.with_selector)


def get_placement_groups(most_recent: Optional[bool] = None,
                         with_selector: Optional[str] = None,
                         opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetPlacementGroupsResult:
    """
    Provides details about multiple Hetzner Cloud Placement Groups.

    ## Example Usage

    ```python
    import pulumi
    import pulumi_hcloud as hcloud

    sample_placement_group1 = hcloud.get_placement_groups()
    sample_placement_group2 = hcloud.get_placement_groups(with_selector="key=value")
    ```


    :param bool most_recent: Sorts list by date.
    :param str with_selector: [Label selector](https://docs.hetzner.cloud/#overview-label-selector)
    """
    __args__ = dict()
    __args__['mostRecent'] = most_recent
    __args__['withSelector'] = with_selector
    if opts is None:
        opts = pulumi.InvokeOptions()
    if opts.version is None:
        opts.version = _utilities.get_version()
    __ret__ = pulumi.runtime.invoke('hcloud:index/getPlacementGroups:getPlacementGroups', __args__, opts=opts, typ=GetPlacementGroupsResult).value

    return AwaitableGetPlacementGroupsResult(
        id=__ret__.id,
        most_recent=__ret__.most_recent,
        placement_groups=__ret__.placement_groups,
        with_selector=__ret__.with_selector)


@_utilities.lift_output_func(get_placement_groups)
def get_placement_groups_output(most_recent: Optional[pulumi.Input[Optional[bool]]] = None,
                                with_selector: Optional[pulumi.Input[Optional[str]]] = None,
                                opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetPlacementGroupsResult]:
    """
    Provides details about multiple Hetzner Cloud Placement Groups.

    ## Example Usage

    ```python
    import pulumi
    import pulumi_hcloud as hcloud

    sample_placement_group1 = hcloud.get_placement_groups()
    sample_placement_group2 = hcloud.get_placement_groups(with_selector="key=value")
    ```


    :param bool most_recent: Sorts list by date.
    :param str with_selector: [Label selector](https://docs.hetzner.cloud/#overview-label-selector)
    """
    ...

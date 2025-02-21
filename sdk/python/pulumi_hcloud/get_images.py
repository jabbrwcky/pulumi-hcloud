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
    'GetImagesResult',
    'AwaitableGetImagesResult',
    'get_images',
    'get_images_output',
]

@pulumi.output_type
class GetImagesResult:
    """
    A collection of values returned by getImages.
    """
    def __init__(__self__, id=None, images=None, most_recent=None, with_selector=None, with_statuses=None):
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        pulumi.set(__self__, "id", id)
        if images and not isinstance(images, list):
            raise TypeError("Expected argument 'images' to be a list")
        pulumi.set(__self__, "images", images)
        if most_recent and not isinstance(most_recent, bool):
            raise TypeError("Expected argument 'most_recent' to be a bool")
        pulumi.set(__self__, "most_recent", most_recent)
        if with_selector and not isinstance(with_selector, str):
            raise TypeError("Expected argument 'with_selector' to be a str")
        pulumi.set(__self__, "with_selector", with_selector)
        if with_statuses and not isinstance(with_statuses, list):
            raise TypeError("Expected argument 'with_statuses' to be a list")
        pulumi.set(__self__, "with_statuses", with_statuses)

    @property
    @pulumi.getter
    def id(self) -> str:
        """
        The provider-assigned unique ID for this managed resource.
        """
        return pulumi.get(self, "id")

    @property
    @pulumi.getter
    def images(self) -> Sequence['outputs.GetImagesImageResult']:
        """
        (list) List of all matching images. See `data.hcloud_image` for schema.
        """
        return pulumi.get(self, "images")

    @property
    @pulumi.getter(name="mostRecent")
    def most_recent(self) -> Optional[bool]:
        return pulumi.get(self, "most_recent")

    @property
    @pulumi.getter(name="withSelector")
    def with_selector(self) -> Optional[str]:
        return pulumi.get(self, "with_selector")

    @property
    @pulumi.getter(name="withStatuses")
    def with_statuses(self) -> Optional[Sequence[str]]:
        return pulumi.get(self, "with_statuses")


class AwaitableGetImagesResult(GetImagesResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetImagesResult(
            id=self.id,
            images=self.images,
            most_recent=self.most_recent,
            with_selector=self.with_selector,
            with_statuses=self.with_statuses)


def get_images(most_recent: Optional[bool] = None,
               with_selector: Optional[str] = None,
               with_statuses: Optional[Sequence[str]] = None,
               opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetImagesResult:
    """
    Provides details about multiple Hetzner Cloud Images.

    ## Example Usage

    ```python
    import pulumi
    import pulumi_hcloud as hcloud

    image2 = hcloud.get_images()
    image3 = hcloud.get_images(with_selector="key=value")
    ```


    :param bool most_recent: Sorts list by date.
    :param str with_selector: [Label selector](https://docs.hetzner.cloud/#overview-label-selector)
    :param Sequence[str] with_statuses: List only images with the specified status, could contain `creating` or `available`.
    """
    __args__ = dict()
    __args__['mostRecent'] = most_recent
    __args__['withSelector'] = with_selector
    __args__['withStatuses'] = with_statuses
    if opts is None:
        opts = pulumi.InvokeOptions()
    if opts.version is None:
        opts.version = _utilities.get_version()
    __ret__ = pulumi.runtime.invoke('hcloud:index/getImages:getImages', __args__, opts=opts, typ=GetImagesResult).value

    return AwaitableGetImagesResult(
        id=__ret__.id,
        images=__ret__.images,
        most_recent=__ret__.most_recent,
        with_selector=__ret__.with_selector,
        with_statuses=__ret__.with_statuses)


@_utilities.lift_output_func(get_images)
def get_images_output(most_recent: Optional[pulumi.Input[Optional[bool]]] = None,
                      with_selector: Optional[pulumi.Input[Optional[str]]] = None,
                      with_statuses: Optional[pulumi.Input[Optional[Sequence[str]]]] = None,
                      opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetImagesResult]:
    """
    Provides details about multiple Hetzner Cloud Images.

    ## Example Usage

    ```python
    import pulumi
    import pulumi_hcloud as hcloud

    image2 = hcloud.get_images()
    image3 = hcloud.get_images(with_selector="key=value")
    ```


    :param bool most_recent: Sorts list by date.
    :param str with_selector: [Label selector](https://docs.hetzner.cloud/#overview-label-selector)
    :param Sequence[str] with_statuses: List only images with the specified status, could contain `creating` or `available`.
    """
    ...

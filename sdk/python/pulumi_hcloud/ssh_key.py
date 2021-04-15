# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
from . import _utilities

__all__ = ['SshKeyArgs', 'SshKey']

@pulumi.input_type
class SshKeyArgs:
    def __init__(__self__, *,
                 public_key: pulumi.Input[str],
                 labels: Optional[pulumi.Input[Mapping[str, Any]]] = None,
                 name: Optional[pulumi.Input[str]] = None):
        """
        The set of arguments for constructing a SshKey resource.
        :param pulumi.Input[str] public_key: The public key. If this is a file, it can be read using the file interpolation function
        :param pulumi.Input[Mapping[str, Any]] labels: (map) User-defined labels (key-value pairs)
        :param pulumi.Input[str] name: Name of the SSH key.
        """
        pulumi.set(__self__, "public_key", public_key)
        if labels is not None:
            pulumi.set(__self__, "labels", labels)
        if name is not None:
            pulumi.set(__self__, "name", name)

    @property
    @pulumi.getter(name="publicKey")
    def public_key(self) -> pulumi.Input[str]:
        """
        The public key. If this is a file, it can be read using the file interpolation function
        """
        return pulumi.get(self, "public_key")

    @public_key.setter
    def public_key(self, value: pulumi.Input[str]):
        pulumi.set(self, "public_key", value)

    @property
    @pulumi.getter
    def labels(self) -> Optional[pulumi.Input[Mapping[str, Any]]]:
        """
        (map) User-defined labels (key-value pairs)
        """
        return pulumi.get(self, "labels")

    @labels.setter
    def labels(self, value: Optional[pulumi.Input[Mapping[str, Any]]]):
        pulumi.set(self, "labels", value)

    @property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[str]]:
        """
        Name of the SSH key.
        """
        return pulumi.get(self, "name")

    @name.setter
    def name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "name", value)


@pulumi.input_type
class _SshKeyState:
    def __init__(__self__, *,
                 fingerprint: Optional[pulumi.Input[str]] = None,
                 labels: Optional[pulumi.Input[Mapping[str, Any]]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 public_key: Optional[pulumi.Input[str]] = None):
        """
        Input properties used for looking up and filtering SshKey resources.
        :param pulumi.Input[str] fingerprint: (string) The fingerprint of the SSH key
        :param pulumi.Input[Mapping[str, Any]] labels: (map) User-defined labels (key-value pairs)
        :param pulumi.Input[str] name: Name of the SSH key.
        :param pulumi.Input[str] public_key: The public key. If this is a file, it can be read using the file interpolation function
        """
        if fingerprint is not None:
            pulumi.set(__self__, "fingerprint", fingerprint)
        if labels is not None:
            pulumi.set(__self__, "labels", labels)
        if name is not None:
            pulumi.set(__self__, "name", name)
        if public_key is not None:
            pulumi.set(__self__, "public_key", public_key)

    @property
    @pulumi.getter
    def fingerprint(self) -> Optional[pulumi.Input[str]]:
        """
        (string) The fingerprint of the SSH key
        """
        return pulumi.get(self, "fingerprint")

    @fingerprint.setter
    def fingerprint(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "fingerprint", value)

    @property
    @pulumi.getter
    def labels(self) -> Optional[pulumi.Input[Mapping[str, Any]]]:
        """
        (map) User-defined labels (key-value pairs)
        """
        return pulumi.get(self, "labels")

    @labels.setter
    def labels(self, value: Optional[pulumi.Input[Mapping[str, Any]]]):
        pulumi.set(self, "labels", value)

    @property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[str]]:
        """
        Name of the SSH key.
        """
        return pulumi.get(self, "name")

    @name.setter
    def name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "name", value)

    @property
    @pulumi.getter(name="publicKey")
    def public_key(self) -> Optional[pulumi.Input[str]]:
        """
        The public key. If this is a file, it can be read using the file interpolation function
        """
        return pulumi.get(self, "public_key")

    @public_key.setter
    def public_key(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "public_key", value)


class SshKey(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 labels: Optional[pulumi.Input[Mapping[str, Any]]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 public_key: Optional[pulumi.Input[str]] = None,
                 __props__=None,
                 __name__=None,
                 __opts__=None):
        """
        Provides a Hetzner Cloud SSH key resource to manage SSH keys for server access.

        ## Example Usage

        ```python
        import pulumi
        import pulumi_hcloud as hcloud

        # Create a new SSH key
        default = hcloud.SshKey("default", public_key=(lambda path: open(path).read())("~/.ssh/id_rsa.pub"))
        ```

        ## Import

        SSH keys can be imported using the SSH key `id`

        ```sh
         $ pulumi import hcloud:index/sshKey:SshKey mykey <id>
        ```

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[Mapping[str, Any]] labels: (map) User-defined labels (key-value pairs)
        :param pulumi.Input[str] name: Name of the SSH key.
        :param pulumi.Input[str] public_key: The public key. If this is a file, it can be read using the file interpolation function
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: SshKeyArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        Provides a Hetzner Cloud SSH key resource to manage SSH keys for server access.

        ## Example Usage

        ```python
        import pulumi
        import pulumi_hcloud as hcloud

        # Create a new SSH key
        default = hcloud.SshKey("default", public_key=(lambda path: open(path).read())("~/.ssh/id_rsa.pub"))
        ```

        ## Import

        SSH keys can be imported using the SSH key `id`

        ```sh
         $ pulumi import hcloud:index/sshKey:SshKey mykey <id>
        ```

        :param str resource_name: The name of the resource.
        :param SshKeyArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(SshKeyArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 labels: Optional[pulumi.Input[Mapping[str, Any]]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 public_key: Optional[pulumi.Input[str]] = None,
                 __props__=None,
                 __name__=None,
                 __opts__=None):
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
            __props__ = SshKeyArgs.__new__(SshKeyArgs)

            __props__.__dict__["labels"] = labels
            __props__.__dict__["name"] = name
            if public_key is None and not opts.urn:
                raise TypeError("Missing required property 'public_key'")
            __props__.__dict__["public_key"] = public_key
            __props__.__dict__["fingerprint"] = None
        super(SshKey, __self__).__init__(
            'hcloud:index/sshKey:SshKey',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None,
            fingerprint: Optional[pulumi.Input[str]] = None,
            labels: Optional[pulumi.Input[Mapping[str, Any]]] = None,
            name: Optional[pulumi.Input[str]] = None,
            public_key: Optional[pulumi.Input[str]] = None) -> 'SshKey':
        """
        Get an existing SshKey resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] fingerprint: (string) The fingerprint of the SSH key
        :param pulumi.Input[Mapping[str, Any]] labels: (map) User-defined labels (key-value pairs)
        :param pulumi.Input[str] name: Name of the SSH key.
        :param pulumi.Input[str] public_key: The public key. If this is a file, it can be read using the file interpolation function
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = _SshKeyState.__new__(_SshKeyState)

        __props__.__dict__["fingerprint"] = fingerprint
        __props__.__dict__["labels"] = labels
        __props__.__dict__["name"] = name
        __props__.__dict__["public_key"] = public_key
        return SshKey(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter
    def fingerprint(self) -> pulumi.Output[str]:
        """
        (string) The fingerprint of the SSH key
        """
        return pulumi.get(self, "fingerprint")

    @property
    @pulumi.getter
    def labels(self) -> pulumi.Output[Optional[Mapping[str, Any]]]:
        """
        (map) User-defined labels (key-value pairs)
        """
        return pulumi.get(self, "labels")

    @property
    @pulumi.getter
    def name(self) -> pulumi.Output[str]:
        """
        Name of the SSH key.
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter(name="publicKey")
    def public_key(self) -> pulumi.Output[str]:
        """
        The public key. If this is a file, it can be read using the file interpolation function
        """
        return pulumi.get(self, "public_key")


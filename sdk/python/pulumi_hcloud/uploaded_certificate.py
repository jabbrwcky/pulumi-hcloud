# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
from . import _utilities, _tables

__all__ = ['UploadedCertificateArgs', 'UploadedCertificate']

@pulumi.input_type
class UploadedCertificateArgs:
    def __init__(__self__, *,
                 certificate: pulumi.Input[str],
                 private_key: pulumi.Input[str],
                 labels: Optional[pulumi.Input[Mapping[str, Any]]] = None,
                 name: Optional[pulumi.Input[str]] = None):
        """
        The set of arguments for constructing a UploadedCertificate resource.
        :param pulumi.Input[str] certificate: PEM encoded TLS certificate.
        :param pulumi.Input[str] private_key: PEM encoded private key belonging to the certificate.
        :param pulumi.Input[Mapping[str, Any]] labels: User-defined labels (key-value pairs) the
               certificate should be created with.
        :param pulumi.Input[str] name: Name of the Certificate.
        """
        pulumi.set(__self__, "certificate", certificate)
        pulumi.set(__self__, "private_key", private_key)
        if labels is not None:
            pulumi.set(__self__, "labels", labels)
        if name is not None:
            pulumi.set(__self__, "name", name)

    @property
    @pulumi.getter
    def certificate(self) -> pulumi.Input[str]:
        """
        PEM encoded TLS certificate.
        """
        return pulumi.get(self, "certificate")

    @certificate.setter
    def certificate(self, value: pulumi.Input[str]):
        pulumi.set(self, "certificate", value)

    @property
    @pulumi.getter(name="privateKey")
    def private_key(self) -> pulumi.Input[str]:
        """
        PEM encoded private key belonging to the certificate.
        """
        return pulumi.get(self, "private_key")

    @private_key.setter
    def private_key(self, value: pulumi.Input[str]):
        pulumi.set(self, "private_key", value)

    @property
    @pulumi.getter
    def labels(self) -> Optional[pulumi.Input[Mapping[str, Any]]]:
        """
        User-defined labels (key-value pairs) the
        certificate should be created with.
        """
        return pulumi.get(self, "labels")

    @labels.setter
    def labels(self, value: Optional[pulumi.Input[Mapping[str, Any]]]):
        pulumi.set(self, "labels", value)

    @property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[str]]:
        """
        Name of the Certificate.
        """
        return pulumi.get(self, "name")

    @name.setter
    def name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "name", value)


class UploadedCertificate(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 certificate: Optional[pulumi.Input[str]] = None,
                 labels: Optional[pulumi.Input[Mapping[str, Any]]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 private_key: Optional[pulumi.Input[str]] = None,
                 __props__=None,
                 __name__=None,
                 __opts__=None):
        """
        Upload a TLS certificate to Hetzner Cloud.

        ## Import

        Uploaded certificates can be imported using their `id`hcl

        ```sh
         $ pulumi import hcloud:index/uploadedCertificate:UploadedCertificate sample_certificate <id>
        ```

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] certificate: PEM encoded TLS certificate.
        :param pulumi.Input[Mapping[str, Any]] labels: User-defined labels (key-value pairs) the
               certificate should be created with.
        :param pulumi.Input[str] name: Name of the Certificate.
        :param pulumi.Input[str] private_key: PEM encoded private key belonging to the certificate.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: UploadedCertificateArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        Upload a TLS certificate to Hetzner Cloud.

        ## Import

        Uploaded certificates can be imported using their `id`hcl

        ```sh
         $ pulumi import hcloud:index/uploadedCertificate:UploadedCertificate sample_certificate <id>
        ```

        :param str resource_name: The name of the resource.
        :param UploadedCertificateArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(UploadedCertificateArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 certificate: Optional[pulumi.Input[str]] = None,
                 labels: Optional[pulumi.Input[Mapping[str, Any]]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 private_key: Optional[pulumi.Input[str]] = None,
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
            __props__ = dict()

            if certificate is None and not opts.urn:
                raise TypeError("Missing required property 'certificate'")
            __props__['certificate'] = certificate
            __props__['labels'] = labels
            __props__['name'] = name
            if private_key is None and not opts.urn:
                raise TypeError("Missing required property 'private_key'")
            __props__['private_key'] = private_key
            __props__['created'] = None
            __props__['domain_names'] = None
            __props__['fingerprint'] = None
            __props__['not_valid_after'] = None
            __props__['not_valid_before'] = None
            __props__['type'] = None
        super(UploadedCertificate, __self__).__init__(
            'hcloud:index/uploadedCertificate:UploadedCertificate',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None,
            certificate: Optional[pulumi.Input[str]] = None,
            created: Optional[pulumi.Input[str]] = None,
            domain_names: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
            fingerprint: Optional[pulumi.Input[str]] = None,
            labels: Optional[pulumi.Input[Mapping[str, Any]]] = None,
            name: Optional[pulumi.Input[str]] = None,
            not_valid_after: Optional[pulumi.Input[str]] = None,
            not_valid_before: Optional[pulumi.Input[str]] = None,
            private_key: Optional[pulumi.Input[str]] = None,
            type: Optional[pulumi.Input[str]] = None) -> 'UploadedCertificate':
        """
        Get an existing UploadedCertificate resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] certificate: PEM encoded TLS certificate.
        :param pulumi.Input[str] created: (string) Point in time when the Certificate was created at Hetzner Cloud (in ISO-8601 format).
        :param pulumi.Input[Sequence[pulumi.Input[str]]] domain_names: (list) Domains and subdomains covered by the certificate.
        :param pulumi.Input[str] fingerprint: (string) Fingerprint of the certificate.
        :param pulumi.Input[Mapping[str, Any]] labels: User-defined labels (key-value pairs) the
               certificate should be created with.
        :param pulumi.Input[str] name: Name of the Certificate.
        :param pulumi.Input[str] not_valid_after: (string) Point in time when the Certificate stops being valid (in ISO-8601 format).
        :param pulumi.Input[str] not_valid_before: (string) Point in time when the Certificate becomes valid (in ISO-8601 format).
        :param pulumi.Input[str] private_key: PEM encoded private key belonging to the certificate.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = dict()

        __props__["certificate"] = certificate
        __props__["created"] = created
        __props__["domain_names"] = domain_names
        __props__["fingerprint"] = fingerprint
        __props__["labels"] = labels
        __props__["name"] = name
        __props__["not_valid_after"] = not_valid_after
        __props__["not_valid_before"] = not_valid_before
        __props__["private_key"] = private_key
        __props__["type"] = type
        return UploadedCertificate(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter
    def certificate(self) -> pulumi.Output[str]:
        """
        PEM encoded TLS certificate.
        """
        return pulumi.get(self, "certificate")

    @property
    @pulumi.getter
    def created(self) -> pulumi.Output[str]:
        """
        (string) Point in time when the Certificate was created at Hetzner Cloud (in ISO-8601 format).
        """
        return pulumi.get(self, "created")

    @property
    @pulumi.getter(name="domainNames")
    def domain_names(self) -> pulumi.Output[Sequence[str]]:
        """
        (list) Domains and subdomains covered by the certificate.
        """
        return pulumi.get(self, "domain_names")

    @property
    @pulumi.getter
    def fingerprint(self) -> pulumi.Output[str]:
        """
        (string) Fingerprint of the certificate.
        """
        return pulumi.get(self, "fingerprint")

    @property
    @pulumi.getter
    def labels(self) -> pulumi.Output[Optional[Mapping[str, Any]]]:
        """
        User-defined labels (key-value pairs) the
        certificate should be created with.
        """
        return pulumi.get(self, "labels")

    @property
    @pulumi.getter
    def name(self) -> pulumi.Output[str]:
        """
        Name of the Certificate.
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter(name="notValidAfter")
    def not_valid_after(self) -> pulumi.Output[str]:
        """
        (string) Point in time when the Certificate stops being valid (in ISO-8601 format).
        """
        return pulumi.get(self, "not_valid_after")

    @property
    @pulumi.getter(name="notValidBefore")
    def not_valid_before(self) -> pulumi.Output[str]:
        """
        (string) Point in time when the Certificate becomes valid (in ISO-8601 format).
        """
        return pulumi.get(self, "not_valid_before")

    @property
    @pulumi.getter(name="privateKey")
    def private_key(self) -> pulumi.Output[str]:
        """
        PEM encoded private key belonging to the certificate.
        """
        return pulumi.get(self, "private_key")

    @property
    @pulumi.getter
    def type(self) -> pulumi.Output[str]:
        return pulumi.get(self, "type")

    def translate_output_property(self, prop):
        return _tables.CAMEL_TO_SNAKE_CASE_TABLE.get(prop) or prop

    def translate_input_property(self, prop):
        return _tables.SNAKE_TO_CAMEL_CASE_TABLE.get(prop) or prop


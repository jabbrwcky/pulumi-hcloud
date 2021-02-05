# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union
from . import _utilities, _tables

__all__ = [
    'GetCertificateResult',
    'AwaitableGetCertificateResult',
    'get_certificate',
]

@pulumi.output_type
class GetCertificateResult:
    """
    A collection of values returned by getCertificate.
    """
    def __init__(__self__, certificate=None, created=None, domain_names=None, fingerprint=None, id=None, labels=None, name=None, not_valid_after=None, not_valid_before=None, with_selector=None):
        if certificate and not isinstance(certificate, str):
            raise TypeError("Expected argument 'certificate' to be a str")
        pulumi.set(__self__, "certificate", certificate)
        if created and not isinstance(created, str):
            raise TypeError("Expected argument 'created' to be a str")
        pulumi.set(__self__, "created", created)
        if domain_names and not isinstance(domain_names, list):
            raise TypeError("Expected argument 'domain_names' to be a list")
        pulumi.set(__self__, "domain_names", domain_names)
        if fingerprint and not isinstance(fingerprint, str):
            raise TypeError("Expected argument 'fingerprint' to be a str")
        pulumi.set(__self__, "fingerprint", fingerprint)
        if id and not isinstance(id, int):
            raise TypeError("Expected argument 'id' to be a int")
        pulumi.set(__self__, "id", id)
        if labels and not isinstance(labels, dict):
            raise TypeError("Expected argument 'labels' to be a dict")
        pulumi.set(__self__, "labels", labels)
        if name and not isinstance(name, str):
            raise TypeError("Expected argument 'name' to be a str")
        pulumi.set(__self__, "name", name)
        if not_valid_after and not isinstance(not_valid_after, str):
            raise TypeError("Expected argument 'not_valid_after' to be a str")
        pulumi.set(__self__, "not_valid_after", not_valid_after)
        if not_valid_before and not isinstance(not_valid_before, str):
            raise TypeError("Expected argument 'not_valid_before' to be a str")
        pulumi.set(__self__, "not_valid_before", not_valid_before)
        if with_selector and not isinstance(with_selector, str):
            raise TypeError("Expected argument 'with_selector' to be a str")
        pulumi.set(__self__, "with_selector", with_selector)

    @property
    @pulumi.getter
    def certificate(self) -> str:
        """
        (string) PEM encoded TLS certificate.
        """
        return pulumi.get(self, "certificate")

    @property
    @pulumi.getter
    def created(self) -> str:
        """
        (string) Point in time when the Certificate was created at Hetzner Cloud (in ISO-8601 format).
        """
        return pulumi.get(self, "created")

    @property
    @pulumi.getter(name="domainNames")
    def domain_names(self) -> Sequence[str]:
        """
        (list) Domains and subdomains covered by the certificate.
        """
        return pulumi.get(self, "domain_names")

    @property
    @pulumi.getter
    def fingerprint(self) -> str:
        """
        (string) Fingerprint of the certificate.
        """
        return pulumi.get(self, "fingerprint")

    @property
    @pulumi.getter
    def id(self) -> int:
        """
        (int) Unique ID of the certificate.
        """
        return pulumi.get(self, "id")

    @property
    @pulumi.getter
    def labels(self) -> Mapping[str, Any]:
        """
        (map) User-defined labels (key-value pairs) assigned to the certificate.
        """
        return pulumi.get(self, "labels")

    @property
    @pulumi.getter
    def name(self) -> Optional[str]:
        """
        (string) Name of the Certificate.
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter(name="notValidAfter")
    def not_valid_after(self) -> str:
        """
        (string) Point in time when the Certificate stops being valid (in ISO-8601 format).
        """
        return pulumi.get(self, "not_valid_after")

    @property
    @pulumi.getter(name="notValidBefore")
    def not_valid_before(self) -> str:
        """
        (string) Point in time when the Certificate becomes valid (in ISO-8601 format).
        """
        return pulumi.get(self, "not_valid_before")

    @property
    @pulumi.getter(name="withSelector")
    def with_selector(self) -> Optional[str]:
        return pulumi.get(self, "with_selector")


class AwaitableGetCertificateResult(GetCertificateResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetCertificateResult(
            certificate=self.certificate,
            created=self.created,
            domain_names=self.domain_names,
            fingerprint=self.fingerprint,
            id=self.id,
            labels=self.labels,
            name=self.name,
            not_valid_after=self.not_valid_after,
            not_valid_before=self.not_valid_before,
            with_selector=self.with_selector)


def get_certificate(id: Optional[int] = None,
                    name: Optional[str] = None,
                    with_selector: Optional[str] = None,
                    opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetCertificateResult:
    """
    Provides details about a specific Hetzner Cloud Certificate.


    :param int id: ID of the certificate.
    :param str name: Name of the certificate.
    :param str with_selector: [Label selector](https://docs.hetzner.cloud/#overview-label-selector)
    """
    __args__ = dict()
    __args__['id'] = id
    __args__['name'] = name
    __args__['withSelector'] = with_selector
    if opts is None:
        opts = pulumi.InvokeOptions()
    if opts.version is None:
        opts.version = _utilities.get_version()
    __ret__ = pulumi.runtime.invoke('hcloud:index/getCertificate:getCertificate', __args__, opts=opts, typ=GetCertificateResult).value

    return AwaitableGetCertificateResult(
        certificate=__ret__.certificate,
        created=__ret__.created,
        domain_names=__ret__.domain_names,
        fingerprint=__ret__.fingerprint,
        id=__ret__.id,
        labels=__ret__.labels,
        name=__ret__.name,
        not_valid_after=__ret__.not_valid_after,
        not_valid_before=__ret__.not_valid_before,
        with_selector=__ret__.with_selector)

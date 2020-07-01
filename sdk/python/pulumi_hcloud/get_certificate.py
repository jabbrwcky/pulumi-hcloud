# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import warnings
import pulumi
import pulumi.runtime
from typing import Union
from . import utilities, tables

class GetCertificateResult:
    """
    A collection of values returned by getCertificate.
    """
    def __init__(__self__, certificate=None, created=None, domain_names=None, fingerprint=None, id=None, labels=None, name=None, not_valid_after=None, not_valid_before=None, with_selector=None):
        if certificate and not isinstance(certificate, str):
            raise TypeError("Expected argument 'certificate' to be a str")
        __self__.certificate = certificate
        if created and not isinstance(created, str):
            raise TypeError("Expected argument 'created' to be a str")
        __self__.created = created
        if domain_names and not isinstance(domain_names, list):
            raise TypeError("Expected argument 'domain_names' to be a list")
        __self__.domain_names = domain_names
        if fingerprint and not isinstance(fingerprint, str):
            raise TypeError("Expected argument 'fingerprint' to be a str")
        __self__.fingerprint = fingerprint
        if id and not isinstance(id, float):
            raise TypeError("Expected argument 'id' to be a float")
        __self__.id = id
        if labels and not isinstance(labels, dict):
            raise TypeError("Expected argument 'labels' to be a dict")
        __self__.labels = labels
        if name and not isinstance(name, str):
            raise TypeError("Expected argument 'name' to be a str")
        __self__.name = name
        if not_valid_after and not isinstance(not_valid_after, str):
            raise TypeError("Expected argument 'not_valid_after' to be a str")
        __self__.not_valid_after = not_valid_after
        if not_valid_before and not isinstance(not_valid_before, str):
            raise TypeError("Expected argument 'not_valid_before' to be a str")
        __self__.not_valid_before = not_valid_before
        if with_selector and not isinstance(with_selector, str):
            raise TypeError("Expected argument 'with_selector' to be a str")
        __self__.with_selector = with_selector
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

def get_certificate(id=None,name=None,with_selector=None,opts=None):
    """
    Provides details about a specific Hetzner Cloud Certificate.
    """
    __args__ = dict()


    __args__['id'] = id
    __args__['name'] = name
    __args__['withSelector'] = with_selector
    if opts is None:
        opts = pulumi.InvokeOptions()
    if opts.version is None:
        opts.version = utilities.get_version()
    __ret__ = pulumi.runtime.invoke('hcloud:index/getCertificate:getCertificate', __args__, opts=opts).value

    return AwaitableGetCertificateResult(
        certificate=__ret__.get('certificate'),
        created=__ret__.get('created'),
        domain_names=__ret__.get('domainNames'),
        fingerprint=__ret__.get('fingerprint'),
        id=__ret__.get('id'),
        labels=__ret__.get('labels'),
        name=__ret__.get('name'),
        not_valid_after=__ret__.get('notValidAfter'),
        not_valid_before=__ret__.get('notValidBefore'),
        with_selector=__ret__.get('withSelector'))

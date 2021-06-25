// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

import * as pulumi from "@pulumi/pulumi";
import { input as inputs, output as outputs } from "./types";
import * as utilities from "./utilities";

/**
 * Provides details about a specific Hetzner Cloud Certificate.
 *
 * ```typescript
 * import * as pulumi from "@pulumi/pulumi";
 * import * as hcloud from "@pulumi/hcloud";
 *
 * const sampleCertificate1 = pulumi.output(hcloud.getCertificate({
 *     name: "sample-certificate-1",
 * }, { async: true }));
 * const sampleCertificate2 = pulumi.output(hcloud.getCertificate({
 *     id: 4711,
 * }, { async: true }));
 * ```
 */
export function getCertificate(args?: GetCertificateArgs, opts?: pulumi.InvokeOptions): Promise<GetCertificateResult> {
    args = args || {};
    if (!opts) {
        opts = {}
    }

    if (!opts.version) {
        opts.version = utilities.getVersion();
    }
    return pulumi.runtime.invoke("hcloud:index/getCertificate:getCertificate", {
        "id": args.id,
        "name": args.name,
        "withSelector": args.withSelector,
    }, opts);
}

/**
 * A collection of arguments for invoking getCertificate.
 */
export interface GetCertificateArgs {
    /**
     * ID of the certificate.
     */
    readonly id?: number;
    /**
     * Name of the certificate.
     */
    readonly name?: string;
    /**
     * [Label selector](https://docs.hetzner.cloud/#overview-label-selector)
     */
    readonly withSelector?: string;
}

/**
 * A collection of values returned by getCertificate.
 */
export interface GetCertificateResult {
    /**
     * (string) PEM encoded TLS certificate.
     */
    readonly certificate: string;
    /**
     * (string) Point in time when the Certificate was created at Hetzner Cloud (in ISO-8601 format).
     */
    readonly created: string;
    /**
     * (list) Domains and subdomains covered by the certificate.
     */
    readonly domainNames: string[];
    /**
     * (string) Fingerprint of the certificate.
     */
    readonly fingerprint: string;
    /**
     * (int) Unique ID of the certificate.
     */
    readonly id: number;
    /**
     * (map) User-defined labels (key-value pairs) assigned to the certificate.
     */
    readonly labels: {[key: string]: any};
    /**
     * (string) Name of the Certificate.
     */
    readonly name?: string;
    /**
     * (string) Point in time when the Certificate stops being valid (in ISO-8601 format).
     */
    readonly notValidAfter: string;
    /**
     * (string) Point in time when the Certificate becomes valid (in ISO-8601 format).
     */
    readonly notValidBefore: string;
    readonly type: string;
    readonly withSelector?: string;
}

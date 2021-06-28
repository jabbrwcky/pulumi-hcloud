// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

import * as pulumi from "@pulumi/pulumi";
import { input as inputs, output as outputs } from "./types";
import * as utilities from "./utilities";

/**
 * Provides details about a specific Hetzner Cloud Firewall.
 *
 * ```typescript
 * import * as pulumi from "@pulumi/pulumi";
 * import * as hcloud from "@pulumi/hcloud";
 *
 * const sampleFirewall1 = pulumi.output(hcloud.getFirewall({
 *     name: "sample-firewall-1",
 * }, { async: true }));
 * const sampleFirewall2 = pulumi.output(hcloud.getFirewall({
 *     id: 4711,
 * }, { async: true }));
 * ```
 */
export function getFirewall(args?: GetFirewallArgs, opts?: pulumi.InvokeOptions): Promise<GetFirewallResult> {
    args = args || {};
    if (!opts) {
        opts = {}
    }

    if (!opts.version) {
        opts.version = utilities.getVersion();
    }
    return pulumi.runtime.invoke("hcloud:index/getFirewall:getFirewall", {
        "id": args.id,
        "labels": args.labels,
        "mostRecent": args.mostRecent,
        "name": args.name,
        "rules": args.rules,
        "withSelector": args.withSelector,
    }, opts);
}

/**
 * A collection of arguments for invoking getFirewall.
 */
export interface GetFirewallArgs {
    /**
     * ID of the firewall.
     */
    readonly id?: number;
    /**
     * (map) User-defined labels (key-value pairs)
     */
    readonly labels?: {[key: string]: any};
    readonly mostRecent?: boolean;
    /**
     * Name of the firewall.
     */
    readonly name?: string;
    /**
     * (string)  Configuration of a Rule from this Firewall.
     */
    readonly rules?: inputs.GetFirewallRule[];
    /**
     * [Label selector](https://docs.hetzner.cloud/#overview-label-selector)
     */
    readonly withSelector?: string;
}

/**
 * A collection of values returned by getFirewall.
 */
export interface GetFirewallResult {
    /**
     * (int) Unique ID of the Firewall.
     */
    readonly id?: number;
    /**
     * (map) User-defined labels (key-value pairs)
     */
    readonly labels?: {[key: string]: any};
    readonly mostRecent?: boolean;
    /**
     * (string) Name of the Firewall.
     */
    readonly name: string;
    /**
     * (string)  Configuration of a Rule from this Firewall.
     */
    readonly rules?: outputs.GetFirewallRule[];
    readonly withSelector?: string;
}

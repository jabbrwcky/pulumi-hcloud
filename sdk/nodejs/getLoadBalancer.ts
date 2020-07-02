// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

import * as pulumi from "@pulumi/pulumi";
import * as inputs from "./types/input";
import * as outputs from "./types/output";
import * as utilities from "./utilities";

/**
 * Provides details about a specific Hetzner Cloud Server.
 *
 * ## Example Usage
 *
 * ```typescript
 * import * as pulumi from "@pulumi/pulumi";
 * import * as hcloud from "@pulumi/hcloud";
 *
 * const lb1 = pulumi.output(hcloud.getLoadBalancer({
 *     name: "my-load-balancer",
 * }, { async: true }));
 * const lb2 = pulumi.output(hcloud.getLoadBalancer({
 *     id: 123,
 * }, { async: true }));
 * const lb3 = pulumi.output(hcloud.getLoadBalancer({
 *     withSelector: "key=value",
 * }, { async: true }));
 * ```
 */
export function getLoadBalancer(args?: GetLoadBalancerArgs, opts?: pulumi.InvokeOptions): Promise<GetLoadBalancerResult> {
    args = args || {};
    if (!opts) {
        opts = {}
    }

    if (!opts.version) {
        opts.version = utilities.getVersion();
    }
    return pulumi.runtime.invoke("hcloud:index/getLoadBalancer:getLoadBalancer", {
        "id": args.id,
        "name": args.name,
        "withSelector": args.withSelector,
    }, opts);
}

/**
 * A collection of arguments for invoking getLoadBalancer.
 */
export interface GetLoadBalancerArgs {
    readonly id?: number;
    readonly name?: string;
    readonly withSelector?: string;
}

/**
 * A collection of values returned by getLoadBalancer.
 */
export interface GetLoadBalancerResult {
    readonly algorithm: outputs.GetLoadBalancerAlgorithm;
    readonly id?: number;
    readonly ipv4: string;
    readonly ipv6: string;
    readonly labels: {[key: string]: any};
    readonly loadBalancerType: string;
    readonly location: string;
    readonly name?: string;
    readonly networkZone: string;
    readonly services: outputs.GetLoadBalancerService[];
    readonly targets: outputs.GetLoadBalancerTarget[];
    readonly withSelector?: string;
}

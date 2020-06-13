// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

import * as pulumi from "@pulumi/pulumi";
import * as inputs from "./types/input";
import * as outputs from "./types/output";
import * as utilities from "./utilities";

/**
 * Provides details about a Hetzner Cloud Floating IP.
 *
 * This resource can be useful when you need to determine a Floating IP ID based on the IP address.
 *
 * ## Example Usage
 *
 * ### Additional Examples
 *
 * ```typescript
 * import * as pulumi from "@pulumi/pulumi";
 * import * as hcloud from "@pulumi/hcloud";
 *
 * const ip1 = pulumi.output(hcloud.getFloatingIp({
 *     ipAddress: "1.2.3.4",
 * }, { async: true }));
 * const image2 = pulumi.output(hcloud.getFloatingIp({
 *     withSelector: "key=value",
 * }, { async: true }));
 * const main: hcloud.FloatingIpAssignment[] = [];
 * for (let i = 0; i < var_counter; i++) {
 *     main.push(new hcloud.FloatingIpAssignment(`main-${i}`, {
 *         floatingIpId: ip1.id!,
 *         serverId: hcloud_server_main.id,
 *     }));
 * }
 * ```
 */
export function getFloatingIp(args?: GetFloatingIpArgs, opts?: pulumi.InvokeOptions): Promise<GetFloatingIpResult> {
    args = args || {};
    if (!opts) {
        opts = {}
    }

    if (!opts.version) {
        opts.version = utilities.getVersion();
    }
    return pulumi.runtime.invoke("hcloud:index/getFloatingIp:getFloatingIp", {
        "id": args.id,
        "ipAddress": args.ipAddress,
        "name": args.name,
        "selector": args.selector,
        "withSelector": args.withSelector,
    }, opts);
}

/**
 * A collection of arguments for invoking getFloatingIp.
 */
export interface GetFloatingIpArgs {
    readonly id?: number;
    readonly ipAddress?: string;
    readonly name?: string;
    /**
     * @deprecated Please use the with_selector property instead.
     */
    readonly selector?: string;
    readonly withSelector?: string;
}

/**
 * A collection of values returned by getFloatingIp.
 */
export interface GetFloatingIpResult {
    readonly description: string;
    readonly homeLocation: string;
    readonly id?: number;
    readonly ipAddress: string;
    readonly ipNetwork: string;
    readonly labels: {[key: string]: any};
    readonly name?: string;
    /**
     * @deprecated Please use the with_selector property instead.
     */
    readonly selector?: string;
    readonly serverId: number;
    readonly type: string;
    readonly withSelector?: string;
}

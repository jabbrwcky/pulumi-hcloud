// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

import * as pulumi from "@pulumi/pulumi";
import * as inputs from "./types/input";
import * as outputs from "./types/output";
import * as utilities from "./utilities";

export function getServer(args?: GetServerArgs, opts?: pulumi.InvokeOptions): Promise<GetServerResult> {
    args = args || {};
    if (!opts) {
        opts = {}
    }

    if (!opts.version) {
        opts.version = utilities.getVersion();
    }
    return pulumi.runtime.invoke("hcloud:index/getServer:getServer", {
        "id": args.id,
        "name": args.name,
        "selector": args.selector,
        "withSelector": args.withSelector,
        "withStatuses": args.withStatuses,
    }, opts);
}

/**
 * A collection of arguments for invoking getServer.
 */
export interface GetServerArgs {
    readonly id?: number;
    readonly name?: string;
    /**
     * @deprecated Please use the with_selector property instead.
     */
    readonly selector?: string;
    readonly withSelector?: string;
    readonly withStatuses?: string[];
}

/**
 * A collection of values returned by getServer.
 */
export interface GetServerResult {
    readonly backupWindow: string;
    readonly backups: boolean;
    readonly datacenter: string;
    readonly id: number;
    readonly image: string;
    readonly ipv4Address: string;
    readonly ipv6Address: string;
    readonly ipv6Network: string;
    readonly iso: string;
    readonly labels: {[key: string]: any};
    readonly location: string;
    readonly name: string;
    readonly rescue: string;
    /**
     * @deprecated Please use the with_selector property instead.
     */
    readonly selector?: string;
    readonly serverType: string;
    readonly status: string;
    readonly withSelector?: string;
    readonly withStatuses?: string[];
}

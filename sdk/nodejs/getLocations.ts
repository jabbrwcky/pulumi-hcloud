// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

import * as pulumi from "@pulumi/pulumi";
import * as inputs from "./types/input";
import * as outputs from "./types/output";
import * as utilities from "./utilities";

/**
 * Provides a list of available Hetzner Cloud Locations.
 * This resource may be useful to create highly available infrastructure, distributed across several locations.
 *
 * ## Example Usage
 *
 * ```typescript
 * import * as pulumi from "@pulumi/pulumi";
 * import * as hcloud from "@pulumi/hcloud";
 *
 * const ds = hcloud.getLocations({});
 * const workers: hcloud.Server[];
 * for (const range = {value: 0}; range.value < 3; range.value++) {
 *     workers.push(new hcloud.Server(`workers-${range.value}`, {
 *         image: "debian-9",
 *         serverType: "cx31",
 *         location: ds.then(ds => ds.names)[range.value],
 *     }));
 * }
 * ```
 */
export function getLocations(args?: GetLocationsArgs, opts?: pulumi.InvokeOptions): Promise<GetLocationsResult> {
    args = args || {};
    if (!opts) {
        opts = {}
    }

    if (!opts.version) {
        opts.version = utilities.getVersion();
    }
    return pulumi.runtime.invoke("hcloud:index/getLocations:getLocations", {
        "locationIds": args.locationIds,
    }, opts);
}

/**
 * A collection of arguments for invoking getLocations.
 */
export interface GetLocationsArgs {
    /**
     * (list) List of unique location identifiers.
     */
    readonly locationIds?: string[];
}

/**
 * A collection of values returned by getLocations.
 */
export interface GetLocationsResult {
    /**
     * (list) List of all location descriptions.
     */
    readonly descriptions: string[];
    /**
     * The provider-assigned unique ID for this managed resource.
     */
    readonly id: string;
    /**
     * (list) List of unique location identifiers.
     */
    readonly locationIds?: string[];
    /**
     * (list) List of location names.
     */
    readonly names: string[];
}

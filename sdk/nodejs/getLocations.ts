// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

import * as pulumi from "@pulumi/pulumi";
import { input as inputs, output as outputs } from "./types";
import * as utilities from "./utilities";

/**
 * Provides a list of available Hetzner Cloud Locations.
 * This resource may be useful to create highly available infrastructure, distributed across several locations.
 */
export function getLocations(args?: GetLocationsArgs, opts?: pulumi.InvokeOptions): Promise<GetLocationsResult> {
    args = args || {};
    if (!opts) {
        opts = {}
    }

    opts = pulumi.mergeOptions(utilities.resourceOptsDefaults(), opts);
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
     *
     * @deprecated Use locations list instead
     */
    locationIds?: string[];
}

/**
 * A collection of values returned by getLocations.
 */
export interface GetLocationsResult {
    /**
     * (list) List of all location descriptions.
     *
     * @deprecated Use locations list instead
     */
    readonly descriptions: string[];
    /**
     * The provider-assigned unique ID for this managed resource.
     */
    readonly id: string;
    /**
     * (list) List of unique location identifiers.
     *
     * @deprecated Use locations list instead
     */
    readonly locationIds?: string[];
    /**
     * (list) List of all locations. See `data.hcloud_location` for schema.
     */
    readonly locations: outputs.GetLocationsLocation[];
    /**
     * (list) List of location names.
     *
     * @deprecated Use locations list instead
     */
    readonly names: string[];
}

export function getLocationsOutput(args?: GetLocationsOutputArgs, opts?: pulumi.InvokeOptions): pulumi.Output<GetLocationsResult> {
    return pulumi.output(args).apply(a => getLocations(a, opts))
}

/**
 * A collection of arguments for invoking getLocations.
 */
export interface GetLocationsOutputArgs {
    /**
     * (list) List of unique location identifiers.
     *
     * @deprecated Use locations list instead
     */
    locationIds?: pulumi.Input<pulumi.Input<string>[]>;
}

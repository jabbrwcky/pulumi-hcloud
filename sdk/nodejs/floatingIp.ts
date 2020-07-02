// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

import * as pulumi from "@pulumi/pulumi";
import * as utilities from "./utilities";

/**
 * Provides a Hetzner Cloud Floating IP to represent a publicly-accessible static IP address that can be mapped to one of your servers.
 *
 * ## Example Usage
 *
 * ```typescript
 * import * as pulumi from "@pulumi/pulumi";
 * import * as hcloud from "@pulumi/hcloud";
 *
 * const node1 = new hcloud.Server("node1", {
 *     image: "debian-9",
 *     serverType: "cx11",
 * });
 * const master = new hcloud.FloatingIp("master", {
 *     serverId: node1.id.apply(id => Number.parseFloat(id)),
 *     type: "ipv4",
 * });
 * ```
 */
export class FloatingIp extends pulumi.CustomResource {
    /**
     * Get an existing FloatingIp resource's state with the given name, ID, and optional extra
     * properties used to qualify the lookup.
     *
     * @param name The _unique_ name of the resulting resource.
     * @param id The _unique_ provider ID of the resource to lookup.
     * @param state Any extra arguments used during the lookup.
     * @param opts Optional settings to control the behavior of the CustomResource.
     */
    public static get(name: string, id: pulumi.Input<pulumi.ID>, state?: FloatingIpState, opts?: pulumi.CustomResourceOptions): FloatingIp {
        return new FloatingIp(name, <any>state, { ...opts, id: id });
    }

    /** @internal */
    public static readonly __pulumiType = 'hcloud:index/floatingIp:FloatingIp';

    /**
     * Returns true if the given object is an instance of FloatingIp.  This is designed to work even
     * when multiple copies of the Pulumi SDK have been loaded into the same process.
     */
    public static isInstance(obj: any): obj is FloatingIp {
        if (obj === undefined || obj === null) {
            return false;
        }
        return obj['__pulumiType'] === FloatingIp.__pulumiType;
    }

    public readonly description!: pulumi.Output<string | undefined>;
    public readonly homeLocation!: pulumi.Output<string>;
    public /*out*/ readonly ipAddress!: pulumi.Output<string>;
    public /*out*/ readonly ipNetwork!: pulumi.Output<string>;
    public readonly labels!: pulumi.Output<{[key: string]: any} | undefined>;
    public readonly name!: pulumi.Output<string>;
    public readonly serverId!: pulumi.Output<number>;
    public readonly type!: pulumi.Output<string>;

    /**
     * Create a FloatingIp resource with the given unique name, arguments, and options.
     *
     * @param name The _unique_ name of the resource.
     * @param args The arguments to use to populate this resource's properties.
     * @param opts A bag of options that control this resource's behavior.
     */
    constructor(name: string, args: FloatingIpArgs, opts?: pulumi.CustomResourceOptions)
    constructor(name: string, argsOrState?: FloatingIpArgs | FloatingIpState, opts?: pulumi.CustomResourceOptions) {
        let inputs: pulumi.Inputs = {};
        if (opts && opts.id) {
            const state = argsOrState as FloatingIpState | undefined;
            inputs["description"] = state ? state.description : undefined;
            inputs["homeLocation"] = state ? state.homeLocation : undefined;
            inputs["ipAddress"] = state ? state.ipAddress : undefined;
            inputs["ipNetwork"] = state ? state.ipNetwork : undefined;
            inputs["labels"] = state ? state.labels : undefined;
            inputs["name"] = state ? state.name : undefined;
            inputs["serverId"] = state ? state.serverId : undefined;
            inputs["type"] = state ? state.type : undefined;
        } else {
            const args = argsOrState as FloatingIpArgs | undefined;
            if (!args || args.type === undefined) {
                throw new Error("Missing required property 'type'");
            }
            inputs["description"] = args ? args.description : undefined;
            inputs["homeLocation"] = args ? args.homeLocation : undefined;
            inputs["labels"] = args ? args.labels : undefined;
            inputs["name"] = args ? args.name : undefined;
            inputs["serverId"] = args ? args.serverId : undefined;
            inputs["type"] = args ? args.type : undefined;
            inputs["ipAddress"] = undefined /*out*/;
            inputs["ipNetwork"] = undefined /*out*/;
        }
        if (!opts) {
            opts = {}
        }

        if (!opts.version) {
            opts.version = utilities.getVersion();
        }
        super(FloatingIp.__pulumiType, name, inputs, opts);
    }
}

/**
 * Input properties used for looking up and filtering FloatingIp resources.
 */
export interface FloatingIpState {
    readonly description?: pulumi.Input<string>;
    readonly homeLocation?: pulumi.Input<string>;
    readonly ipAddress?: pulumi.Input<string>;
    readonly ipNetwork?: pulumi.Input<string>;
    readonly labels?: pulumi.Input<{[key: string]: any}>;
    readonly name?: pulumi.Input<string>;
    readonly serverId?: pulumi.Input<number>;
    readonly type?: pulumi.Input<string>;
}

/**
 * The set of arguments for constructing a FloatingIp resource.
 */
export interface FloatingIpArgs {
    readonly description?: pulumi.Input<string>;
    readonly homeLocation?: pulumi.Input<string>;
    readonly labels?: pulumi.Input<{[key: string]: any}>;
    readonly name?: pulumi.Input<string>;
    readonly serverId?: pulumi.Input<number>;
    readonly type: pulumi.Input<string>;
}

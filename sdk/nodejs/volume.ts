// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

import * as pulumi from "@pulumi/pulumi";
import * as utilities from "./utilities";

/**
 * Provides a Hetzner Cloud volume resource to manage volumes.
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
 * const master = new hcloud.Volume("master", {
 *     automount: true,
 *     serverId: node1.id.apply(id => Number.parseFloat(id)),
 *     size: 50,
 * });
 * ```
 */
export class Volume extends pulumi.CustomResource {
    /**
     * Get an existing Volume resource's state with the given name, ID, and optional extra
     * properties used to qualify the lookup.
     *
     * @param name The _unique_ name of the resulting resource.
     * @param id The _unique_ provider ID of the resource to lookup.
     * @param state Any extra arguments used during the lookup.
     * @param opts Optional settings to control the behavior of the CustomResource.
     */
    public static get(name: string, id: pulumi.Input<pulumi.ID>, state?: VolumeState, opts?: pulumi.CustomResourceOptions): Volume {
        return new Volume(name, <any>state, { ...opts, id: id });
    }

    /** @internal */
    public static readonly __pulumiType = 'hcloud:index/volume:Volume';

    /**
     * Returns true if the given object is an instance of Volume.  This is designed to work even
     * when multiple copies of the Pulumi SDK have been loaded into the same process.
     */
    public static isInstance(obj: any): obj is Volume {
        if (obj === undefined || obj === null) {
            return false;
        }
        return obj['__pulumiType'] === Volume.__pulumiType;
    }

    public readonly automount!: pulumi.Output<boolean | undefined>;
    public readonly format!: pulumi.Output<string | undefined>;
    public readonly labels!: pulumi.Output<{[key: string]: any} | undefined>;
    public /*out*/ readonly linuxDevice!: pulumi.Output<string>;
    public readonly location!: pulumi.Output<string>;
    public readonly name!: pulumi.Output<string>;
    public readonly serverId!: pulumi.Output<number>;
    public readonly size!: pulumi.Output<number>;

    /**
     * Create a Volume resource with the given unique name, arguments, and options.
     *
     * @param name The _unique_ name of the resource.
     * @param args The arguments to use to populate this resource's properties.
     * @param opts A bag of options that control this resource's behavior.
     */
    constructor(name: string, args: VolumeArgs, opts?: pulumi.CustomResourceOptions)
    constructor(name: string, argsOrState?: VolumeArgs | VolumeState, opts?: pulumi.CustomResourceOptions) {
        let inputs: pulumi.Inputs = {};
        if (opts && opts.id) {
            const state = argsOrState as VolumeState | undefined;
            inputs["automount"] = state ? state.automount : undefined;
            inputs["format"] = state ? state.format : undefined;
            inputs["labels"] = state ? state.labels : undefined;
            inputs["linuxDevice"] = state ? state.linuxDevice : undefined;
            inputs["location"] = state ? state.location : undefined;
            inputs["name"] = state ? state.name : undefined;
            inputs["serverId"] = state ? state.serverId : undefined;
            inputs["size"] = state ? state.size : undefined;
        } else {
            const args = argsOrState as VolumeArgs | undefined;
            if (!args || args.size === undefined) {
                throw new Error("Missing required property 'size'");
            }
            inputs["automount"] = args ? args.automount : undefined;
            inputs["format"] = args ? args.format : undefined;
            inputs["labels"] = args ? args.labels : undefined;
            inputs["location"] = args ? args.location : undefined;
            inputs["name"] = args ? args.name : undefined;
            inputs["serverId"] = args ? args.serverId : undefined;
            inputs["size"] = args ? args.size : undefined;
            inputs["linuxDevice"] = undefined /*out*/;
        }
        if (!opts) {
            opts = {}
        }

        if (!opts.version) {
            opts.version = utilities.getVersion();
        }
        super(Volume.__pulumiType, name, inputs, opts);
    }
}

/**
 * Input properties used for looking up and filtering Volume resources.
 */
export interface VolumeState {
    readonly automount?: pulumi.Input<boolean>;
    readonly format?: pulumi.Input<string>;
    readonly labels?: pulumi.Input<{[key: string]: any}>;
    readonly linuxDevice?: pulumi.Input<string>;
    readonly location?: pulumi.Input<string>;
    readonly name?: pulumi.Input<string>;
    readonly serverId?: pulumi.Input<number>;
    readonly size?: pulumi.Input<number>;
}

/**
 * The set of arguments for constructing a Volume resource.
 */
export interface VolumeArgs {
    readonly automount?: pulumi.Input<boolean>;
    readonly format?: pulumi.Input<string>;
    readonly labels?: pulumi.Input<{[key: string]: any}>;
    readonly location?: pulumi.Input<string>;
    readonly name?: pulumi.Input<string>;
    readonly serverId?: pulumi.Input<number>;
    readonly size: pulumi.Input<number>;
}

// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

import * as pulumi from "@pulumi/pulumi";
import * as utilities from "./utilities";

/**
 * Adds a target to a Hetzner Cloud Load Balancer.
 *
 * ## Example Usage
 *
 * ```typescript
 * import * as pulumi from "@pulumi/pulumi";
 * import * as hcloud from "@pulumi/hcloud";
 *
 * const myServer = new hcloud.Server("myServer", {
 *     serverType: "cx11",
 *     image: "ubuntu-18.04",
 * });
 * const loadBalancer = new hcloud.LoadBalancer("loadBalancer", {
 *     loadBalancerType: "lb11",
 *     location: "nbg1",
 * });
 * const loadBalancerTarget = new hcloud.LoadBalancerTarget("loadBalancerTarget", {
 *     type: "server",
 *     loadBalancerId: loadBalancer.id,
 *     serverId: myServer.id,
 * });
 * ```
 */
export class LoadBalancerTarget extends pulumi.CustomResource {
    /**
     * Get an existing LoadBalancerTarget resource's state with the given name, ID, and optional extra
     * properties used to qualify the lookup.
     *
     * @param name The _unique_ name of the resulting resource.
     * @param id The _unique_ provider ID of the resource to lookup.
     * @param state Any extra arguments used during the lookup.
     * @param opts Optional settings to control the behavior of the CustomResource.
     */
    public static get(name: string, id: pulumi.Input<pulumi.ID>, state?: LoadBalancerTargetState, opts?: pulumi.CustomResourceOptions): LoadBalancerTarget {
        return new LoadBalancerTarget(name, <any>state, { ...opts, id: id });
    }

    /** @internal */
    public static readonly __pulumiType = 'hcloud:index/loadBalancerTarget:LoadBalancerTarget';

    /**
     * Returns true if the given object is an instance of LoadBalancerTarget.  This is designed to work even
     * when multiple copies of the Pulumi SDK have been loaded into the same process.
     */
    public static isInstance(obj: any): obj is LoadBalancerTarget {
        if (obj === undefined || obj === null) {
            return false;
        }
        return obj['__pulumiType'] === LoadBalancerTarget.__pulumiType;
    }

    /**
     * IP address for an IP Target. Required if
     * `type` is `ip`.
     */
    public readonly ip!: pulumi.Output<string | undefined>;
    /**
     * Label Selector selecting targets
     * for this Load Balancer. Required if `type` is `labelSelector`.
     */
    public readonly labelSelector!: pulumi.Output<string | undefined>;
    /**
     * ID of the Load Balancer to which
     * the target gets attached.
     */
    public readonly loadBalancerId!: pulumi.Output<number>;
    /**
     * ID of the server which should be a
     * target for this Load Balancer. Required if `type` is `server`
     */
    public readonly serverId!: pulumi.Output<number | undefined>;
    /**
     * Type of the target. Possible values
     * `server`, `labelSelector`, `ip`.
     */
    public readonly type!: pulumi.Output<string>;
    /**
     * use the private IP to connect to
     * Load Balancer targets. Only allowed if type is `server` or
     * `labelSelector`.
     */
    public readonly usePrivateIp!: pulumi.Output<boolean>;

    /**
     * Create a LoadBalancerTarget resource with the given unique name, arguments, and options.
     *
     * @param name The _unique_ name of the resource.
     * @param args The arguments to use to populate this resource's properties.
     * @param opts A bag of options that control this resource's behavior.
     */
    constructor(name: string, args: LoadBalancerTargetArgs, opts?: pulumi.CustomResourceOptions)
    constructor(name: string, argsOrState?: LoadBalancerTargetArgs | LoadBalancerTargetState, opts?: pulumi.CustomResourceOptions) {
        let inputs: pulumi.Inputs = {};
        opts = opts || {};
        if (opts.id) {
            const state = argsOrState as LoadBalancerTargetState | undefined;
            inputs["ip"] = state ? state.ip : undefined;
            inputs["labelSelector"] = state ? state.labelSelector : undefined;
            inputs["loadBalancerId"] = state ? state.loadBalancerId : undefined;
            inputs["serverId"] = state ? state.serverId : undefined;
            inputs["type"] = state ? state.type : undefined;
            inputs["usePrivateIp"] = state ? state.usePrivateIp : undefined;
        } else {
            const args = argsOrState as LoadBalancerTargetArgs | undefined;
            if ((!args || args.loadBalancerId === undefined) && !opts.urn) {
                throw new Error("Missing required property 'loadBalancerId'");
            }
            if ((!args || args.type === undefined) && !opts.urn) {
                throw new Error("Missing required property 'type'");
            }
            inputs["ip"] = args ? args.ip : undefined;
            inputs["labelSelector"] = args ? args.labelSelector : undefined;
            inputs["loadBalancerId"] = args ? args.loadBalancerId : undefined;
            inputs["serverId"] = args ? args.serverId : undefined;
            inputs["type"] = args ? args.type : undefined;
            inputs["usePrivateIp"] = args ? args.usePrivateIp : undefined;
        }
        if (!opts.version) {
            opts = pulumi.mergeOptions(opts, { version: utilities.getVersion()});
        }
        super(LoadBalancerTarget.__pulumiType, name, inputs, opts);
    }
}

/**
 * Input properties used for looking up and filtering LoadBalancerTarget resources.
 */
export interface LoadBalancerTargetState {
    /**
     * IP address for an IP Target. Required if
     * `type` is `ip`.
     */
    ip?: pulumi.Input<string>;
    /**
     * Label Selector selecting targets
     * for this Load Balancer. Required if `type` is `labelSelector`.
     */
    labelSelector?: pulumi.Input<string>;
    /**
     * ID of the Load Balancer to which
     * the target gets attached.
     */
    loadBalancerId?: pulumi.Input<number>;
    /**
     * ID of the server which should be a
     * target for this Load Balancer. Required if `type` is `server`
     */
    serverId?: pulumi.Input<number>;
    /**
     * Type of the target. Possible values
     * `server`, `labelSelector`, `ip`.
     */
    type?: pulumi.Input<string>;
    /**
     * use the private IP to connect to
     * Load Balancer targets. Only allowed if type is `server` or
     * `labelSelector`.
     */
    usePrivateIp?: pulumi.Input<boolean>;
}

/**
 * The set of arguments for constructing a LoadBalancerTarget resource.
 */
export interface LoadBalancerTargetArgs {
    /**
     * IP address for an IP Target. Required if
     * `type` is `ip`.
     */
    ip?: pulumi.Input<string>;
    /**
     * Label Selector selecting targets
     * for this Load Balancer. Required if `type` is `labelSelector`.
     */
    labelSelector?: pulumi.Input<string>;
    /**
     * ID of the Load Balancer to which
     * the target gets attached.
     */
    loadBalancerId: pulumi.Input<number>;
    /**
     * ID of the server which should be a
     * target for this Load Balancer. Required if `type` is `server`
     */
    serverId?: pulumi.Input<number>;
    /**
     * Type of the target. Possible values
     * `server`, `labelSelector`, `ip`.
     */
    type: pulumi.Input<string>;
    /**
     * use the private IP to connect to
     * Load Balancer targets. Only allowed if type is `server` or
     * `labelSelector`.
     */
    usePrivateIp?: pulumi.Input<boolean>;
}

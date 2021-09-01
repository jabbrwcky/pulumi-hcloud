// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

import * as pulumi from "@pulumi/pulumi";
import * as utilities from "./utilities";

/**
 * Provides a Hetzner Cloud Reverse DNS Entry to create, modify and reset reverse dns entries for Hetzner Cloud Servers, Floating IPs or Load Balancers.
 *
 * ## Example Usage
 *
 * For servers:
 *
 * ```typescript
 * import * as pulumi from "@pulumi/pulumi";
 * import * as hcloud from "@pulumi/hcloud";
 *
 * const node1 = new hcloud.Server("node1", {
 *     image: "debian-9",
 *     serverType: "cx11",
 * });
 * const master = new hcloud.Rdns("master", {
 *     serverId: node1.id,
 *     ipAddress: node1.ipv4Address,
 *     dnsPtr: "example.com",
 * });
 * ```
 *
 * For Floating IPs:
 *
 * ```typescript
 * import * as pulumi from "@pulumi/pulumi";
 * import * as hcloud from "@pulumi/hcloud";
 *
 * const floating1 = new hcloud.FloatingIp("floating1", {
 *     homeLocation: "nbg1",
 *     type: "ipv4",
 * });
 * const floatingMaster = new hcloud.Rdns("floating_master", {
 *     dnsPtr: "example.com",
 *     floatingIpId: floating1.id.apply(id => Number.parseFloat(id)),
 *     ipAddress: floating1.ipAddress,
 * });
 * ```
 *
 * For Load Balancers:
 *
 * ```typescript
 * import * as pulumi from "@pulumi/pulumi";
 * import * as hcloud from "@pulumi/hcloud";
 *
 * const loadBalancer1 = new hcloud.LoadBalancer("load_balancer1", {
 *     loadBalancerType: "lb11",
 *     location: "fsn1",
 * });
 * const loadBalancerMaster = new hcloud.Rdns("load_balancer_master", {
 *     dnsPtr: "example.com",
 *     ipAddress: loadBalancer1.ipv4,
 *     loadBalancerId: loadBalancer1.id.apply(id => Number.parseFloat(id)),
 * });
 * ```
 *
 * ## Import
 *
 * Reverse DNS entries can be imported using a compound ID with the following format`<prefix (s for server/ f for floating ip / l for load balancer)>-<server, floating ip or load balancer ID>-<IP address>` # import reverse dns entry on server with id 123, ip 192.168.100.1
 *
 * ```sh
 *  $ pulumi import hcloud:index/rdns:Rdns myrdns s-123-192.168.100.1
 * ```
 *
 * # import reverse dns entry on floating ip with id 123, ip 2001:db8::1
 *
 * ```sh
 *  $ pulumi import hcloud:index/rdns:Rdns myrdns f-123-2001:db8::1
 * ```
 *
 * # import reverse dns entry on load balancer with id 123, ip 2001:db8::1
 *
 * ```sh
 *  $ pulumi import hcloud:index/rdns:Rdns myrdns l-123-2001:db8::1
 * ```
 */
export class Rdns extends pulumi.CustomResource {
    /**
     * Get an existing Rdns resource's state with the given name, ID, and optional extra
     * properties used to qualify the lookup.
     *
     * @param name The _unique_ name of the resulting resource.
     * @param id The _unique_ provider ID of the resource to lookup.
     * @param state Any extra arguments used during the lookup.
     * @param opts Optional settings to control the behavior of the CustomResource.
     */
    public static get(name: string, id: pulumi.Input<pulumi.ID>, state?: RdnsState, opts?: pulumi.CustomResourceOptions): Rdns {
        return new Rdns(name, <any>state, { ...opts, id: id });
    }

    /** @internal */
    public static readonly __pulumiType = 'hcloud:index/rdns:Rdns';

    /**
     * Returns true if the given object is an instance of Rdns.  This is designed to work even
     * when multiple copies of the Pulumi SDK have been loaded into the same process.
     */
    public static isInstance(obj: any): obj is Rdns {
        if (obj === undefined || obj === null) {
            return false;
        }
        return obj['__pulumiType'] === Rdns.__pulumiType;
    }

    /**
     * The DNS address the `ipAddress` should resolve to.
     */
    public readonly dnsPtr!: pulumi.Output<string>;
    /**
     * The Floating IP the `ipAddress` belongs to. Specify only one of `serverId`, `floatingIpId` and `loadBalancerId`.
     */
    public readonly floatingIpId!: pulumi.Output<number | undefined>;
    /**
     * The IP address that should point to `dnsPtr`.
     */
    public readonly ipAddress!: pulumi.Output<string>;
    /**
     * The Load Balancer the `ipAddress` belongs to. Specify only one of `serverId`, `floatingIpId` and `loadBalancerId`.
     */
    public readonly loadBalancerId!: pulumi.Output<number | undefined>;
    /**
     * The server the `ipAddress` belongs to. Specify only one of `serverId`, `floatingIpId` and `loadBalancerId`.
     */
    public readonly serverId!: pulumi.Output<number | undefined>;

    /**
     * Create a Rdns resource with the given unique name, arguments, and options.
     *
     * @param name The _unique_ name of the resource.
     * @param args The arguments to use to populate this resource's properties.
     * @param opts A bag of options that control this resource's behavior.
     */
    constructor(name: string, args: RdnsArgs, opts?: pulumi.CustomResourceOptions)
    constructor(name: string, argsOrState?: RdnsArgs | RdnsState, opts?: pulumi.CustomResourceOptions) {
        let inputs: pulumi.Inputs = {};
        opts = opts || {};
        if (opts.id) {
            const state = argsOrState as RdnsState | undefined;
            inputs["dnsPtr"] = state ? state.dnsPtr : undefined;
            inputs["floatingIpId"] = state ? state.floatingIpId : undefined;
            inputs["ipAddress"] = state ? state.ipAddress : undefined;
            inputs["loadBalancerId"] = state ? state.loadBalancerId : undefined;
            inputs["serverId"] = state ? state.serverId : undefined;
        } else {
            const args = argsOrState as RdnsArgs | undefined;
            if ((!args || args.dnsPtr === undefined) && !opts.urn) {
                throw new Error("Missing required property 'dnsPtr'");
            }
            if ((!args || args.ipAddress === undefined) && !opts.urn) {
                throw new Error("Missing required property 'ipAddress'");
            }
            inputs["dnsPtr"] = args ? args.dnsPtr : undefined;
            inputs["floatingIpId"] = args ? args.floatingIpId : undefined;
            inputs["ipAddress"] = args ? args.ipAddress : undefined;
            inputs["loadBalancerId"] = args ? args.loadBalancerId : undefined;
            inputs["serverId"] = args ? args.serverId : undefined;
        }
        if (!opts.version) {
            opts = pulumi.mergeOptions(opts, { version: utilities.getVersion()});
        }
        super(Rdns.__pulumiType, name, inputs, opts);
    }
}

/**
 * Input properties used for looking up and filtering Rdns resources.
 */
export interface RdnsState {
    /**
     * The DNS address the `ipAddress` should resolve to.
     */
    readonly dnsPtr?: pulumi.Input<string>;
    /**
     * The Floating IP the `ipAddress` belongs to. Specify only one of `serverId`, `floatingIpId` and `loadBalancerId`.
     */
    readonly floatingIpId?: pulumi.Input<number>;
    /**
     * The IP address that should point to `dnsPtr`.
     */
    readonly ipAddress?: pulumi.Input<string>;
    /**
     * The Load Balancer the `ipAddress` belongs to. Specify only one of `serverId`, `floatingIpId` and `loadBalancerId`.
     */
    readonly loadBalancerId?: pulumi.Input<number>;
    /**
     * The server the `ipAddress` belongs to. Specify only one of `serverId`, `floatingIpId` and `loadBalancerId`.
     */
    readonly serverId?: pulumi.Input<number>;
}

/**
 * The set of arguments for constructing a Rdns resource.
 */
export interface RdnsArgs {
    /**
     * The DNS address the `ipAddress` should resolve to.
     */
    readonly dnsPtr: pulumi.Input<string>;
    /**
     * The Floating IP the `ipAddress` belongs to. Specify only one of `serverId`, `floatingIpId` and `loadBalancerId`.
     */
    readonly floatingIpId?: pulumi.Input<number>;
    /**
     * The IP address that should point to `dnsPtr`.
     */
    readonly ipAddress: pulumi.Input<string>;
    /**
     * The Load Balancer the `ipAddress` belongs to. Specify only one of `serverId`, `floatingIpId` and `loadBalancerId`.
     */
    readonly loadBalancerId?: pulumi.Input<number>;
    /**
     * The server the `ipAddress` belongs to. Specify only one of `serverId`, `floatingIpId` and `loadBalancerId`.
     */
    readonly serverId?: pulumi.Input<number>;
}

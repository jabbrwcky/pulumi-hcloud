// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

import * as pulumi from "@pulumi/pulumi";
import { input as inputs, output as outputs } from "../types";

export interface FirewallRule {
    destinationIps?: pulumi.Input<pulumi.Input<string>[]>;
    /**
     * Direction of the Firewall Rule. `in`
     */
    direction: pulumi.Input<string>;
    /**
     * Port of the Firewall Rule. Required when `protocol` is `tcp` or `udp`
     */
    port?: pulumi.Input<string>;
    /**
     * Protocol of the Firewall Rule. `tcp`, `icmp`, `udp`
     */
    protocol: pulumi.Input<string>;
    /**
     * List of CIDRs that are allowed within this Firewall Rule
     */
    sourceIps?: pulumi.Input<pulumi.Input<string>[]>;
}

export interface GetFirewallRule {
    /**
     * (Required, string) Direction of the Firewall Rule. `in`
     */
    direction: string;
    /**
     * (Required, string) Port of the Firewall Rule. Required when `protocol` is `tcp` or `udp`
     */
    port?: string;
    /**
     * (Required, string) Protocol of the Firewall Rule. `tcp`, `icmp`, `udp`
     */
    protocol?: string;
    /**
     * (Required, List) List of CIDRs that are allowed within this Firewall Rule
     */
    sourceIps?: string[];
}

export interface LoadBalancerAlgorithm {
    /**
     * Type of the Load Balancer Algorithm. `roundRobin` or `leastConnections`
     */
    type?: pulumi.Input<string>;
}

export interface LoadBalancerServiceHealthCheck {
    /**
     * List of http configurations. Required if `protocol` is `http`.
     */
    http?: pulumi.Input<inputs.LoadBalancerServiceHealthCheckHttp>;
    /**
     * Interval how often the health check will be performed, in seconds.
     */
    interval: pulumi.Input<number>;
    /**
     * Port the health check tries to connect to, required if protocol is `tcp`. Can be everything between `1` and `65535`. Must be unique per Load Balancer.
     */
    port: pulumi.Input<number>;
    /**
     * Protocol the health check uses. `http` or `tcp`
     */
    protocol: pulumi.Input<string>;
    /**
     * Number of tries a health check will be performed until a target will be listed as `unhealthy`.
     */
    retries?: pulumi.Input<number>;
    /**
     * Timeout when a health check try will be canceled if there is no response, in seconds.
     */
    timeout: pulumi.Input<number>;
}

export interface LoadBalancerServiceHealthCheckHttp {
    /**
     * Domain we try to access when performing the Health Check.
     */
    domain?: pulumi.Input<string>;
    /**
     * Path we try to access when performing the Health Check.
     */
    path?: pulumi.Input<string>;
    /**
     * Response we expect to be included in the Target response when a Health Check was performed.
     */
    response?: pulumi.Input<string>;
    /**
     * We expect that the target answers with these status codes. If not the target is marked as `unhealthy`.
     */
    statusCodes?: pulumi.Input<pulumi.Input<string>[]>;
    /**
     * Enable TLS certificate checking.
     */
    tls?: pulumi.Input<boolean>;
}

export interface LoadBalancerServiceHttp {
    /**
     * List of IDs from certificates which the Load Balancer has.
     */
    certificates?: pulumi.Input<pulumi.Input<number>[]>;
    /**
     * Lifetime of the cookie for sticky session (in seconds). Default: `300`
     */
    cookieLifetime?: pulumi.Input<number>;
    /**
     * Name of the cookie for sticky session. Default: `HCLBSTICKY`
     */
    cookieName?: pulumi.Input<string>;
    /**
     * Redirect HTTP to HTTPS traffic. Only supported for services with `protocol` `https` using the default HTTP port `80`.
     */
    redirectHttp?: pulumi.Input<boolean>;
    /**
     * Enable sticky sessions
     */
    stickySessions?: pulumi.Input<boolean>;
}

export interface LoadBalancerTarget {
    /**
     * ID of the server which should be a target for this Load Balancer. Required if `type` is `server`
     */
    serverId?: pulumi.Input<number>;
    /**
     * Type of the target. `server`
     */
    type: pulumi.Input<string>;
    /**
     * @deprecated Does not work. Use the hcloud_load_balancer_target resource instead.
     */
    usePrivateIp?: pulumi.Input<boolean>;
}

export interface ServerNetwork {
    aliasIps?: pulumi.Input<pulumi.Input<string>[]>;
    ip?: pulumi.Input<string>;
    macAddress?: pulumi.Input<string>;
    networkId: pulumi.Input<number>;
}

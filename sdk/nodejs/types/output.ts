// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

import * as pulumi from "@pulumi/pulumi";
import { input as inputs, output as outputs } from "../types";

export interface GetLoadBalancerAlgorithm {
    /**
     * (string) Type of the target. `server` or `labelSelector`
     */
    type: string;
}

export interface GetLoadBalancerService {
    /**
     * (int) Port the service connects to the targets on. Can be everything between `1` and `65535`.
     */
    destinationPort: number;
    /**
     * (list) List of http configurations when `protocol` is `http` or `https`.
     */
    healthChecks: outputs.GetLoadBalancerServiceHealthCheck[];
    /**
     * (list) List of http configurations when `protocol` is `http` or `https`.
     */
    https: outputs.GetLoadBalancerServiceHttp[];
    /**
     * (int) Port the service listen on`. Can be everything between `1` and `65535`. Must be unique per Load Balancer.
     */
    listenPort: number;
    /**
     * (string) Protocol the health check uses. `http`, `https` or `tcp`
     */
    protocol: string;
    /**
     * (bool) Enable proxyprotocol.
     */
    proxyprotocol: boolean;
}

export interface GetLoadBalancerServiceHealthCheck {
    /**
     * (list) List of http configurations when `protocol` is `http` or `https`.
     */
    https: outputs.GetLoadBalancerServiceHealthCheckHttp[];
    /**
     * (int) Interval how often the health check will be performed, in seconds.
     */
    interval: number;
    /**
     * (int) Port the health check tries to connect to. Can be everything between `1` and `65535`.
     */
    port: number;
    /**
     * (string) Protocol the health check uses. `http`, `https` or `tcp`
     */
    protocol: string;
    /**
     * (int) Number of tries a health check will be performed until a target will be listed as `unhealthy`.
     */
    retries: number;
    /**
     * (int) Timeout when a health check try will be canceled if there is no response, in seconds.
     */
    timeout: number;
}

export interface GetLoadBalancerServiceHealthCheckHttp {
    /**
     * string) Domain we try to access when performing the Health Check.
     */
    domain: string;
    /**
     * (string) Path we try to access when performing the Health Check.
     */
    path: string;
    /**
     * (string) Response we expect to be included in the Target response when a Health Check was performed.
     */
    response: string;
    /**
     * (list[int]) We expect that the target answers with these status codes. If not the target is marked as `unhealthy`.
     */
    statusCodes: number[];
    /**
     * (bool) Enable TLS certificate checking.
     */
    tls: boolean;
}

export interface GetLoadBalancerServiceHttp {
    /**
     * (list[int]) List of IDs from certificates which the Load Balancer has.
     */
    certificates: string[];
    /**
     * (int) Lifetime of the cookie for sticky session (in seconds).
     */
    cookieLifetime: number;
    /**
     * (string) Name of the cookie for sticky session.
     */
    cookieName: string;
    /**
     * (string) Determine if all requests from port 80 should be redirected to port 443.
     */
    redirectHttp: boolean;
    /**
     * (string) Determine if sticky sessions are enabled or not.
     */
    stickySessions: boolean;
}

export interface GetLoadBalancerTarget {
    /**
     * (string) Label Selector to add a group of resources based on the label.
     */
    labelSelector: string;
    /**
     * (int) ID of the server which should be a target for this Load Balancer.
     */
    serverId: number;
    /**
     * (string) Type of the target. `server` or `labelSelector`
     */
    type: string;
}

export interface GetSshKeysSshKey {
    fingerprint: string;
    id: number;
    labels: {[key: string]: any};
    name: string;
    publicKey: string;
}

export interface LoadBalancerAlgorithm {
    /**
     * Type of the Load Balancer Algorithm. `roundRobin` or `leastConnections`
     */
    type: string;
}

export interface LoadBalancerServiceHealthCheck {
    /**
     * List of http configurations. Required if `protocol` is `http`.
     */
    http: outputs.LoadBalancerServiceHealthCheckHttp;
    /**
     * Interval how often the health check will be performed, in seconds.
     */
    interval: number;
    /**
     * Port the health check tries to connect to, required if protocol is `tcp`. Can be everything between `1` and `65535`. Must be unique per Load Balancer.
     */
    port: number;
    /**
     * Protocol the health check uses. `http` or `tcp`
     */
    protocol: string;
    /**
     * Number of tries a health check will be performed until a target will be listed as `unhealthy`.
     */
    retries: number;
    /**
     * Timeout when a health check try will be canceled if there is no response, in seconds.
     */
    timeout: number;
}

export interface LoadBalancerServiceHealthCheckHttp {
    /**
     * Domain we try to access when performing the Health Check.
     */
    domain?: string;
    /**
     * Path we try to access when performing the Health Check.
     */
    path?: string;
    /**
     * Response we expect to be included in the Target response when a Health Check was performed.
     */
    response?: string;
    /**
     * We expect that the target answers with these status codes. If not the target is marked as `unhealthy`.
     */
    statusCodes?: string[];
    /**
     * Enable TLS certificate checking.
     */
    tls?: boolean;
}

export interface LoadBalancerServiceHttp {
    /**
     * List of IDs from certificates which the Load Balancer has.
     */
    certificates?: number[];
    /**
     * Lifetime of the cookie for sticky session (in seconds). Default: `300`
     */
    cookieLifetime: number;
    /**
     * Name of the cookie for sticky session. Default: `HCLBSTICKY`
     */
    cookieName: string;
    /**
     * Redirect HTTP to HTTPS traffic. Only supported for services with `protocol` `https` using the default HTTP port `80`.
     */
    redirectHttp: boolean;
    /**
     * Enable sticky sessions
     */
    stickySessions: boolean;
}

export interface LoadBalancerTarget {
    /**
     * ID of the server which should be a target for this Load Balancer. Required if `type` is `server`
     */
    serverId?: number;
    /**
     * Type of the target. `server`
     */
    type: string;
    /**
     * @deprecated Does not work. Use the hcloud_load_balancer_target resource instead.
     */
    usePrivateIp?: boolean;
}

export interface ServerNetwork {
    aliasIps?: string[];
    ip: string;
    macAddress: string;
    networkId: number;
}

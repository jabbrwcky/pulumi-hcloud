// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

import * as pulumi from "@pulumi/pulumi";
import * as utilities from "./utilities";

// Export members:
export * from "./certificate";
export * from "./firewall";
export * from "./floatingIp";
export * from "./floatingIpAssignment";
export * from "./getCertificate";
export * from "./getDatacenter";
export * from "./getDatacenters";
export * from "./getFirewall";
export * from "./getFloatingIp";
export * from "./getImage";
export * from "./getLoadBalancer";
export * from "./getLocation";
export * from "./getLocations";
export * from "./getNetwork";
export * from "./getServer";
export * from "./getServerType";
export * from "./getServerTypes";
export * from "./getSshKey";
export * from "./getSshKeys";
export * from "./getVolume";
export * from "./loadBalancer";
export * from "./loadBalancerNetwork";
export * from "./loadBalancerService";
export * from "./loadBalancerTarget";
export * from "./managedCertificate";
export * from "./network";
export * from "./networkRoute";
export * from "./networkSubnet";
export * from "./provider";
export * from "./rdns";
export * from "./server";
export * from "./serverNetwork";
export * from "./snapshot";
export * from "./sshKey";
export * from "./uploadedCertificate";
export * from "./volume";
export * from "./volumeAttachment";

// Export sub-modules:
import * as config from "./config";
import * as types from "./types";

export {
    config,
    types,
};

// Import resources to register:
import { Certificate } from "./certificate";
import { Firewall } from "./firewall";
import { FloatingIp } from "./floatingIp";
import { FloatingIpAssignment } from "./floatingIpAssignment";
import { LoadBalancer } from "./loadBalancer";
import { LoadBalancerNetwork } from "./loadBalancerNetwork";
import { LoadBalancerService } from "./loadBalancerService";
import { LoadBalancerTarget } from "./loadBalancerTarget";
import { ManagedCertificate } from "./managedCertificate";
import { Network } from "./network";
import { NetworkRoute } from "./networkRoute";
import { NetworkSubnet } from "./networkSubnet";
import { Rdns } from "./rdns";
import { Server } from "./server";
import { ServerNetwork } from "./serverNetwork";
import { Snapshot } from "./snapshot";
import { SshKey } from "./sshKey";
import { UploadedCertificate } from "./uploadedCertificate";
import { Volume } from "./volume";
import { VolumeAttachment } from "./volumeAttachment";

const _module = {
    version: utilities.getVersion(),
    construct: (name: string, type: string, urn: string): pulumi.Resource => {
        switch (type) {
            case "hcloud:index/certificate:Certificate":
                return new Certificate(name, <any>undefined, { urn })
            case "hcloud:index/firewall:Firewall":
                return new Firewall(name, <any>undefined, { urn })
            case "hcloud:index/floatingIp:FloatingIp":
                return new FloatingIp(name, <any>undefined, { urn })
            case "hcloud:index/floatingIpAssignment:FloatingIpAssignment":
                return new FloatingIpAssignment(name, <any>undefined, { urn })
            case "hcloud:index/loadBalancer:LoadBalancer":
                return new LoadBalancer(name, <any>undefined, { urn })
            case "hcloud:index/loadBalancerNetwork:LoadBalancerNetwork":
                return new LoadBalancerNetwork(name, <any>undefined, { urn })
            case "hcloud:index/loadBalancerService:LoadBalancerService":
                return new LoadBalancerService(name, <any>undefined, { urn })
            case "hcloud:index/loadBalancerTarget:LoadBalancerTarget":
                return new LoadBalancerTarget(name, <any>undefined, { urn })
            case "hcloud:index/managedCertificate:ManagedCertificate":
                return new ManagedCertificate(name, <any>undefined, { urn })
            case "hcloud:index/network:Network":
                return new Network(name, <any>undefined, { urn })
            case "hcloud:index/networkRoute:NetworkRoute":
                return new NetworkRoute(name, <any>undefined, { urn })
            case "hcloud:index/networkSubnet:NetworkSubnet":
                return new NetworkSubnet(name, <any>undefined, { urn })
            case "hcloud:index/rdns:Rdns":
                return new Rdns(name, <any>undefined, { urn })
            case "hcloud:index/server:Server":
                return new Server(name, <any>undefined, { urn })
            case "hcloud:index/serverNetwork:ServerNetwork":
                return new ServerNetwork(name, <any>undefined, { urn })
            case "hcloud:index/snapshot:Snapshot":
                return new Snapshot(name, <any>undefined, { urn })
            case "hcloud:index/sshKey:SshKey":
                return new SshKey(name, <any>undefined, { urn })
            case "hcloud:index/uploadedCertificate:UploadedCertificate":
                return new UploadedCertificate(name, <any>undefined, { urn })
            case "hcloud:index/volume:Volume":
                return new Volume(name, <any>undefined, { urn })
            case "hcloud:index/volumeAttachment:VolumeAttachment":
                return new VolumeAttachment(name, <any>undefined, { urn })
            default:
                throw new Error(`unknown resource type ${type}`);
        }
    },
};
pulumi.runtime.registerResourceModule("hcloud", "index/certificate", _module)
pulumi.runtime.registerResourceModule("hcloud", "index/firewall", _module)
pulumi.runtime.registerResourceModule("hcloud", "index/floatingIp", _module)
pulumi.runtime.registerResourceModule("hcloud", "index/floatingIpAssignment", _module)
pulumi.runtime.registerResourceModule("hcloud", "index/loadBalancer", _module)
pulumi.runtime.registerResourceModule("hcloud", "index/loadBalancerNetwork", _module)
pulumi.runtime.registerResourceModule("hcloud", "index/loadBalancerService", _module)
pulumi.runtime.registerResourceModule("hcloud", "index/loadBalancerTarget", _module)
pulumi.runtime.registerResourceModule("hcloud", "index/managedCertificate", _module)
pulumi.runtime.registerResourceModule("hcloud", "index/network", _module)
pulumi.runtime.registerResourceModule("hcloud", "index/networkRoute", _module)
pulumi.runtime.registerResourceModule("hcloud", "index/networkSubnet", _module)
pulumi.runtime.registerResourceModule("hcloud", "index/rdns", _module)
pulumi.runtime.registerResourceModule("hcloud", "index/server", _module)
pulumi.runtime.registerResourceModule("hcloud", "index/serverNetwork", _module)
pulumi.runtime.registerResourceModule("hcloud", "index/snapshot", _module)
pulumi.runtime.registerResourceModule("hcloud", "index/sshKey", _module)
pulumi.runtime.registerResourceModule("hcloud", "index/uploadedCertificate", _module)
pulumi.runtime.registerResourceModule("hcloud", "index/volume", _module)
pulumi.runtime.registerResourceModule("hcloud", "index/volumeAttachment", _module)

import { Provider } from "./provider";

pulumi.runtime.registerResourcePackage("hcloud", {
    version: utilities.getVersion(),
    constructProvider: (name: string, type: string, urn: string): pulumi.ProviderResource => {
        if (type !== "pulumi:providers:hcloud") {
            throw new Error(`unknown provider type ${type}`);
        }
        return new Provider(name, <any>undefined, { urn });
    },
});

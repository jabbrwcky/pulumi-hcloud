// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

import * as pulumi from "@pulumi/pulumi";
import * as utilities from "../utilities";

let __config = new pulumi.Config("hcloud");

export let endpoint: string | undefined = __config.get("endpoint");
export let pollInterval: string | undefined = __config.get("pollInterval");
/**
 * The API token to access the Hetzner cloud.
 */
export let token: string | undefined = __config.get("token");

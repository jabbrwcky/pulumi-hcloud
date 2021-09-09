// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

package hcloud

import (
	"github.com/pulumi/pulumi/sdk/v3/go/pulumi"
)

// Provides details about multiple Hetzner Cloud Firewall.
//
// ## Example Usage
//
// ```go
// package main
//
// import (
// 	"github.com/pulumi/pulumi-hcloud/sdk/go/hcloud"
// 	"github.com/pulumi/pulumi/sdk/v3/go/pulumi"
// )
//
// func main() {
// 	pulumi.Run(func(ctx *pulumi.Context) error {
// 		opt0 := "key=value"
// 		_, err := hcloud.GetFirewalls(ctx, &hcloud.GetFirewallsArgs{
// 			WithSelector: &opt0,
// 		}, nil)
// 		if err != nil {
// 			return err
// 		}
// 		return nil
// 	})
// }
// ```
func GetFirewalls(ctx *pulumi.Context, args *GetFirewallsArgs, opts ...pulumi.InvokeOption) (*GetFirewallsResult, error) {
	var rv GetFirewallsResult
	err := ctx.Invoke("hcloud:index/getFirewalls:getFirewalls", args, &rv, opts...)
	if err != nil {
		return nil, err
	}
	return &rv, nil
}

// A collection of arguments for invoking getFirewalls.
type GetFirewallsArgs struct {
	// Sorts list by date.
	MostRecent *bool `pulumi:"mostRecent"`
	// [Label selector](https://docs.hetzner.cloud/#overview-label-selector)
	WithSelector *string `pulumi:"withSelector"`
}

// A collection of values returned by getFirewalls.
type GetFirewallsResult struct {
	// (list) List of all matching firewalls. See `data.hcloud_firewall` for schema.
	Firewalls []GetFirewallsFirewall `pulumi:"firewalls"`
	// The provider-assigned unique ID for this managed resource.
	Id           string  `pulumi:"id"`
	MostRecent   *bool   `pulumi:"mostRecent"`
	WithSelector *string `pulumi:"withSelector"`
}

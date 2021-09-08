// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

package hcloud

import (
	"github.com/pulumi/pulumi/sdk/v3/go/pulumi"
)

// Provides details about a specific Hetzner Cloud Firewall.
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
// 		opt0 := "sample-firewall-1"
// 		_, err := hcloud.LookupFirewall(ctx, &hcloud.LookupFirewallArgs{
// 			Name: &opt0,
// 		}, nil)
// 		if err != nil {
// 			return err
// 		}
// 		opt1 := 4711
// 		_, err = hcloud.LookupFirewall(ctx, &hcloud.LookupFirewallArgs{
// 			Id: &opt1,
// 		}, nil)
// 		if err != nil {
// 			return err
// 		}
// 		return nil
// 	})
// }
// ```
func LookupFirewall(ctx *pulumi.Context, args *LookupFirewallArgs, opts ...pulumi.InvokeOption) (*LookupFirewallResult, error) {
	var rv LookupFirewallResult
	err := ctx.Invoke("hcloud:index/getFirewall:getFirewall", args, &rv, opts...)
	if err != nil {
		return nil, err
	}
	return &rv, nil
}

// A collection of arguments for invoking getFirewall.
type LookupFirewallArgs struct {
	// Configuration of the Applied Resources
	ApplyTos []GetFirewallApplyTo `pulumi:"applyTos"`
	// ID of the firewall.
	Id *int `pulumi:"id"`
	// (map) User-defined labels (key-value pairs)
	Labels map[string]interface{} `pulumi:"labels"`
	// Return most recent firewall if multiple are found.
	MostRecent *bool `pulumi:"mostRecent"`
	// Name of the firewall.
	Name *string `pulumi:"name"`
	// (string)  Configuration of a Rule from this Firewall.
	Rules []GetFirewallRule `pulumi:"rules"`
	// [Label selector](https://docs.hetzner.cloud/#overview-label-selector)
	WithSelector *string `pulumi:"withSelector"`
}

// A collection of values returned by getFirewall.
type LookupFirewallResult struct {
	// Configuration of the Applied Resources
	ApplyTos []GetFirewallApplyTo `pulumi:"applyTos"`
	// (int) Unique ID of the Firewall.
	Id *int `pulumi:"id"`
	// (map) User-defined labels (key-value pairs)
	Labels     map[string]interface{} `pulumi:"labels"`
	MostRecent *bool                  `pulumi:"mostRecent"`
	// (string) Name of the Firewall.
	Name string `pulumi:"name"`
	// (string)  Configuration of a Rule from this Firewall.
	Rules        []GetFirewallRule `pulumi:"rules"`
	WithSelector *string           `pulumi:"withSelector"`
}

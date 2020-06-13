// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

package hcloud

import (
	"github.com/pulumi/pulumi/sdk/v2/go/pulumi"
)

// Provides details about a specific Hetzner Cloud Location.
// Use this resource to get detailed information about specific location.
func GetLocation(ctx *pulumi.Context, args *GetLocationArgs, opts ...pulumi.InvokeOption) (*GetLocationResult, error) {
	var rv GetLocationResult
	err := ctx.Invoke("hcloud:index/getLocation:getLocation", args, &rv, opts...)
	if err != nil {
		return nil, err
	}
	return &rv, nil
}

// A collection of arguments for invoking getLocation.
type GetLocationArgs struct {
	Id   *int    `pulumi:"id"`
	Name *string `pulumi:"name"`
}

// A collection of values returned by getLocation.
type GetLocationResult struct {
	City        string  `pulumi:"city"`
	Country     string  `pulumi:"country"`
	Description string  `pulumi:"description"`
	Id          int     `pulumi:"id"`
	Latitude    float64 `pulumi:"latitude"`
	Longitude   float64 `pulumi:"longitude"`
	Name        string  `pulumi:"name"`
}

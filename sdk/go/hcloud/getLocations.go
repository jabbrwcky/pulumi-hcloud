// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

package hcloud

import (
	"github.com/pulumi/pulumi/sdk/v3/go/pulumi"
)

// Provides a list of available Hetzner Cloud Locations.
// This resource may be useful to create highly available infrastructure, distributed across several locations.
func GetLocations(ctx *pulumi.Context, args *GetLocationsArgs, opts ...pulumi.InvokeOption) (*GetLocationsResult, error) {
	var rv GetLocationsResult
	err := ctx.Invoke("hcloud:index/getLocations:getLocations", args, &rv, opts...)
	if err != nil {
		return nil, err
	}
	return &rv, nil
}

// A collection of arguments for invoking getLocations.
type GetLocationsArgs struct {
	// (list) List of unique location identifiers.
	//
	// Deprecated: Use locations list instead
	LocationIds []string `pulumi:"locationIds"`
}

// A collection of values returned by getLocations.
type GetLocationsResult struct {
	// (list) List of all location descriptions.
	//
	// Deprecated: Use locations list instead
	Descriptions []string `pulumi:"descriptions"`
	// The provider-assigned unique ID for this managed resource.
	Id string `pulumi:"id"`
	// (list) List of unique location identifiers.
	//
	// Deprecated: Use locations list instead
	LocationIds []string `pulumi:"locationIds"`
	// (list) List of all locations. See `data.hcloud_location` for schema.
	Locations []GetLocationsLocation `pulumi:"locations"`
	// (list) List of location names.
	//
	// Deprecated: Use locations list instead
	Names []string `pulumi:"names"`
}

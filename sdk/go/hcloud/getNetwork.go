// Code generated by the Pulumi Terraform Bridge (tfgen) Tool DO NOT EDIT.
// *** WARNING: Do not edit by hand unless you're certain you know what you are doing! ***

package hcloud

import (
	"context"
	"reflect"

	"github.com/pulumi/pulumi/sdk/v3/go/pulumi"
)

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
// 		_, err := hcloud.LookupNetwork(ctx, &GetNetworkArgs{
// 			Id: pulumi.IntRef(1234),
// 		}, nil)
// 		if err != nil {
// 			return err
// 		}
// 		_, err = hcloud.LookupNetwork(ctx, &GetNetworkArgs{
// 			Name: pulumi.StringRef("my-network"),
// 		}, nil)
// 		if err != nil {
// 			return err
// 		}
// 		_, err = hcloud.LookupNetwork(ctx, &GetNetworkArgs{
// 			WithSelector: pulumi.StringRef("key=value"),
// 		}, nil)
// 		if err != nil {
// 			return err
// 		}
// 		return nil
// 	})
// }
// ```
func LookupNetwork(ctx *pulumi.Context, args *LookupNetworkArgs, opts ...pulumi.InvokeOption) (*LookupNetworkResult, error) {
	var rv LookupNetworkResult
	err := ctx.Invoke("hcloud:index/getNetwork:getNetwork", args, &rv, opts...)
	if err != nil {
		return nil, err
	}
	return &rv, nil
}

// A collection of arguments for invoking getNetwork.
type LookupNetworkArgs struct {
	// ID of the Network.
	Id *int `pulumi:"id"`
	// IPv4 prefix of the Network.
	IpRange    *string                `pulumi:"ipRange"`
	Labels     map[string]interface{} `pulumi:"labels"`
	MostRecent *bool                  `pulumi:"mostRecent"`
	// Name of the Network.
	Name *string `pulumi:"name"`
	// Label Selector. For more information about possible values, visit the [Hetzner Cloud Documentation](https://docs.hetzner.cloud/#overview-label-selector).
	WithSelector *string `pulumi:"withSelector"`
}

// A collection of values returned by getNetwork.
type LookupNetworkResult struct {
	// (boolean) Whether delete protection is enabled.
	DeleteProtection bool `pulumi:"deleteProtection"`
	// Unique ID of the Network.
	Id int `pulumi:"id"`
	// IPv4 prefix of the Network.
	IpRange    *string                `pulumi:"ipRange"`
	Labels     map[string]interface{} `pulumi:"labels"`
	MostRecent *bool                  `pulumi:"mostRecent"`
	// Name of the Network.
	Name         *string `pulumi:"name"`
	WithSelector *string `pulumi:"withSelector"`
}

func LookupNetworkOutput(ctx *pulumi.Context, args LookupNetworkOutputArgs, opts ...pulumi.InvokeOption) LookupNetworkResultOutput {
	return pulumi.ToOutputWithContext(context.Background(), args).
		ApplyT(func(v interface{}) (LookupNetworkResult, error) {
			args := v.(LookupNetworkArgs)
			r, err := LookupNetwork(ctx, &args, opts...)
			var s LookupNetworkResult
			if r != nil {
				s = *r
			}
			return s, err
		}).(LookupNetworkResultOutput)
}

// A collection of arguments for invoking getNetwork.
type LookupNetworkOutputArgs struct {
	// ID of the Network.
	Id pulumi.IntPtrInput `pulumi:"id"`
	// IPv4 prefix of the Network.
	IpRange    pulumi.StringPtrInput `pulumi:"ipRange"`
	Labels     pulumi.MapInput       `pulumi:"labels"`
	MostRecent pulumi.BoolPtrInput   `pulumi:"mostRecent"`
	// Name of the Network.
	Name pulumi.StringPtrInput `pulumi:"name"`
	// Label Selector. For more information about possible values, visit the [Hetzner Cloud Documentation](https://docs.hetzner.cloud/#overview-label-selector).
	WithSelector pulumi.StringPtrInput `pulumi:"withSelector"`
}

func (LookupNetworkOutputArgs) ElementType() reflect.Type {
	return reflect.TypeOf((*LookupNetworkArgs)(nil)).Elem()
}

// A collection of values returned by getNetwork.
type LookupNetworkResultOutput struct{ *pulumi.OutputState }

func (LookupNetworkResultOutput) ElementType() reflect.Type {
	return reflect.TypeOf((*LookupNetworkResult)(nil)).Elem()
}

func (o LookupNetworkResultOutput) ToLookupNetworkResultOutput() LookupNetworkResultOutput {
	return o
}

func (o LookupNetworkResultOutput) ToLookupNetworkResultOutputWithContext(ctx context.Context) LookupNetworkResultOutput {
	return o
}

// (boolean) Whether delete protection is enabled.
func (o LookupNetworkResultOutput) DeleteProtection() pulumi.BoolOutput {
	return o.ApplyT(func(v LookupNetworkResult) bool { return v.DeleteProtection }).(pulumi.BoolOutput)
}

// Unique ID of the Network.
func (o LookupNetworkResultOutput) Id() pulumi.IntOutput {
	return o.ApplyT(func(v LookupNetworkResult) int { return v.Id }).(pulumi.IntOutput)
}

// IPv4 prefix of the Network.
func (o LookupNetworkResultOutput) IpRange() pulumi.StringPtrOutput {
	return o.ApplyT(func(v LookupNetworkResult) *string { return v.IpRange }).(pulumi.StringPtrOutput)
}

func (o LookupNetworkResultOutput) Labels() pulumi.MapOutput {
	return o.ApplyT(func(v LookupNetworkResult) map[string]interface{} { return v.Labels }).(pulumi.MapOutput)
}

func (o LookupNetworkResultOutput) MostRecent() pulumi.BoolPtrOutput {
	return o.ApplyT(func(v LookupNetworkResult) *bool { return v.MostRecent }).(pulumi.BoolPtrOutput)
}

// Name of the Network.
func (o LookupNetworkResultOutput) Name() pulumi.StringPtrOutput {
	return o.ApplyT(func(v LookupNetworkResult) *string { return v.Name }).(pulumi.StringPtrOutput)
}

func (o LookupNetworkResultOutput) WithSelector() pulumi.StringPtrOutput {
	return o.ApplyT(func(v LookupNetworkResult) *string { return v.WithSelector }).(pulumi.StringPtrOutput)
}

func init() {
	pulumi.RegisterOutputType(LookupNetworkResultOutput{})
}

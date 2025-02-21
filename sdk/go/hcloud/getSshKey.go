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
// 		sshKey1, err := hcloud.LookupSshKey(ctx, &GetSshKeyArgs{
// 			Id: pulumi.IntRef(1234),
// 		}, nil)
// 		if err != nil {
// 			return err
// 		}
// 		sshKey2, err := hcloud.LookupSshKey(ctx, &GetSshKeyArgs{
// 			Name: pulumi.StringRef("my-ssh-key"),
// 		}, nil)
// 		if err != nil {
// 			return err
// 		}
// 		sshKey3, err := hcloud.LookupSshKey(ctx, &GetSshKeyArgs{
// 			Fingerprint: pulumi.StringRef("43:51:43:a1:b5:fc:8b:b7:0a:3a:a9:b1:0f:66:73:a8"),
// 		}, nil)
// 		if err != nil {
// 			return err
// 		}
// 		_, err = hcloud.LookupSshKey(ctx, &GetSshKeyArgs{
// 			WithSelector: pulumi.StringRef("key=value"),
// 		}, nil)
// 		if err != nil {
// 			return err
// 		}
// 		_, err = hcloud.NewServer(ctx, "main", &hcloud.ServerArgs{
// 			SshKeys: pulumi.StringArray{
// 				pulumi.Int(sshKey1.Id),
// 				pulumi.Int(sshKey2.Id),
// 				pulumi.Int(sshKey3.Id),
// 			},
// 		})
// 		if err != nil {
// 			return err
// 		}
// 		return nil
// 	})
// }
// ```
func LookupSshKey(ctx *pulumi.Context, args *LookupSshKeyArgs, opts ...pulumi.InvokeOption) (*LookupSshKeyResult, error) {
	var rv LookupSshKeyResult
	err := ctx.Invoke("hcloud:index/getSshKey:getSshKey", args, &rv, opts...)
	if err != nil {
		return nil, err
	}
	return &rv, nil
}

// A collection of arguments for invoking getSshKey.
type LookupSshKeyArgs struct {
	// Fingerprint of the SSH Key.
	Fingerprint *string `pulumi:"fingerprint"`
	// ID of the SSH Key.
	Id *int `pulumi:"id"`
	// Name of the SSH Key.
	Name *string `pulumi:"name"`
	// Deprecated: Please use the with_selector property instead.
	Selector *string `pulumi:"selector"`
	// [Label selector](https://docs.hetzner.cloud/#overview-label-selector)
	WithSelector *string `pulumi:"withSelector"`
}

// A collection of values returned by getSshKey.
type LookupSshKeyResult struct {
	// (string) Fingerprint of the SSH Key.
	Fingerprint string `pulumi:"fingerprint"`
	// (int) Unique ID of the SSH Key.
	Id     int                    `pulumi:"id"`
	Labels map[string]interface{} `pulumi:"labels"`
	// (string) Name of the SSH Key.
	Name string `pulumi:"name"`
	// (string) Public Key of the SSH Key.
	PublicKey string `pulumi:"publicKey"`
	// Deprecated: Please use the with_selector property instead.
	Selector     *string `pulumi:"selector"`
	WithSelector *string `pulumi:"withSelector"`
}

func LookupSshKeyOutput(ctx *pulumi.Context, args LookupSshKeyOutputArgs, opts ...pulumi.InvokeOption) LookupSshKeyResultOutput {
	return pulumi.ToOutputWithContext(context.Background(), args).
		ApplyT(func(v interface{}) (LookupSshKeyResult, error) {
			args := v.(LookupSshKeyArgs)
			r, err := LookupSshKey(ctx, &args, opts...)
			var s LookupSshKeyResult
			if r != nil {
				s = *r
			}
			return s, err
		}).(LookupSshKeyResultOutput)
}

// A collection of arguments for invoking getSshKey.
type LookupSshKeyOutputArgs struct {
	// Fingerprint of the SSH Key.
	Fingerprint pulumi.StringPtrInput `pulumi:"fingerprint"`
	// ID of the SSH Key.
	Id pulumi.IntPtrInput `pulumi:"id"`
	// Name of the SSH Key.
	Name pulumi.StringPtrInput `pulumi:"name"`
	// Deprecated: Please use the with_selector property instead.
	Selector pulumi.StringPtrInput `pulumi:"selector"`
	// [Label selector](https://docs.hetzner.cloud/#overview-label-selector)
	WithSelector pulumi.StringPtrInput `pulumi:"withSelector"`
}

func (LookupSshKeyOutputArgs) ElementType() reflect.Type {
	return reflect.TypeOf((*LookupSshKeyArgs)(nil)).Elem()
}

// A collection of values returned by getSshKey.
type LookupSshKeyResultOutput struct{ *pulumi.OutputState }

func (LookupSshKeyResultOutput) ElementType() reflect.Type {
	return reflect.TypeOf((*LookupSshKeyResult)(nil)).Elem()
}

func (o LookupSshKeyResultOutput) ToLookupSshKeyResultOutput() LookupSshKeyResultOutput {
	return o
}

func (o LookupSshKeyResultOutput) ToLookupSshKeyResultOutputWithContext(ctx context.Context) LookupSshKeyResultOutput {
	return o
}

// (string) Fingerprint of the SSH Key.
func (o LookupSshKeyResultOutput) Fingerprint() pulumi.StringOutput {
	return o.ApplyT(func(v LookupSshKeyResult) string { return v.Fingerprint }).(pulumi.StringOutput)
}

// (int) Unique ID of the SSH Key.
func (o LookupSshKeyResultOutput) Id() pulumi.IntOutput {
	return o.ApplyT(func(v LookupSshKeyResult) int { return v.Id }).(pulumi.IntOutput)
}

func (o LookupSshKeyResultOutput) Labels() pulumi.MapOutput {
	return o.ApplyT(func(v LookupSshKeyResult) map[string]interface{} { return v.Labels }).(pulumi.MapOutput)
}

// (string) Name of the SSH Key.
func (o LookupSshKeyResultOutput) Name() pulumi.StringOutput {
	return o.ApplyT(func(v LookupSshKeyResult) string { return v.Name }).(pulumi.StringOutput)
}

// (string) Public Key of the SSH Key.
func (o LookupSshKeyResultOutput) PublicKey() pulumi.StringOutput {
	return o.ApplyT(func(v LookupSshKeyResult) string { return v.PublicKey }).(pulumi.StringOutput)
}

// Deprecated: Please use the with_selector property instead.
func (o LookupSshKeyResultOutput) Selector() pulumi.StringPtrOutput {
	return o.ApplyT(func(v LookupSshKeyResult) *string { return v.Selector }).(pulumi.StringPtrOutput)
}

func (o LookupSshKeyResultOutput) WithSelector() pulumi.StringPtrOutput {
	return o.ApplyT(func(v LookupSshKeyResult) *string { return v.WithSelector }).(pulumi.StringPtrOutput)
}

func init() {
	pulumi.RegisterOutputType(LookupSshKeyResultOutput{})
}

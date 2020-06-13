// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

package hcloud

import (
	"context"
	"reflect"

	"github.com/pulumi/pulumi/sdk/v2/go/pulumi"
)

type GetSshKeysSshKey struct {
	Fingerprint string                 `pulumi:"fingerprint"`
	Id          int                    `pulumi:"id"`
	Labels      map[string]interface{} `pulumi:"labels"`
	Name        string                 `pulumi:"name"`
	PublicKey   string                 `pulumi:"publicKey"`
}

// GetSshKeysSshKeyInput is an input type that accepts GetSshKeysSshKeyArgs and GetSshKeysSshKeyOutput values.
// You can construct a concrete instance of `GetSshKeysSshKeyInput` via:
//
// 		 GetSshKeysSshKeyArgs{...}
//
type GetSshKeysSshKeyInput interface {
	pulumi.Input

	ToGetSshKeysSshKeyOutput() GetSshKeysSshKeyOutput
	ToGetSshKeysSshKeyOutputWithContext(context.Context) GetSshKeysSshKeyOutput
}

type GetSshKeysSshKeyArgs struct {
	Fingerprint pulumi.StringInput `pulumi:"fingerprint"`
	Id          pulumi.IntInput    `pulumi:"id"`
	Labels      pulumi.MapInput    `pulumi:"labels"`
	Name        pulumi.StringInput `pulumi:"name"`
	PublicKey   pulumi.StringInput `pulumi:"publicKey"`
}

func (GetSshKeysSshKeyArgs) ElementType() reflect.Type {
	return reflect.TypeOf((*GetSshKeysSshKey)(nil)).Elem()
}

func (i GetSshKeysSshKeyArgs) ToGetSshKeysSshKeyOutput() GetSshKeysSshKeyOutput {
	return i.ToGetSshKeysSshKeyOutputWithContext(context.Background())
}

func (i GetSshKeysSshKeyArgs) ToGetSshKeysSshKeyOutputWithContext(ctx context.Context) GetSshKeysSshKeyOutput {
	return pulumi.ToOutputWithContext(ctx, i).(GetSshKeysSshKeyOutput)
}

// GetSshKeysSshKeyArrayInput is an input type that accepts GetSshKeysSshKeyArray and GetSshKeysSshKeyArrayOutput values.
// You can construct a concrete instance of `GetSshKeysSshKeyArrayInput` via:
//
// 		 GetSshKeysSshKeyArray{ GetSshKeysSshKeyArgs{...} }
//
type GetSshKeysSshKeyArrayInput interface {
	pulumi.Input

	ToGetSshKeysSshKeyArrayOutput() GetSshKeysSshKeyArrayOutput
	ToGetSshKeysSshKeyArrayOutputWithContext(context.Context) GetSshKeysSshKeyArrayOutput
}

type GetSshKeysSshKeyArray []GetSshKeysSshKeyInput

func (GetSshKeysSshKeyArray) ElementType() reflect.Type {
	return reflect.TypeOf((*[]GetSshKeysSshKey)(nil)).Elem()
}

func (i GetSshKeysSshKeyArray) ToGetSshKeysSshKeyArrayOutput() GetSshKeysSshKeyArrayOutput {
	return i.ToGetSshKeysSshKeyArrayOutputWithContext(context.Background())
}

func (i GetSshKeysSshKeyArray) ToGetSshKeysSshKeyArrayOutputWithContext(ctx context.Context) GetSshKeysSshKeyArrayOutput {
	return pulumi.ToOutputWithContext(ctx, i).(GetSshKeysSshKeyArrayOutput)
}

type GetSshKeysSshKeyOutput struct{ *pulumi.OutputState }

func (GetSshKeysSshKeyOutput) ElementType() reflect.Type {
	return reflect.TypeOf((*GetSshKeysSshKey)(nil)).Elem()
}

func (o GetSshKeysSshKeyOutput) ToGetSshKeysSshKeyOutput() GetSshKeysSshKeyOutput {
	return o
}

func (o GetSshKeysSshKeyOutput) ToGetSshKeysSshKeyOutputWithContext(ctx context.Context) GetSshKeysSshKeyOutput {
	return o
}

func (o GetSshKeysSshKeyOutput) Fingerprint() pulumi.StringOutput {
	return o.ApplyT(func(v GetSshKeysSshKey) string { return v.Fingerprint }).(pulumi.StringOutput)
}

func (o GetSshKeysSshKeyOutput) Id() pulumi.IntOutput {
	return o.ApplyT(func(v GetSshKeysSshKey) int { return v.Id }).(pulumi.IntOutput)
}

func (o GetSshKeysSshKeyOutput) Labels() pulumi.MapOutput {
	return o.ApplyT(func(v GetSshKeysSshKey) map[string]interface{} { return v.Labels }).(pulumi.MapOutput)
}

func (o GetSshKeysSshKeyOutput) Name() pulumi.StringOutput {
	return o.ApplyT(func(v GetSshKeysSshKey) string { return v.Name }).(pulumi.StringOutput)
}

func (o GetSshKeysSshKeyOutput) PublicKey() pulumi.StringOutput {
	return o.ApplyT(func(v GetSshKeysSshKey) string { return v.PublicKey }).(pulumi.StringOutput)
}

type GetSshKeysSshKeyArrayOutput struct{ *pulumi.OutputState }

func (GetSshKeysSshKeyArrayOutput) ElementType() reflect.Type {
	return reflect.TypeOf((*[]GetSshKeysSshKey)(nil)).Elem()
}

func (o GetSshKeysSshKeyArrayOutput) ToGetSshKeysSshKeyArrayOutput() GetSshKeysSshKeyArrayOutput {
	return o
}

func (o GetSshKeysSshKeyArrayOutput) ToGetSshKeysSshKeyArrayOutputWithContext(ctx context.Context) GetSshKeysSshKeyArrayOutput {
	return o
}

func (o GetSshKeysSshKeyArrayOutput) Index(i pulumi.IntInput) GetSshKeysSshKeyOutput {
	return pulumi.All(o, i).ApplyT(func(vs []interface{}) GetSshKeysSshKey {
		return vs[0].([]GetSshKeysSshKey)[vs[1].(int)]
	}).(GetSshKeysSshKeyOutput)
}

func init() {
	pulumi.RegisterOutputType(GetSshKeysSshKeyOutput{})
	pulumi.RegisterOutputType(GetSshKeysSshKeyArrayOutput{})
}

// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

package hcloud

import (
	"context"
	"reflect"

	"github.com/pkg/errors"
	"github.com/pulumi/pulumi/sdk/v3/go/pulumi"
)

// Alias for `UploadedCertificate` to remain backwards compatible.
// Deprecated.
type Certificate struct {
	pulumi.CustomResourceState

	Certificate    pulumi.StringOutput      `pulumi:"certificate"`
	Created        pulumi.StringOutput      `pulumi:"created"`
	DomainNames    pulumi.StringArrayOutput `pulumi:"domainNames"`
	Fingerprint    pulumi.StringOutput      `pulumi:"fingerprint"`
	Labels         pulumi.MapOutput         `pulumi:"labels"`
	Name           pulumi.StringOutput      `pulumi:"name"`
	NotValidAfter  pulumi.StringOutput      `pulumi:"notValidAfter"`
	NotValidBefore pulumi.StringOutput      `pulumi:"notValidBefore"`
	PrivateKey     pulumi.StringOutput      `pulumi:"privateKey"`
	Type           pulumi.StringOutput      `pulumi:"type"`
}

// NewCertificate registers a new resource with the given unique name, arguments, and options.
func NewCertificate(ctx *pulumi.Context,
	name string, args *CertificateArgs, opts ...pulumi.ResourceOption) (*Certificate, error) {
	if args == nil {
		return nil, errors.New("missing one or more required arguments")
	}

	if args.Certificate == nil {
		return nil, errors.New("invalid value for required argument 'Certificate'")
	}
	if args.PrivateKey == nil {
		return nil, errors.New("invalid value for required argument 'PrivateKey'")
	}
	var resource Certificate
	err := ctx.RegisterResource("hcloud:index/certificate:Certificate", name, args, &resource, opts...)
	if err != nil {
		return nil, err
	}
	return &resource, nil
}

// GetCertificate gets an existing Certificate resource's state with the given name, ID, and optional
// state properties that are used to uniquely qualify the lookup (nil if not required).
func GetCertificate(ctx *pulumi.Context,
	name string, id pulumi.IDInput, state *CertificateState, opts ...pulumi.ResourceOption) (*Certificate, error) {
	var resource Certificate
	err := ctx.ReadResource("hcloud:index/certificate:Certificate", name, id, state, &resource, opts...)
	if err != nil {
		return nil, err
	}
	return &resource, nil
}

// Input properties used for looking up and filtering Certificate resources.
type certificateState struct {
	Certificate    *string                `pulumi:"certificate"`
	Created        *string                `pulumi:"created"`
	DomainNames    []string               `pulumi:"domainNames"`
	Fingerprint    *string                `pulumi:"fingerprint"`
	Labels         map[string]interface{} `pulumi:"labels"`
	Name           *string                `pulumi:"name"`
	NotValidAfter  *string                `pulumi:"notValidAfter"`
	NotValidBefore *string                `pulumi:"notValidBefore"`
	PrivateKey     *string                `pulumi:"privateKey"`
	Type           *string                `pulumi:"type"`
}

type CertificateState struct {
	Certificate    pulumi.StringPtrInput
	Created        pulumi.StringPtrInput
	DomainNames    pulumi.StringArrayInput
	Fingerprint    pulumi.StringPtrInput
	Labels         pulumi.MapInput
	Name           pulumi.StringPtrInput
	NotValidAfter  pulumi.StringPtrInput
	NotValidBefore pulumi.StringPtrInput
	PrivateKey     pulumi.StringPtrInput
	Type           pulumi.StringPtrInput
}

func (CertificateState) ElementType() reflect.Type {
	return reflect.TypeOf((*certificateState)(nil)).Elem()
}

type certificateArgs struct {
	Certificate string                 `pulumi:"certificate"`
	Labels      map[string]interface{} `pulumi:"labels"`
	Name        *string                `pulumi:"name"`
	PrivateKey  string                 `pulumi:"privateKey"`
}

// The set of arguments for constructing a Certificate resource.
type CertificateArgs struct {
	Certificate pulumi.StringInput
	Labels      pulumi.MapInput
	Name        pulumi.StringPtrInput
	PrivateKey  pulumi.StringInput
}

func (CertificateArgs) ElementType() reflect.Type {
	return reflect.TypeOf((*certificateArgs)(nil)).Elem()
}

type CertificateInput interface {
	pulumi.Input

	ToCertificateOutput() CertificateOutput
	ToCertificateOutputWithContext(ctx context.Context) CertificateOutput
}

func (*Certificate) ElementType() reflect.Type {
	return reflect.TypeOf((*Certificate)(nil))
}

func (i *Certificate) ToCertificateOutput() CertificateOutput {
	return i.ToCertificateOutputWithContext(context.Background())
}

func (i *Certificate) ToCertificateOutputWithContext(ctx context.Context) CertificateOutput {
	return pulumi.ToOutputWithContext(ctx, i).(CertificateOutput)
}

func (i *Certificate) ToCertificatePtrOutput() CertificatePtrOutput {
	return i.ToCertificatePtrOutputWithContext(context.Background())
}

func (i *Certificate) ToCertificatePtrOutputWithContext(ctx context.Context) CertificatePtrOutput {
	return pulumi.ToOutputWithContext(ctx, i).(CertificatePtrOutput)
}

type CertificatePtrInput interface {
	pulumi.Input

	ToCertificatePtrOutput() CertificatePtrOutput
	ToCertificatePtrOutputWithContext(ctx context.Context) CertificatePtrOutput
}

type certificatePtrType CertificateArgs

func (*certificatePtrType) ElementType() reflect.Type {
	return reflect.TypeOf((**Certificate)(nil))
}

func (i *certificatePtrType) ToCertificatePtrOutput() CertificatePtrOutput {
	return i.ToCertificatePtrOutputWithContext(context.Background())
}

func (i *certificatePtrType) ToCertificatePtrOutputWithContext(ctx context.Context) CertificatePtrOutput {
	return pulumi.ToOutputWithContext(ctx, i).(CertificatePtrOutput)
}

// CertificateArrayInput is an input type that accepts CertificateArray and CertificateArrayOutput values.
// You can construct a concrete instance of `CertificateArrayInput` via:
//
//          CertificateArray{ CertificateArgs{...} }
type CertificateArrayInput interface {
	pulumi.Input

	ToCertificateArrayOutput() CertificateArrayOutput
	ToCertificateArrayOutputWithContext(context.Context) CertificateArrayOutput
}

type CertificateArray []CertificateInput

func (CertificateArray) ElementType() reflect.Type {
	return reflect.TypeOf((*[]*Certificate)(nil)).Elem()
}

func (i CertificateArray) ToCertificateArrayOutput() CertificateArrayOutput {
	return i.ToCertificateArrayOutputWithContext(context.Background())
}

func (i CertificateArray) ToCertificateArrayOutputWithContext(ctx context.Context) CertificateArrayOutput {
	return pulumi.ToOutputWithContext(ctx, i).(CertificateArrayOutput)
}

// CertificateMapInput is an input type that accepts CertificateMap and CertificateMapOutput values.
// You can construct a concrete instance of `CertificateMapInput` via:
//
//          CertificateMap{ "key": CertificateArgs{...} }
type CertificateMapInput interface {
	pulumi.Input

	ToCertificateMapOutput() CertificateMapOutput
	ToCertificateMapOutputWithContext(context.Context) CertificateMapOutput
}

type CertificateMap map[string]CertificateInput

func (CertificateMap) ElementType() reflect.Type {
	return reflect.TypeOf((*map[string]*Certificate)(nil)).Elem()
}

func (i CertificateMap) ToCertificateMapOutput() CertificateMapOutput {
	return i.ToCertificateMapOutputWithContext(context.Background())
}

func (i CertificateMap) ToCertificateMapOutputWithContext(ctx context.Context) CertificateMapOutput {
	return pulumi.ToOutputWithContext(ctx, i).(CertificateMapOutput)
}

type CertificateOutput struct{ *pulumi.OutputState }

func (CertificateOutput) ElementType() reflect.Type {
	return reflect.TypeOf((*Certificate)(nil))
}

func (o CertificateOutput) ToCertificateOutput() CertificateOutput {
	return o
}

func (o CertificateOutput) ToCertificateOutputWithContext(ctx context.Context) CertificateOutput {
	return o
}

func (o CertificateOutput) ToCertificatePtrOutput() CertificatePtrOutput {
	return o.ToCertificatePtrOutputWithContext(context.Background())
}

func (o CertificateOutput) ToCertificatePtrOutputWithContext(ctx context.Context) CertificatePtrOutput {
	return o.ApplyTWithContext(ctx, func(_ context.Context, v Certificate) *Certificate {
		return &v
	}).(CertificatePtrOutput)
}

type CertificatePtrOutput struct{ *pulumi.OutputState }

func (CertificatePtrOutput) ElementType() reflect.Type {
	return reflect.TypeOf((**Certificate)(nil))
}

func (o CertificatePtrOutput) ToCertificatePtrOutput() CertificatePtrOutput {
	return o
}

func (o CertificatePtrOutput) ToCertificatePtrOutputWithContext(ctx context.Context) CertificatePtrOutput {
	return o
}

func (o CertificatePtrOutput) Elem() CertificateOutput {
	return o.ApplyT(func(v *Certificate) Certificate {
		if v != nil {
			return *v
		}
		var ret Certificate
		return ret
	}).(CertificateOutput)
}

type CertificateArrayOutput struct{ *pulumi.OutputState }

func (CertificateArrayOutput) ElementType() reflect.Type {
	return reflect.TypeOf((*[]Certificate)(nil))
}

func (o CertificateArrayOutput) ToCertificateArrayOutput() CertificateArrayOutput {
	return o
}

func (o CertificateArrayOutput) ToCertificateArrayOutputWithContext(ctx context.Context) CertificateArrayOutput {
	return o
}

func (o CertificateArrayOutput) Index(i pulumi.IntInput) CertificateOutput {
	return pulumi.All(o, i).ApplyT(func(vs []interface{}) Certificate {
		return vs[0].([]Certificate)[vs[1].(int)]
	}).(CertificateOutput)
}

type CertificateMapOutput struct{ *pulumi.OutputState }

func (CertificateMapOutput) ElementType() reflect.Type {
	return reflect.TypeOf((*map[string]Certificate)(nil))
}

func (o CertificateMapOutput) ToCertificateMapOutput() CertificateMapOutput {
	return o
}

func (o CertificateMapOutput) ToCertificateMapOutputWithContext(ctx context.Context) CertificateMapOutput {
	return o
}

func (o CertificateMapOutput) MapIndex(k pulumi.StringInput) CertificateOutput {
	return pulumi.All(o, k).ApplyT(func(vs []interface{}) Certificate {
		return vs[0].(map[string]Certificate)[vs[1].(string)]
	}).(CertificateOutput)
}

func init() {
	pulumi.RegisterInputType(reflect.TypeOf((*CertificateInput)(nil)).Elem(), &Certificate{})
	pulumi.RegisterInputType(reflect.TypeOf((*CertificatePtrInput)(nil)).Elem(), &Certificate{})
	pulumi.RegisterInputType(reflect.TypeOf((*CertificateArrayInput)(nil)).Elem(), CertificateArray{})
	pulumi.RegisterInputType(reflect.TypeOf((*CertificateMapInput)(nil)).Elem(), CertificateMap{})
	pulumi.RegisterOutputType(CertificateOutput{})
	pulumi.RegisterOutputType(CertificatePtrOutput{})
	pulumi.RegisterOutputType(CertificateArrayOutput{})
	pulumi.RegisterOutputType(CertificateMapOutput{})
}

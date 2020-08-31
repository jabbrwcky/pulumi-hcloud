// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

package hcloud

import (
	"github.com/pulumi/pulumi/sdk/v2/go/pulumi"
)

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
	Id     *int                   `pulumi:"id"`
	Labels map[string]interface{} `pulumi:"labels"`
	// (string) Name of the SSH Key.
	Name string `pulumi:"name"`
	// (string) Public Key of the SSH Key.
	PublicKey string `pulumi:"publicKey"`
	// Deprecated: Please use the with_selector property instead.
	Selector     *string `pulumi:"selector"`
	WithSelector *string `pulumi:"withSelector"`
}

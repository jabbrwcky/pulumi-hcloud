// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

package hcloud

import (
	"github.com/pulumi/pulumi/sdk/v2/go/pulumi"
)

func LookupVolume(ctx *pulumi.Context, args *LookupVolumeArgs, opts ...pulumi.InvokeOption) (*LookupVolumeResult, error) {
	var rv LookupVolumeResult
	err := ctx.Invoke("hcloud:index/getVolume:getVolume", args, &rv, opts...)
	if err != nil {
		return nil, err
	}
	return &rv, nil
}

// A collection of arguments for invoking getVolume.
type LookupVolumeArgs struct {
	Id       *int    `pulumi:"id"`
	Location *string `pulumi:"location"`
	Name     *string `pulumi:"name"`
	// Deprecated: Please use the with_selector property instead.
	Selector     *string  `pulumi:"selector"`
	Server       *string  `pulumi:"server"`
	WithSelector *string  `pulumi:"withSelector"`
	WithStatuses []string `pulumi:"withStatuses"`
}

// A collection of values returned by getVolume.
type LookupVolumeResult struct {
	Id          *int                   `pulumi:"id"`
	Labels      map[string]interface{} `pulumi:"labels"`
	LinuxDevice string                 `pulumi:"linuxDevice"`
	Location    *string                `pulumi:"location"`
	Name        string                 `pulumi:"name"`
	// Deprecated: Please use the with_selector property instead.
	Selector     *string  `pulumi:"selector"`
	Server       *string  `pulumi:"server"`
	Size         int      `pulumi:"size"`
	WithSelector *string  `pulumi:"withSelector"`
	WithStatuses []string `pulumi:"withStatuses"`
}

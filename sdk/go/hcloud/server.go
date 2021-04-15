// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

package hcloud

import (
	"context"
	"reflect"

	"github.com/pkg/errors"
	"github.com/pulumi/pulumi/sdk/v3/go/pulumi"
)

// ## Import
//
// Servers can be imported using the server `id`
//
// ```sh
//  $ pulumi import hcloud:index/server:Server myserver <id>
// ```
type Server struct {
	pulumi.CustomResourceState

	// (string) The backup window of the server, if enabled.
	//
	// Deprecated: You should remove this property from your terraform configuration.
	BackupWindow pulumi.StringOutput `pulumi:"backupWindow"`
	// Enable or disable backups.
	Backups pulumi.BoolPtrOutput `pulumi:"backups"`
	// The datacenter name to create the server in.
	Datacenter  pulumi.StringOutput   `pulumi:"datacenter"`
	FirewallIds pulumi.IntArrayOutput `pulumi:"firewallIds"`
	// Name or ID of the image the server is created from.
	Image pulumi.StringOutput `pulumi:"image"`
	// (string) The IPv4 address.
	Ipv4Address pulumi.StringOutput `pulumi:"ipv4Address"`
	// (string) The first IPv6 address of the assigned network.
	Ipv6Address pulumi.StringOutput `pulumi:"ipv6Address"`
	// (string) The IPv6 network.
	Ipv6Network pulumi.StringOutput `pulumi:"ipv6Network"`
	// ID or Name of an ISO image to mount.
	Iso pulumi.StringPtrOutput `pulumi:"iso"`
	// If true, do not upgrade the disk. This allows downgrading the server type later.
	KeepDisk pulumi.BoolPtrOutput `pulumi:"keepDisk"`
	// User-defined labels (key-value pairs) should be created with.
	Labels pulumi.MapOutput `pulumi:"labels"`
	// The location name to create the server in. `nbg1`, `fsn1` or `hel1`
	Location pulumi.StringOutput `pulumi:"location"`
	// Name of the server to create (must be unique per project and a valid hostname as per RFC 1123).
	Name     pulumi.StringOutput          `pulumi:"name"`
	Networks ServerNetworkTypeArrayOutput `pulumi:"networks"`
	// Enable and boot in to the specified rescue system. This enables simple installation of custom operating systems. `linux64` `linux32` or `freebsd64`
	Rescue pulumi.StringPtrOutput `pulumi:"rescue"`
	// Name of the server type this server should be created with.
	ServerType pulumi.StringOutput `pulumi:"serverType"`
	// SSH key IDs or names which should be injected into the server at creation time
	SshKeys pulumi.StringArrayOutput `pulumi:"sshKeys"`
	// (string) The status of the server.
	Status pulumi.StringOutput `pulumi:"status"`
	// Cloud-Init user data to use during server creation
	UserData pulumi.StringPtrOutput `pulumi:"userData"`
}

// NewServer registers a new resource with the given unique name, arguments, and options.
func NewServer(ctx *pulumi.Context,
	name string, args *ServerArgs, opts ...pulumi.ResourceOption) (*Server, error) {
	if args == nil {
		return nil, errors.New("missing one or more required arguments")
	}

	if args.Image == nil {
		return nil, errors.New("invalid value for required argument 'Image'")
	}
	if args.ServerType == nil {
		return nil, errors.New("invalid value for required argument 'ServerType'")
	}
	var resource Server
	err := ctx.RegisterResource("hcloud:index/server:Server", name, args, &resource, opts...)
	if err != nil {
		return nil, err
	}
	return &resource, nil
}

// GetServer gets an existing Server resource's state with the given name, ID, and optional
// state properties that are used to uniquely qualify the lookup (nil if not required).
func GetServer(ctx *pulumi.Context,
	name string, id pulumi.IDInput, state *ServerState, opts ...pulumi.ResourceOption) (*Server, error) {
	var resource Server
	err := ctx.ReadResource("hcloud:index/server:Server", name, id, state, &resource, opts...)
	if err != nil {
		return nil, err
	}
	return &resource, nil
}

// Input properties used for looking up and filtering Server resources.
type serverState struct {
	// (string) The backup window of the server, if enabled.
	//
	// Deprecated: You should remove this property from your terraform configuration.
	BackupWindow *string `pulumi:"backupWindow"`
	// Enable or disable backups.
	Backups *bool `pulumi:"backups"`
	// The datacenter name to create the server in.
	Datacenter  *string `pulumi:"datacenter"`
	FirewallIds []int   `pulumi:"firewallIds"`
	// Name or ID of the image the server is created from.
	Image *string `pulumi:"image"`
	// (string) The IPv4 address.
	Ipv4Address *string `pulumi:"ipv4Address"`
	// (string) The first IPv6 address of the assigned network.
	Ipv6Address *string `pulumi:"ipv6Address"`
	// (string) The IPv6 network.
	Ipv6Network *string `pulumi:"ipv6Network"`
	// ID or Name of an ISO image to mount.
	Iso *string `pulumi:"iso"`
	// If true, do not upgrade the disk. This allows downgrading the server type later.
	KeepDisk *bool `pulumi:"keepDisk"`
	// User-defined labels (key-value pairs) should be created with.
	Labels map[string]interface{} `pulumi:"labels"`
	// The location name to create the server in. `nbg1`, `fsn1` or `hel1`
	Location *string `pulumi:"location"`
	// Name of the server to create (must be unique per project and a valid hostname as per RFC 1123).
	Name     *string             `pulumi:"name"`
	Networks []ServerNetworkType `pulumi:"networks"`
	// Enable and boot in to the specified rescue system. This enables simple installation of custom operating systems. `linux64` `linux32` or `freebsd64`
	Rescue *string `pulumi:"rescue"`
	// Name of the server type this server should be created with.
	ServerType *string `pulumi:"serverType"`
	// SSH key IDs or names which should be injected into the server at creation time
	SshKeys []string `pulumi:"sshKeys"`
	// (string) The status of the server.
	Status *string `pulumi:"status"`
	// Cloud-Init user data to use during server creation
	UserData *string `pulumi:"userData"`
}

type ServerState struct {
	// (string) The backup window of the server, if enabled.
	//
	// Deprecated: You should remove this property from your terraform configuration.
	BackupWindow pulumi.StringPtrInput
	// Enable or disable backups.
	Backups pulumi.BoolPtrInput
	// The datacenter name to create the server in.
	Datacenter  pulumi.StringPtrInput
	FirewallIds pulumi.IntArrayInput
	// Name or ID of the image the server is created from.
	Image pulumi.StringPtrInput
	// (string) The IPv4 address.
	Ipv4Address pulumi.StringPtrInput
	// (string) The first IPv6 address of the assigned network.
	Ipv6Address pulumi.StringPtrInput
	// (string) The IPv6 network.
	Ipv6Network pulumi.StringPtrInput
	// ID or Name of an ISO image to mount.
	Iso pulumi.StringPtrInput
	// If true, do not upgrade the disk. This allows downgrading the server type later.
	KeepDisk pulumi.BoolPtrInput
	// User-defined labels (key-value pairs) should be created with.
	Labels pulumi.MapInput
	// The location name to create the server in. `nbg1`, `fsn1` or `hel1`
	Location pulumi.StringPtrInput
	// Name of the server to create (must be unique per project and a valid hostname as per RFC 1123).
	Name     pulumi.StringPtrInput
	Networks ServerNetworkTypeArrayInput
	// Enable and boot in to the specified rescue system. This enables simple installation of custom operating systems. `linux64` `linux32` or `freebsd64`
	Rescue pulumi.StringPtrInput
	// Name of the server type this server should be created with.
	ServerType pulumi.StringPtrInput
	// SSH key IDs or names which should be injected into the server at creation time
	SshKeys pulumi.StringArrayInput
	// (string) The status of the server.
	Status pulumi.StringPtrInput
	// Cloud-Init user data to use during server creation
	UserData pulumi.StringPtrInput
}

func (ServerState) ElementType() reflect.Type {
	return reflect.TypeOf((*serverState)(nil)).Elem()
}

type serverArgs struct {
	// Enable or disable backups.
	Backups *bool `pulumi:"backups"`
	// The datacenter name to create the server in.
	Datacenter  *string `pulumi:"datacenter"`
	FirewallIds []int   `pulumi:"firewallIds"`
	// Name or ID of the image the server is created from.
	Image string `pulumi:"image"`
	// ID or Name of an ISO image to mount.
	Iso *string `pulumi:"iso"`
	// If true, do not upgrade the disk. This allows downgrading the server type later.
	KeepDisk *bool `pulumi:"keepDisk"`
	// User-defined labels (key-value pairs) should be created with.
	Labels map[string]interface{} `pulumi:"labels"`
	// The location name to create the server in. `nbg1`, `fsn1` or `hel1`
	Location *string `pulumi:"location"`
	// Name of the server to create (must be unique per project and a valid hostname as per RFC 1123).
	Name     *string             `pulumi:"name"`
	Networks []ServerNetworkType `pulumi:"networks"`
	// Enable and boot in to the specified rescue system. This enables simple installation of custom operating systems. `linux64` `linux32` or `freebsd64`
	Rescue *string `pulumi:"rescue"`
	// Name of the server type this server should be created with.
	ServerType string `pulumi:"serverType"`
	// SSH key IDs or names which should be injected into the server at creation time
	SshKeys []string `pulumi:"sshKeys"`
	// Cloud-Init user data to use during server creation
	UserData *string `pulumi:"userData"`
}

// The set of arguments for constructing a Server resource.
type ServerArgs struct {
	// Enable or disable backups.
	Backups pulumi.BoolPtrInput
	// The datacenter name to create the server in.
	Datacenter  pulumi.StringPtrInput
	FirewallIds pulumi.IntArrayInput
	// Name or ID of the image the server is created from.
	Image pulumi.StringInput
	// ID or Name of an ISO image to mount.
	Iso pulumi.StringPtrInput
	// If true, do not upgrade the disk. This allows downgrading the server type later.
	KeepDisk pulumi.BoolPtrInput
	// User-defined labels (key-value pairs) should be created with.
	Labels pulumi.MapInput
	// The location name to create the server in. `nbg1`, `fsn1` or `hel1`
	Location pulumi.StringPtrInput
	// Name of the server to create (must be unique per project and a valid hostname as per RFC 1123).
	Name     pulumi.StringPtrInput
	Networks ServerNetworkTypeArrayInput
	// Enable and boot in to the specified rescue system. This enables simple installation of custom operating systems. `linux64` `linux32` or `freebsd64`
	Rescue pulumi.StringPtrInput
	// Name of the server type this server should be created with.
	ServerType pulumi.StringInput
	// SSH key IDs or names which should be injected into the server at creation time
	SshKeys pulumi.StringArrayInput
	// Cloud-Init user data to use during server creation
	UserData pulumi.StringPtrInput
}

func (ServerArgs) ElementType() reflect.Type {
	return reflect.TypeOf((*serverArgs)(nil)).Elem()
}

type ServerInput interface {
	pulumi.Input

	ToServerOutput() ServerOutput
	ToServerOutputWithContext(ctx context.Context) ServerOutput
}

func (*Server) ElementType() reflect.Type {
	return reflect.TypeOf((*Server)(nil))
}

func (i *Server) ToServerOutput() ServerOutput {
	return i.ToServerOutputWithContext(context.Background())
}

func (i *Server) ToServerOutputWithContext(ctx context.Context) ServerOutput {
	return pulumi.ToOutputWithContext(ctx, i).(ServerOutput)
}

func (i *Server) ToServerPtrOutput() ServerPtrOutput {
	return i.ToServerPtrOutputWithContext(context.Background())
}

func (i *Server) ToServerPtrOutputWithContext(ctx context.Context) ServerPtrOutput {
	return pulumi.ToOutputWithContext(ctx, i).(ServerPtrOutput)
}

type ServerPtrInput interface {
	pulumi.Input

	ToServerPtrOutput() ServerPtrOutput
	ToServerPtrOutputWithContext(ctx context.Context) ServerPtrOutput
}

type serverPtrType ServerArgs

func (*serverPtrType) ElementType() reflect.Type {
	return reflect.TypeOf((**Server)(nil))
}

func (i *serverPtrType) ToServerPtrOutput() ServerPtrOutput {
	return i.ToServerPtrOutputWithContext(context.Background())
}

func (i *serverPtrType) ToServerPtrOutputWithContext(ctx context.Context) ServerPtrOutput {
	return pulumi.ToOutputWithContext(ctx, i).(ServerPtrOutput)
}

// ServerArrayInput is an input type that accepts ServerArray and ServerArrayOutput values.
// You can construct a concrete instance of `ServerArrayInput` via:
//
//          ServerArray{ ServerArgs{...} }
type ServerArrayInput interface {
	pulumi.Input

	ToServerArrayOutput() ServerArrayOutput
	ToServerArrayOutputWithContext(context.Context) ServerArrayOutput
}

type ServerArray []ServerInput

func (ServerArray) ElementType() reflect.Type {
	return reflect.TypeOf(([]*Server)(nil))
}

func (i ServerArray) ToServerArrayOutput() ServerArrayOutput {
	return i.ToServerArrayOutputWithContext(context.Background())
}

func (i ServerArray) ToServerArrayOutputWithContext(ctx context.Context) ServerArrayOutput {
	return pulumi.ToOutputWithContext(ctx, i).(ServerArrayOutput)
}

// ServerMapInput is an input type that accepts ServerMap and ServerMapOutput values.
// You can construct a concrete instance of `ServerMapInput` via:
//
//          ServerMap{ "key": ServerArgs{...} }
type ServerMapInput interface {
	pulumi.Input

	ToServerMapOutput() ServerMapOutput
	ToServerMapOutputWithContext(context.Context) ServerMapOutput
}

type ServerMap map[string]ServerInput

func (ServerMap) ElementType() reflect.Type {
	return reflect.TypeOf((map[string]*Server)(nil))
}

func (i ServerMap) ToServerMapOutput() ServerMapOutput {
	return i.ToServerMapOutputWithContext(context.Background())
}

func (i ServerMap) ToServerMapOutputWithContext(ctx context.Context) ServerMapOutput {
	return pulumi.ToOutputWithContext(ctx, i).(ServerMapOutput)
}

type ServerOutput struct {
	*pulumi.OutputState
}

func (ServerOutput) ElementType() reflect.Type {
	return reflect.TypeOf((*Server)(nil))
}

func (o ServerOutput) ToServerOutput() ServerOutput {
	return o
}

func (o ServerOutput) ToServerOutputWithContext(ctx context.Context) ServerOutput {
	return o
}

func (o ServerOutput) ToServerPtrOutput() ServerPtrOutput {
	return o.ToServerPtrOutputWithContext(context.Background())
}

func (o ServerOutput) ToServerPtrOutputWithContext(ctx context.Context) ServerPtrOutput {
	return o.ApplyT(func(v Server) *Server {
		return &v
	}).(ServerPtrOutput)
}

type ServerPtrOutput struct {
	*pulumi.OutputState
}

func (ServerPtrOutput) ElementType() reflect.Type {
	return reflect.TypeOf((**Server)(nil))
}

func (o ServerPtrOutput) ToServerPtrOutput() ServerPtrOutput {
	return o
}

func (o ServerPtrOutput) ToServerPtrOutputWithContext(ctx context.Context) ServerPtrOutput {
	return o
}

type ServerArrayOutput struct{ *pulumi.OutputState }

func (ServerArrayOutput) ElementType() reflect.Type {
	return reflect.TypeOf((*[]Server)(nil))
}

func (o ServerArrayOutput) ToServerArrayOutput() ServerArrayOutput {
	return o
}

func (o ServerArrayOutput) ToServerArrayOutputWithContext(ctx context.Context) ServerArrayOutput {
	return o
}

func (o ServerArrayOutput) Index(i pulumi.IntInput) ServerOutput {
	return pulumi.All(o, i).ApplyT(func(vs []interface{}) Server {
		return vs[0].([]Server)[vs[1].(int)]
	}).(ServerOutput)
}

type ServerMapOutput struct{ *pulumi.OutputState }

func (ServerMapOutput) ElementType() reflect.Type {
	return reflect.TypeOf((*map[string]Server)(nil))
}

func (o ServerMapOutput) ToServerMapOutput() ServerMapOutput {
	return o
}

func (o ServerMapOutput) ToServerMapOutputWithContext(ctx context.Context) ServerMapOutput {
	return o
}

func (o ServerMapOutput) MapIndex(k pulumi.StringInput) ServerOutput {
	return pulumi.All(o, k).ApplyT(func(vs []interface{}) Server {
		return vs[0].(map[string]Server)[vs[1].(string)]
	}).(ServerOutput)
}

func init() {
	pulumi.RegisterOutputType(ServerOutput{})
	pulumi.RegisterOutputType(ServerPtrOutput{})
	pulumi.RegisterOutputType(ServerArrayOutput{})
	pulumi.RegisterOutputType(ServerMapOutput{})
}

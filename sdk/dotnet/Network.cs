// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.HCloud
{
    /// <summary>
    /// Provides a Hetzner Cloud Network to represent a Network in the Hetzner Cloud.
    /// 
    /// ## Example Usage
    /// 
    /// ```csharp
    /// using Pulumi;
    /// using HCloud = Pulumi.HCloud;
    /// 
    /// class MyStack : Stack
    /// {
    ///     public MyStack()
    ///     {
    ///         var privNet = new HCloud.Network("privNet", new HCloud.NetworkArgs
    ///         {
    ///             IpRange = "10.0.1.0/24",
    ///         });
    ///     }
    /// 
    /// }
    /// ```
    /// 
    /// ## Import
    /// 
    /// Networks can be imported using its `id`
    /// 
    /// ```sh
    ///  $ pulumi import hcloud:index/network:Network myip &lt;id&gt;
    /// ```
    /// </summary>
    [HCloudResourceType("hcloud:index/network:Network")]
    public partial class Network : Pulumi.CustomResource
    {
        /// <summary>
        /// Enable or disable delete protection.
        /// </summary>
        [Output("deleteProtection")]
        public Output<bool?> DeleteProtection { get; private set; } = null!;

        /// <summary>
        /// IP Range of the whole Network which must span all included subnets and route destinations. Must be one of the private ipv4 ranges of RFC1918.
        /// </summary>
        [Output("ipRange")]
        public Output<string> IpRange { get; private set; } = null!;

        /// <summary>
        /// User-defined labels (key-value pairs) should be created with.
        /// </summary>
        [Output("labels")]
        public Output<ImmutableDictionary<string, object>?> Labels { get; private set; } = null!;

        /// <summary>
        /// Name of the Network to create (must be unique per project).
        /// </summary>
        [Output("name")]
        public Output<string> Name { get; private set; } = null!;


        /// <summary>
        /// Create a Network resource with the given unique name, arguments, and options.
        /// </summary>
        ///
        /// <param name="name">The unique name of the resource</param>
        /// <param name="args">The arguments used to populate this resource's properties</param>
        /// <param name="options">A bag of options that control this resource's behavior</param>
        public Network(string name, NetworkArgs args, CustomResourceOptions? options = null)
            : base("hcloud:index/network:Network", name, args ?? new NetworkArgs(), MakeResourceOptions(options, ""))
        {
        }

        private Network(string name, Input<string> id, NetworkState? state = null, CustomResourceOptions? options = null)
            : base("hcloud:index/network:Network", name, state, MakeResourceOptions(options, id))
        {
        }

        private static CustomResourceOptions MakeResourceOptions(CustomResourceOptions? options, Input<string>? id)
        {
            var defaultOptions = new CustomResourceOptions
            {
                Version = Utilities.Version,
            };
            var merged = CustomResourceOptions.Merge(defaultOptions, options);
            // Override the ID if one was specified for consistency with other language SDKs.
            merged.Id = id ?? merged.Id;
            return merged;
        }
        /// <summary>
        /// Get an existing Network resource's state with the given name, ID, and optional extra
        /// properties used to qualify the lookup.
        /// </summary>
        ///
        /// <param name="name">The unique name of the resulting resource.</param>
        /// <param name="id">The unique provider ID of the resource to lookup.</param>
        /// <param name="state">Any extra arguments used during the lookup.</param>
        /// <param name="options">A bag of options that control this resource's behavior</param>
        public static Network Get(string name, Input<string> id, NetworkState? state = null, CustomResourceOptions? options = null)
        {
            return new Network(name, id, state, options);
        }
    }

    public sealed class NetworkArgs : Pulumi.ResourceArgs
    {
        /// <summary>
        /// Enable or disable delete protection.
        /// </summary>
        [Input("deleteProtection")]
        public Input<bool>? DeleteProtection { get; set; }

        /// <summary>
        /// IP Range of the whole Network which must span all included subnets and route destinations. Must be one of the private ipv4 ranges of RFC1918.
        /// </summary>
        [Input("ipRange", required: true)]
        public Input<string> IpRange { get; set; } = null!;

        [Input("labels")]
        private InputMap<object>? _labels;

        /// <summary>
        /// User-defined labels (key-value pairs) should be created with.
        /// </summary>
        public InputMap<object> Labels
        {
            get => _labels ?? (_labels = new InputMap<object>());
            set => _labels = value;
        }

        /// <summary>
        /// Name of the Network to create (must be unique per project).
        /// </summary>
        [Input("name")]
        public Input<string>? Name { get; set; }

        public NetworkArgs()
        {
        }
    }

    public sealed class NetworkState : Pulumi.ResourceArgs
    {
        /// <summary>
        /// Enable or disable delete protection.
        /// </summary>
        [Input("deleteProtection")]
        public Input<bool>? DeleteProtection { get; set; }

        /// <summary>
        /// IP Range of the whole Network which must span all included subnets and route destinations. Must be one of the private ipv4 ranges of RFC1918.
        /// </summary>
        [Input("ipRange")]
        public Input<string>? IpRange { get; set; }

        [Input("labels")]
        private InputMap<object>? _labels;

        /// <summary>
        /// User-defined labels (key-value pairs) should be created with.
        /// </summary>
        public InputMap<object> Labels
        {
            get => _labels ?? (_labels = new InputMap<object>());
            set => _labels = value;
        }

        /// <summary>
        /// Name of the Network to create (must be unique per project).
        /// </summary>
        [Input("name")]
        public Input<string>? Name { get; set; }

        public NetworkState()
        {
        }
    }
}

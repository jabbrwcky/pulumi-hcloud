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
    /// Provides a Hetzner Cloud Load Balancer to represent a Load Balancer in the Hetzner Cloud.
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
    ///         var myserver = new HCloud.Server("myserver", new HCloud.ServerArgs
    ///         {
    ///             ServerType = "cx11",
    ///             Image = "ubuntu-18.04",
    ///         });
    ///         var loadBalancer = new HCloud.LoadBalancer("loadBalancer", new HCloud.LoadBalancerArgs
    ///         {
    ///             LoadBalancerType = "lb11",
    ///             Location = "nbg1",
    ///             Targets = 
    ///             {
    ///                 new HCloud.Inputs.LoadBalancerTargetArgs
    ///                 {
    ///                     Type = "server",
    ///                     ServerId = myserver.Id,
    ///                 },
    ///             },
    ///         });
    ///     }
    /// 
    /// }
    /// ```
    /// 
    /// ## Import
    /// 
    /// Load Balancers can be imported using its `id`
    /// 
    /// ```sh
    ///  $ pulumi import hcloud:index/loadBalancer:LoadBalancer my_load_balancer &lt;id&gt;
    /// ```
    /// </summary>
    [HCloudResourceType("hcloud:index/loadBalancer:LoadBalancer")]
    public partial class LoadBalancer : Pulumi.CustomResource
    {
        /// <summary>
        /// Configuration of the algorithm the Load Balancer use.
        /// </summary>
        [Output("algorithm")]
        public Output<Outputs.LoadBalancerAlgorithm> Algorithm { get; private set; } = null!;

        /// <summary>
        /// Enable or disable delete protection.
        /// </summary>
        [Output("deleteProtection")]
        public Output<bool?> DeleteProtection { get; private set; } = null!;

        /// <summary>
        /// (string) IPv4 Address of the Load Balancer.
        /// </summary>
        [Output("ipv4")]
        public Output<string> Ipv4 { get; private set; } = null!;

        /// <summary>
        /// (string) IPv4 Address of the Load Balancer.
        /// </summary>
        [Output("ipv6")]
        public Output<string> Ipv6 { get; private set; } = null!;

        /// <summary>
        /// User-defined labels (key-value pairs) should be created with.
        /// </summary>
        [Output("labels")]
        public Output<ImmutableDictionary<string, object>> Labels { get; private set; } = null!;

        /// <summary>
        /// Type of the Load Balancer.
        /// </summary>
        [Output("loadBalancerType")]
        public Output<string> LoadBalancerType { get; private set; } = null!;

        /// <summary>
        /// Location of the Load Balancer. Require when no network_zone is set.
        /// </summary>
        [Output("location")]
        public Output<string> Location { get; private set; } = null!;

        /// <summary>
        /// Name of the Load Balancer.
        /// </summary>
        [Output("name")]
        public Output<string> Name { get; private set; } = null!;

        [Output("networkId")]
        public Output<int> NetworkId { get; private set; } = null!;

        [Output("networkIp")]
        public Output<string> NetworkIp { get; private set; } = null!;

        /// <summary>
        /// Network Zone of the Load Balancer. Require when no location is set.
        /// </summary>
        [Output("networkZone")]
        public Output<string> NetworkZone { get; private set; } = null!;

        [Output("targets")]
        public Output<ImmutableArray<Outputs.LoadBalancerTarget>> Targets { get; private set; } = null!;


        /// <summary>
        /// Create a LoadBalancer resource with the given unique name, arguments, and options.
        /// </summary>
        ///
        /// <param name="name">The unique name of the resource</param>
        /// <param name="args">The arguments used to populate this resource's properties</param>
        /// <param name="options">A bag of options that control this resource's behavior</param>
        public LoadBalancer(string name, LoadBalancerArgs args, CustomResourceOptions? options = null)
            : base("hcloud:index/loadBalancer:LoadBalancer", name, args ?? new LoadBalancerArgs(), MakeResourceOptions(options, ""))
        {
        }

        private LoadBalancer(string name, Input<string> id, LoadBalancerState? state = null, CustomResourceOptions? options = null)
            : base("hcloud:index/loadBalancer:LoadBalancer", name, state, MakeResourceOptions(options, id))
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
        /// Get an existing LoadBalancer resource's state with the given name, ID, and optional extra
        /// properties used to qualify the lookup.
        /// </summary>
        ///
        /// <param name="name">The unique name of the resulting resource.</param>
        /// <param name="id">The unique provider ID of the resource to lookup.</param>
        /// <param name="state">Any extra arguments used during the lookup.</param>
        /// <param name="options">A bag of options that control this resource's behavior</param>
        public static LoadBalancer Get(string name, Input<string> id, LoadBalancerState? state = null, CustomResourceOptions? options = null)
        {
            return new LoadBalancer(name, id, state, options);
        }
    }

    public sealed class LoadBalancerArgs : Pulumi.ResourceArgs
    {
        /// <summary>
        /// Configuration of the algorithm the Load Balancer use.
        /// </summary>
        [Input("algorithm")]
        public Input<Inputs.LoadBalancerAlgorithmArgs>? Algorithm { get; set; }

        /// <summary>
        /// Enable or disable delete protection.
        /// </summary>
        [Input("deleteProtection")]
        public Input<bool>? DeleteProtection { get; set; }

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
        /// Type of the Load Balancer.
        /// </summary>
        [Input("loadBalancerType", required: true)]
        public Input<string> LoadBalancerType { get; set; } = null!;

        /// <summary>
        /// Location of the Load Balancer. Require when no network_zone is set.
        /// </summary>
        [Input("location")]
        public Input<string>? Location { get; set; }

        /// <summary>
        /// Name of the Load Balancer.
        /// </summary>
        [Input("name")]
        public Input<string>? Name { get; set; }

        /// <summary>
        /// Network Zone of the Load Balancer. Require when no location is set.
        /// </summary>
        [Input("networkZone")]
        public Input<string>? NetworkZone { get; set; }

        [Input("targets")]
        private InputList<Inputs.LoadBalancerTargetArgs>? _targets;
        [Obsolete(@"Use hcloud_load_balancer_target resource instead. This allows the full control over the selected targets.")]
        public InputList<Inputs.LoadBalancerTargetArgs> Targets
        {
            get => _targets ?? (_targets = new InputList<Inputs.LoadBalancerTargetArgs>());
            set => _targets = value;
        }

        public LoadBalancerArgs()
        {
        }
    }

    public sealed class LoadBalancerState : Pulumi.ResourceArgs
    {
        /// <summary>
        /// Configuration of the algorithm the Load Balancer use.
        /// </summary>
        [Input("algorithm")]
        public Input<Inputs.LoadBalancerAlgorithmGetArgs>? Algorithm { get; set; }

        /// <summary>
        /// Enable or disable delete protection.
        /// </summary>
        [Input("deleteProtection")]
        public Input<bool>? DeleteProtection { get; set; }

        /// <summary>
        /// (string) IPv4 Address of the Load Balancer.
        /// </summary>
        [Input("ipv4")]
        public Input<string>? Ipv4 { get; set; }

        /// <summary>
        /// (string) IPv4 Address of the Load Balancer.
        /// </summary>
        [Input("ipv6")]
        public Input<string>? Ipv6 { get; set; }

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
        /// Type of the Load Balancer.
        /// </summary>
        [Input("loadBalancerType")]
        public Input<string>? LoadBalancerType { get; set; }

        /// <summary>
        /// Location of the Load Balancer. Require when no network_zone is set.
        /// </summary>
        [Input("location")]
        public Input<string>? Location { get; set; }

        /// <summary>
        /// Name of the Load Balancer.
        /// </summary>
        [Input("name")]
        public Input<string>? Name { get; set; }

        [Input("networkId")]
        public Input<int>? NetworkId { get; set; }

        [Input("networkIp")]
        public Input<string>? NetworkIp { get; set; }

        /// <summary>
        /// Network Zone of the Load Balancer. Require when no location is set.
        /// </summary>
        [Input("networkZone")]
        public Input<string>? NetworkZone { get; set; }

        [Input("targets")]
        private InputList<Inputs.LoadBalancerTargetGetArgs>? _targets;
        [Obsolete(@"Use hcloud_load_balancer_target resource instead. This allows the full control over the selected targets.")]
        public InputList<Inputs.LoadBalancerTargetGetArgs> Targets
        {
            get => _targets ?? (_targets = new InputList<Inputs.LoadBalancerTargetGetArgs>());
            set => _targets = value;
        }

        public LoadBalancerState()
        {
        }
    }
}

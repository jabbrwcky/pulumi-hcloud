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
    /// Define services for Hetzner Cloud Load Balancers.
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
    ///         var loadBalancer = new HCloud.LoadBalancer("loadBalancer", new HCloud.LoadBalancerArgs
    ///         {
    ///             LoadBalancerType = "lb11",
    ///             Location = "nbg1",
    ///         });
    ///         var loadBalancerService = new HCloud.LoadBalancerService("loadBalancerService", new HCloud.LoadBalancerServiceArgs
    ///         {
    ///             LoadBalancerId = hcloud_load_balancer.Test_load_balancer.Id,
    ///             Protocol = "http",
    ///         });
    ///     }
    /// 
    /// }
    /// ```
    /// </summary>
    public partial class LoadBalancerService : Pulumi.CustomResource
    {
        [Output("destinationPort")]
        public Output<int> DestinationPort { get; private set; } = null!;

        [Output("healthCheck")]
        public Output<Outputs.LoadBalancerServiceHealthCheck> HealthCheck { get; private set; } = null!;

        [Output("http")]
        public Output<Outputs.LoadBalancerServiceHttp?> Http { get; private set; } = null!;

        [Output("listenPort")]
        public Output<int> ListenPort { get; private set; } = null!;

        [Output("loadBalancerId")]
        public Output<string> LoadBalancerId { get; private set; } = null!;

        [Output("protocol")]
        public Output<string> Protocol { get; private set; } = null!;

        [Output("proxyprotocol")]
        public Output<bool> Proxyprotocol { get; private set; } = null!;


        /// <summary>
        /// Create a LoadBalancerService resource with the given unique name, arguments, and options.
        /// </summary>
        ///
        /// <param name="name">The unique name of the resource</param>
        /// <param name="args">The arguments used to populate this resource's properties</param>
        /// <param name="options">A bag of options that control this resource's behavior</param>
        public LoadBalancerService(string name, LoadBalancerServiceArgs args, CustomResourceOptions? options = null)
            : base("hcloud:index/loadBalancerService:LoadBalancerService", name, args ?? new LoadBalancerServiceArgs(), MakeResourceOptions(options, ""))
        {
        }

        private LoadBalancerService(string name, Input<string> id, LoadBalancerServiceState? state = null, CustomResourceOptions? options = null)
            : base("hcloud:index/loadBalancerService:LoadBalancerService", name, state, MakeResourceOptions(options, id))
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
        /// Get an existing LoadBalancerService resource's state with the given name, ID, and optional extra
        /// properties used to qualify the lookup.
        /// </summary>
        ///
        /// <param name="name">The unique name of the resulting resource.</param>
        /// <param name="id">The unique provider ID of the resource to lookup.</param>
        /// <param name="state">Any extra arguments used during the lookup.</param>
        /// <param name="options">A bag of options that control this resource's behavior</param>
        public static LoadBalancerService Get(string name, Input<string> id, LoadBalancerServiceState? state = null, CustomResourceOptions? options = null)
        {
            return new LoadBalancerService(name, id, state, options);
        }
    }

    public sealed class LoadBalancerServiceArgs : Pulumi.ResourceArgs
    {
        [Input("destinationPort")]
        public Input<int>? DestinationPort { get; set; }

        [Input("healthCheck")]
        public Input<Inputs.LoadBalancerServiceHealthCheckArgs>? HealthCheck { get; set; }

        [Input("http")]
        public Input<Inputs.LoadBalancerServiceHttpArgs>? Http { get; set; }

        [Input("listenPort")]
        public Input<int>? ListenPort { get; set; }

        [Input("loadBalancerId", required: true)]
        public Input<string> LoadBalancerId { get; set; } = null!;

        [Input("protocol", required: true)]
        public Input<string> Protocol { get; set; } = null!;

        [Input("proxyprotocol")]
        public Input<bool>? Proxyprotocol { get; set; }

        public LoadBalancerServiceArgs()
        {
        }
    }

    public sealed class LoadBalancerServiceState : Pulumi.ResourceArgs
    {
        [Input("destinationPort")]
        public Input<int>? DestinationPort { get; set; }

        [Input("healthCheck")]
        public Input<Inputs.LoadBalancerServiceHealthCheckGetArgs>? HealthCheck { get; set; }

        [Input("http")]
        public Input<Inputs.LoadBalancerServiceHttpGetArgs>? Http { get; set; }

        [Input("listenPort")]
        public Input<int>? ListenPort { get; set; }

        [Input("loadBalancerId")]
        public Input<string>? LoadBalancerId { get; set; }

        [Input("protocol")]
        public Input<string>? Protocol { get; set; }

        [Input("proxyprotocol")]
        public Input<bool>? Proxyprotocol { get; set; }

        public LoadBalancerServiceState()
        {
        }
    }
}

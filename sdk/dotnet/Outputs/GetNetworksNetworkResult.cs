// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.HCloud.Outputs
{

    [OutputType]
    public sealed class GetNetworksNetworkResult
    {
        public readonly bool DeleteProtection;
        public readonly int Id;
        public readonly string? IpRange;
        public readonly ImmutableDictionary<string, object>? Labels;
        public readonly string? Name;

        [OutputConstructor]
        private GetNetworksNetworkResult(
            bool deleteProtection,

            int id,

            string? ipRange,

            ImmutableDictionary<string, object>? labels,

            string? name)
        {
            DeleteProtection = deleteProtection;
            Id = id;
            IpRange = ipRange;
            Labels = labels;
            Name = name;
        }
    }
}

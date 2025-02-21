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
    public sealed class GetDatacentersDatacenterResult
    {
        public readonly ImmutableArray<int> AvailableServerTypeIds;
        public readonly string Description;
        public readonly int Id;
        public readonly ImmutableDictionary<string, object> Location;
        public readonly string Name;
        public readonly ImmutableArray<int> SupportedServerTypeIds;

        [OutputConstructor]
        private GetDatacentersDatacenterResult(
            ImmutableArray<int> availableServerTypeIds,

            string description,

            int id,

            ImmutableDictionary<string, object> location,

            string name,

            ImmutableArray<int> supportedServerTypeIds)
        {
            AvailableServerTypeIds = availableServerTypeIds;
            Description = description;
            Id = id;
            Location = location;
            Name = name;
            SupportedServerTypeIds = supportedServerTypeIds;
        }
    }
}

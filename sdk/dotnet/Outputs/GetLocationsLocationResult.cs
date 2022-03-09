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
    public sealed class GetLocationsLocationResult
    {
        public readonly string City;
        public readonly string Country;
        public readonly string Description;
        public readonly int Id;
        public readonly double Latitude;
        public readonly double Longitude;
        public readonly string Name;
        public readonly string NetworkZone;

        [OutputConstructor]
        private GetLocationsLocationResult(
            string city,

            string country,

            string description,

            int id,

            double latitude,

            double longitude,

            string name,

            string networkZone)
        {
            City = city;
            Country = country;
            Description = description;
            Id = id;
            Latitude = latitude;
            Longitude = longitude;
            Name = name;
            NetworkZone = networkZone;
        }
    }
}

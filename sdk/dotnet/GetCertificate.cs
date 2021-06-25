// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.HCloud
{
    public static class GetCertificate
    {
        /// <summary>
        /// Provides details about a specific Hetzner Cloud Certificate.
        /// 
        /// ```csharp
        /// using Pulumi;
        /// using HCloud = Pulumi.HCloud;
        /// 
        /// class MyStack : Stack
        /// {
        ///     public MyStack()
        ///     {
        ///         var sampleCertificate1 = Output.Create(HCloud.GetCertificate.InvokeAsync(new HCloud.GetCertificateArgs
        ///         {
        ///             Name = "sample-certificate-1",
        ///         }));
        ///         var sampleCertificate2 = Output.Create(HCloud.GetCertificate.InvokeAsync(new HCloud.GetCertificateArgs
        ///         {
        ///             Id = 4711,
        ///         }));
        ///     }
        /// 
        /// }
        /// ```
        /// </summary>
        public static Task<GetCertificateResult> InvokeAsync(GetCertificateArgs? args = null, InvokeOptions? options = null)
            => Pulumi.Deployment.Instance.InvokeAsync<GetCertificateResult>("hcloud:index/getCertificate:getCertificate", args ?? new GetCertificateArgs(), options.WithVersion());
    }


    public sealed class GetCertificateArgs : Pulumi.InvokeArgs
    {
        /// <summary>
        /// ID of the certificate.
        /// </summary>
        [Input("id")]
        public int? Id { get; set; }

        /// <summary>
        /// Name of the certificate.
        /// </summary>
        [Input("name")]
        public string? Name { get; set; }

        /// <summary>
        /// [Label selector](https://docs.hetzner.cloud/#overview-label-selector)
        /// </summary>
        [Input("withSelector")]
        public string? WithSelector { get; set; }

        public GetCertificateArgs()
        {
        }
    }


    [OutputType]
    public sealed class GetCertificateResult
    {
        /// <summary>
        /// (string) PEM encoded TLS certificate.
        /// </summary>
        public readonly string Certificate;
        /// <summary>
        /// (string) Point in time when the Certificate was created at Hetzner Cloud (in ISO-8601 format).
        /// </summary>
        public readonly string Created;
        /// <summary>
        /// (list) Domains and subdomains covered by the certificate.
        /// </summary>
        public readonly ImmutableArray<string> DomainNames;
        /// <summary>
        /// (string) Fingerprint of the certificate.
        /// </summary>
        public readonly string Fingerprint;
        /// <summary>
        /// (int) Unique ID of the certificate.
        /// </summary>
        public readonly int Id;
        /// <summary>
        /// (map) User-defined labels (key-value pairs) assigned to the certificate.
        /// </summary>
        public readonly ImmutableDictionary<string, object> Labels;
        /// <summary>
        /// (string) Name of the Certificate.
        /// </summary>
        public readonly string? Name;
        /// <summary>
        /// (string) Point in time when the Certificate stops being valid (in ISO-8601 format).
        /// </summary>
        public readonly string NotValidAfter;
        /// <summary>
        /// (string) Point in time when the Certificate becomes valid (in ISO-8601 format).
        /// </summary>
        public readonly string NotValidBefore;
        public readonly string Type;
        public readonly string? WithSelector;

        [OutputConstructor]
        private GetCertificateResult(
            string certificate,

            string created,

            ImmutableArray<string> domainNames,

            string fingerprint,

            int id,

            ImmutableDictionary<string, object> labels,

            string? name,

            string notValidAfter,

            string notValidBefore,

            string type,

            string? withSelector)
        {
            Certificate = certificate;
            Created = created;
            DomainNames = domainNames;
            Fingerprint = fingerprint;
            Id = id;
            Labels = labels;
            Name = name;
            NotValidAfter = notValidAfter;
            NotValidBefore = notValidBefore;
            Type = type;
            WithSelector = withSelector;
        }
    }
}

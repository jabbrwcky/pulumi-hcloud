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
    /// Provides a Hetzner Clould Certificate to represent a TLS certificate in the Hetzner Cloud.
    /// </summary>
    public partial class Certificate : Pulumi.CustomResource
    {
        /// <summary>
        /// PEM encoded TLS certificate.
        /// </summary>
        [Output("certificate")]
        public Output<string> CertificateContents { get; private set; } = null!;

        /// <summary>
        /// (string) Point in time when the Certificate was created at Hetzner Cloud (in ISO-8601 format).
        /// </summary>
        [Output("created")]
        public Output<string> Created { get; private set; } = null!;

        /// <summary>
        /// (list) Domains and subdomains covered by the certificate.
        /// </summary>
        [Output("domainNames")]
        public Output<ImmutableArray<string>> DomainNames { get; private set; } = null!;

        /// <summary>
        /// (string) Fingerprint of the certificate.
        /// </summary>
        [Output("fingerprint")]
        public Output<string> Fingerprint { get; private set; } = null!;

        /// <summary>
        /// User-defined labels (key-value pairs) the
        /// certificate should be created with.
        /// </summary>
        [Output("labels")]
        public Output<ImmutableDictionary<string, object>?> Labels { get; private set; } = null!;

        /// <summary>
        /// Name of the Certificate.
        /// </summary>
        [Output("name")]
        public Output<string> Name { get; private set; } = null!;

        /// <summary>
        /// (string) Point in time when the Certificate stops being valid (in ISO-8601 format).
        /// </summary>
        [Output("notValidAfter")]
        public Output<string> NotValidAfter { get; private set; } = null!;

        /// <summary>
        /// (string) Point in time when the Certificate becomes valid (in ISO-8601 format).
        /// </summary>
        [Output("notValidBefore")]
        public Output<string> NotValidBefore { get; private set; } = null!;

        /// <summary>
        /// PEM encoded private key belonging to the certificate.
        /// </summary>
        [Output("privateKey")]
        public Output<string> PrivateKey { get; private set; } = null!;


        /// <summary>
        /// Create a Certificate resource with the given unique name, arguments, and options.
        /// </summary>
        ///
        /// <param name="name">The unique name of the resource</param>
        /// <param name="args">The arguments used to populate this resource's properties</param>
        /// <param name="options">A bag of options that control this resource's behavior</param>
        public Certificate(string name, CertificateArgs args, CustomResourceOptions? options = null)
            : base("hcloud:index/certificate:Certificate", name, args ?? new CertificateArgs(), MakeResourceOptions(options, ""))
        {
        }

        private Certificate(string name, Input<string> id, CertificateState? state = null, CustomResourceOptions? options = null)
            : base("hcloud:index/certificate:Certificate", name, state, MakeResourceOptions(options, id))
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
        /// Get an existing Certificate resource's state with the given name, ID, and optional extra
        /// properties used to qualify the lookup.
        /// </summary>
        ///
        /// <param name="name">The unique name of the resulting resource.</param>
        /// <param name="id">The unique provider ID of the resource to lookup.</param>
        /// <param name="state">Any extra arguments used during the lookup.</param>
        /// <param name="options">A bag of options that control this resource's behavior</param>
        public static Certificate Get(string name, Input<string> id, CertificateState? state = null, CustomResourceOptions? options = null)
        {
            return new Certificate(name, id, state, options);
        }
    }

    public sealed class CertificateArgs : Pulumi.ResourceArgs
    {
        /// <summary>
        /// PEM encoded TLS certificate.
        /// </summary>
        [Input("certificate", required: true)]
        public Input<string> CertificateContents { get; set; } = null!;

        [Input("labels")]
        private InputMap<object>? _labels;

        /// <summary>
        /// User-defined labels (key-value pairs) the
        /// certificate should be created with.
        /// </summary>
        public InputMap<object> Labels
        {
            get => _labels ?? (_labels = new InputMap<object>());
            set => _labels = value;
        }

        /// <summary>
        /// Name of the Certificate.
        /// </summary>
        [Input("name")]
        public Input<string>? Name { get; set; }

        /// <summary>
        /// PEM encoded private key belonging to the certificate.
        /// </summary>
        [Input("privateKey", required: true)]
        public Input<string> PrivateKey { get; set; } = null!;

        public CertificateArgs()
        {
        }
    }

    public sealed class CertificateState : Pulumi.ResourceArgs
    {
        /// <summary>
        /// PEM encoded TLS certificate.
        /// </summary>
        [Input("certificate")]
        public Input<string>? CertificateContents { get; set; }

        /// <summary>
        /// (string) Point in time when the Certificate was created at Hetzner Cloud (in ISO-8601 format).
        /// </summary>
        [Input("created")]
        public Input<string>? Created { get; set; }

        [Input("domainNames")]
        private InputList<string>? _domainNames;

        /// <summary>
        /// (list) Domains and subdomains covered by the certificate.
        /// </summary>
        public InputList<string> DomainNames
        {
            get => _domainNames ?? (_domainNames = new InputList<string>());
            set => _domainNames = value;
        }

        /// <summary>
        /// (string) Fingerprint of the certificate.
        /// </summary>
        [Input("fingerprint")]
        public Input<string>? Fingerprint { get; set; }

        [Input("labels")]
        private InputMap<object>? _labels;

        /// <summary>
        /// User-defined labels (key-value pairs) the
        /// certificate should be created with.
        /// </summary>
        public InputMap<object> Labels
        {
            get => _labels ?? (_labels = new InputMap<object>());
            set => _labels = value;
        }

        /// <summary>
        /// Name of the Certificate.
        /// </summary>
        [Input("name")]
        public Input<string>? Name { get; set; }

        /// <summary>
        /// (string) Point in time when the Certificate stops being valid (in ISO-8601 format).
        /// </summary>
        [Input("notValidAfter")]
        public Input<string>? NotValidAfter { get; set; }

        /// <summary>
        /// (string) Point in time when the Certificate becomes valid (in ISO-8601 format).
        /// </summary>
        [Input("notValidBefore")]
        public Input<string>? NotValidBefore { get; set; }

        /// <summary>
        /// PEM encoded private key belonging to the certificate.
        /// </summary>
        [Input("privateKey")]
        public Input<string>? PrivateKey { get; set; }

        public CertificateState()
        {
        }
    }
}

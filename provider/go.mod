module github.com/pulumi/pulumi-hcloud/provider

go 1.14

replace github.com/Azure/go-autorest => github.com/Azure/go-autorest v12.4.3+incompatible

require (
	github.com/hashicorp/terraform-plugin-sdk v1.9.1
	github.com/pulumi/pulumi-terraform-bridge/v2 v2.5.0
	github.com/pulumi/pulumi/sdk/v2 v2.4.0
	github.com/terraform-providers/terraform-provider-hcloud v1.16.0
)

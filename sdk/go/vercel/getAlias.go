// Code generated by the Pulumi Terraform Bridge (tfgen) Tool DO NOT EDIT.
// *** WARNING: Do not edit by hand unless you're certain you know what you are doing! ***

package vercel

import (
	"context"
	"reflect"

	"github.com/pulumi/pulumi/sdk/v3/go/pulumi"
	"github.com/pulumi/pulumi/sdk/v3/go/pulumix"
	"github.com/pulumiverse/pulumi-vercel/sdk/go/vercel/internal"
)

// Provides information about an existing Alias resource.
//
// An Alias allows a `Deployment` to be accessed through a different URL.
func LookupAlias(ctx *pulumi.Context, args *LookupAliasArgs, opts ...pulumi.InvokeOption) (*LookupAliasResult, error) {
	opts = internal.PkgInvokeDefaultOpts(opts)
	var rv LookupAliasResult
	err := ctx.Invoke("vercel:index/getAlias:getAlias", args, &rv, opts...)
	if err != nil {
		return nil, err
	}
	return &rv, nil
}

// A collection of arguments for invoking getAlias.
type LookupAliasArgs struct {
	// The Alias or Alias ID to be retrieved.
	Alias string `pulumi:"alias"`
	// The ID of the team the Alias and Deployment exist under. Required when configuring a team resource if a default team has not been set in the provider.
	TeamId *string `pulumi:"teamId"`
}

// A collection of values returned by getAlias.
type LookupAliasResult struct {
	// The Alias or Alias ID to be retrieved.
	Alias string `pulumi:"alias"`
	// The ID of the Deployment the Alias is associated with.
	DeploymentId string `pulumi:"deploymentId"`
	// The ID of this resource.
	Id string `pulumi:"id"`
	// The ID of the team the Alias and Deployment exist under. Required when configuring a team resource if a default team has not been set in the provider.
	TeamId string `pulumi:"teamId"`
}

func LookupAliasOutput(ctx *pulumi.Context, args LookupAliasOutputArgs, opts ...pulumi.InvokeOption) LookupAliasResultOutput {
	return pulumi.ToOutputWithContext(context.Background(), args).
		ApplyT(func(v interface{}) (LookupAliasResult, error) {
			args := v.(LookupAliasArgs)
			r, err := LookupAlias(ctx, &args, opts...)
			var s LookupAliasResult
			if r != nil {
				s = *r
			}
			return s, err
		}).(LookupAliasResultOutput)
}

// A collection of arguments for invoking getAlias.
type LookupAliasOutputArgs struct {
	// The Alias or Alias ID to be retrieved.
	Alias pulumi.StringInput `pulumi:"alias"`
	// The ID of the team the Alias and Deployment exist under. Required when configuring a team resource if a default team has not been set in the provider.
	TeamId pulumi.StringPtrInput `pulumi:"teamId"`
}

func (LookupAliasOutputArgs) ElementType() reflect.Type {
	return reflect.TypeOf((*LookupAliasArgs)(nil)).Elem()
}

// A collection of values returned by getAlias.
type LookupAliasResultOutput struct{ *pulumi.OutputState }

func (LookupAliasResultOutput) ElementType() reflect.Type {
	return reflect.TypeOf((*LookupAliasResult)(nil)).Elem()
}

func (o LookupAliasResultOutput) ToLookupAliasResultOutput() LookupAliasResultOutput {
	return o
}

func (o LookupAliasResultOutput) ToLookupAliasResultOutputWithContext(ctx context.Context) LookupAliasResultOutput {
	return o
}

func (o LookupAliasResultOutput) ToOutput(ctx context.Context) pulumix.Output[LookupAliasResult] {
	return pulumix.Output[LookupAliasResult]{
		OutputState: o.OutputState,
	}
}

// The Alias or Alias ID to be retrieved.
func (o LookupAliasResultOutput) Alias() pulumi.StringOutput {
	return o.ApplyT(func(v LookupAliasResult) string { return v.Alias }).(pulumi.StringOutput)
}

// The ID of the Deployment the Alias is associated with.
func (o LookupAliasResultOutput) DeploymentId() pulumi.StringOutput {
	return o.ApplyT(func(v LookupAliasResult) string { return v.DeploymentId }).(pulumi.StringOutput)
}

// The ID of this resource.
func (o LookupAliasResultOutput) Id() pulumi.StringOutput {
	return o.ApplyT(func(v LookupAliasResult) string { return v.Id }).(pulumi.StringOutput)
}

// The ID of the team the Alias and Deployment exist under. Required when configuring a team resource if a default team has not been set in the provider.
func (o LookupAliasResultOutput) TeamId() pulumi.StringOutput {
	return o.ApplyT(func(v LookupAliasResult) string { return v.TeamId }).(pulumi.StringOutput)
}

func init() {
	pulumi.RegisterOutputType(LookupAliasResultOutput{})
}

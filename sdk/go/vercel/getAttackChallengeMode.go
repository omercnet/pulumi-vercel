// Code generated by the Pulumi Terraform Bridge (tfgen) Tool DO NOT EDIT.
// *** WARNING: Do not edit by hand unless you're certain you know what you are doing! ***

package vercel

import (
	"context"
	"reflect"

	"github.com/pulumi/pulumi/sdk/v3/go/pulumi"
	"github.com/pulumiverse/pulumi-vercel/sdk/go/vercel/internal"
)

// Provides an Attack Challenge Mode resource.
//
// Attack Challenge Mode prevent malicious traffic by showing a verification challenge for every visitor.
//
// ## Example Usage
//
// ```go
// package main
//
// import (
//
//	"github.com/pulumi/pulumi/sdk/v3/go/pulumi"
//	"github.com/pulumiverse/pulumi-vercel/sdk/go/vercel"
//
// )
//
//	func main() {
//		pulumi.Run(func(ctx *pulumi.Context) error {
//			_, err := vercel.LookupAttackChallengeMode(ctx, &vercel.LookupAttackChallengeModeArgs{
//				ProjectId: vercel_project.Example.Id,
//			}, nil)
//			if err != nil {
//				return err
//			}
//			return nil
//		})
//	}
//
// ```
func LookupAttackChallengeMode(ctx *pulumi.Context, args *LookupAttackChallengeModeArgs, opts ...pulumi.InvokeOption) (*LookupAttackChallengeModeResult, error) {
	opts = internal.PkgInvokeDefaultOpts(opts)
	var rv LookupAttackChallengeModeResult
	err := ctx.Invoke("vercel:index/getAttackChallengeMode:getAttackChallengeMode", args, &rv, opts...)
	if err != nil {
		return nil, err
	}
	return &rv, nil
}

// A collection of arguments for invoking getAttackChallengeMode.
type LookupAttackChallengeModeArgs struct {
	// The ID of the Project to adjust the CPU for.
	ProjectId string `pulumi:"projectId"`
	// The ID of the team the Project exists under. Required when configuring a team resource if a default team has not been set in the provider.
	TeamId *string `pulumi:"teamId"`
}

// A collection of values returned by getAttackChallengeMode.
type LookupAttackChallengeModeResult struct {
	// Whether Attack Challenge Mode is enabled or not.
	Enabled bool `pulumi:"enabled"`
	// The resource identifier.
	Id string `pulumi:"id"`
	// The ID of the Project to adjust the CPU for.
	ProjectId string `pulumi:"projectId"`
	// The ID of the team the Project exists under. Required when configuring a team resource if a default team has not been set in the provider.
	TeamId string `pulumi:"teamId"`
}

func LookupAttackChallengeModeOutput(ctx *pulumi.Context, args LookupAttackChallengeModeOutputArgs, opts ...pulumi.InvokeOption) LookupAttackChallengeModeResultOutput {
	return pulumi.ToOutputWithContext(context.Background(), args).
		ApplyT(func(v interface{}) (LookupAttackChallengeModeResult, error) {
			args := v.(LookupAttackChallengeModeArgs)
			r, err := LookupAttackChallengeMode(ctx, &args, opts...)
			var s LookupAttackChallengeModeResult
			if r != nil {
				s = *r
			}
			return s, err
		}).(LookupAttackChallengeModeResultOutput)
}

// A collection of arguments for invoking getAttackChallengeMode.
type LookupAttackChallengeModeOutputArgs struct {
	// The ID of the Project to adjust the CPU for.
	ProjectId pulumi.StringInput `pulumi:"projectId"`
	// The ID of the team the Project exists under. Required when configuring a team resource if a default team has not been set in the provider.
	TeamId pulumi.StringPtrInput `pulumi:"teamId"`
}

func (LookupAttackChallengeModeOutputArgs) ElementType() reflect.Type {
	return reflect.TypeOf((*LookupAttackChallengeModeArgs)(nil)).Elem()
}

// A collection of values returned by getAttackChallengeMode.
type LookupAttackChallengeModeResultOutput struct{ *pulumi.OutputState }

func (LookupAttackChallengeModeResultOutput) ElementType() reflect.Type {
	return reflect.TypeOf((*LookupAttackChallengeModeResult)(nil)).Elem()
}

func (o LookupAttackChallengeModeResultOutput) ToLookupAttackChallengeModeResultOutput() LookupAttackChallengeModeResultOutput {
	return o
}

func (o LookupAttackChallengeModeResultOutput) ToLookupAttackChallengeModeResultOutputWithContext(ctx context.Context) LookupAttackChallengeModeResultOutput {
	return o
}

// Whether Attack Challenge Mode is enabled or not.
func (o LookupAttackChallengeModeResultOutput) Enabled() pulumi.BoolOutput {
	return o.ApplyT(func(v LookupAttackChallengeModeResult) bool { return v.Enabled }).(pulumi.BoolOutput)
}

// The resource identifier.
func (o LookupAttackChallengeModeResultOutput) Id() pulumi.StringOutput {
	return o.ApplyT(func(v LookupAttackChallengeModeResult) string { return v.Id }).(pulumi.StringOutput)
}

// The ID of the Project to adjust the CPU for.
func (o LookupAttackChallengeModeResultOutput) ProjectId() pulumi.StringOutput {
	return o.ApplyT(func(v LookupAttackChallengeModeResult) string { return v.ProjectId }).(pulumi.StringOutput)
}

// The ID of the team the Project exists under. Required when configuring a team resource if a default team has not been set in the provider.
func (o LookupAttackChallengeModeResultOutput) TeamId() pulumi.StringOutput {
	return o.ApplyT(func(v LookupAttackChallengeModeResult) string { return v.TeamId }).(pulumi.StringOutput)
}

func init() {
	pulumi.RegisterOutputType(LookupAttackChallengeModeResultOutput{})
}

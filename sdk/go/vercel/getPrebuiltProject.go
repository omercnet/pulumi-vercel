// Code generated by the Pulumi Terraform Bridge (tfgen) Tool DO NOT EDIT.
// *** WARNING: Do not edit by hand unless you're certain you know what you are doing! ***

package vercel

import (
	"context"
	"reflect"

	"github.com/pulumi/pulumi/sdk/v3/go/pulumi"
	"github.com/pulumiverse/pulumi-vercel/sdk/go/vercel/internal"
)

func GetPrebuiltProject(ctx *pulumi.Context, args *GetPrebuiltProjectArgs, opts ...pulumi.InvokeOption) (*GetPrebuiltProjectResult, error) {
	opts = internal.PkgInvokeDefaultOpts(opts)
	var rv GetPrebuiltProjectResult
	err := ctx.Invoke("vercel:index/getPrebuiltProject:getPrebuiltProject", args, &rv, opts...)
	if err != nil {
		return nil, err
	}
	return &rv, nil
}

// A collection of arguments for invoking getPrebuiltProject.
type GetPrebuiltProjectArgs struct {
	Path string `pulumi:"path"`
}

// A collection of values returned by getPrebuiltProject.
type GetPrebuiltProjectResult struct {
	Id     string            `pulumi:"id"`
	Output map[string]string `pulumi:"output"`
	Path   string            `pulumi:"path"`
}

func GetPrebuiltProjectOutput(ctx *pulumi.Context, args GetPrebuiltProjectOutputArgs, opts ...pulumi.InvokeOption) GetPrebuiltProjectResultOutput {
	return pulumi.ToOutputWithContext(context.Background(), args).
		ApplyT(func(v interface{}) (GetPrebuiltProjectResult, error) {
			args := v.(GetPrebuiltProjectArgs)
			r, err := GetPrebuiltProject(ctx, &args, opts...)
			var s GetPrebuiltProjectResult
			if r != nil {
				s = *r
			}
			return s, err
		}).(GetPrebuiltProjectResultOutput)
}

// A collection of arguments for invoking getPrebuiltProject.
type GetPrebuiltProjectOutputArgs struct {
	Path pulumi.StringInput `pulumi:"path"`
}

func (GetPrebuiltProjectOutputArgs) ElementType() reflect.Type {
	return reflect.TypeOf((*GetPrebuiltProjectArgs)(nil)).Elem()
}

// A collection of values returned by getPrebuiltProject.
type GetPrebuiltProjectResultOutput struct{ *pulumi.OutputState }

func (GetPrebuiltProjectResultOutput) ElementType() reflect.Type {
	return reflect.TypeOf((*GetPrebuiltProjectResult)(nil)).Elem()
}

func (o GetPrebuiltProjectResultOutput) ToGetPrebuiltProjectResultOutput() GetPrebuiltProjectResultOutput {
	return o
}

func (o GetPrebuiltProjectResultOutput) ToGetPrebuiltProjectResultOutputWithContext(ctx context.Context) GetPrebuiltProjectResultOutput {
	return o
}

func (o GetPrebuiltProjectResultOutput) Id() pulumi.StringOutput {
	return o.ApplyT(func(v GetPrebuiltProjectResult) string { return v.Id }).(pulumi.StringOutput)
}

func (o GetPrebuiltProjectResultOutput) Output() pulumi.StringMapOutput {
	return o.ApplyT(func(v GetPrebuiltProjectResult) map[string]string { return v.Output }).(pulumi.StringMapOutput)
}

func (o GetPrebuiltProjectResultOutput) Path() pulumi.StringOutput {
	return o.ApplyT(func(v GetPrebuiltProjectResult) string { return v.Path }).(pulumi.StringOutput)
}

func init() {
	pulumi.RegisterOutputType(GetPrebuiltProjectResultOutput{})
}

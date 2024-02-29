// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;
using Pulumi;

namespace Pulumiverse.Vercel
{
    public static class GetSharedEnvironmentVariable
    {
        /// <summary>
        /// Provides information about an existing Shared Environment Variable within Vercel.
        /// 
        /// A Shared Environment Variable resource defines an Environment Variable that can be shared between multiple Vercel Projects.
        /// 
        /// For more detailed information, please see the [Vercel documentation](https://vercel.com/docs/concepts/projects/environment-variables/shared-environment-variables).
        /// 
        /// {{% examples %}}
        /// ## Example Usage
        /// {{% example %}}
        /// 
        /// ```csharp
        /// using System.Collections.Generic;
        /// using System.Linq;
        /// using Pulumi;
        /// using Vercel = Pulumi.Vercel;
        /// 
        /// return await Deployment.RunAsync(() =&gt; 
        /// {
        ///     var example = Vercel.GetSharedEnvironmentVariable.Invoke(new()
        ///     {
        ///         Id = "xxxxxxxxxxxxxxx",
        ///     });
        /// 
        ///     var exampleByKeyAndTarget = Vercel.GetSharedEnvironmentVariable.Invoke(new()
        ///     {
        ///         Key = "MY_ENV_VAR",
        ///         Targets = new[]
        ///         {
        ///             "production",
        ///             "preview",
        ///         },
        ///     });
        /// 
        /// });
        /// ```
        /// {{% /example %}}
        /// {{% /examples %}}
        /// </summary>
        public static Task<GetSharedEnvironmentVariableResult> InvokeAsync(GetSharedEnvironmentVariableArgs? args = null, InvokeOptions? options = null)
            => global::Pulumi.Deployment.Instance.InvokeAsync<GetSharedEnvironmentVariableResult>("vercel:index/getSharedEnvironmentVariable:getSharedEnvironmentVariable", args ?? new GetSharedEnvironmentVariableArgs(), options.WithDefaults());

        /// <summary>
        /// Provides information about an existing Shared Environment Variable within Vercel.
        /// 
        /// A Shared Environment Variable resource defines an Environment Variable that can be shared between multiple Vercel Projects.
        /// 
        /// For more detailed information, please see the [Vercel documentation](https://vercel.com/docs/concepts/projects/environment-variables/shared-environment-variables).
        /// 
        /// {{% examples %}}
        /// ## Example Usage
        /// {{% example %}}
        /// 
        /// ```csharp
        /// using System.Collections.Generic;
        /// using System.Linq;
        /// using Pulumi;
        /// using Vercel = Pulumi.Vercel;
        /// 
        /// return await Deployment.RunAsync(() =&gt; 
        /// {
        ///     var example = Vercel.GetSharedEnvironmentVariable.Invoke(new()
        ///     {
        ///         Id = "xxxxxxxxxxxxxxx",
        ///     });
        /// 
        ///     var exampleByKeyAndTarget = Vercel.GetSharedEnvironmentVariable.Invoke(new()
        ///     {
        ///         Key = "MY_ENV_VAR",
        ///         Targets = new[]
        ///         {
        ///             "production",
        ///             "preview",
        ///         },
        ///     });
        /// 
        /// });
        /// ```
        /// {{% /example %}}
        /// {{% /examples %}}
        /// </summary>
        public static Output<GetSharedEnvironmentVariableResult> Invoke(GetSharedEnvironmentVariableInvokeArgs? args = null, InvokeOptions? options = null)
            => global::Pulumi.Deployment.Instance.Invoke<GetSharedEnvironmentVariableResult>("vercel:index/getSharedEnvironmentVariable:getSharedEnvironmentVariable", args ?? new GetSharedEnvironmentVariableInvokeArgs(), options.WithDefaults());
    }


    public sealed class GetSharedEnvironmentVariableArgs : global::Pulumi.InvokeArgs
    {
        /// <summary>
        /// The ID of the Environment Variable.
        /// </summary>
        [Input("id")]
        public string? Id { get; set; }

        /// <summary>
        /// The name of the Environment Variable.
        /// </summary>
        [Input("key")]
        public string? Key { get; set; }

        [Input("targets")]
        private List<string>? _targets;

        /// <summary>
        /// The environments that the Environment Variable should be present on. Valid targets are either `production`, `preview`, or `development`.
        /// </summary>
        public List<string> Targets
        {
            get => _targets ?? (_targets = new List<string>());
            set => _targets = value;
        }

        /// <summary>
        /// The ID of the Vercel team. Shared environment variables require a team.
        /// </summary>
        [Input("teamId")]
        public string? TeamId { get; set; }

        public GetSharedEnvironmentVariableArgs()
        {
        }
        public static new GetSharedEnvironmentVariableArgs Empty => new GetSharedEnvironmentVariableArgs();
    }

    public sealed class GetSharedEnvironmentVariableInvokeArgs : global::Pulumi.InvokeArgs
    {
        /// <summary>
        /// The ID of the Environment Variable.
        /// </summary>
        [Input("id")]
        public Input<string>? Id { get; set; }

        /// <summary>
        /// The name of the Environment Variable.
        /// </summary>
        [Input("key")]
        public Input<string>? Key { get; set; }

        [Input("targets")]
        private InputList<string>? _targets;

        /// <summary>
        /// The environments that the Environment Variable should be present on. Valid targets are either `production`, `preview`, or `development`.
        /// </summary>
        public InputList<string> Targets
        {
            get => _targets ?? (_targets = new InputList<string>());
            set => _targets = value;
        }

        /// <summary>
        /// The ID of the Vercel team. Shared environment variables require a team.
        /// </summary>
        [Input("teamId")]
        public Input<string>? TeamId { get; set; }

        public GetSharedEnvironmentVariableInvokeArgs()
        {
        }
        public static new GetSharedEnvironmentVariableInvokeArgs Empty => new GetSharedEnvironmentVariableInvokeArgs();
    }


    [OutputType]
    public sealed class GetSharedEnvironmentVariableResult
    {
        /// <summary>
        /// The ID of the Environment Variable.
        /// </summary>
        public readonly string Id;
        /// <summary>
        /// The name of the Environment Variable.
        /// </summary>
        public readonly string Key;
        /// <summary>
        /// The ID of the Vercel project.
        /// </summary>
        public readonly ImmutableArray<string> ProjectIds;
        /// <summary>
        /// Whether the Environment Variable is sensitive or not.
        /// </summary>
        public readonly bool Sensitive;
        /// <summary>
        /// The environments that the Environment Variable should be present on. Valid targets are either `production`, `preview`, or `development`.
        /// </summary>
        public readonly ImmutableArray<string> Targets;
        /// <summary>
        /// The ID of the Vercel team. Shared environment variables require a team.
        /// </summary>
        public readonly string TeamId;
        /// <summary>
        /// The value of the Environment Variable.
        /// </summary>
        public readonly string Value;

        [OutputConstructor]
        private GetSharedEnvironmentVariableResult(
            string id,

            string key,

            ImmutableArray<string> projectIds,

            bool sensitive,

            ImmutableArray<string> targets,

            string teamId,

            string value)
        {
            Id = id;
            Key = key;
            ProjectIds = projectIds;
            Sensitive = sensitive;
            Targets = targets;
            TeamId = teamId;
            Value = value;
        }
    }
}

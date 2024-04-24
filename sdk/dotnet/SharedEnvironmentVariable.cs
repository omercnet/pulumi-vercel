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
    /// <summary>
    /// Provides a Shared Environment Variable resource.
    /// 
    /// A Shared Environment Variable resource defines an Environment Variable that can be shared between multiple Vercel Projects.
    /// 
    /// For more detailed information, please see the [Vercel documentation](https://vercel.com/docs/concepts/projects/environment-variables/shared-environment-variables).
    /// 
    /// ## Example Usage
    /// 
    /// ```csharp
    /// using System.Collections.Generic;
    /// using System.Linq;
    /// using Pulumi;
    /// using Vercel = Pulumiverse.Vercel;
    /// 
    /// return await Deployment.RunAsync(() =&gt; 
    /// {
    ///     var exampleProject = new Vercel.Project("exampleProject", new()
    ///     {
    ///         GitRepository = new Vercel.Inputs.ProjectGitRepositoryArgs
    ///         {
    ///             Type = "github",
    ///             Repo = "vercel/some-repo",
    ///         },
    ///     });
    /// 
    ///     // A shared environment variable that will be created
    ///     // and associated with the "example" project.
    ///     var exampleSharedEnvironmentVariable = new Vercel.SharedEnvironmentVariable("exampleSharedEnvironmentVariable", new()
    ///     {
    ///         Key = "EXAMPLE",
    ///         Value = "some_value",
    ///         Targets = new[]
    ///         {
    ///             "production",
    ///         },
    ///         ProjectIds = new[]
    ///         {
    ///             exampleProject.Id,
    ///         },
    ///     });
    /// 
    /// });
    /// ```
    /// 
    /// ## Import
    /// 
    /// You can import via the team_id and environment variable id.
    /// 
    /// - team_id can be found in the team `settings` tab in the Vercel UI.
    /// 
    /// - environment variable id can be taken from the network tab inside developer tools, while you are on the project page.
    /// 
    /// # 
    /// 
    /// Note also, that the value field for sensitive environment variables will be imported as `null`.
    /// 
    /// ```sh
    /// $ pulumi import vercel:index/sharedEnvironmentVariable:SharedEnvironmentVariable example team_xxxxxxxxxxxxxxxxxxxxxxxx/env_yyyyyyyyyyyyy
    /// ```
    /// </summary>
    [VercelResourceType("vercel:index/sharedEnvironmentVariable:SharedEnvironmentVariable")]
    public partial class SharedEnvironmentVariable : global::Pulumi.CustomResource
    {
        /// <summary>
        /// The name of the Environment Variable.
        /// </summary>
        [Output("key")]
        public Output<string> Key { get; private set; } = null!;

        /// <summary>
        /// The ID of the Vercel project.
        /// </summary>
        [Output("projectIds")]
        public Output<ImmutableArray<string>> ProjectIds { get; private set; } = null!;

        /// <summary>
        /// Whether the Environment Variable is sensitive or not.
        /// </summary>
        [Output("sensitive")]
        public Output<bool> Sensitive { get; private set; } = null!;

        /// <summary>
        /// The environments that the Environment Variable should be present on. Valid targets are either `production`, `preview`, or `development`.
        /// </summary>
        [Output("targets")]
        public Output<ImmutableArray<string>> Targets { get; private set; } = null!;

        /// <summary>
        /// The ID of the Vercel team. Shared environment variables require a team.
        /// </summary>
        [Output("teamId")]
        public Output<string> TeamId { get; private set; } = null!;

        /// <summary>
        /// The value of the Environment Variable.
        /// </summary>
        [Output("value")]
        public Output<string> Value { get; private set; } = null!;


        /// <summary>
        /// Create a SharedEnvironmentVariable resource with the given unique name, arguments, and options.
        /// </summary>
        ///
        /// <param name="name">The unique name of the resource</param>
        /// <param name="args">The arguments used to populate this resource's properties</param>
        /// <param name="options">A bag of options that control this resource's behavior</param>
        public SharedEnvironmentVariable(string name, SharedEnvironmentVariableArgs args, CustomResourceOptions? options = null)
            : base("vercel:index/sharedEnvironmentVariable:SharedEnvironmentVariable", name, args ?? new SharedEnvironmentVariableArgs(), MakeResourceOptions(options, ""))
        {
        }

        private SharedEnvironmentVariable(string name, Input<string> id, SharedEnvironmentVariableState? state = null, CustomResourceOptions? options = null)
            : base("vercel:index/sharedEnvironmentVariable:SharedEnvironmentVariable", name, state, MakeResourceOptions(options, id))
        {
        }

        private static CustomResourceOptions MakeResourceOptions(CustomResourceOptions? options, Input<string>? id)
        {
            var defaultOptions = new CustomResourceOptions
            {
                Version = Utilities.Version,
                PluginDownloadURL = "github://api.github.com/pulumiverse",
                AdditionalSecretOutputs =
                {
                    "value",
                },
            };
            var merged = CustomResourceOptions.Merge(defaultOptions, options);
            // Override the ID if one was specified for consistency with other language SDKs.
            merged.Id = id ?? merged.Id;
            return merged;
        }
        /// <summary>
        /// Get an existing SharedEnvironmentVariable resource's state with the given name, ID, and optional extra
        /// properties used to qualify the lookup.
        /// </summary>
        ///
        /// <param name="name">The unique name of the resulting resource.</param>
        /// <param name="id">The unique provider ID of the resource to lookup.</param>
        /// <param name="state">Any extra arguments used during the lookup.</param>
        /// <param name="options">A bag of options that control this resource's behavior</param>
        public static SharedEnvironmentVariable Get(string name, Input<string> id, SharedEnvironmentVariableState? state = null, CustomResourceOptions? options = null)
        {
            return new SharedEnvironmentVariable(name, id, state, options);
        }
    }

    public sealed class SharedEnvironmentVariableArgs : global::Pulumi.ResourceArgs
    {
        /// <summary>
        /// The name of the Environment Variable.
        /// </summary>
        [Input("key", required: true)]
        public Input<string> Key { get; set; } = null!;

        [Input("projectIds", required: true)]
        private InputList<string>? _projectIds;

        /// <summary>
        /// The ID of the Vercel project.
        /// </summary>
        public InputList<string> ProjectIds
        {
            get => _projectIds ?? (_projectIds = new InputList<string>());
            set => _projectIds = value;
        }

        /// <summary>
        /// Whether the Environment Variable is sensitive or not.
        /// </summary>
        [Input("sensitive")]
        public Input<bool>? Sensitive { get; set; }

        [Input("targets", required: true)]
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

        [Input("value", required: true)]
        private Input<string>? _value;

        /// <summary>
        /// The value of the Environment Variable.
        /// </summary>
        public Input<string>? Value
        {
            get => _value;
            set
            {
                var emptySecret = Output.CreateSecret(0);
                _value = Output.Tuple<Input<string>?, int>(value, emptySecret).Apply(t => t.Item1);
            }
        }

        public SharedEnvironmentVariableArgs()
        {
        }
        public static new SharedEnvironmentVariableArgs Empty => new SharedEnvironmentVariableArgs();
    }

    public sealed class SharedEnvironmentVariableState : global::Pulumi.ResourceArgs
    {
        /// <summary>
        /// The name of the Environment Variable.
        /// </summary>
        [Input("key")]
        public Input<string>? Key { get; set; }

        [Input("projectIds")]
        private InputList<string>? _projectIds;

        /// <summary>
        /// The ID of the Vercel project.
        /// </summary>
        public InputList<string> ProjectIds
        {
            get => _projectIds ?? (_projectIds = new InputList<string>());
            set => _projectIds = value;
        }

        /// <summary>
        /// Whether the Environment Variable is sensitive or not.
        /// </summary>
        [Input("sensitive")]
        public Input<bool>? Sensitive { get; set; }

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

        [Input("value")]
        private Input<string>? _value;

        /// <summary>
        /// The value of the Environment Variable.
        /// </summary>
        public Input<string>? Value
        {
            get => _value;
            set
            {
                var emptySecret = Output.CreateSecret(0);
                _value = Output.Tuple<Input<string>?, int>(value, emptySecret).Apply(t => t.Item1);
            }
        }

        public SharedEnvironmentVariableState()
        {
        }
        public static new SharedEnvironmentVariableState Empty => new SharedEnvironmentVariableState();
    }
}

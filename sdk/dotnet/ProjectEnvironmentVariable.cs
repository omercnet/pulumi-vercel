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
    /// ## Example Usage
    /// 
    /// &lt;!--Start PulumiCodeChooser --&gt;
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
    ///     // An environment variable that will be created
    ///     // for this project for the "production" environment.
    ///     var exampleProjectEnvironmentVariable = new Vercel.ProjectEnvironmentVariable("exampleProjectEnvironmentVariable", new()
    ///     {
    ///         ProjectId = exampleProject.Id,
    ///         Key = "foo",
    ///         Value = "bar",
    ///         Targets = new[]
    ///         {
    ///             "production",
    ///         },
    ///     });
    /// 
    ///     // An environment variable that will be created
    ///     // for this project for the "preview" environment when the branch is "staging".
    ///     var exampleGitBranch = new Vercel.ProjectEnvironmentVariable("exampleGitBranch", new()
    ///     {
    ///         ProjectId = exampleProject.Id,
    ///         Key = "foo",
    ///         Value = "bar-staging",
    ///         Targets = new[]
    ///         {
    ///             "preview",
    ///         },
    ///         GitBranch = "staging",
    ///     });
    /// 
    ///     // A sensitive environment variable that will be created
    ///     // for this project for the "production" environment.
    ///     var exampleSensitive = new Vercel.ProjectEnvironmentVariable("exampleSensitive", new()
    ///     {
    ///         ProjectId = exampleProject.Id,
    ///         Key = "foo",
    ///         Value = "bar-production",
    ///         Targets = new[]
    ///         {
    ///             "production",
    ///         },
    ///         Sensitive = true,
    ///     });
    /// 
    /// });
    /// ```
    /// &lt;!--End PulumiCodeChooser --&gt;
    /// 
    /// ## Import
    /// 
    /// If importing into a personal account, or with a team configured on
    /// 
    /// the provider, simply use the project_id and environment variable id.
    /// 
    /// - project_id can be found in the project `settings` tab in the Vercel UI.
    /// 
    /// - environment variable id can be taken from the network tab inside developer tools, while you are on the project page,
    /// 
    /// or can be queried from Vercel API directly (https://vercel.com/docs/rest-api/endpoints/projects#retrieve-the-environment-variables-of-a-project-by-id-or-name)
    /// 
    /// # 
    /// 
    /// Note also, that the value field for sensitive environment variables will be imported as `null`.
    /// 
    /// ```sh
    /// $ pulumi import vercel:index/projectEnvironmentVariable:ProjectEnvironmentVariable example prj_xxxxxxxxxxxxxxxxxxxxxxxxxxxx/FdT2e1E5Of6Cihmt
    /// ```
    /// 
    /// Alternatively, you can import via the team_id, project_id and
    /// 
    /// environment variable id.
    /// 
    /// - team_id can be found in the team `settings` tab in the Vercel UI.
    /// 
    /// - project_id can be found in the project `settings` tab in the Vercel UI.
    /// 
    /// - environment variable id can be taken from the network tab inside developer tools, while you are on the project page,
    /// 
    /// or can be queried from Vercel API directly (https://vercel.com/docs/rest-api/endpoints/projects#retrieve-the-environment-variables-of-a-project-by-id-or-name)
    /// 
    /// # 
    /// 
    /// Note also, that the value field for sensitive environment variables will be imported as `null`.
    /// 
    /// ```sh
    /// $ pulumi import vercel:index/projectEnvironmentVariable:ProjectEnvironmentVariable example team_xxxxxxxxxxxxxxxxxxxxxxxx/prj_xxxxxxxxxxxxxxxxxxxxxxxxxxxx/FdT2e1E5Of6Cihmt
    /// ```
    /// </summary>
    [VercelResourceType("vercel:index/projectEnvironmentVariable:ProjectEnvironmentVariable")]
    public partial class ProjectEnvironmentVariable : global::Pulumi.CustomResource
    {
        /// <summary>
        /// The git branch of the Environment Variable.
        /// </summary>
        [Output("gitBranch")]
        public Output<string?> GitBranch { get; private set; } = null!;

        /// <summary>
        /// The name of the Environment Variable.
        /// </summary>
        [Output("key")]
        public Output<string> Key { get; private set; } = null!;

        /// <summary>
        /// The ID of the Vercel project.
        /// </summary>
        [Output("projectId")]
        public Output<string> ProjectId { get; private set; } = null!;

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
        /// The ID of the Vercel team.Required when configuring a team resource if a default team has not been set in the provider.
        /// </summary>
        [Output("teamId")]
        public Output<string> TeamId { get; private set; } = null!;

        /// <summary>
        /// The value of the Environment Variable.
        /// </summary>
        [Output("value")]
        public Output<string> Value { get; private set; } = null!;


        /// <summary>
        /// Create a ProjectEnvironmentVariable resource with the given unique name, arguments, and options.
        /// </summary>
        ///
        /// <param name="name">The unique name of the resource</param>
        /// <param name="args">The arguments used to populate this resource's properties</param>
        /// <param name="options">A bag of options that control this resource's behavior</param>
        public ProjectEnvironmentVariable(string name, ProjectEnvironmentVariableArgs args, CustomResourceOptions? options = null)
            : base("vercel:index/projectEnvironmentVariable:ProjectEnvironmentVariable", name, args ?? new ProjectEnvironmentVariableArgs(), MakeResourceOptions(options, ""))
        {
        }

        private ProjectEnvironmentVariable(string name, Input<string> id, ProjectEnvironmentVariableState? state = null, CustomResourceOptions? options = null)
            : base("vercel:index/projectEnvironmentVariable:ProjectEnvironmentVariable", name, state, MakeResourceOptions(options, id))
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
        /// Get an existing ProjectEnvironmentVariable resource's state with the given name, ID, and optional extra
        /// properties used to qualify the lookup.
        /// </summary>
        ///
        /// <param name="name">The unique name of the resulting resource.</param>
        /// <param name="id">The unique provider ID of the resource to lookup.</param>
        /// <param name="state">Any extra arguments used during the lookup.</param>
        /// <param name="options">A bag of options that control this resource's behavior</param>
        public static ProjectEnvironmentVariable Get(string name, Input<string> id, ProjectEnvironmentVariableState? state = null, CustomResourceOptions? options = null)
        {
            return new ProjectEnvironmentVariable(name, id, state, options);
        }
    }

    public sealed class ProjectEnvironmentVariableArgs : global::Pulumi.ResourceArgs
    {
        /// <summary>
        /// The git branch of the Environment Variable.
        /// </summary>
        [Input("gitBranch")]
        public Input<string>? GitBranch { get; set; }

        /// <summary>
        /// The name of the Environment Variable.
        /// </summary>
        [Input("key", required: true)]
        public Input<string> Key { get; set; } = null!;

        /// <summary>
        /// The ID of the Vercel project.
        /// </summary>
        [Input("projectId", required: true)]
        public Input<string> ProjectId { get; set; } = null!;

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
        /// The ID of the Vercel team.Required when configuring a team resource if a default team has not been set in the provider.
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

        public ProjectEnvironmentVariableArgs()
        {
        }
        public static new ProjectEnvironmentVariableArgs Empty => new ProjectEnvironmentVariableArgs();
    }

    public sealed class ProjectEnvironmentVariableState : global::Pulumi.ResourceArgs
    {
        /// <summary>
        /// The git branch of the Environment Variable.
        /// </summary>
        [Input("gitBranch")]
        public Input<string>? GitBranch { get; set; }

        /// <summary>
        /// The name of the Environment Variable.
        /// </summary>
        [Input("key")]
        public Input<string>? Key { get; set; }

        /// <summary>
        /// The ID of the Vercel project.
        /// </summary>
        [Input("projectId")]
        public Input<string>? ProjectId { get; set; }

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
        /// The ID of the Vercel team.Required when configuring a team resource if a default team has not been set in the provider.
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

        public ProjectEnvironmentVariableState()
        {
        }
        public static new ProjectEnvironmentVariableState Empty => new ProjectEnvironmentVariableState();
    }
}

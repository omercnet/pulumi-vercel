// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;
using Pulumi;

namespace Pulumiverse.Vercel.Outputs
{

    [OutputType]
    public sealed class FirewallConfigRulesRule
    {
        /// <summary>
        /// Actions to take when the condition groups match a request
        /// </summary>
        public readonly Outputs.FirewallConfigRulesRuleAction Action;
        /// <summary>
        /// Rule is active or disabled
        /// </summary>
        public readonly bool? Active;
        /// <summary>
        /// Sets of conditions that may match a request
        /// </summary>
        public readonly ImmutableArray<Outputs.FirewallConfigRulesRuleConditionGroup> ConditionGroups;
        public readonly string? Description;
        public readonly string? Id;
        /// <summary>
        /// Name to identify the rule
        /// </summary>
        public readonly string Name;

        [OutputConstructor]
        private FirewallConfigRulesRule(
            Outputs.FirewallConfigRulesRuleAction action,

            bool? active,

            ImmutableArray<Outputs.FirewallConfigRulesRuleConditionGroup> conditionGroups,

            string? description,

            string? id,

            string name)
        {
            Action = action;
            Active = active;
            ConditionGroups = conditionGroups;
            Description = description;
            Id = id;
            Name = name;
        }
    }
}

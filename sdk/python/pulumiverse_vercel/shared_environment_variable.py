# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import copy
import warnings
import pulumi
import pulumi.runtime
from typing import Any, Callable, Mapping, Optional, Sequence, Union, overload
from . import _utilities

__all__ = ['SharedEnvironmentVariableArgs', 'SharedEnvironmentVariable']

@pulumi.input_type
class SharedEnvironmentVariableArgs:
    def __init__(__self__, *,
                 key: pulumi.Input[str],
                 project_ids: pulumi.Input[Sequence[pulumi.Input[str]]],
                 targets: pulumi.Input[Sequence[pulumi.Input[str]]],
                 value: pulumi.Input[str],
                 team_id: Optional[pulumi.Input[str]] = None):
        """
        The set of arguments for constructing a SharedEnvironmentVariable resource.
        :param pulumi.Input[str] key: The name of the Environment Variable.
        :param pulumi.Input[Sequence[pulumi.Input[str]]] project_ids: The ID of the Vercel project.
        :param pulumi.Input[Sequence[pulumi.Input[str]]] targets: The environments that the Environment Variable should be present on. Valid targets are either `production`, `preview`, or `development`.
        :param pulumi.Input[str] value: The value of the Environment Variable.
        :param pulumi.Input[str] team_id: The ID of the Vercel team. Shared environment variables require a team.
        """
        SharedEnvironmentVariableArgs._configure(
            lambda key, value: pulumi.set(__self__, key, value),
            key=key,
            project_ids=project_ids,
            targets=targets,
            value=value,
            team_id=team_id,
        )
    @staticmethod
    def _configure(
             _setter: Callable[[Any, Any], None],
             key: pulumi.Input[str],
             project_ids: pulumi.Input[Sequence[pulumi.Input[str]]],
             targets: pulumi.Input[Sequence[pulumi.Input[str]]],
             value: pulumi.Input[str],
             team_id: Optional[pulumi.Input[str]] = None,
             opts: Optional[pulumi.ResourceOptions]=None):
        _setter("key", key)
        _setter("project_ids", project_ids)
        _setter("targets", targets)
        _setter("value", value)
        if team_id is not None:
            _setter("team_id", team_id)

    @property
    @pulumi.getter
    def key(self) -> pulumi.Input[str]:
        """
        The name of the Environment Variable.
        """
        return pulumi.get(self, "key")

    @key.setter
    def key(self, value: pulumi.Input[str]):
        pulumi.set(self, "key", value)

    @property
    @pulumi.getter(name="projectIds")
    def project_ids(self) -> pulumi.Input[Sequence[pulumi.Input[str]]]:
        """
        The ID of the Vercel project.
        """
        return pulumi.get(self, "project_ids")

    @project_ids.setter
    def project_ids(self, value: pulumi.Input[Sequence[pulumi.Input[str]]]):
        pulumi.set(self, "project_ids", value)

    @property
    @pulumi.getter
    def targets(self) -> pulumi.Input[Sequence[pulumi.Input[str]]]:
        """
        The environments that the Environment Variable should be present on. Valid targets are either `production`, `preview`, or `development`.
        """
        return pulumi.get(self, "targets")

    @targets.setter
    def targets(self, value: pulumi.Input[Sequence[pulumi.Input[str]]]):
        pulumi.set(self, "targets", value)

    @property
    @pulumi.getter
    def value(self) -> pulumi.Input[str]:
        """
        The value of the Environment Variable.
        """
        return pulumi.get(self, "value")

    @value.setter
    def value(self, value: pulumi.Input[str]):
        pulumi.set(self, "value", value)

    @property
    @pulumi.getter(name="teamId")
    def team_id(self) -> Optional[pulumi.Input[str]]:
        """
        The ID of the Vercel team. Shared environment variables require a team.
        """
        return pulumi.get(self, "team_id")

    @team_id.setter
    def team_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "team_id", value)


@pulumi.input_type
class _SharedEnvironmentVariableState:
    def __init__(__self__, *,
                 key: Optional[pulumi.Input[str]] = None,
                 project_ids: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 targets: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 team_id: Optional[pulumi.Input[str]] = None,
                 value: Optional[pulumi.Input[str]] = None):
        """
        Input properties used for looking up and filtering SharedEnvironmentVariable resources.
        :param pulumi.Input[str] key: The name of the Environment Variable.
        :param pulumi.Input[Sequence[pulumi.Input[str]]] project_ids: The ID of the Vercel project.
        :param pulumi.Input[Sequence[pulumi.Input[str]]] targets: The environments that the Environment Variable should be present on. Valid targets are either `production`, `preview`, or `development`.
        :param pulumi.Input[str] team_id: The ID of the Vercel team. Shared environment variables require a team.
        :param pulumi.Input[str] value: The value of the Environment Variable.
        """
        _SharedEnvironmentVariableState._configure(
            lambda key, value: pulumi.set(__self__, key, value),
            key=key,
            project_ids=project_ids,
            targets=targets,
            team_id=team_id,
            value=value,
        )
    @staticmethod
    def _configure(
             _setter: Callable[[Any, Any], None],
             key: Optional[pulumi.Input[str]] = None,
             project_ids: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
             targets: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
             team_id: Optional[pulumi.Input[str]] = None,
             value: Optional[pulumi.Input[str]] = None,
             opts: Optional[pulumi.ResourceOptions]=None):
        if key is not None:
            _setter("key", key)
        if project_ids is not None:
            _setter("project_ids", project_ids)
        if targets is not None:
            _setter("targets", targets)
        if team_id is not None:
            _setter("team_id", team_id)
        if value is not None:
            _setter("value", value)

    @property
    @pulumi.getter
    def key(self) -> Optional[pulumi.Input[str]]:
        """
        The name of the Environment Variable.
        """
        return pulumi.get(self, "key")

    @key.setter
    def key(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "key", value)

    @property
    @pulumi.getter(name="projectIds")
    def project_ids(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]:
        """
        The ID of the Vercel project.
        """
        return pulumi.get(self, "project_ids")

    @project_ids.setter
    def project_ids(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]):
        pulumi.set(self, "project_ids", value)

    @property
    @pulumi.getter
    def targets(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]:
        """
        The environments that the Environment Variable should be present on. Valid targets are either `production`, `preview`, or `development`.
        """
        return pulumi.get(self, "targets")

    @targets.setter
    def targets(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]):
        pulumi.set(self, "targets", value)

    @property
    @pulumi.getter(name="teamId")
    def team_id(self) -> Optional[pulumi.Input[str]]:
        """
        The ID of the Vercel team. Shared environment variables require a team.
        """
        return pulumi.get(self, "team_id")

    @team_id.setter
    def team_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "team_id", value)

    @property
    @pulumi.getter
    def value(self) -> Optional[pulumi.Input[str]]:
        """
        The value of the Environment Variable.
        """
        return pulumi.get(self, "value")

    @value.setter
    def value(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "value", value)


class SharedEnvironmentVariable(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 key: Optional[pulumi.Input[str]] = None,
                 project_ids: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 targets: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 team_id: Optional[pulumi.Input[str]] = None,
                 value: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        """
        Provides a Shared Environment Variable resource.

        A Shared Environment Variable resource defines an Environment Variable that can be shared between multiple Vercel Projects.

        For more detailed information, please see the [Vercel documentation](https://vercel.com/docs/concepts/projects/environment-variables/shared-environment-variables).

        ## Example Usage

        ```python
        import pulumi
        import pulumiverse_vercel as vercel

        example_project = vercel.Project("exampleProject", git_repository=vercel.ProjectGitRepositoryArgs(
            type="github",
            repo="vercel/some-repo",
        ))
        # A shared environment variable that will be created
        # and associated with the "example" project.
        example_shared_environment_variable = vercel.SharedEnvironmentVariable("exampleSharedEnvironmentVariable",
            key="EXAMPLE",
            value="some_value",
            targets=["production"],
            project_ids=[example_project.id])
        ```

        ## Import

        You can import via the team_id and environment variable id. - team_id can be found in the team `settings` tab in the Vercel UI. - environment variable id can be taken from the network tab on the shared environment variable page.

        ```sh
         $ pulumi import vercel:index/sharedEnvironmentVariable:SharedEnvironmentVariable example team_xxxxxxxxxxxxxxxxxxxxxxxx/env_yyyyyyyyyyyyy
        ```

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] key: The name of the Environment Variable.
        :param pulumi.Input[Sequence[pulumi.Input[str]]] project_ids: The ID of the Vercel project.
        :param pulumi.Input[Sequence[pulumi.Input[str]]] targets: The environments that the Environment Variable should be present on. Valid targets are either `production`, `preview`, or `development`.
        :param pulumi.Input[str] team_id: The ID of the Vercel team. Shared environment variables require a team.
        :param pulumi.Input[str] value: The value of the Environment Variable.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: SharedEnvironmentVariableArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        Provides a Shared Environment Variable resource.

        A Shared Environment Variable resource defines an Environment Variable that can be shared between multiple Vercel Projects.

        For more detailed information, please see the [Vercel documentation](https://vercel.com/docs/concepts/projects/environment-variables/shared-environment-variables).

        ## Example Usage

        ```python
        import pulumi
        import pulumiverse_vercel as vercel

        example_project = vercel.Project("exampleProject", git_repository=vercel.ProjectGitRepositoryArgs(
            type="github",
            repo="vercel/some-repo",
        ))
        # A shared environment variable that will be created
        # and associated with the "example" project.
        example_shared_environment_variable = vercel.SharedEnvironmentVariable("exampleSharedEnvironmentVariable",
            key="EXAMPLE",
            value="some_value",
            targets=["production"],
            project_ids=[example_project.id])
        ```

        ## Import

        You can import via the team_id and environment variable id. - team_id can be found in the team `settings` tab in the Vercel UI. - environment variable id can be taken from the network tab on the shared environment variable page.

        ```sh
         $ pulumi import vercel:index/sharedEnvironmentVariable:SharedEnvironmentVariable example team_xxxxxxxxxxxxxxxxxxxxxxxx/env_yyyyyyyyyyyyy
        ```

        :param str resource_name: The name of the resource.
        :param SharedEnvironmentVariableArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(SharedEnvironmentVariableArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            kwargs = kwargs or {}
            def _setter(key, value):
                kwargs[key] = value
            SharedEnvironmentVariableArgs._configure(_setter, **kwargs)
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 key: Optional[pulumi.Input[str]] = None,
                 project_ids: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 targets: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 team_id: Optional[pulumi.Input[str]] = None,
                 value: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = SharedEnvironmentVariableArgs.__new__(SharedEnvironmentVariableArgs)

            if key is None and not opts.urn:
                raise TypeError("Missing required property 'key'")
            __props__.__dict__["key"] = key
            if project_ids is None and not opts.urn:
                raise TypeError("Missing required property 'project_ids'")
            __props__.__dict__["project_ids"] = project_ids
            if targets is None and not opts.urn:
                raise TypeError("Missing required property 'targets'")
            __props__.__dict__["targets"] = targets
            __props__.__dict__["team_id"] = team_id
            if value is None and not opts.urn:
                raise TypeError("Missing required property 'value'")
            __props__.__dict__["value"] = None if value is None else pulumi.Output.secret(value)
        secret_opts = pulumi.ResourceOptions(additional_secret_outputs=["value"])
        opts = pulumi.ResourceOptions.merge(opts, secret_opts)
        super(SharedEnvironmentVariable, __self__).__init__(
            'vercel:index/sharedEnvironmentVariable:SharedEnvironmentVariable',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None,
            key: Optional[pulumi.Input[str]] = None,
            project_ids: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
            targets: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
            team_id: Optional[pulumi.Input[str]] = None,
            value: Optional[pulumi.Input[str]] = None) -> 'SharedEnvironmentVariable':
        """
        Get an existing SharedEnvironmentVariable resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] key: The name of the Environment Variable.
        :param pulumi.Input[Sequence[pulumi.Input[str]]] project_ids: The ID of the Vercel project.
        :param pulumi.Input[Sequence[pulumi.Input[str]]] targets: The environments that the Environment Variable should be present on. Valid targets are either `production`, `preview`, or `development`.
        :param pulumi.Input[str] team_id: The ID of the Vercel team. Shared environment variables require a team.
        :param pulumi.Input[str] value: The value of the Environment Variable.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = _SharedEnvironmentVariableState.__new__(_SharedEnvironmentVariableState)

        __props__.__dict__["key"] = key
        __props__.__dict__["project_ids"] = project_ids
        __props__.__dict__["targets"] = targets
        __props__.__dict__["team_id"] = team_id
        __props__.__dict__["value"] = value
        return SharedEnvironmentVariable(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter
    def key(self) -> pulumi.Output[str]:
        """
        The name of the Environment Variable.
        """
        return pulumi.get(self, "key")

    @property
    @pulumi.getter(name="projectIds")
    def project_ids(self) -> pulumi.Output[Sequence[str]]:
        """
        The ID of the Vercel project.
        """
        return pulumi.get(self, "project_ids")

    @property
    @pulumi.getter
    def targets(self) -> pulumi.Output[Sequence[str]]:
        """
        The environments that the Environment Variable should be present on. Valid targets are either `production`, `preview`, or `development`.
        """
        return pulumi.get(self, "targets")

    @property
    @pulumi.getter(name="teamId")
    def team_id(self) -> pulumi.Output[str]:
        """
        The ID of the Vercel team. Shared environment variables require a team.
        """
        return pulumi.get(self, "team_id")

    @property
    @pulumi.getter
    def value(self) -> pulumi.Output[str]:
        """
        The value of the Environment Variable.
        """
        return pulumi.get(self, "value")


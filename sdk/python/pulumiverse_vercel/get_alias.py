# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import copy
import warnings
import sys
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
if sys.version_info >= (3, 11):
    from typing import NotRequired, TypedDict, TypeAlias
else:
    from typing_extensions import NotRequired, TypedDict, TypeAlias
from . import _utilities

__all__ = [
    'GetAliasResult',
    'AwaitableGetAliasResult',
    'get_alias',
    'get_alias_output',
]

@pulumi.output_type
class GetAliasResult:
    """
    A collection of values returned by getAlias.
    """
    def __init__(__self__, alias=None, deployment_id=None, id=None, team_id=None):
        if alias and not isinstance(alias, str):
            raise TypeError("Expected argument 'alias' to be a str")
        pulumi.set(__self__, "alias", alias)
        if deployment_id and not isinstance(deployment_id, str):
            raise TypeError("Expected argument 'deployment_id' to be a str")
        pulumi.set(__self__, "deployment_id", deployment_id)
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        pulumi.set(__self__, "id", id)
        if team_id and not isinstance(team_id, str):
            raise TypeError("Expected argument 'team_id' to be a str")
        pulumi.set(__self__, "team_id", team_id)

    @property
    @pulumi.getter
    def alias(self) -> str:
        """
        The Alias or Alias ID to be retrieved.
        """
        return pulumi.get(self, "alias")

    @property
    @pulumi.getter(name="deploymentId")
    def deployment_id(self) -> str:
        """
        The ID of the Deployment the Alias is associated with.
        """
        return pulumi.get(self, "deployment_id")

    @property
    @pulumi.getter
    def id(self) -> str:
        """
        The ID of this resource.
        """
        return pulumi.get(self, "id")

    @property
    @pulumi.getter(name="teamId")
    def team_id(self) -> str:
        """
        The ID of the team the Alias and Deployment exist under. Required when configuring a team resource if a default team has not been set in the provider.
        """
        return pulumi.get(self, "team_id")


class AwaitableGetAliasResult(GetAliasResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetAliasResult(
            alias=self.alias,
            deployment_id=self.deployment_id,
            id=self.id,
            team_id=self.team_id)


def get_alias(alias: Optional[str] = None,
              team_id: Optional[str] = None,
              opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetAliasResult:
    """
    Provides information about an existing Alias resource.

    An Alias allows a `Deployment` to be accessed through a different URL.


    :param str alias: The Alias or Alias ID to be retrieved.
    :param str team_id: The ID of the team the Alias and Deployment exist under. Required when configuring a team resource if a default team has not been set in the provider.
    """
    __args__ = dict()
    __args__['alias'] = alias
    __args__['teamId'] = team_id
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('vercel:index/getAlias:getAlias', __args__, opts=opts, typ=GetAliasResult).value

    return AwaitableGetAliasResult(
        alias=pulumi.get(__ret__, 'alias'),
        deployment_id=pulumi.get(__ret__, 'deployment_id'),
        id=pulumi.get(__ret__, 'id'),
        team_id=pulumi.get(__ret__, 'team_id'))
def get_alias_output(alias: Optional[pulumi.Input[str]] = None,
                     team_id: Optional[pulumi.Input[Optional[str]]] = None,
                     opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetAliasResult]:
    """
    Provides information about an existing Alias resource.

    An Alias allows a `Deployment` to be accessed through a different URL.


    :param str alias: The Alias or Alias ID to be retrieved.
    :param str team_id: The ID of the team the Alias and Deployment exist under. Required when configuring a team resource if a default team has not been set in the provider.
    """
    __args__ = dict()
    __args__['alias'] = alias
    __args__['teamId'] = team_id
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke_output('vercel:index/getAlias:getAlias', __args__, opts=opts, typ=GetAliasResult)
    return __ret__.apply(lambda __response__: GetAliasResult(
        alias=pulumi.get(__response__, 'alias'),
        deployment_id=pulumi.get(__response__, 'deployment_id'),
        id=pulumi.get(__response__, 'id'),
        team_id=pulumi.get(__response__, 'team_id')))

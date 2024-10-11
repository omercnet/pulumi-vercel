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
    'GetEdgeConfigTokenResult',
    'AwaitableGetEdgeConfigTokenResult',
    'get_edge_config_token',
    'get_edge_config_token_output',
]

@pulumi.output_type
class GetEdgeConfigTokenResult:
    """
    A collection of values returned by getEdgeConfigToken.
    """
    def __init__(__self__, connection_string=None, edge_config_id=None, id=None, label=None, team_id=None, token=None):
        if connection_string and not isinstance(connection_string, str):
            raise TypeError("Expected argument 'connection_string' to be a str")
        pulumi.set(__self__, "connection_string", connection_string)
        if edge_config_id and not isinstance(edge_config_id, str):
            raise TypeError("Expected argument 'edge_config_id' to be a str")
        pulumi.set(__self__, "edge_config_id", edge_config_id)
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        pulumi.set(__self__, "id", id)
        if label and not isinstance(label, str):
            raise TypeError("Expected argument 'label' to be a str")
        pulumi.set(__self__, "label", label)
        if team_id and not isinstance(team_id, str):
            raise TypeError("Expected argument 'team_id' to be a str")
        pulumi.set(__self__, "team_id", team_id)
        if token and not isinstance(token, str):
            raise TypeError("Expected argument 'token' to be a str")
        pulumi.set(__self__, "token", token)

    @property
    @pulumi.getter(name="connectionString")
    def connection_string(self) -> str:
        """
        A connection string is a URL that connects a project to an Edge Config. The variable can be called anything, but our Edge Config client SDK will search for process.env.EDGE_CONFIG by default.
        """
        return pulumi.get(self, "connection_string")

    @property
    @pulumi.getter(name="edgeConfigId")
    def edge_config_id(self) -> str:
        """
        The label of the Edge Config Token.
        """
        return pulumi.get(self, "edge_config_id")

    @property
    @pulumi.getter
    def id(self) -> str:
        """
        The ID of this resource.
        """
        return pulumi.get(self, "id")

    @property
    @pulumi.getter
    def label(self) -> str:
        """
        The label of the Edge Config Token.
        """
        return pulumi.get(self, "label")

    @property
    @pulumi.getter(name="teamId")
    def team_id(self) -> str:
        """
        The ID of the team the Edge Config should exist under. Required when configuring a team resource if a default team has not been set in the provider.
        """
        return pulumi.get(self, "team_id")

    @property
    @pulumi.getter
    def token(self) -> str:
        """
        A read access token used for authenticating against the Edge Config's endpoint for high volume, low-latency requests.
        """
        return pulumi.get(self, "token")


class AwaitableGetEdgeConfigTokenResult(GetEdgeConfigTokenResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetEdgeConfigTokenResult(
            connection_string=self.connection_string,
            edge_config_id=self.edge_config_id,
            id=self.id,
            label=self.label,
            team_id=self.team_id,
            token=self.token)


def get_edge_config_token(edge_config_id: Optional[str] = None,
                          team_id: Optional[str] = None,
                          token: Optional[str] = None,
                          opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetEdgeConfigTokenResult:
    """
    Provides information about an existing Edge Config Token.

    An Edge Config is a global data store that enables experimentation with feature flags, A/B testing, critical redirects, and more.

    An Edge Config token is used to authenticate against an Edge Config's endpoint.

    ## Example Usage

    ```python
    import pulumi
    import pulumi_vercel as vercel

    test = vercel.get_edge_config_token(edge_config_id="ecfg_xxxxxxxxxxxxxxxxxxxxxxxxxxxx",
        token="xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx")
    ```


    :param str edge_config_id: The label of the Edge Config Token.
    :param str team_id: The ID of the team the Edge Config should exist under. Required when configuring a team resource if a default team has not been set in the provider.
    :param str token: A read access token used for authenticating against the Edge Config's endpoint for high volume, low-latency requests.
    """
    __args__ = dict()
    __args__['edgeConfigId'] = edge_config_id
    __args__['teamId'] = team_id
    __args__['token'] = token
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('vercel:index/getEdgeConfigToken:getEdgeConfigToken', __args__, opts=opts, typ=GetEdgeConfigTokenResult).value

    return AwaitableGetEdgeConfigTokenResult(
        connection_string=pulumi.get(__ret__, 'connection_string'),
        edge_config_id=pulumi.get(__ret__, 'edge_config_id'),
        id=pulumi.get(__ret__, 'id'),
        label=pulumi.get(__ret__, 'label'),
        team_id=pulumi.get(__ret__, 'team_id'),
        token=pulumi.get(__ret__, 'token'))
def get_edge_config_token_output(edge_config_id: Optional[pulumi.Input[str]] = None,
                                 team_id: Optional[pulumi.Input[Optional[str]]] = None,
                                 token: Optional[pulumi.Input[str]] = None,
                                 opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetEdgeConfigTokenResult]:
    """
    Provides information about an existing Edge Config Token.

    An Edge Config is a global data store that enables experimentation with feature flags, A/B testing, critical redirects, and more.

    An Edge Config token is used to authenticate against an Edge Config's endpoint.

    ## Example Usage

    ```python
    import pulumi
    import pulumi_vercel as vercel

    test = vercel.get_edge_config_token(edge_config_id="ecfg_xxxxxxxxxxxxxxxxxxxxxxxxxxxx",
        token="xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx")
    ```


    :param str edge_config_id: The label of the Edge Config Token.
    :param str team_id: The ID of the team the Edge Config should exist under. Required when configuring a team resource if a default team has not been set in the provider.
    :param str token: A read access token used for authenticating against the Edge Config's endpoint for high volume, low-latency requests.
    """
    __args__ = dict()
    __args__['edgeConfigId'] = edge_config_id
    __args__['teamId'] = team_id
    __args__['token'] = token
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke_output('vercel:index/getEdgeConfigToken:getEdgeConfigToken', __args__, opts=opts, typ=GetEdgeConfigTokenResult)
    return __ret__.apply(lambda __response__: GetEdgeConfigTokenResult(
        connection_string=pulumi.get(__response__, 'connection_string'),
        edge_config_id=pulumi.get(__response__, 'edge_config_id'),
        id=pulumi.get(__response__, 'id'),
        label=pulumi.get(__response__, 'label'),
        team_id=pulumi.get(__response__, 'team_id'),
        token=pulumi.get(__response__, 'token')))

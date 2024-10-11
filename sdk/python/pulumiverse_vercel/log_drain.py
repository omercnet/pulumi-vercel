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

__all__ = ['LogDrainArgs', 'LogDrain']

@pulumi.input_type
class LogDrainArgs:
    def __init__(__self__, *,
                 delivery_format: pulumi.Input[str],
                 endpoint: pulumi.Input[str],
                 environments: pulumi.Input[Sequence[pulumi.Input[str]]],
                 sources: pulumi.Input[Sequence[pulumi.Input[str]]],
                 headers: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
                 project_ids: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 sampling_rate: Optional[pulumi.Input[float]] = None,
                 secret: Optional[pulumi.Input[str]] = None,
                 team_id: Optional[pulumi.Input[str]] = None):
        """
        The set of arguments for constructing a LogDrain resource.
        :param pulumi.Input[str] delivery_format: The format log data should be delivered in. Can be `json` or `ndjson`.
        :param pulumi.Input[str] endpoint: Logs will be sent as POST requests to this URL. The endpoint will be verified, and must return a `200` status code and an `x-vercel-verify` header taken from the endpoint_verification data source. The value the `x-vercel-verify` header should be can be read from the `vercel_endpoint_verification_code` data source.
        :param pulumi.Input[Sequence[pulumi.Input[str]]] environments: Logs from the selected environments will be forwarded to your webhook. At least one must be present.
        :param pulumi.Input[Sequence[pulumi.Input[str]]] sources: A set of sources that the log drain should send logs for. Valid values are `static`, `edge`, `external`, `build` and `lambda`.
        :param pulumi.Input[Mapping[str, pulumi.Input[str]]] headers: Custom headers to include in requests to the log drain endpoint.
        :param pulumi.Input[Sequence[pulumi.Input[str]]] project_ids: A list of project IDs that the log drain should be associated with. Logs from these projects will be sent log events to the specified endpoint. If omitted, logs will be sent for all projects.
        :param pulumi.Input[float] sampling_rate: A ratio of logs matching the sampling rate will be sent to your log drain. Should be a value between 0 and 1. If unspecified, all logs are sent.
        :param pulumi.Input[str] secret: A custom secret to be used for signing log events. You can use this secret to verify that log events are coming from Vercel and are not tampered with. See https://vercel.com/docs/observability/log-drains/log-drains-reference#secure-log-drains for full info.
        :param pulumi.Input[str] team_id: The ID of the team the Log Drain should exist under. Required when configuring a team resource if a default team has not been set in the provider.
        """
        pulumi.set(__self__, "delivery_format", delivery_format)
        pulumi.set(__self__, "endpoint", endpoint)
        pulumi.set(__self__, "environments", environments)
        pulumi.set(__self__, "sources", sources)
        if headers is not None:
            pulumi.set(__self__, "headers", headers)
        if project_ids is not None:
            pulumi.set(__self__, "project_ids", project_ids)
        if sampling_rate is not None:
            pulumi.set(__self__, "sampling_rate", sampling_rate)
        if secret is not None:
            pulumi.set(__self__, "secret", secret)
        if team_id is not None:
            pulumi.set(__self__, "team_id", team_id)

    @property
    @pulumi.getter(name="deliveryFormat")
    def delivery_format(self) -> pulumi.Input[str]:
        """
        The format log data should be delivered in. Can be `json` or `ndjson`.
        """
        return pulumi.get(self, "delivery_format")

    @delivery_format.setter
    def delivery_format(self, value: pulumi.Input[str]):
        pulumi.set(self, "delivery_format", value)

    @property
    @pulumi.getter
    def endpoint(self) -> pulumi.Input[str]:
        """
        Logs will be sent as POST requests to this URL. The endpoint will be verified, and must return a `200` status code and an `x-vercel-verify` header taken from the endpoint_verification data source. The value the `x-vercel-verify` header should be can be read from the `vercel_endpoint_verification_code` data source.
        """
        return pulumi.get(self, "endpoint")

    @endpoint.setter
    def endpoint(self, value: pulumi.Input[str]):
        pulumi.set(self, "endpoint", value)

    @property
    @pulumi.getter
    def environments(self) -> pulumi.Input[Sequence[pulumi.Input[str]]]:
        """
        Logs from the selected environments will be forwarded to your webhook. At least one must be present.
        """
        return pulumi.get(self, "environments")

    @environments.setter
    def environments(self, value: pulumi.Input[Sequence[pulumi.Input[str]]]):
        pulumi.set(self, "environments", value)

    @property
    @pulumi.getter
    def sources(self) -> pulumi.Input[Sequence[pulumi.Input[str]]]:
        """
        A set of sources that the log drain should send logs for. Valid values are `static`, `edge`, `external`, `build` and `lambda`.
        """
        return pulumi.get(self, "sources")

    @sources.setter
    def sources(self, value: pulumi.Input[Sequence[pulumi.Input[str]]]):
        pulumi.set(self, "sources", value)

    @property
    @pulumi.getter
    def headers(self) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]]:
        """
        Custom headers to include in requests to the log drain endpoint.
        """
        return pulumi.get(self, "headers")

    @headers.setter
    def headers(self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]]):
        pulumi.set(self, "headers", value)

    @property
    @pulumi.getter(name="projectIds")
    def project_ids(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]:
        """
        A list of project IDs that the log drain should be associated with. Logs from these projects will be sent log events to the specified endpoint. If omitted, logs will be sent for all projects.
        """
        return pulumi.get(self, "project_ids")

    @project_ids.setter
    def project_ids(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]):
        pulumi.set(self, "project_ids", value)

    @property
    @pulumi.getter(name="samplingRate")
    def sampling_rate(self) -> Optional[pulumi.Input[float]]:
        """
        A ratio of logs matching the sampling rate will be sent to your log drain. Should be a value between 0 and 1. If unspecified, all logs are sent.
        """
        return pulumi.get(self, "sampling_rate")

    @sampling_rate.setter
    def sampling_rate(self, value: Optional[pulumi.Input[float]]):
        pulumi.set(self, "sampling_rate", value)

    @property
    @pulumi.getter
    def secret(self) -> Optional[pulumi.Input[str]]:
        """
        A custom secret to be used for signing log events. You can use this secret to verify that log events are coming from Vercel and are not tampered with. See https://vercel.com/docs/observability/log-drains/log-drains-reference#secure-log-drains for full info.
        """
        return pulumi.get(self, "secret")

    @secret.setter
    def secret(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "secret", value)

    @property
    @pulumi.getter(name="teamId")
    def team_id(self) -> Optional[pulumi.Input[str]]:
        """
        The ID of the team the Log Drain should exist under. Required when configuring a team resource if a default team has not been set in the provider.
        """
        return pulumi.get(self, "team_id")

    @team_id.setter
    def team_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "team_id", value)


@pulumi.input_type
class _LogDrainState:
    def __init__(__self__, *,
                 delivery_format: Optional[pulumi.Input[str]] = None,
                 endpoint: Optional[pulumi.Input[str]] = None,
                 environments: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 headers: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
                 project_ids: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 sampling_rate: Optional[pulumi.Input[float]] = None,
                 secret: Optional[pulumi.Input[str]] = None,
                 sources: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 team_id: Optional[pulumi.Input[str]] = None):
        """
        Input properties used for looking up and filtering LogDrain resources.
        :param pulumi.Input[str] delivery_format: The format log data should be delivered in. Can be `json` or `ndjson`.
        :param pulumi.Input[str] endpoint: Logs will be sent as POST requests to this URL. The endpoint will be verified, and must return a `200` status code and an `x-vercel-verify` header taken from the endpoint_verification data source. The value the `x-vercel-verify` header should be can be read from the `vercel_endpoint_verification_code` data source.
        :param pulumi.Input[Sequence[pulumi.Input[str]]] environments: Logs from the selected environments will be forwarded to your webhook. At least one must be present.
        :param pulumi.Input[Mapping[str, pulumi.Input[str]]] headers: Custom headers to include in requests to the log drain endpoint.
        :param pulumi.Input[Sequence[pulumi.Input[str]]] project_ids: A list of project IDs that the log drain should be associated with. Logs from these projects will be sent log events to the specified endpoint. If omitted, logs will be sent for all projects.
        :param pulumi.Input[float] sampling_rate: A ratio of logs matching the sampling rate will be sent to your log drain. Should be a value between 0 and 1. If unspecified, all logs are sent.
        :param pulumi.Input[str] secret: A custom secret to be used for signing log events. You can use this secret to verify that log events are coming from Vercel and are not tampered with. See https://vercel.com/docs/observability/log-drains/log-drains-reference#secure-log-drains for full info.
        :param pulumi.Input[Sequence[pulumi.Input[str]]] sources: A set of sources that the log drain should send logs for. Valid values are `static`, `edge`, `external`, `build` and `lambda`.
        :param pulumi.Input[str] team_id: The ID of the team the Log Drain should exist under. Required when configuring a team resource if a default team has not been set in the provider.
        """
        if delivery_format is not None:
            pulumi.set(__self__, "delivery_format", delivery_format)
        if endpoint is not None:
            pulumi.set(__self__, "endpoint", endpoint)
        if environments is not None:
            pulumi.set(__self__, "environments", environments)
        if headers is not None:
            pulumi.set(__self__, "headers", headers)
        if project_ids is not None:
            pulumi.set(__self__, "project_ids", project_ids)
        if sampling_rate is not None:
            pulumi.set(__self__, "sampling_rate", sampling_rate)
        if secret is not None:
            pulumi.set(__self__, "secret", secret)
        if sources is not None:
            pulumi.set(__self__, "sources", sources)
        if team_id is not None:
            pulumi.set(__self__, "team_id", team_id)

    @property
    @pulumi.getter(name="deliveryFormat")
    def delivery_format(self) -> Optional[pulumi.Input[str]]:
        """
        The format log data should be delivered in. Can be `json` or `ndjson`.
        """
        return pulumi.get(self, "delivery_format")

    @delivery_format.setter
    def delivery_format(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "delivery_format", value)

    @property
    @pulumi.getter
    def endpoint(self) -> Optional[pulumi.Input[str]]:
        """
        Logs will be sent as POST requests to this URL. The endpoint will be verified, and must return a `200` status code and an `x-vercel-verify` header taken from the endpoint_verification data source. The value the `x-vercel-verify` header should be can be read from the `vercel_endpoint_verification_code` data source.
        """
        return pulumi.get(self, "endpoint")

    @endpoint.setter
    def endpoint(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "endpoint", value)

    @property
    @pulumi.getter
    def environments(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]:
        """
        Logs from the selected environments will be forwarded to your webhook. At least one must be present.
        """
        return pulumi.get(self, "environments")

    @environments.setter
    def environments(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]):
        pulumi.set(self, "environments", value)

    @property
    @pulumi.getter
    def headers(self) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]]:
        """
        Custom headers to include in requests to the log drain endpoint.
        """
        return pulumi.get(self, "headers")

    @headers.setter
    def headers(self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]]):
        pulumi.set(self, "headers", value)

    @property
    @pulumi.getter(name="projectIds")
    def project_ids(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]:
        """
        A list of project IDs that the log drain should be associated with. Logs from these projects will be sent log events to the specified endpoint. If omitted, logs will be sent for all projects.
        """
        return pulumi.get(self, "project_ids")

    @project_ids.setter
    def project_ids(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]):
        pulumi.set(self, "project_ids", value)

    @property
    @pulumi.getter(name="samplingRate")
    def sampling_rate(self) -> Optional[pulumi.Input[float]]:
        """
        A ratio of logs matching the sampling rate will be sent to your log drain. Should be a value between 0 and 1. If unspecified, all logs are sent.
        """
        return pulumi.get(self, "sampling_rate")

    @sampling_rate.setter
    def sampling_rate(self, value: Optional[pulumi.Input[float]]):
        pulumi.set(self, "sampling_rate", value)

    @property
    @pulumi.getter
    def secret(self) -> Optional[pulumi.Input[str]]:
        """
        A custom secret to be used for signing log events. You can use this secret to verify that log events are coming from Vercel and are not tampered with. See https://vercel.com/docs/observability/log-drains/log-drains-reference#secure-log-drains for full info.
        """
        return pulumi.get(self, "secret")

    @secret.setter
    def secret(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "secret", value)

    @property
    @pulumi.getter
    def sources(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]:
        """
        A set of sources that the log drain should send logs for. Valid values are `static`, `edge`, `external`, `build` and `lambda`.
        """
        return pulumi.get(self, "sources")

    @sources.setter
    def sources(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]):
        pulumi.set(self, "sources", value)

    @property
    @pulumi.getter(name="teamId")
    def team_id(self) -> Optional[pulumi.Input[str]]:
        """
        The ID of the team the Log Drain should exist under. Required when configuring a team resource if a default team has not been set in the provider.
        """
        return pulumi.get(self, "team_id")

    @team_id.setter
    def team_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "team_id", value)


class LogDrain(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 delivery_format: Optional[pulumi.Input[str]] = None,
                 endpoint: Optional[pulumi.Input[str]] = None,
                 environments: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 headers: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
                 project_ids: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 sampling_rate: Optional[pulumi.Input[float]] = None,
                 secret: Optional[pulumi.Input[str]] = None,
                 sources: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 team_id: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        """
        Provides a Configurable Log Drain resource.

        > For Log Drain integrations, please see the [Integration Log Drain docs](https://vercel.com/docs/observability/log-drains#log-drains-integration).

        Log Drains collect all of your logs using a service specializing in storing app logs.

        Teams on Pro and Enterprise plans can subscribe to log drains that are generic and configurable from the Vercel dashboard without creating an integration. This allows you to use a HTTP service to receive logs through Vercel's log drains.

        > Only Pro and Enterprise teams can create Configurable Log Drains.

        ## Example Usage

        ```python
        import pulumi
        import pulumi_vercel as vercel
        import pulumiverse_vercel as vercel

        example_endpoint_verification = vercel.get_endpoint_verification()
        example_project = vercel.Project("exampleProject")
        example_log_drain = vercel.LogDrain("exampleLogDrain",
            delivery_format="json",
            environments=["production"],
            headers={
                "some-key": "some-value",
            },
            project_ids=[example_project.id],
            sampling_rate=0.8,
            secret="a_very_long_and_very_well_specified_secret",
            sources=["static"],
            endpoint="https://example.com/my-log-drain-endpoint")
        ```

        ## Import

        If importing into a personal account, or with a team configured on

        the provider, simply use the log_drain_id.

        - log_drain_id can be found by querying the Vercel REST API (https://vercel.com/docs/rest-api/endpoints/logDrains#retrieves-a-list-of-all-the-log-drains).

        ```sh
        $ pulumi import vercel:index/logDrain:LogDrain example ecfg_xxxxxxxxxxxxxxxxxxxxxxxxxxxx/xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx
        ```

        Alternatively, you can import via the team_id and edge_config_id.

        - team_id can be found in the team `settings` tab in the Vercel UI.

        - log_drain_id can be found by querying the Vercel REST API (https://vercel.com/docs/rest-api/endpoints/logDrains#retrieves-a-list-of-all-the-log-drains).

        ```sh
        $ pulumi import vercel:index/logDrain:LogDrain example team_xxxxxxxxxxxxxxxxxxxxxxxx/ecfg_xxxxxxxxxxxxxxxxxxxxxxxxxxxx/xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx
        ```

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] delivery_format: The format log data should be delivered in. Can be `json` or `ndjson`.
        :param pulumi.Input[str] endpoint: Logs will be sent as POST requests to this URL. The endpoint will be verified, and must return a `200` status code and an `x-vercel-verify` header taken from the endpoint_verification data source. The value the `x-vercel-verify` header should be can be read from the `vercel_endpoint_verification_code` data source.
        :param pulumi.Input[Sequence[pulumi.Input[str]]] environments: Logs from the selected environments will be forwarded to your webhook. At least one must be present.
        :param pulumi.Input[Mapping[str, pulumi.Input[str]]] headers: Custom headers to include in requests to the log drain endpoint.
        :param pulumi.Input[Sequence[pulumi.Input[str]]] project_ids: A list of project IDs that the log drain should be associated with. Logs from these projects will be sent log events to the specified endpoint. If omitted, logs will be sent for all projects.
        :param pulumi.Input[float] sampling_rate: A ratio of logs matching the sampling rate will be sent to your log drain. Should be a value between 0 and 1. If unspecified, all logs are sent.
        :param pulumi.Input[str] secret: A custom secret to be used for signing log events. You can use this secret to verify that log events are coming from Vercel and are not tampered with. See https://vercel.com/docs/observability/log-drains/log-drains-reference#secure-log-drains for full info.
        :param pulumi.Input[Sequence[pulumi.Input[str]]] sources: A set of sources that the log drain should send logs for. Valid values are `static`, `edge`, `external`, `build` and `lambda`.
        :param pulumi.Input[str] team_id: The ID of the team the Log Drain should exist under. Required when configuring a team resource if a default team has not been set in the provider.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: LogDrainArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        Provides a Configurable Log Drain resource.

        > For Log Drain integrations, please see the [Integration Log Drain docs](https://vercel.com/docs/observability/log-drains#log-drains-integration).

        Log Drains collect all of your logs using a service specializing in storing app logs.

        Teams on Pro and Enterprise plans can subscribe to log drains that are generic and configurable from the Vercel dashboard without creating an integration. This allows you to use a HTTP service to receive logs through Vercel's log drains.

        > Only Pro and Enterprise teams can create Configurable Log Drains.

        ## Example Usage

        ```python
        import pulumi
        import pulumi_vercel as vercel
        import pulumiverse_vercel as vercel

        example_endpoint_verification = vercel.get_endpoint_verification()
        example_project = vercel.Project("exampleProject")
        example_log_drain = vercel.LogDrain("exampleLogDrain",
            delivery_format="json",
            environments=["production"],
            headers={
                "some-key": "some-value",
            },
            project_ids=[example_project.id],
            sampling_rate=0.8,
            secret="a_very_long_and_very_well_specified_secret",
            sources=["static"],
            endpoint="https://example.com/my-log-drain-endpoint")
        ```

        ## Import

        If importing into a personal account, or with a team configured on

        the provider, simply use the log_drain_id.

        - log_drain_id can be found by querying the Vercel REST API (https://vercel.com/docs/rest-api/endpoints/logDrains#retrieves-a-list-of-all-the-log-drains).

        ```sh
        $ pulumi import vercel:index/logDrain:LogDrain example ecfg_xxxxxxxxxxxxxxxxxxxxxxxxxxxx/xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx
        ```

        Alternatively, you can import via the team_id and edge_config_id.

        - team_id can be found in the team `settings` tab in the Vercel UI.

        - log_drain_id can be found by querying the Vercel REST API (https://vercel.com/docs/rest-api/endpoints/logDrains#retrieves-a-list-of-all-the-log-drains).

        ```sh
        $ pulumi import vercel:index/logDrain:LogDrain example team_xxxxxxxxxxxxxxxxxxxxxxxx/ecfg_xxxxxxxxxxxxxxxxxxxxxxxxxxxx/xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx
        ```

        :param str resource_name: The name of the resource.
        :param LogDrainArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(LogDrainArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 delivery_format: Optional[pulumi.Input[str]] = None,
                 endpoint: Optional[pulumi.Input[str]] = None,
                 environments: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 headers: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
                 project_ids: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 sampling_rate: Optional[pulumi.Input[float]] = None,
                 secret: Optional[pulumi.Input[str]] = None,
                 sources: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 team_id: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = LogDrainArgs.__new__(LogDrainArgs)

            if delivery_format is None and not opts.urn:
                raise TypeError("Missing required property 'delivery_format'")
            __props__.__dict__["delivery_format"] = delivery_format
            if endpoint is None and not opts.urn:
                raise TypeError("Missing required property 'endpoint'")
            __props__.__dict__["endpoint"] = endpoint
            if environments is None and not opts.urn:
                raise TypeError("Missing required property 'environments'")
            __props__.__dict__["environments"] = environments
            __props__.__dict__["headers"] = headers
            __props__.__dict__["project_ids"] = project_ids
            __props__.__dict__["sampling_rate"] = sampling_rate
            __props__.__dict__["secret"] = None if secret is None else pulumi.Output.secret(secret)
            if sources is None and not opts.urn:
                raise TypeError("Missing required property 'sources'")
            __props__.__dict__["sources"] = sources
            __props__.__dict__["team_id"] = team_id
        secret_opts = pulumi.ResourceOptions(additional_secret_outputs=["secret"])
        opts = pulumi.ResourceOptions.merge(opts, secret_opts)
        super(LogDrain, __self__).__init__(
            'vercel:index/logDrain:LogDrain',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None,
            delivery_format: Optional[pulumi.Input[str]] = None,
            endpoint: Optional[pulumi.Input[str]] = None,
            environments: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
            headers: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
            project_ids: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
            sampling_rate: Optional[pulumi.Input[float]] = None,
            secret: Optional[pulumi.Input[str]] = None,
            sources: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
            team_id: Optional[pulumi.Input[str]] = None) -> 'LogDrain':
        """
        Get an existing LogDrain resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] delivery_format: The format log data should be delivered in. Can be `json` or `ndjson`.
        :param pulumi.Input[str] endpoint: Logs will be sent as POST requests to this URL. The endpoint will be verified, and must return a `200` status code and an `x-vercel-verify` header taken from the endpoint_verification data source. The value the `x-vercel-verify` header should be can be read from the `vercel_endpoint_verification_code` data source.
        :param pulumi.Input[Sequence[pulumi.Input[str]]] environments: Logs from the selected environments will be forwarded to your webhook. At least one must be present.
        :param pulumi.Input[Mapping[str, pulumi.Input[str]]] headers: Custom headers to include in requests to the log drain endpoint.
        :param pulumi.Input[Sequence[pulumi.Input[str]]] project_ids: A list of project IDs that the log drain should be associated with. Logs from these projects will be sent log events to the specified endpoint. If omitted, logs will be sent for all projects.
        :param pulumi.Input[float] sampling_rate: A ratio of logs matching the sampling rate will be sent to your log drain. Should be a value between 0 and 1. If unspecified, all logs are sent.
        :param pulumi.Input[str] secret: A custom secret to be used for signing log events. You can use this secret to verify that log events are coming from Vercel and are not tampered with. See https://vercel.com/docs/observability/log-drains/log-drains-reference#secure-log-drains for full info.
        :param pulumi.Input[Sequence[pulumi.Input[str]]] sources: A set of sources that the log drain should send logs for. Valid values are `static`, `edge`, `external`, `build` and `lambda`.
        :param pulumi.Input[str] team_id: The ID of the team the Log Drain should exist under. Required when configuring a team resource if a default team has not been set in the provider.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = _LogDrainState.__new__(_LogDrainState)

        __props__.__dict__["delivery_format"] = delivery_format
        __props__.__dict__["endpoint"] = endpoint
        __props__.__dict__["environments"] = environments
        __props__.__dict__["headers"] = headers
        __props__.__dict__["project_ids"] = project_ids
        __props__.__dict__["sampling_rate"] = sampling_rate
        __props__.__dict__["secret"] = secret
        __props__.__dict__["sources"] = sources
        __props__.__dict__["team_id"] = team_id
        return LogDrain(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="deliveryFormat")
    def delivery_format(self) -> pulumi.Output[str]:
        """
        The format log data should be delivered in. Can be `json` or `ndjson`.
        """
        return pulumi.get(self, "delivery_format")

    @property
    @pulumi.getter
    def endpoint(self) -> pulumi.Output[str]:
        """
        Logs will be sent as POST requests to this URL. The endpoint will be verified, and must return a `200` status code and an `x-vercel-verify` header taken from the endpoint_verification data source. The value the `x-vercel-verify` header should be can be read from the `vercel_endpoint_verification_code` data source.
        """
        return pulumi.get(self, "endpoint")

    @property
    @pulumi.getter
    def environments(self) -> pulumi.Output[Sequence[str]]:
        """
        Logs from the selected environments will be forwarded to your webhook. At least one must be present.
        """
        return pulumi.get(self, "environments")

    @property
    @pulumi.getter
    def headers(self) -> pulumi.Output[Optional[Mapping[str, str]]]:
        """
        Custom headers to include in requests to the log drain endpoint.
        """
        return pulumi.get(self, "headers")

    @property
    @pulumi.getter(name="projectIds")
    def project_ids(self) -> pulumi.Output[Optional[Sequence[str]]]:
        """
        A list of project IDs that the log drain should be associated with. Logs from these projects will be sent log events to the specified endpoint. If omitted, logs will be sent for all projects.
        """
        return pulumi.get(self, "project_ids")

    @property
    @pulumi.getter(name="samplingRate")
    def sampling_rate(self) -> pulumi.Output[Optional[float]]:
        """
        A ratio of logs matching the sampling rate will be sent to your log drain. Should be a value between 0 and 1. If unspecified, all logs are sent.
        """
        return pulumi.get(self, "sampling_rate")

    @property
    @pulumi.getter
    def secret(self) -> pulumi.Output[str]:
        """
        A custom secret to be used for signing log events. You can use this secret to verify that log events are coming from Vercel and are not tampered with. See https://vercel.com/docs/observability/log-drains/log-drains-reference#secure-log-drains for full info.
        """
        return pulumi.get(self, "secret")

    @property
    @pulumi.getter
    def sources(self) -> pulumi.Output[Sequence[str]]:
        """
        A set of sources that the log drain should send logs for. Valid values are `static`, `edge`, `external`, `build` and `lambda`.
        """
        return pulumi.get(self, "sources")

    @property
    @pulumi.getter(name="teamId")
    def team_id(self) -> pulumi.Output[str]:
        """
        The ID of the team the Log Drain should exist under. Required when configuring a team resource if a default team has not been set in the provider.
        """
        return pulumi.get(self, "team_id")


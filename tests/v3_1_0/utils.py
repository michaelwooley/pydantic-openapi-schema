from pydantic import Field

from pydantic_openapi_schema.base import PackageBaseModel


class PingRequest(PackageBaseModel):
    """Ping Request."""

    __schema_name__ = "RenamedPingRequest"

    req_foo: str = Field(description="foo value of the request")
    req_bar: str = Field(description="bar value of the request")


class PingResponse(PackageBaseModel):
    """Ping response."""

    __schema_name__ = "RenamedPingResponse"

    resp_foo: str = Field(description="foo value of the response")
    resp_bar: str = Field(description="bar value of the response")

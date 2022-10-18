from typing import Dict, List, Literal, Optional, Union

from pydantic import Extra, Field

from pydantic_openapi_schema.base import PackageBaseModel

from .components import Components
from .external_documentation import ExternalDocumentation
from .info import Info
from .path_item import PathItem
from .paths import Paths
from .reference import Reference
from .security_requirement import SecurityRequirement
from .server import Server
from .tag import Tag


class OpenAPI(PackageBaseModel):
    """This is the root document object of the OpenAPI document."""

    openapi: Literal["3.1.0"] = Field("3.1.0", const=True)
    """
    **REQUIRED**. This string MUST be the [version number](https://spec.openapis.org/oas/v3.1.0#versions)
    of the OpenAPI Specification that the OpenAPI document uses.
    The `openapi` field SHOULD be used by tooling to interpret the OpenAPI document.
    This is *not* related to the API [info.version](https://spec.openapis.org/oas/v3.1.0#infoVersion) string.
    """

    info: Info
    """
    **REQUIRED**. Provides metadata about the API. The metadata MAY be used by tooling as required.
    """

    json_schema_dialect: Optional[str] = Field(None, alias="jsonSchemaDialect")
    """
    The default value for the `$schema` keyword within [Schema Objects](https://spec.openapis.org/oas/v3.1.0#schemaObject)
    contained within this OAS document. This MUST be in the form of a URI.
    """

    servers: List[Server] = Field(default_factory=list)
    """
    An array of Server Objects, which provide connectivity information to a target server.
    If the `servers` property is not provided, or is an empty array,
    the default value would be a [Server Object](https://spec.openapis.org/oas/v3.1.0#serverObject)
    with a [url](https://spec.openapis.org/oas/v3.1.0#serverUrl) value of `/`.
    """

    # paths: Optional[Paths] = None
    paths: Paths = Field(default_factory=dict)
    """
    The available paths and operations for the API.
    """

    webhooks: Dict[str, Union[PathItem, Reference]] = Field(default_factory=dict)
    """
    The incoming webhooks that MAY be received as part of this API and that the API consumer MAY choose to implement.
    Closely related to the `callbacks` feature, this section describes requests initiated other than by an API call,
    for example by an out of band registration.
    The key name is a unique string to refer to each webhook,
    while the (optionally referenced) Path Item Object describes a request
    that may be initiated by the API provider and the expected responses.
    An [example](https://github.com/OAI/OpenAPI-Specification/blob/main/examples/v3.1/webhook-example.yaml) is available.
    """

    components: Optional[Components] = None
    """
    An element to hold various schemas for the document.
    """

    security: List[SecurityRequirement] = Field(default_factory=list)
    """
    A declaration of which security mechanisms can be used across the API.
    The list of values includes alternative security requirement objects that can be used.
    Only one of the security requirement objects need to be satisfied to authorize a request.
    Individual operations can override this definition.
    To make security optional, an empty security requirement (`{}`) can be included in the array.
    """

    tags: Optional[List[Tag]] = None
    """
    A list of tags used by the document with additional metadata.
    The order of the tags can be used to reflect on their order by the parsing tools.
    Not all tags that are used by the [Operation Object](https://spec.openapis.org/oas/v3.1.0#operationObject) must be declared.
    The tags that are not declared MAY be organized randomly or based on the tools' logic.
    Each tag name in the list MUST be unique.
    """

    external_docs: Optional[ExternalDocumentation] = Field(None, alias="externalDocs")
    """
    Additional external documentation.
    """

    def __init__(self, **data):
        if "openapi" not in data:
            data["openapi"] = self.__fields__["openapi"].default
        super().__init__(**data)

    class Config:
        extra = Extra.ignore
        allow_population_by_field_name = True

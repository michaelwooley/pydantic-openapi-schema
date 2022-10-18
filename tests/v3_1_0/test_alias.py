from pydantic_openapi_schema.v3_1_0 import (
    Header,
    MediaType,
    Parameter,
    ParameterLocation,
    PathItem,
    Reference,
    Schema,
    SecurityScheme,
)


def test_header_alias() -> None:
    header_1 = Header(param_in=ParameterLocation.HEADER)
    header_2 = Header.parse_obj({"param_in": "header"})
    header_3 = Header.parse_obj({"in": "header"})
    assert header_1 == header_2 == header_3
    header_4 = Header.parse_obj({"in": ParameterLocation.HEADER})
    assert header_1 == header_2 == header_3 == header_4


def test_media_type_alias() -> None:
    media_type_1 = MediaType(schema=Schema())
    media_type_2 = MediaType.parse_obj({"schema": Schema()})
    media_type_3 = MediaType.parse_obj({"schema": Schema()})
    assert media_type_1 == media_type_2 == media_type_3


def test_parameter_alias() -> None:
    parameter_1 = Parameter(name="test", param_in="path", param_schema=Schema())
    parameter_2 = Parameter.parse_obj({"name": "test", "param_in": "path", "param_schema": Schema()})
    parameter_3 = Parameter.parse_obj({"name": "test", "in": "path", "schema": Schema()})
    assert parameter_1 == parameter_2 == parameter_3


def test_parameter_param_in() -> None:
    pl = ParameterLocation.HEADER
    header_1 = Parameter(name="test", param_in=pl, param_schema=Schema())
    assert header_1.param_in == pl


def test_path_item_alias() -> None:
    path_item_1 = PathItem(ref="#/dummy")
    path_item_2 = PathItem.parse_obj({"ref": "#/dummy"})
    path_item_3 = PathItem.parse_obj({"$ref": "#/dummy"})
    assert path_item_1 == path_item_2 == path_item_3


def test_reference_alias() -> None:
    reference_1 = Reference(ref="#/dummy")
    reference_2 = Reference.parse_obj({"ref": "#/dummy"})
    reference_3 = Reference.parse_obj({"$ref": "#/dummy"})
    assert reference_1 == reference_2 == reference_3


def test_security_scheme() -> None:
    security_scheme_1 = SecurityScheme(type="apiKey", security_scheme_in="header")
    security_scheme_2 = SecurityScheme.parse_obj({"type": "apiKey", "security_scheme_in": "header"})
    security_scheme_3 = SecurityScheme.parse_obj({"type": "apiKey", "in": "header"})
    assert security_scheme_1 == security_scheme_2 == security_scheme_3


def test_schema() -> None:
    schema_1 = Schema(schema_not=Schema(), schema_format="email")
    schema_2 = Schema.parse_obj({"schema_not": Schema(), "schema_format": "email"})
    schema_3 = Schema.parse_obj({"not": Schema(), "format": "email"})
    assert schema_1 == schema_2 == schema_3

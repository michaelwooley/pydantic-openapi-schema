from pydantic import BaseModel, Extra


class PackageBaseModel(BaseModel):
    """Base model for pkg"""

    class Config:
        """Common config"""

        extra = Extra.ignore
        allow_population_by_field_name = True

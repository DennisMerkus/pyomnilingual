from pydantic import BaseModel


class IetfComponents(BaseModel):
    language: bool = True
    script: bool = False
    region: bool = False

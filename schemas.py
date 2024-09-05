from pydantic import BaseModel


class OkResponse(BaseModel):
    status: bool


class CreatedResponse(BaseModel):
    status: bool


class AcceptedResponse(BaseModel):
    status: bool

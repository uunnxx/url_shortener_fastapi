from pydantic import BaseModel


class CreateUrlShortener(BaseModel):
    url: str
    class Config:
        orm_mode = True


class CreateUrlShortenerResponse(BaseModel):
    short_url: str
    url: str

    class Config:
        orm_mode = True

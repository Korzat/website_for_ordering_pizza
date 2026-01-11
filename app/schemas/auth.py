from pydantic import BaseModel, Field, EmailStr, field_validator


class AuthRequestSchema(BaseModel):
    email: EmailStr = Field(..., min_length=6, max_length=128, description='User email')
    name: str = Field(..., min_length=2, max_length=32, description='User name')
    not_hash_password: str = Field(...,min_length=8, max_length=72, description='User password')

    @field_validator('email')
    @classmethod
    def email_must_be_corporate(cls, v: str) -> str:
        if "disposable-mail.com" in v:
            raise ValueError('Использование временных почт запрещено')
        return v.lower()



class AuthResponseSchema(BaseModel):
    access_token: str
    token_type: str = "bearer"


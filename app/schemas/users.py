from pydantic import EmailStr, Field, field_validator


class UserSchema:
    email: EmailStr = Field(...,min_length=6, max_length=128, description='User email')
    name: str = Field(...,min_length=2, max_length=32, description='User name')

    @field_validator('email')
    @classmethod
    def validate_email(cls, value: EmailStr) -> EmailStr:
        if not value:
            raise ValueError('Email is required')
        return value

class UserCreateSchema(UserSchema):
    not_hash_password: str = Field(...,min_length=8, max_length=128, description='User password')

    @field_validator('password')
    @classmethod
    def validate_password(cls, value: str) -> str:
        if not value:
            raise ValueError('Password is required')
        return value



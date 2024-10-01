from sqlmodel import Field, Relationship, SQLModel

class Clients(SQLModel, table=True):
    id: int = Field(default=None, primary_key=True)
    name: str = Field(max_length=50, nullable=False)
    srnames: str = Field(max_length=50, nullable=False)
    company: str = Field(max_length=50, nullable=False)
    nif: str = Field(max_length=9, nullable=False)
    address: str = Field(max_length=50, nullable=False)
    city: str = Field(max_length=50, nullable=False)
    post_code: int = Field(max_length=5, nullable=False)
    phone: int = Field(max_length=9, nullable=False)
    email: str = Field(max_length=50, nullable=False)

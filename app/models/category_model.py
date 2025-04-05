from sqlmodel import Field, Relationship, SQLModel

class Category(SQLModel, table=True):
  id: int = Field(default=None, primary_key=True)
  name: str = Field(max_length=50, unique=True)
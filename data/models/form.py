from sqlalchemy.orm import Mapped, mapped_column, relationship
from typing import List

from data.database import db
from data.models.form_block import FormBlock

class Form(db.Model):
    __tablename__ = 'form'

    # Attributes
    id: Mapped[int] = mapped_column(primary_key = True, autoincrement = True)
    token: Mapped[str] = mapped_column(unique = True, nullable = False)
    owner: Mapped[int] = mapped_column(nullable = False, default = 1)
    
    title: Mapped[str]
    description: Mapped[str]
    blocks: Mapped[list['FormBlock']] = relationship(
        cascade = 'all, delete-orphan'
    )

    def __repr__(self):
        return f'<Form {self.id}>'
    
    def __len__(self):
        return len(self.blocks)        return len(self.blocks)

def get_forms() -> List[Form]:
    _query = db.select(Form)
    forms: List[Form] = db.session.execute(_query).scalars()
    return forms
    
def get_form_by_id(form_id: int) -> Form | None:
    _query = db.select(Form).where(Form.id == form_id)
    form: Form | None = db.session.execute(_query).scalar_one_or_none()
    return form

def get_form_by_token(form_token: str) -> Form | None:
    _query = db.select(Form).where(Form.token == form_token)
    form: Form | None = db.session.execute(_query).scalar_one_or_none()
    return form

def get_forms_by_owner(owner_id: int) -> List[Form]:
    _query = db.select(Form).where(Form.owner == owner_id)
    forms: List[Form] = db.session.execute(_query).scalars()
    return forms
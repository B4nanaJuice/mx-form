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
        return len(self.blocks)
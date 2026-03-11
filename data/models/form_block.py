from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import ForeignKey
from typing import List

from data.database import db

class FormBlock(db.Model):
    __tablename__ = 'form_block'

    # Attributes
    id: Mapped[int] = mapped_column(primary_key = True, autoincrement = True)

    title: Mapped[str] = mapped_column(nullable = False, default = 'Block title')
    description: Mapped[str] = mapped_column(default = '')
    required: Mapped[bool] = mapped_column(default = False)

    form_id: Mapped[int] = mapped_column(ForeignKey('form.id'))

    block_type: Mapped[str]
    __mapper_args__ = {
        'polymorrphic_on': 'block_type',
        'polymorphic_identity': 'form_block'
    }

    def __repr__(self):
        return f'<FormBlock {self.title}>'
    
    def __len__(self):
        return len(self.answers)
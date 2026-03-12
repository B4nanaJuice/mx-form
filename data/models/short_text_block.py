from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship
from typing import List

from data.database import db
from data.models.form_block import FormBlock

class ShortTextBlock(FormBlock):
    __tablename__ = 'short_text_block'

    # Attributes
    id: Mapped[int] = mapped_column(ForeignKey('form_block.id'), primary_key = True)

    answers: Mapped[List['ShortTextAnswer']] = relationship(
        cascade = 'all, delete-orphan'
    )

    __mapper_args__ = {
        'polymorphic_identity': 'short_text_block'
    }

    def __repr__(self):
        return f'<ShortTextBlock {self.title}>'
    
class ShortTextAnswer(db.Model):
    __tablename__ = 'short_text_answer'

    # Attributes
    id: Mapped[int] = mapped_column(primary_key = True, autoincrement = True)

    value = Mapped[str] = mapped_column(nullable = True)
    
    short_text_block_id: Mapped[int] = mapped_column(ForeignKey('short_text_block.id'))

    def __repr__(self):
        return f'<ShortTextAnswer {self.value}>'
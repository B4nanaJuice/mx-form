from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship

from data.database import db
from data.models.form_block import FormBlock

class SmallTextBlock(FormBlock):
    __tablename__ = 'small_text_block'

    # Attributes
    id: Mapped[int] = mapped_column(ForeignKey('form_block.id'), primary_key = True)

    __mapper_args__ = {
        'polymorphic_identity': 'small_text_block'
    }

    def __repr__(self):
        return f'<SmallTextBlock {self.title}>'
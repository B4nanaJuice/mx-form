from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import ForeignKey

from data.database import db

class FormBlock(db.Model):
    __tablename__ = 'form_block'

    # Attributes
    form_id: Mapped[int] = mapped_column(ForeignKey('form.id'))
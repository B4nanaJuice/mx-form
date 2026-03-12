from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import ForeignKey

from data.database import db

class FormBlock(db.Model):
    """
    Abstract class that represent a block in a form. The block is representing
    a question (or a simple Section title + Description) with its title (question),
    optional description and if the answer is required or not.

    Attributes
    ----------
    id: int
        The unique identifier of the block
    title: str
        The title of the block
    description: str
        A description that will give more details about the title
    required: bool
        Wheter the answer is required or not
    form_id: int
        The id of the form that contains this block
    block_type: str
        The type of the block. For more information, check `ShortTextBlock`,
        `LongTextBlock`, `NumberBlock`, `PhoneBlock`, 
    """
    __tablename__ = 'form_block'

    # Attributes
    id: Mapped[int] = mapped_column(primary_key = True, autoincrement = True)

    title: Mapped[str] = mapped_column(nullable = False, default = 'Block title')
    description: Mapped[str] = mapped_column(nullable = True)
    required: Mapped[bool] = mapped_column(default = False)

    form_id: Mapped[int] = mapped_column(ForeignKey('form.id'))

    block_type: Mapped[str]
    __mapper_args__ = {
        'polymorrphic_on': 'block_type',
        'polymorphic_identity': 'form_block'
    }

    def __repr__(self):
        return f'<FormBlock {self.title}>'
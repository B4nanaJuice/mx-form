from sqlalchemy.orm import Mapped, mapped_column, relationship
from typing import List

from data.database import db
from data.models.form_block import FormBlock

class Form(db.Model):
    """
    Class that represents a form with different blocks representing the 
    questions. The form can be modified by the owner only and the modification 
    page is accessible at `/path/<token>`. For the users to fill in the form, 
    it can be done at `/path/<token>`.

    Attributes
    ----------
    id: int
        The unique identifier of the form
    token: string
        A string that will also identify the form
    owner: int
        The id of the owner of the form
    title: str
        The title of the form
    description: str
        A description that will give more information about the form
        or could be used to give context
    blocks: list[FormBlock]
        The blocks (questions) contained in the form
    """
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

def get_forms() -> List[Form]:
    """
    Method to get all existing forms.

    Returns
    -------
    List[Form]
        A list containing every form
    """
    _query = db.select(Form)
    forms: List[Form] = db.session.execute(_query).scalars()
    return forms
    
def get_form_by_id(form_id: int) -> Form | None:
    """
    Method to get a form by its id. Will return the form if anything is found
    with the given id. Otherwise, it will return None.

    Attributes
    ----------
    form_id: int
        The id of the form

    Returns
    -------
    Form | None
        The form if it's found, or None if nothing is found
    """
    _query = db.select(Form).where(Form.id == form_id)
    form: Form | None = db.session.execute(_query).scalar_one_or_none()
    return form

def get_form_by_token(form_token: str) -> Form | None:
    """
    Method to get a form by its token. Will return the form if anything is found
    with the given id. Otherwise, it will return None.

    Attributes
    ----------
    form_token: string
        The token of the form

    Returns
    -------
    Form | None
        The form if it's found, or None if nothing is found
    """
    _query = db.select(Form).where(Form.token == form_token)
    form: Form | None = db.session.execute(_query).scalar_one_or_none()
    return form

def get_forms_by_owner(owner_id: int) -> List[Form]:
    """
    Method to get all forms owned by someone, with its id.

    Attributes
    ----------
    owner_id: int
        The id of the owner

    Returns
    -------
    List[Form]
        A list containing every form owner by the person
    """
    _query = db.select(Form).where(Form.owner == owner_id)
    forms: List[Form] = db.session.execute(_query).scalars()
    return forms
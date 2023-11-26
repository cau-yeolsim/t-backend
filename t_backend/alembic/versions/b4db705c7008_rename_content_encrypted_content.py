"""rename: content -> encrypted_content

Revision ID: b4db705c7008
Revises: bf2b64ac492b
Create Date: 2023-11-27 01:18:34.688399

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision: str = "b4db705c7008"
down_revision: Union[str, None] = "bf2b64ac492b"
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column("message", sa.Column("encrypted_content", sa.Text(), nullable=True))
    op.drop_column("message", "content")
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column(
        "message", "content", nullable=False, new_column_name="encrypted_content"
    )
    # ### end Alembic commands ###

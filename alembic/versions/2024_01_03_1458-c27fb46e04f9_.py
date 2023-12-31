"""empty message

Revision ID: c27fb46e04f9
Revises: 212ba973dfdc
Create Date: 2024-01-03 14:58:13.912716

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'c27fb46e04f9'
down_revision: Union[str, None] = '212ba973dfdc'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.execute(
        f"""INSERT INTO country (name, continent_id) VALUES ('Brazil', 1)
        """
    )
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    pass
    # ### end Alembic commands ###

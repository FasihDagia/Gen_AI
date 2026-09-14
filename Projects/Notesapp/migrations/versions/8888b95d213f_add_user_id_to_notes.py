"""add user_id to notes

Revision ID: 8888b95d213f
Revises:
Create Date: 2026-09-15 02:32:49.211266
"""

from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = "8888b95d213f"
down_revision: Union[str, Sequence[str], None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""

    # Add user_id column to user_notes
    op.add_column(
        "user_notes",
        sa.Column("user_id", sa.Integer(), nullable=True)
    )

    # Create foreign key relationship
    op.create_foreign_key(
        "fk_user_notes_user_id",
        "user_notes",
        "user_info",
        ["user_id"],
        ["id"],
        ondelete="CASCADE"
    )


def downgrade() -> None:
    """Downgrade schema."""

    op.drop_constraint(
        "fk_user_notes_user_id",
        "user_notes",
        type_="foreignkey"
    )

    op.drop_column("user_notes", "user_id")
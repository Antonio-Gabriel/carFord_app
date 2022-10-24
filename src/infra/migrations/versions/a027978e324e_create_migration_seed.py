"""Create migration seed

Revision ID: a027978e324e
Revises: 9de713bbda55
Create Date: 2022-10-23 11:38:52.701485

"""
import bcrypt
from alembic import op
import sqlalchemy as sa

from uuid import uuid4
from sqlalchemy.sql import table, column

# revision identifiers, used by Alembic.
revision = 'a027978e324e'
down_revision = '9de713bbda55'
branch_labels = None
depends_on = None


def upgrade() -> None:
    person_table = table('person',
                         column('id', sa.String),
                         column('name', sa.String),
                         column('email', sa.String),
                         column('is_admin', sa.Boolean)
                         )

    admin_table = table('admin',
                        column('id', sa.String),
                        column('person_id', sa.String),
                        column('password', sa.String)
                        )

    person_ids = ['7bf4af59-e712-4a5c-a265-db8ec8077d5f',
                  'c1d89aa1-1715-4221-be73-e5700e8fe391']
    salt = bcrypt.gensalt()

    op.bulk_insert(person_table, [
        {"id": person_ids[0], "name": "Herlander Bento",
         "email": "herlanderbento@gmail.com", "is_admin": True},
        {"id": person_ids[1], "name": "Jorge Neto",
            "email": "jorgeneto@gmail.com", "is_admin": True},
    ])

    op.bulk_insert(admin_table, [
        {"id": str(uuid4()), "person_id": person_ids[0], "password": bcrypt.hashpw(
            "herlanderbento".encode('utf-8'), salt).decode('utf-8')},
        {"id": str(uuid4()), "person_id": person_ids[1], "password": bcrypt.hashpw(
            "jorgeneto".encode('utf-8'), salt).decode('utf-8')},
    ])


def downgrade() -> None:
    pass

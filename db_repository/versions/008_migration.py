from sqlalchemy import *
from migrate import *


from migrate.changeset import schema
pre_meta = MetaData()
post_meta = MetaData()
post = Table('post', pre_meta,
    Column('id', INTEGER, primary_key=True, nullable=False),
    Column('body', VARCHAR(length=10000)),
    Column('user_id', INTEGER),
    Column('abstract', VARCHAR(length=1000)),
    Column('title', VARCHAR(length=100)),
    Column('repo_url', VARCHAR(length=200)),
    Column('created', DATETIME),
    Column('updated', DATETIME),
)

post = Table('post', post_meta,
    Column('id', Integer, primary_key=True, nullable=False),
    Column('title', String(length=100)),
    Column('abstract', String(length=1000)),
    Column('body', String(length=10000)),
    Column('created_date', String(length=25)),
    Column('updated_date', String(length=25)),
    Column('repo_url', String(length=200)),
    Column('user_id', Integer),
)


def upgrade(migrate_engine):
    # Upgrade operations go here. Don't create your own engine; bind
    # migrate_engine to your metadata
    pre_meta.bind = migrate_engine
    post_meta.bind = migrate_engine
    pre_meta.tables['post'].columns['created'].drop()
    pre_meta.tables['post'].columns['updated'].drop()
    post_meta.tables['post'].columns['created_date'].create()
    post_meta.tables['post'].columns['updated_date'].create()


def downgrade(migrate_engine):
    # Operations to reverse the above upgrade go here.
    pre_meta.bind = migrate_engine
    post_meta.bind = migrate_engine
    pre_meta.tables['post'].columns['created'].create()
    pre_meta.tables['post'].columns['updated'].create()
    post_meta.tables['post'].columns['created_date'].drop()
    post_meta.tables['post'].columns['updated_date'].drop()

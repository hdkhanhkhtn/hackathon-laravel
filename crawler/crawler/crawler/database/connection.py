# -*- coding: utf-8 -*-

from migrate import *
from .settings import *
from .model import create_table
import model

create_table(engine)

def upgrade(migrate_engine):
    model.meta.bind = migrate_engine
    model.table.create()

def downgrade(migrate_engine):
    model.meta.bind = migrate_engine
    model.table.drop()
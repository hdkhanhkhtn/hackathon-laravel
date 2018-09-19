#!/usr/bin/env python
import sys
from migrate.versioning.shell import main
from crawler.database.settings import *
print(connection_str)
if __name__ == '__main__':
    main(debug='False', url=connection_str, repository='./migration')

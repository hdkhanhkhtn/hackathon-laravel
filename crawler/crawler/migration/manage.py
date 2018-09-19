#!/usr/bin/env python
import sys
from migrate.versioning.shell import main
from crawler.database.settings import *

if __name__ == '__main__':
    main(debug='False', url=connection_str, repository='.')

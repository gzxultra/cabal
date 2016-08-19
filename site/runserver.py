#!/usr/bin/env python
# coding: utf-8
import sys
from app import app


def main():
    try:
        port = int(sys.argv[1])
    except:
        print 'Usage:\n\t./runserver port'
        sys.exit(1)
    app.run(host='0.0.0.0', debug=True, port=port)

def create_tables():
    database.connect()
    database.create_tables([User])

if __name__ == '__main__':
    main()

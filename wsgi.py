from __future__ import absolute_import
from flask import Flask
from app.__init__ import create_app

app = create_app()

if __name__ == '__main__':
    app.run()

import os

class Config:
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://moringa:7995@localhost/pitch'
    SQLALCHEMY_TRACK_MODIFICATIONS = True
    UPLOADED_PHOTOS_DEST ='app/static/photos'
class ProdConfig(Config):
    pass

class DevConfig(Config):
    DEBUG = True

config_options ={
    'development':DevConfig,
    'production':ProdConfig
    }

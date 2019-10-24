import os

class Config:
    SECRET_KEY = 'youarestrong'
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://moringa:faith@localhost/pitch'
    SQLALCHEMY_TRACK_MODIFICATIONS = True
    SIMPLEMDE_JS_IIFE = True
    SIMPLEMDE_USE_CDN = True
    
    

    #  email configurations
    MAIL_SERVER = 'smtp.googlemail.com'
    MAIL_PORT = 587
    MAIL_USE_TLS = True
    MAIL_USERNAME = os.environ.get("MAIL_USERNAME")
    MAIL_PASSWORD = os.environ.get("MAIL_PASSWORD")
    
    DEBUG = True

class ProdConfig(Config):
    '''
    Pruduction configuration child class
    Args:
        Config: The parent configuration class with General configuration settings
    '''
    SQLALCHEMY_DATABASE_URI = os.environ.get("DATABASE_URL")

class TestConfig(Config):
   '''
   Testing configuration child class
  
   Args:
       Config: The parent configuration class with General configuration settings
   '''
   SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://moringa:faith@localhost/pitch'

   pass

class DevConfig(Config):
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://moringa:faith@localhost/pitch'
    

    DEBUG = True

config_options ={
    'development':DevConfig,
    'production':ProdConfig,
    'test': TestConfig
    }

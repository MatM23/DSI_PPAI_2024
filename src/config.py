from decouple import config

class Config:
    SECRET_KEY=config('SECRET_KEY')

class DevelopmentConfig(Config):
    DEBUG=True

#Crea configuración con la depuración activada, donde cada cambio
#se reinicia sólo el servidor.

config = {
    'development': DevelopmentConfig
}
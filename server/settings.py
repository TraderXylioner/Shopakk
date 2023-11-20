import environs

env = environs.Env()
env.read_env('server/.env')


class Database:
    HOST = env('DATABASE_HOST')
    USER = env('DATABASE_USER')
    PASSWORD = env('DATABASE_PASSWORD')
    DATABASE = env('DATABASE_DATABASE')
    PORT = env('DATABASE_PORT')
    url = f"postgresql+asyncpg://{USER}:{PASSWORD}@{HOST}:{PORT}/{DATABASE}"

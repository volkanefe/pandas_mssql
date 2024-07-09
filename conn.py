from sqlalchemy import create_engine, text

server = 'localhost'
database = 'MikroDB'
username = 'sa'
password = 'Admin123'

engine = create_engine(f'mssql+pymssql://{username}:{password}@{server}/{database}')
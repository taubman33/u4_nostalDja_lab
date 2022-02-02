-- settings.sql
DROP DATABASE nostaldja;
CREATE DATABASE nostaldja;
CREATE USER nostaldjauser WITH PASSWORD 'nostaldja';
GRANT ALL PRIVILEGES ON DATABASE nostaldja TO nostaldjauser;
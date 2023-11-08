DROP TABLE IF EXISTS Cache
GO

CREATE TABLE Cache(
    ID INT IDENTITY(1,1) PRIMARY KEY,
    URLAddress VARCHAR(55),
    LastAccess DATETIME
)
GO

DROP TABLE IF EXISTS History
GO

CREATE TABLE History(
    ID INT IDENTITY PRIMARY KEY,
    URLAddress VARCHAR(55),
    LastAccess DATETIME
)
GO

DROP TABLE IF EXISTS Parameters
GO

CREATE TABLE Parameters(
    Name VARCHAR(10),
    Value INT
)
GO

INSERT INTO Parameters(Name, [Value])
VALUES ('max_cache', 4)
GO

INSERT INTO Cache(URLAddress, LastAccess)
VALUES ('https://stackoverflow.com/', '2023-11-05 14:28:50.400'),
        ('https://chat.openai.com/', '2023-11-06 02:41:16.690'),
        ('https://www.youtube.com/', '2023-11-06 12:41:16.690')
GO

SELECT * FROM Cache
SELECT * from Parameters
go  
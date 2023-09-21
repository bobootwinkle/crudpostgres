import psycopg2


def connectdb():
    connection = psycopg2.connect(
        host='localhost',
        user='postgres',
        password='1111',
        database='sampledb',
        port=5432,
    )
    return connection


# call function
print(connectdb())

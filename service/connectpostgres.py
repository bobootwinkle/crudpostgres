import psycopg2

#local database
# def connectdb():
#     connection = psycopg2.connect(
#         host='localhost',
#         user='postgres',
#         password='1111',
#         database='sampledb',
#         port=5432,
#     )
#     return connection

#server database
def connectdb():
    connection = psycopg2.connect(
        host='dpg-ck5snk8s0i2c73bv6p2g-a',
        user='admin',
        password='XhiFJIScQB4EB9iSabRmp8gnx113sA15',
        database='sampledb',
        port=5432,
    )
    return connection

# call function
print(connectdb())

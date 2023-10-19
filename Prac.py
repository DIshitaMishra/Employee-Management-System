from mysql.connector import connect
a = connect(host='localhost',user = 'root', password = 'root', database = 'sys')

b = a.cursor()

sql = 'select sno from emp'
#sno = int(input('Enter the serial number : '))
b.execute(sql)
r = b.fetchall()
f = []
for i in r:
    c = int(i[0])
    f.append(c)


b.close()
a.close()
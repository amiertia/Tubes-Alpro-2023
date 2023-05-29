import mysql.connector
from prettytable import PrettyTable


class Database:
    def __init__(self):
        self.db = mysql.connector.connect(
            host='localhost',
            user='root',
            password='',
            database='rs_siti_rahmah'
        )
        if self.db.is_connected():
            print("Successfully connected to MySQL database")

    def data_RawatInap(self, val):
        cursor = self.db.cursor()
        sql = "INSERT INTO rawatinap (dokter, spesialisasi, pasien, umur, penyakit, suhu, kamar) VALUES (%s, %s, %s, %s, %s, %s, %s)"
        cursor.execute(sql, val)
        self.db.commit()
        print("{} Data telah di eksekusi!".format(cursor.rowcount))

    def data_RawatJalan(self, val):
        cursor = self.db.cursor()
        sql = "INSERT INTO rawatjalan (dokter, spesialisasi, pasien, umur, penyakit, suhu) VALUES (%s, %s, %s, %s, %s, %s)"
        cursor.execute(sql, val)
        self.db.commit()
        print("{} Data telah di eksekusi!".format(cursor.rowcount))

    def show_data_RawatInap(self):
        cursor = self.db.cursor()
        sql = "SELECT * FROM rawatinap"
        cursor.execute(sql)
        results = cursor.fetchall()

        table = PrettyTable()
        table.field_names = ['ID', 'DOKTER', 'SPESIALISASI', 'PASIEN', 'UMUR', 'PENYAKIT', 'SUHU', 'KAMAR']

        for i in results:
            table.add_row(list(i))
        print(table)

    def show_data_RawatJalan(self):
        cursor = self.db.cursor()
        sql = "SELECT * FROM rawatjalan"
        cursor.execute(sql)
        results = cursor.fetchall()

        table = PrettyTable()
        table.field_names = ['ID', 'DOKTER', 'SPESIALISASI', 'PASIEN', 'UMUR', 'PENYAKIT', 'SUHU']

        for i in results:
            table.add_row(list(i))
        print(table)
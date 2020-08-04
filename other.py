import math
import mysql.connector
import time

height = 0.0
radius = 0.0
sl_height = 0.0
transaction_id = 0.0
exists = False


def get_input():
    global height, radius, sl_height, transaction_id
    radius = float(input('Enter radius for tent (in meters) : '))
    sl_height = float(input('Enter slant height for tent (in meters) : '))
    height = float(input('Enter height for tent (in meters) : '))
    transaction_id = time.time()


class Tent:
    price_per_unit = 0.5

    def __init__(self, h=0.0, r=0.0, sl=0.0):

        self.h = h
        self.r = r
        self.sl = sl

        print('Generating price for this tent...')

        self.my_db = mysql.connector.connect(host='localhost', user='root', passwd='KINGSHUKYou@Mysql')
        self.my_cursor = self.my_db.cursor()

        Tent.show(self)

    def show(self):
        print('Price for this tent is : $', Tent.calculate(self))

    def calculate(self):
        total_surface_area_cylinder = 2 * math.pi * self.r * (self.r + self.h)
        total_surface_area_cone = math.pi * self.r * (self.r + self.sl)
        total_surface_area_tent = total_surface_area_cylinder + total_surface_area_cone
        total_price_exclusive_tax = (Tent.price_per_unit * total_surface_area_tent)
        total_tax = 18 / 100 * total_price_exclusive_tax
        total_price_inclusive_tax = total_price_exclusive_tax + total_tax
        Tent.store(self, total_price_exclusive_tax, total_tax, total_price_inclusive_tax)
        return math.ceil(total_price_inclusive_tax)

    def store(self, tpe=0.0, tt=0.0, tpi=0.0):
        Tent.create_db(self)
        self.my_cursor.execute('insert into tent_transactions.transactions (Transaction_ID, '
                               'total_price_exclusive_tax, total_tax, '
                               'total_price_inclusive_tax) values (%f, %f, %f, %f) ' % (transaction_id, tpe, tt,
                                                                                        tpe + tt))
        self.my_db.commit()
        self.my_cursor.close()

    def create_db(self):
        global exists
        self.my_cursor.execute('show databases')
        databases = self.my_cursor.fetchall()
        for db in databases:
            if db == ('tent_transactions',):
                exists = True
                break

        if exists is not True:
            self.my_cursor.execute('CREATE SCHEMA `tent_transactions` ;')
            self.my_cursor.execute('CREATE TABLE `tent_transactions`.`transactions` ( `Transaction_ID` FLOAT NOT NULL, '
                                   '`total_price_exclusive_tax` FLOAT NOT NULL,  `total_tax` FLOAT NOT NULL,  '
                                   '`total_price_inclusive_tax` FLOAT NOT NULL,  PRIMARY KEY (`Transaction_ID`));')


def run():
    get_input()
    T1 = Tent(height, radius, sl_height)

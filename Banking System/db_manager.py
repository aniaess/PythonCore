import sqlite3
conn = sqlite3.connect('card.s3db')
cur = conn.cursor()

cur.execute("""CREATE TABLE IF NOT EXISTS card(
    id INTEGER,
    number TEXT,
    pin TEXT,
    balance INTEGER
);""")
conn.commit()

class DataBase():

    def __init__(self):
        self.id = 1

    def selecting_data(self):
        cur.execute("SELECT number, pin, balance FROM card")
        list_of_clients = cur.fetchall()
        return list_of_clients

    def insert_customer(self, data_base):
        cur.execute("""INSERT INTO card (id, number, pin, balance) VALUES (?,?,?,?);""",
                    (self.id, data_base[0], data_base[1], 0))
        conn.commit()
        self.id += 1

    def log_into(self, card, my_pin):
        list_of_clients =self.selecting_data()
        for client in list_of_clients:
            if card in client and my_pin in client:
                return 1

    def balance(self, card):
        list_of_clients = self.selecting_data()
        for client in list_of_clients:
            if card in client:
                return client[2]

    def close_account(self, num_card):
        cur.execute("DELETE FROM card WHERE number = ?", (num_card,))
        conn.commit()
        print("The account has been closed!")

    def add_money(self, num_card, income):
        cur.execute("UPDATE card SET balance = balance + ? WHERE number = ?", (income, num_card))
        conn.commit()

    def transfer_money(self, my_card, number_to_transfer, money):
        cur.execute("UPDATE card SET balance = balance - ? WHERE number = ?", (money, my_card))
        conn.commit()
        cur.execute("UPDATE card SET balance = balance + ? WHERE number = ?", (money, number_to_transfer))
        conn.commit()

    def checking_if_exist(self, number_to_transfer):
        list_of_clients = self.selecting_data()
        for client in list_of_clients:
            if number_to_transfer in client:
                return 1
import requests
import json

class CurrencyExchange:

    all_currencies = ["usd", "eur", "ils", "rub", "nok", "sek", "isk", "rsd", "pln", "ves", "jpy"]

    def __init__(self):
        self.cache = {}
        self.json_diki = {}
#2
    def get_json(self, user):
        r = requests.get(f"http://www.floatrates.com/daily/{user}.json")
        response = r.text
        currencies = json.loads(response)
        return currencies

    def update_cache(self, your_currency):
        if your_currency != "usd" and your_currency != "eur":
            self.cache["eur"] = self.json_diki["eur"]["rate"]
            self.cache["usd"] = self.json_diki["usd"]["rate"]
        elif your_currency != "eur":
            self.cache["eur"] = self.json_diki["eur"]["rate"]
        elif your_currency != "usd":
            self.cache["usd"] = self.json_diki["usd"]["rate"]
        print(self.cache)

    def main(self):
        your_currency = input().lower()
        self.json_diki = self.get_json(your_currency)
        convert_to = input()
        self.update_cache(your_currency)
        money = int(input())

        while convert_to in self.json_diki:
            print("Checking the cache...")
            if convert_to in self.cache:
                print("Oh! It is in the cache!")
            else:
                print("Sorry, but it is not in the cache!")
                rate = self.get_json(your_currency)[convert_to]["rate"]
                self.cache[convert_to] = rate
            you_get = money * self.cache[convert_to]
            print(f"You received {round(you_get, 2)} {convert_to.upper()}.")
            convert_to = input()
            if convert_to == "":
                break
            money = int(input())
            print(self.cache)



client = CurrencyExchange()
client.main()








#last


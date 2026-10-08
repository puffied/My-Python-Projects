

import requests
import sys
import platform
import os
import time
import signal


#bruh
CURRENCY_LIST = [
"EUR: Euro", "AED: UAE Dirham", "AFN: Afghani", "ALL: Lek",
"AMD: Armenian Dram", "ANG: Netherlands Antillean Guilder", "AOA: Kwanza",
"ARS: Argentine Peso", "AUD: Australian Dollar", "AWG: Aruban Florin",
"AZN: Azerbaijan Manat", "BAM: Convertible Mark", "BBD: Barbados Dollar",
"BDT: Taka", "BGN: Bulgarian Lev", "BHD: Bahraini Dinar", "BIF: Burundi Franc",
"BMD: Bermudian Dollar", "BND: Brunei Dollar", "BOB: Boliviano",
"BRL: Brazilian Real", "BSD: Bahamian Dollar", "BTN: Ngultrum", "BWP: Pula",
"BYN: Belarusian Ruble", "BZD: Belize Dollar", "CAD: Canadian Dollar",
"CDF: Congolese Franc", "CHF: Swiss Franc", "CLF: Unidad de Fomento",
"CLP: Chilean Peso", "CNH: Chinese Yuan (Offshore)", "CNY: Yuan Renminbi",
"COP: Colombian Peso", "CRC: Costa Rican Colon", "CUP: Cuban Peso",
"CVE: Cabo Verde Escudo", "CZK: Czech Koruna", "DJF: Djibouti Franc",
"DKK: Danish Krone", "DOP: Dominican Peso", "DZD: Algerian Dinar",
"EGP: Egyptian Pound", "ERN: Nakfa", "ETB: Ethiopian Birr",
"FJD: Fiji Dollar", "FKP: Falkland Islands Pound", "FOK: Faroese Króna",
"GBP: Pound Sterling", "GEL: Lari", "GGP: Guernsey Pound", "GHS: Ghana Cedi",
"GIP: Gibraltar Pound", "GMD: Dalasi", "GNF: Guinean Franc",
"GTQ: Quetzal", "GYD: Guyana Dollar", "HKD: Hong Kong Dollar",
"HNL: Lempira", "HRK: Croatian Kuna", "HTG: Gourde", "HUF: Forint",
"IDR: Rupiah", "ILS: Israeli Sheqel", "IMP: Manx Pound",
"INR: Indian Rupee", "IQD: Iraqi Dinar", "IRR: Iranian Rial",
"ISK: Iceland Krona", "JEP: Jersey Pound", "JMD: Jamaican Dollar",
"JOD: Jordanian Dinar", "JPY: Yen", "KES: Kenyan Shilling", "KGS: Som",
"KHR: Riel", "KID: Kiribati Dollar", "KMF: Comorian Franc", "KRW: Won",
"KWD: Kuwaiti Dinar", "KYD: Cayman Islands Dollar", "KZT: Tenge",
"LAK: Lao Kip", "LBP: Lebanese Pound", "LKR: Sri Lanka Rupee",
"LRD: Liberian Dollar", "LSL: Loti", "LYD: Libyan Dinar",
"MAD: Moroccan Dirham", "MDL: Moldovan Leu", "MGA: Malagasy Ariary",
"MKD: Denar", "MMK: Kyat", "MNT: Tugrik", "MOP: Pataca", "MRU: Ouguiya",
"MUR: Mauritius Rupee", "MVR: Rufiyaa", "MWK: Malawi Kwacha",
"MXN: Mexican Peso", "MYR: Malaysian Ringgit", "MZN: Mozambique Metical",
"NAD: Namibia Dollar", "NGN: Naira", "NIO: Cordoba Oro",
"NOK: Norwegian Krone", "NPR: Nepalese Rupee", "NZD: New Zealand Dollar",
"OMR: Rial Omani", "PAB: Balboa", "PEN: Sol", "PGK: Kina",
"PHP: Philippine Peso", "PKR: Pakistan Rupee", "PLN: Zloty",
"PYG: Guarani", "QAR: Qatari Rial", "RON: Romanian Leu",
"RSD: Serbian Dinar", "RUB: Russian Ruble", "RWF: Rwanda Franc",
"SAR: Saudi Riyal", "SBD: Solomon Islands Dollar",
"SCR: Seychelles Rupee", "SDG: Sudanese Pound", "SEK: Swedish Krona",
"SGD: Singapore Dollar", "SHP: Saint Helena Pound", "SLE: Sierra Leonean Leone",
"SLL: Old Leone", "SOS: Somali Shilling", "SRD: Surinam Dollar",
"SSP: South Sudanese Pound", "STN: Dobra", "SYP: Syrian Pound",
"SZL: Lilangeni", "THB: Baht", "TJS: Somoni",
"TMT: Turkmenistan New Manat", "TND: Tunisian Dinar", "TOP: Pa'anga",
"TRY: Turkish Lira", "TTD: Trinidad and Tobago Dollar",
"TVD: Tuvaluan Dollar", "TWD: New Taiwan Dollar",
"TZS: Tanzanian Shilling", "UAH: Hryvnia", "UGX: Uganda Shilling",
"USD: US Dollar", "UYU: Peso Uruguayo", "UZS: Uzbekistan Sum",
"VES: Bolívar Soberano", "VND: Dong", "VUV: Vatu", "WST: Tala",
"XAF: CFA Franc BEAC", "XCD: East Caribbean Dollar", "XCG: Caribbean Guilder",
"XDR: SDR (Special Drawing Right)", "XOF: CFA Franc BCEAO",
"XPF: CFP Franc", "YER: Yemeni Rial", "ZAR: Rand",
"ZMW: Zambian Kwacha", "ZWG: Zimbabwe Gold", "ZWL: Zimbabwe Dollar",
]

VALID_CODES = {entry.split(": ")[0] for entry in CURRENCY_LIST}







def clear():
    if platform.system() == 'Windows':
        os.system('cls')
    else:
        os.system('clear')



def ctrl_c_handler(sig, frame):
    print("\nGoodbye!")
    sys.exit()
signal.signal(signal.SIGINT, ctrl_c_handler)



def CurrencyHelpcentral(self):
    while True:
        print("'ENTER' to leave")
        search = input("\nSearch ► ")
        if search == "":
            clear()
            self.convert_currency()
        else:
            found = False
            for entry in CURRENCY_LIST:                    
                code, name = entry.split(": ")             
                if name == search:                         
                    print(f"Code ►", code)
                    time.sleep(1.4)
                    clear()
                    found = True
                    continue   
        if not found:              
            print("Currency not found.")
            time.sleep(1)
            clear()
            continue


def UnitHelpcentral(self):
    while True:
        print("'ENTER' to leave\n")
        print("kg ► kilogram/s\nlbs ► pound/s\nm ► meter/s\nft ► feet")
        input("\n► ")
        clear()
        self.convert_units()
        
        

                









class multiConverter:
    def __init__(self):
        pass #placeholder


    def run(self):
        while True:
            print("=== CONVERTER ===")
            print("1 ► Convert Currency")
            print("2 ► Convert Units")
            print("\n3 ► Exit the program")
            
            choice = input("\nYour Choice ► ").strip().lower()
            while True:
                if choice == "1":
                    clear()
                    self.convert_currency()
                elif choice == "2":
                    clear()
                    self.convert_units()
                elif choice == "3":
                    print("Goodbye!")
                    break
                else:
                    print("Invalid input! please try again.\n")
                    time.sleep(1.2)
                    continue
                    






    
    
    def convert_currency(self):
      while True:    
        print("\n=== Currency Converter ===")
        print("\n'CTRL + C' to exit anywhere\n")

        print("'HELP' to search for a currencies short name\n")
        base = input("From currency ► ").strip().upper()
        if base == "HELP":
            clear()
            CurrencyHelpcentral(self)

        if base not in VALID_CODES:
            print("Currency does not exist!\nPlease try again.")
            time.sleep(1.2)
            clear()
            continue
            

        else:

            url = f"https://open.er-api.com/v6/latest/{base}"
            target = input("To currency ► ").strip().upper()
            if target == "HELP":
                clear()
                CurrencyHelpcentral(self)

            if target not in VALID_CODES:
                print("Currency does not exist!\nPlease try again.")
                time.sleep(1.2)
                clear()
                continue

            else:

                try:
                    amount = float(input("\nThe amount that you would like to convert: "))
                    if amount < 0:
                        raise ValueError

                
                    response = requests.get(url)
                    data = response.json()

                    if response.status_code == 200 and "rates" in data:
                        if target in data["rates"]:
                            rate = data["rates"][target]
                            result = amount * rate
                            print(f"\n► {amount} {base} = {result:.2f} {target}\n")
                            print("1 ► Again\n2 ► Return to the Menu")
                            query = input("Your Choice ► ")
                            if query == "1":
                                clear()
                                continue
                            elif query == "2":
                                clear()
                                self.run()
                        else:
                            print(f"Error: The Currency '{target}' was not found.\n")
                            time.sleep(1)
                            self.convert_currency()
                    else:
                        print("Error: Couldnt fetch data from the API. Possibly because of wrong entry.\n")
                        print("Restarting..")
                        time.sleep(1.4)
                        clear()
                        self.convert_currency()

            
                except ValueError:
                    print("\nError: Please enter a valid number!")
                    time.sleep(1.2)
                    clear()
                    self.convert_currency()


                except Exception as e:
                    print(f"\nInvalid value! could not convert.\nMore detailed explanation ►{e}\n")
                    time.sleep(1.2)
                    clear()
                    self.convert_currency()
                        

            
        

    def convert_units(self): 
        print("\n=== Unit Converter ===")
        print("'HELP' to open the full names of the units\n")
        print("1 ► kg to lbs")
        print("2 ► lbs to kg")
        print("3 ► m to ft")
        print("4 ► ft to m")
            
        choice = input("Your choice ► ").strip().upper()
        if choice == "HELP":
            clear()
            UnitHelpcentral(self)
        else:


        
            try: 
                value = float(input("Enter value to convert ► "))
                if value <= 0:
                    raise ValueError
                else:
                    clear()
                

                    if choice == "1":
                        result = value * 2.20462
                        print(f"\nResult ► {value} kg = {result:.2f} lbs\n")
                        print("1 ► Again\n2 ► Return to the Menu")
                        query = input("Your Choice ► ")
                        if query == "1":
                                clear()
                                self.convert_units()
                        elif query == "2":
                                clear()
                                self.run()

                    elif choice == "2":
                        result = value / 2.20462
                        print(f"\nResult ► {value} lbs = {result:.2f} kg\n")
                        print("1 ► Again\n2 ► Return to the Menu")
                        query = input("Your Choice ► ")
                        if query == "1":
                                clear()
                                self.convert_units()
                        elif query == "2":
                                clear()
                                self.run()

                    elif choice == "3":
                        result = value * 3.28084
                        print(f"\nResult ► {value} m = {result:.2f} ft\n")
                        print("1 ► Again\n2 ► Return to the Menu")
                        query = input("Your Choice ► ")
                        if query == "1":
                                clear()
                                self.convert_units()
                        elif query == "2":
                                clear()
                                self.run()

                    elif choice == "4":
                        result = value / 3.28084
                        print(f"\nResult ► {value} ft = {result:.2f} m\n")
                        print("1 ► Again\n2 ► Return to the Menu")
                        query = input("Your Choice ► ")
                        if query == "1":
                                clear()
                                self.convert_units()
                        elif query == "2":
                                clear()
                                self.run()

                    else:
                        print("\nInvalid unit conversion choice!\n")
                        time.sleep(1)
                        clear()
                        self.convert_units()
            
            except ValueError:
                print("\nError: Please enter a valid number!\n")
                time.sleep(1.2)
                clear()
                return
            
            
    


if __name__ == "__main__":
    converter = multiConverter()
    converter.run()

                    


            


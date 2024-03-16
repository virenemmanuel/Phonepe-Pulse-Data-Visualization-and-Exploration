# [File handling library]
import os
import json
import pandas as pd



#Aggre_transaction

path1 = "C:/Users/viren/OneDrive/Desktop/IIT-MADARAS(GUVI)/Phonepay project/pulse/data/aggregated/transaction/country/india/state/"
agg_tran_list = os.listdir(path1)

columns1 = {"States":[], "Years":[], "Quarter":[], "Transaction_type": [], "Transaction_count":[], "Transaction_amount":[]}

for state in agg_tran_list:
    current_states = path1 + state + "/"
    agg_year_list = os.listdir(current_states)
    
    for year in agg_year_list:
        current_year = current_states + year + "/"
        agg_file_list = os.listdir(current_year)
        
        for file in agg_file_list:
            current_file = current_year + file 
            data = open(current_file,"r")

            A = json.load(data)

            for i in A["data"]["transactionData"]:
                name = i["name"]
                count = i["paymentInstruments"][0]["count"]
                amount = i["paymentInstruments"][0]["count"]
                columns1["Transaction_type"].append(name)
                columns1["Transaction_count"].append(count)
                columns1["Transaction_amount"].append(amount)
                columns1["States"].append(state)
                columns1["Years"].append(year)
                columns1["Quarter"].append(int(file.strip(".json")))


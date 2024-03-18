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


Aggre_transaction = pd.DataFrame(columns1)



#Aggregated_user

path2 = "C:/Users/viren/OneDrive/Desktop/IIT-MADARAS(GUVI)/Phonepay project/pulse/data/aggregated/user/country/india/state/"
agg_user_list = os.listdir(path2)

columns2 = {"States":[], "Years":[], "Quarter":[], "Brands": [], "Transaction_count":[], "Percentage":[]}

for state in agg_user_list:
    current_states = path2 + state + "/"
    agg_year_list = os.listdir(current_states)

    for year in agg_year_list:
        current_year = current_states + year + "/"
        agg_file_list = os.listdir(current_year)

        for file in agg_file_list:
            current_file = current_year + file
            data = open(current_file,"r")

            B = json.load(data)
            
            try:
                for i in B["data"]["usersByDevice"]:
                                brand = i["brand"]
                                count = i["count"]
                                percentage = i["percentage"]
                                columns2["Brands"].append(brand)
                                columns2["Transaction_count"].append(count)
                                columns2["Percentage"].append(percentage)
                                columns2["States"].append(state)
                                columns2["Years"].append(year)
                                columns2["Quarter"].append(int(file.strip(".json")))

            except:
                pass

Aggregated_user = pd.DataFrame(columns2)

           

#Aggregated_insurance

path3 = "C:/Users/viren/OneDrive/Desktop/IIT-MADARAS(GUVI)/Phonepay project/pulse/data/aggregated/insurance/country/india/state/"
agg_insurance_list = os.listdir(path3)

columns3 = {"States":[],"Years":[],"Quarter":[],"Transaction_type":[],"Transaction_count":[],"Transaction_amount":[]}

for state in agg_insurance_list:
    current_states = path3 + state + "/"
    agg_year_list = os.listdir(current_states)

    for year in agg_year_list:
        current_year = current_states + year + "/"
        agg_file_list = os.listdir(current_year)

        for file in agg_file_list:
            current_file =  current_year + file
            data = open(current_file,"r")

            C = json.load(data)

           
            for i in C["data"]["transactionData"]:
                name = i["name"]
                count = i["paymentInstruments"][0]["count"]
                amount = i["paymentInstruments"][0]["amount"]
                columns3["Transaction_type"].append(name)
                columns3["Transaction_count"].append(count)
                columns3["Transaction_amount"].append(amount)
                columns3["States"].append(state)
                columns3["Years"].append(year)
                columns3["Quarter"].append(int(file.strip(".json")))


Aggregated_insurance = pd.DataFrame(columns3)


#Map_insurance 

path4 = "C:/Users/viren/OneDrive/Desktop/IIT-MADARAS(GUVI)/Phonepay project/pulse/data/map/insurance/hover/country/india/state/"
map_insurance_list = os.listdir(path4)

columns4 = {"States":[],"Years":[],"Quarter":[],"Districts":[],"Transaction_count":[],"Transaction_amount":[]}

for state in map_insurance_list:
    current_states = path4 + state + "/"
    agg_year_list = os.listdir(current_states)

    for year in agg_year_list:
        current_year = current_states + year + "/"
        agg_file_list = os.listdir(current_year)

        for file in agg_file_list:
            current_file =  current_year + file
            data = open(current_file,"r")

            D = json.load(data)
            
            for i in D["data"]["hoverDataList"]:
                name = i["name"]
                count = i["metric"][0]["count"]
                amount = i["metric"][0]["amount"]
                columns4["Districts"].append(name)
                columns4["Transaction_count"].append(count)
                columns4["Transaction_amount"].append(amount)
                columns4["States"].append(state)
                columns4["Years"].append(year)
                columns4["Quarter"].append(int(file.strip(".json")))


Map_insurance = pd.DataFrame(columns4)



#Map_transcation

path5 = "C:/Users/viren/OneDrive/Desktop/IIT-MADARAS(GUVI)/Phonepay project/pulse/data/map/transaction/hover/country/india/state/"
map_transaction_list = os.listdir(path5)

columns5 = {"States":[],"Years":[],"Quarter":[],"Districts":[],"Transaction_count":[],"Transaction_amount":[]}

for state in map_transaction_list:
    current_states = path5 + state + "/"
    map_year_list = os.listdir(current_states)

    for year in map_year_list:
        current_year = current_states + year + "/"
        map_file_list = os.listdir(current_year)

        for file in map_file_list:
            current_file =   current_year + file
            data = open(current_file,"r")

            E = json.load(data)

            for i in E["data"]["hoverDataList"]:
                name = i["name"]
                count = i["metric"][0]["count"]
                amount = i["metric"][0]["amount"]
                columns5["Districts"].append(name)
                columns5["Transaction_count"].append(count)
                columns5["Transaction_amount"].append(amount)
                columns5["States"].append(state)
                columns5["Years"].append(year)
                columns5["Quarter"].append(int(file.strip(".json")))    

Map_transcation = pd.DataFrame(columns5)

# установить пандас перед началом работы
# pip install pandas
# pip install openpyxl xlsxwriter xlrd 


import json
import pandas as pd
import os

# Сюда прописать директорию, где лежат json файлы. По дефолту берет из той же, где и файл
list_files = os.listdir("./")
list_json_files = []

for file in list_files:
    if file.endswith(".json"):
        list_json_files.append(file)

df_dict = {}

print(list_json_files) 

for file in list_json_files:

    file_df = open(file, 'r', encoding='utf-8')

    df_json  = file_df.read()
    file_df.close()


    df_after_parse = json.loads(df_json)
    phrases_count = len(df_after_parse['userSays'])

    current_phrase_number = 0
    list_intent_phrases = []

    intent = df_after_parse['name']

    while current_phrase_number < phrases_count:
        phrase = ""

        count_parts_phrase = len(df_after_parse['userSays'][current_phrase_number]['data'])
        current_part_number = 0    

        while current_part_number < count_parts_phrase:

            phrase = phrase + df_after_parse['userSays'][current_phrase_number]['data'][current_part_number]['text']
            current_part_number = current_part_number + 1
        
        print(phrase)
        current_phrase_number = current_phrase_number + 1
        list_intent_phrases.append(phrase)     


    df = pd.DataFrame({'Intent': intent,
                    'Phrase': list_intent_phrases})  

    # куда сохраняем
    df.to_csv(f"./intents.csv", mode='a', index=False, encoding='utf-8-sig')






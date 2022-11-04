import requests
import csv
import os
import numpy as np

# Токен для тестов
test_token = "k_xp1fwhr8"

token_0 = "k_vmyq50so" #
token_1 = "k_og2q816b" #
token_2 = "k_6938h0jt" #
token_3 = "k_8pckz9id" #
token_4 = "k_6cezfuj1" #
token_5 = "k_0p7e1rqn" #
token_6 = "k_cgmtp37h" #
token_7 = "k_jgk21r5t" #
token_8 = "k_ids2kvyd" #
token_9 = "k_mpgnwqrm" #
token_10 = "k_a0nsmdge" #
token_11 = "k_aav3sqh9" #
token_12 = "k_2o9o6o88" # -
token_13 = "k_gtb10g0l"
token_14 = "k_ussq040l" # -
token_15 = "k_v5xn58o4"
token_16 = "k_47ckyb0e"
token_17 = "k_25t5gytc"
token_18 = "k_pv1u9lep"
token_19 = "k_ymdnu13t"

token_20 = "k_gi4w5gdh"
token_21 = "k_2tmp9xw1"
token_22 = "k_5amy90jg"
token_23 = "k_7md5kz1u"
token_24 = "k_ejfu9ubn"
token_25 = "k_6xf92k3z"

token_26 = "k_t2ndx3o4"
token_27 = "k_vfl8z6oe"
token_28 = "k_dczfh346"
token_29 = "k_ak61czvp"
token_30 = "k_wakdjbh2"
token_31 = "k_ro1xxyqx"

token_32 = "k_16zhx6dg"
token_33 = "k_t6q6q81t"
token_34 = "k_zi7did21"
token_35 = "k_23f5buy9"
token_36 = "k_wkklphbz"
token_37 = "k_dz0e8fqy"

token_list = [token_18, token_19]


file_path_imdb = "C:/Users/Home PC/Desktop/Python/VKR/Parsing_dataset/imdb_parsing.csv"

if (not os.path.exists(file_path_imdb)) or os.path.getsize(file_path_imdb) == 0:
    with open("C:/Users/Home PC/Desktop/Python/VKR/Parsing_dataset/imdb_parsing.csv", "w", encoding="utf-8",newline='') as file:
        a_pen = csv.writer(file)
        a_pen.writerow(("imdb_id", "star_list", "writer_list", "director_list", "companies_list", "awards", "imdb_budget", "imdb_fees", "releaseDate", "runtimeStr", "runtime_imdb"))

with open("C:/Users/Home PC/Desktop/Python/VKR/Parsing_dataset/detailed_kp.csv", "r", encoding="utf-8",newline='') as input_file, open("C:/Users/Home PC/Desktop/Python/VKR/Parsing_dataset/imdb_parsing.csv", "a", encoding="utf-8",newline='') as output_file:
    reader = csv.reader(input_file)
    writer = csv.writer(output_file)
    count = 0
    response_counter = 0
    x = 0
    token = token_list[x]
    for j in reader:
        count += 1
        if count == 1:
            continue
        if j[1] == '':
            writer.writerow(("No IMDB Info", "No IMDB Info", "No IMDB Info", "No IMDB Info", "No IMDB Info", "No IMDB Info", "No IMDB Info",
                             "No IMDB Info", "No IMDB Info", "No IMDB Info", "No IMDB Info"))
            continue
        if response_counter == 100:
            x += 1
            if x == 2:
                break
            token = token_list[x]
            response_counter = 0
            # Смена токена
        url = f"https://imdb-api.com/en/API/Title/{token}/{j[1]}"
        response = requests.get(url)
        response_counter += 1
        data = response.json()

        try:
            if "Maximum usage" in data['errorMessage']:
                break
        except:
            pass
        try:
            if data['errorMessage'] == 'Invalid API Key':
                print(f'API-key {token} заблокировали')
                break
        except:
            pass

        try:
            star_list = []
            for i in data['starList']:
                star_list.append(i['name'])
        except:
            star_list = None

        # Есть и в обычном запросе
        try:
            writer_list = []
            for i in data['writerList']:
                writer_list.append(i['name'])
        except:
            writer_list = None

        # Есть и в обычном запросе
        try:
            director_list = []
            for i in data['directorList']:
                director_list.append(i['name'])
        except:
            director_list = None

        # Есть и в обычном запросе
        try:
            companies_list = []
            for i in data['companyList']:
                companies_list.append(i['name'])
        except:
            companies_list = None
        try:
            awards = data['awards']
        except:
            awards = None

        try:
            imdb_budget = data["boxOffice"]["budget"]
        except:
            imdb_budget = None

        try:
            imdb_fees = data["boxOffice"]["cumulativeWorldwideGross"]
        except:
            imdb_fees = None

        try:
            releaseDate = data["releaseDate"]
        except:
            releaseDate = None

        # RuntimeMinsStr
        try:
            runtimeStr = data['runtimeStr']
        except:
            runtimeStr = None

        # ImdbRuntimeMins
        try:
            runtime_imdb = data['runtimeMins']
        except:
            runtime_imdb = None


        print('imdb_id', star_list, writer_list, director_list, companies_list, awards, imdb_budget, imdb_fees, releaseDate, runtimeStr, runtime_imdb)
        writer.writerow((j[1], star_list, writer_list, director_list, companies_list, awards, imdb_budget, imdb_fees, releaseDate, runtimeStr, runtime_imdb))
                # Что нужно собрать
                # Кинонаграды
                # imdb_trailer
                # imdb_poster
                # Режиссер
                # Сценарист
                # Возрастной рейтинг
                # Главные звезды


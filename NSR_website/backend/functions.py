import csv
import json
import pandas as pd
import sys, operator
import os
import requests
from bs4 import BeautifulSoup

DIRNAME = os.path.dirname(__file__)

def read_json(name):
    with open(os.path.join(DIRNAME, 'data', name+'.json'), 'r') as load_f:
        json_data = json.load(load_f)
        return json_data


def csv_to_json(name):
    f = open("data/"+name+".csv")
    # Change each fieldname to the appropriate field name. I know, so difficult.
    reader = csv.DictReader(f)
    # Parse the CSV into JSON
    out = json.dumps([row for row in reader])
    file_name = "data/" + name + ".json"
    # Save the JSON
    f = open(file_name, 'w')
    f.write(out)


def getrank(name):
    if name == 'culture':
        df = pd.read_csv(os.path.join(DIRNAME, 'data', 'Data_Culture_norm.csv'))
        df = df.sort_values(by='Culture', axis=0, ascending=False)
        df.to_json('data/'+name+'.json', orient='records', lines=True)
    if name == 'sustainbility':
        df = pd.read_csv(os.path.join(DIRNAME, 'data', 'Data_Sustainability_norm.csv'))
        df = df.sort_values(by='Opt_Index', axis=0, ascending=False)
        df.to_json('data/' + name + '.json', orient='records', lines=True)
    if name == 'oppotunity':
        df = pd.read_csv(os.path.join(DIRNAME, 'data', 'Data_OportInd_norm_v2.csv'))
        df = df.sort_values(by='Opt_Index', axis=0, ascending=False)
        df.to_json('data/' + name + '.json', orient='records', lines=True)


def get_color_data():
    with open(DIRNAME+'/data/total.json', 'r') as f:
        data = json.load(f)
        return data


def get_selected_score(target):
    df = pd.read_csv(os.path.join(DIRNAME, 'data', 'total.csv'))
    target = int(target)
    val1 = df[(df['GEOID'] == target)]['Cult_Index'].values[0]
    print(val1)
    val2 = df[(df['GEOID'] == target)]['Sust_Index'].values[0]
    val3 = df[(df['GEOID'] == target)]['Opt_Index'].values[0]

    out = []
    cur1 = {}
    cur1['name'] = 'culture'
    cur1['score'] = round(val1, 2)
    df['Rank'] = df["Cult_Index"].rank()
    cur1['rank'] = df[(df["GEOID"] == target)]['Rank'].values[0]
    out.append(cur1)
    cur2 = {}
    cur2['name'] = 'sustainability'
    cur2['score'] = round(val2, 2)
    df['Rank'] = df["Sust_Index"].rank()
    cur2['rank'] = df[(df["GEOID"] == target)]['Rank'].values[0]
    out.append(cur2)
    cur = {}
    cur['name'] = 'opportunity'
    cur['score'] = round(val3, 2)
    df['Rank'] = df["Opt_Index"].rank()
    cur['rank'] = df[(df["GEOID"] == target)]['Rank'].values[0]
    out.append(cur)
    return out


def get_selected_score_2(features_tag,features):
    with open('data/total.json', 'r') as f:
        df = json.load(f)
    cur_max = [0, 0, 0, 0]
    cur_min = [100, 100, 100, 100]
    out = []
    for row in df:
        val1 = 0
        val2 = 0
        val3 = 0
        if features_tag == 'culture':
            for feature in features:
                if row[feature] != '':
                    val1 = val1 + float(row[feature])
            val1 = val1 / len(features)
            val2 = float(row["Sust_Index"])
            val3 = float(row["Opt_Index"])
        elif features_tag == 'sustainability':
            for feature in features:
                if row[feature] != '':
                    val2 = val2 + float(row[feature])
            val1 = float(row["Cult_Index"])
            val2 = val2 / len(features)
            val3 = float(row["Opt_Index"])
        elif features_tag == 'opportunity':
            for feature in features:
                if row[feature] != '':
                    val3 = val3 + float(row[feature])
            val1 = float(row["Cult_Index"])
            val2 = float(row["Sust_Index"])
            val3 = val3 / len(features)
        sum = (val1 + val2 + val3)/3
        cur_max[0] = max((cur_max[0], val1))
        cur_max[1] = max((cur_max[1], val2))
        cur_max[2] = max((cur_max[2], val3))
        cur_max[3] = max((cur_max[3], sum))
        cur_min[0] = min((cur_min[0], val1))
        cur_min[1] = min((cur_min[1], val2))
        cur_min[2] = min((cur_min[2], val3))
        cur_min[3] = min((cur_min[3], sum))
        cur = {}
        cur['GEOID'] = row["GEOID"]
        cur['culture'] = round(val1,2)
        cur['sustainability'] = round(val2,2)
        cur['opportunity'] = round(val3,2)
        cur['vibrancy'] = round(sum,2)
        out.append(cur)
    return out


def get_row_data(target):
    dic = {
        'INDI_2_2': 'Percent of population that is obese',
        'INDI_2_1': 'Percent of population receiving SNAP benefits',
        'INDI_1_21n1_fam': 'Current poverty levels as defined by USA, by sections of the population. {woman}',
        'INDI_1_21n1_sing_women': 'Current poverty levels as defined by USA, by sections of the population. {parents}',
        'INDI_1_31n4': 'Percent of people covered by at least one social protection benefit, by sections of the population',
        'INDI_1_31n3': 'Percentage of population receiving TANF, by sections of the population.',
        'INDI_1_31n7': 'Percent of people with severe disabilities receiving disability cash benefit, by sections of the population',
        'INDI_1_31n8': 'Percent of people receiving unemployment cash benefit, by sex, or other relevant sections of population, by sections of the population',
        'INDI_3_41n1': 'Percent of people with cardiovascular disease, by section of population',
        'INDI_3_41n3': 'Percent of people with diabetes disease, by section of population',
        'INDI_3_41n2': 'Percent of people with cancer, by section of population',
        'INDI_3_51n3': 'Percent of people with cardiovascular disease, by section of population',
        'INDI_3_61n1': 'Number or percent of people who are experiencing issues with substance abuse and/or addiction',
        'INDI_4_22n1': 'Percentage of 2, 3, and 4 year children attending preschool programs, by section of population',
        'INDI_4_31n1': 'Percentage of adults with did not complete high school or high school equivalency, by section of population',
        'INDI_4_31n2': 'Percentage of adults that the highest educational level is high school or high school equivalency, by section of population.',
        'INDI_4_31n3': 'Percentage of adults who have attending college, by section of population.',
        'INDI_4_31n4': 'Percentage of adults who have earned a 1 year or 2 year professional certificate or an Associates Degree, by section of population.',
        'INDI_4_31n5': 'Percentage of adults who have earned a 4 year degree, by section of population.',
        'INDI_4_31n6': 'Percentage of adults who have earned a Graduate degree or higher, by section of population.',
        'INDI_5_1': '',
        'INDI_6_31n3': '',
        'INDI_6_31n2': '',
        'INDI_7_12n1': '',
        'INDI_7_1': '',
        'INID_11_71n1': 'Sustainable Cities & Communities',
        'INDI_8_52n1': '',
        'INDI_8_61n1': '',
        'INDI_8_61n2_2': '',
        'INDI_9_c1n1': '',
        'INDI_10_2': 'Income distribution',
        'INDI_10_3': 'Racial segregation',
        '12_toxic_release_of_air': '',
        'INDI_15_1': '',
    }
    words = target.split(";")
    with open(os.path.join(DIRNAME, 'data', 'total.json'), 'r') as f:
        df = json.load(f)
    for row in df:
        if row["GEOID"] == words[0]:
            out = []
            for key, value in row.items():
                #Origin_name = df
                cur = {}
                cur['id'] = key
                if(dic.get(key)):
                    cur['name'] = dic.get(key)
                else:
                    cur['name'] = key
                cur['value'] = value
                out.append(cur)
    return out


def getname(target):
    df = pd.read_csv(os.path.join(DIRNAME, 'data', 'Data_OportInd_norm_v2.csv'))
    val1 = df[df['GEOID'] == int(target)]['Tract'].values[0]
    return val1


def get_address_id(name, zip_code):
    street_name = name.replace(' ', '+')
    url = "https://geocoding.geo.census.gov/geocoder/geographies/address?street="+street_name+"&city=pittsburgh&state=PA&zip="+zip_code+"&benchmark=4&vintage=4"
    request_headers = {
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3',
        'Accept-Encoding': 'gzip, deflate, br',
        'Accept-Language': 'en-US,en;q=0.9,zh-CN;q=0.8,zh;q=0.7,la;q=0.6',
        'Cache-Control': 'private',
        'Connection': 'keep-alive',
        'Cookie': '_ga=GA1.2.1704734502.1565025028; s_fid=43B81A3A77958FEE-1E67575C35C79A52; _gid=GA1.2.1680803319.1565535787; s_cc=true; ak_bmsc=04B53E375FAACDD33EDED149DDC6806117C91F95ED6D0000292E505D426DD71A~plhFsiEdAstySJU2jQFP+t9402iI/0ztp17Aq6QzaBD3AGghvE0ds4gnYJzhXWoKFyZYabhAu8ljleQgXIUMW4oXXbkEJrhZuDY5TMTUdy8g1gQwN+3Aq6IkIExTaPR1BQAd//V4vMadpJkASESUasmeD79OdYxQh4rwRkmHsfF7lsTneANSN8Uq3v1cjPWcQELsQe3hyKuDdcJwErTeeuTI+X2kDjLfmj7hhO54rjwIMgyij9Kdff8NrEZa7cUtAq; s_getNewRepeat=1565536188835-Repeat; bm_sv=996D5CDD182F7D0178AB876688106110~vaNahqx+vD232oQy83WgTgagtL4sSxlOIcHZIyIpjGJyXKjGFIpbw/GZTlD+jIi4ofAKtp1N77k/zdUjjKNzgw5c5nCgJ78udvXt6zcs7P0Cy7N5yCGMKoP09c9u4QO5KwLgdxm1nnvNgIVefFqoDCRYRADPuQvwJ4E8LanBF24=; ADRUM=s=1565536230579&r=https%3A%2F%2Fwww.census.gov%2Fprograms-surveys%2Fgeography%2Fguidance%2Fgeo-identifiers.html%3F0; s_gnr=1565539827667-Repeat; undefined_s=First%20Visit; s_vnum=1570209028694%26vn%3D6; s_invisit=true; s_sq=cebucensusglobalprod%3D%2526c.%2526a.%2526activitymap.%2526page%253DWelcome%252520to%252520Geocoder%2526link%253DVintages%2526region%253Dfi_vintage_benchmark%2526pageIDType%253D1%2526.activitymap%2526.a%2526.c; JSESSIONID=962Bch0K9DBkf6zbNvhDWWk8pXwmKZsx2GgXV5wn0JspGdlIActe!-329365693',
        'Host': 'geocoding.geo.census.gov',
        'Sec-Fetch-Mode': 'navigate',
        'Sec-Fetch-Site': 'none',
        'Sec-Fetch-User': '?1',
        'Upgrade-Insecure-Requests': '1',
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.100 Safari/537.36'
    }
    wbdata = requests.get(url, headers=request_headers).content
    soup = BeautifulSoup(wbdata, 'lxml')
    target = soup.find("div", {"id": "pl_gov_census_geo_geocoder_domain_AddressResult"})

    con = target.contents
    con_next = str(con[len(con) - 1])
    if "Census Tracts: " in con_next:
        con_next = con_next.split("Census Tracts: ")[1]
        con_next = con_next.split("<br/>")[1]
        con_next = con_next.split("GEOID: ")[1]
        return con_next


def get_selected_feature_in_census(features):
    df = pd.read_csv(os.path.join(DIRNAME, 'data', 'total.csv'))
    val = []


def get_vibrancy_rank(target):
    df = pd.read_csv(os.path.join(DIRNAME, 'data', 'total.csv'))
    target = int(target)
    df['Rank'] = df["Vibrant_Index"].rank()
    out = df[(df["GEOID"] == target)]['Rank'].values[0]
    return out
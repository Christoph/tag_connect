import pandas as pd

happy = pd.read_csv("../datasets/2017.csv")
facts = pd.read_json("../datasets/factbook.json")

# add new columns
happy["internet_percent_of_population"] = None
happy["cellular_percent"] = None
happy["surplus_deficit_percent_of_gdp"] = None
happy["familiy_income_gini"] = None
happy["gdp_per_capita_dollar"] = None
happy["inflation_rate"] = None
happy["military_expenditures"] = None
happy["map_reference"] = None
happy["biggest_official_language"] = None
happy["population"] = None

for raw_country in happy["Country"].tolist():
    country = raw_country.lower().replace(" ", "_")

    # Translate country names between datasets
    if country == "czech_republic":
        country = "czechia"
    if country == "taiwan_province_of_china":
        country = "taiwan"
    if country == "south_korea":
        country = "korea_south"
    if country == "north_cyprus":
        country = "cyprus"
    if country == "hong_kong_s.a.r.,_china":
        country = "hong_kong"
    if country == "palestinian_territories":
        country = "west_bank"
    if country == "myanmar":
        country = "burma"
    if country == "congo_(brazzaville)":
        country = "congo_republic_of_the"
    if country == "congo_(kinshasa)":
        country = "congo_democratic_republic_of_the"
    if country == "ivory_coast":
        country = "cote_d'_ivoire"

    if "internet" in data["communications"]:
        if "users" in data["communications"]["internet"]:
            if "percent_of_population" in data["communications"]["internet"]["users"]:
                happy.loc[happy["Country"] == raw_country, "internet_percent_of_population"] = data["communications"]["internet"]["users"]["percent_of_population"]

    try:
        happy.loc[happy["Country"] == raw_country, "cellular_percent"] = data["communications"]["telephones"]["mobile_cellular"]["subscriptions_per_one_hundred_inhabitants"]
    except KeyError:
        print(raw_country)
        continue

    try:
        happy.loc[happy["Country"] == raw_country, "surplus_deficit_percent_of_gdp"] = data["economy"]["budget_surplus_or_deficit"]["percent_of_gdp"]
    except KeyError:
        print(raw_country)
        continue

    if "distribution_of_family_income" in data["economy"]:
        happy.loc[happy["Country"] == raw_country, "familiy_income_gini"] = data["economy"]["distribution_of_family_income"]["annual_values"][0]["value"]

    try:
        happy.loc[happy["Country"] == raw_country, "gdp_per_capita_dollar"] = data["economy"]["gdp"]["per_capita_purchasing_power_parity"]["annual_values"][0]["value"]
    except KeyError:
        print(raw_country)
        continue

    try:
        happy.loc[happy["Country"] == raw_country, "inflation_rate"] = data["economy"]["inflation_rate"]["annual_values"][0]["value"]
    except KeyError:
        print(raw_country)
        continue

    if "expenditures" in data["military_and_security"]:
        happy.loc[happy["Country"] == raw_country, "military_expenditures"] = data["military_and_security"]["expenditures"]["annual_values"][0]["value"]

    try:
        happy.loc[happy["Country"] == raw_country, "map_reference"] = data["geography"]["map_references"]
    except KeyError:
        print(raw_country)
        continue

    try:
        happy.loc[happy["Country"] == raw_country, "biggest_official_language"] = data["people"]["languages"]["language"][0]["name"]
    except KeyError:
        print(raw_country)
        continue

    try:
        happy.loc[happy["Country"] == raw_country, "population"] = data["people"]["population"]["total"]
    except KeyError:
        print(raw_country)
        continue

happy.to_csv("happiness.csv", index=False)

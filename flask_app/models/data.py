import pandas as pd


# Read the data from the "data.txt" file and set column names
column_names = [
    "CREDIT SCORE",
    "FIRST PAYMENT DATE",
    "FIRST TIME HOMEBUYER FLAG",
    "MATURITY DATE",
    "METROPOLITAN STATISTICAL AREA (MSA) OR METROPOLITAN DIVISION",
    "MORTGAGE INSURANCE PERCENTAGE (MI)",
    "NUMBER OF UNITS",
    "OCCUPANCY STATUS",
    "ORIGINAL COMBINED LOAN-TO-VALUE (CLTV)",
    "ORIGINAL DEBT-TO-INCOME (DTI) RATIO",
    "ORIGINAL UPB",
    "ORIGINAL LOAN-TO-VALUE (LTV)",
    "ORIGINAL INTEREST RATE",
    "CHANNEL",
    "PREPAYMENT PENALTY MORTGAGE (PPM) FLAG",
    "AMORTIZATION TYPE",
    "PROPERTY STATE",
    "PROPERTY TYPE",
    "POSTAL CODE",
    "LOAN SEQUENCE NUMBER",
    "LOAN PURPOSE",
    "ORIGINAL LOAN TERM",
    "NUMBER OF BORROWERS",
    "SELLER NAME",
    "SERVICER NAME",
    "SUPER CONFORMING FLAG",
    "PRE-RELIEF REFINANCE LOAN SEQUENCE NUMBER",
    "PROGRAM INDICATOR",
    "RELIEF REFINANCE INDICATOR",
    "PROPERTY VALUATION METHOD",
    "INTEREST ONLY INDICATOR (I/O INDICATOR)",
    "MI CANCELLATION INDICATOR"
]

#data_file = "/mnt/c/Users/14023/Downloads/sample_orig_2022.txt"
path_data_file = 'C:/Users/14023/Downloads/sample_orig_2023.txt'

data = pd.read_csv(path_data_file, sep="|", names=column_names)

# Function 1: Get the mean credit score for the whole year
def get_mean_credit_score():
    credit_scores = {
        "lowest": {
            "credit_score": int(data["CREDIT SCORE"].min()),
            "average_interest_rate": round(data[data["CREDIT SCORE"] == data["CREDIT SCORE"].min()]["ORIGINAL INTEREST RATE"].mean(), 2)
        },
        "mean": {
            "credit_score": round(data["CREDIT SCORE"].mean(), 2),
            "average_interest_rate": round(data[data["CREDIT SCORE"] == data["CREDIT SCORE"].mean()]["ORIGINAL INTEREST RATE"].mean(), 2)
        },
        "highest": {
            "credit_score": int(data["CREDIT SCORE"].max()),
            "average_interest_rate": round(data[data["CREDIT SCORE"] == data["CREDIT SCORE"].max()]["ORIGINAL INTEREST RATE"].mean(), 2)
        }
    }

    return credit_scores

# Function 2: Get total number of buyers, first time buyers, and their percentage
def get_buyer_statistics():
    buyer_counts = {}
    unit_types = data["PROPERTY TYPE"].unique()

    for unit_type in unit_types:
        unit_data = data[data["PROPERTY TYPE"] == unit_type]
        total_buyers = unit_data.shape[0]
        first_time_buyers = unit_data[unit_data["FIRST TIME HOMEBUYER FLAG"] == "Y"].shape[0]
        percentage_first_time_buyers = round((first_time_buyers / total_buyers) * 100, 2)

        buyer_counts[unit_type] = {
            "total_buyers": total_buyers,
            "first_time_buyers": first_time_buyers,
            "percentage_first_time_buyers": percentage_first_time_buyers
        }

    return buyer_counts

# Function 3: Get total number of units sold, occupied, and vacant
def get_units_statistics():
    unit_counts = {}
    unit_types = data["PROPERTY TYPE"].unique()

    for unit_type in unit_types:
        unit_data = data[data["PROPERTY TYPE"] == unit_type]
        total_units = int(unit_data["NUMBER OF UNITS"].sum())
        occupied_units = int(unit_data[unit_data["OCCUPANCY STATUS"] == "P"].shape[0])
        vacant_units = total_units - occupied_units

        unit_counts[unit_type] = {
            "total_units": total_units,
            "occupied_units": occupied_units,
            "vacant_units": vacant_units
        }

    return unit_counts

# Function 4: Get top 10 states which sold the most number of units
def get_top_10_states_most_units():
    top_10_states = data["PROPERTY STATE"].value_counts().head(10).reset_index()
    top_10_states.columns = ["State", "Units Sold"]
    top_10_states = top_10_states.sort_values(by="Units Sold", ascending=False)
    return top_10_states.to_dict(orient="records")

# Function 5: Get top 10 states which sold the least number of units
def get_top_10_states_least_units():
    bottom_10_states = data["PROPERTY STATE"].value_counts().tail(10).reset_index()
    bottom_10_states.columns = ["State", "Units Sold"]
    bottom_10_states = bottom_10_states.sort_values(by="Units Sold")
    return bottom_10_states.to_dict(orient="records")

# Function 6: Get mean price of houses
def get_mean_price():
    mean_prices = data.groupby(["PROPERTY STATE", "PROPERTY TYPE"])["ORIGINAL UPB"].mean()
    mean_prices = mean_prices.reset_index()
    mean_prices = mean_prices.rename(columns={"ORIGINAL UPB": "mean_price"})
    mean_prices["mean_price"] = mean_prices["mean_price"].round(2)
    return mean_prices.to_dict(orient="records")

# Function 7: Get mean loan amount taken
def get_mean_loan_amount():
    mean_loan_amount = round(data["ORIGINAL LOAN-TO-VALUE (LTV)"].mean(), 2)
    return {"loan_mean_amount": mean_loan_amount}

# usage:
#print("Mean Credit Score:", get_mean_credit_score())
#print("Buyer Statistics:", get_buyer_statistics())
#print("Units Statistics:", get_units_statistics())
#print("Top 10 States (Most Units):", get_top_10_states_most_units())
#print("Top 10 States (Least Units):", get_top_10_states_least_units())
#print("Mean Price of Houses:", get_mean_price())
#print("Mean Loan Amount Taken:", get_mean_loan_amount())

#dummy data
data2 = pd.DataFrame({
    'year': [2020, 2020, 2021, 2021],
    'issuer': ['Issuer1', 'Issuer2', 'Issuer1', 'Issuer3'],
    'loan_amount': [1000000, 2000000, 1500000, 2500000]
})

def get_summary():
    return data2.describe()

def get_top_loan_issuers():
    return data2['issuer'].value_counts().head(10)

def get_loan_origination_by_year():
    return data2.groupby('year')['loan_amount'].sum()

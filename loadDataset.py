import pandas as pd
import os

#Load Data
csv_file = os.path.join("./phishingemails_dataset", "Phishing_Email.csv")
data = pd.read_csv(csv_file)

for i in range(10):
    row = data.iloc[i]
    email_text = row['Email Text']
    email_type = row['Email Type']

    print("Email:", email_text)
    print("Type:", email_type)
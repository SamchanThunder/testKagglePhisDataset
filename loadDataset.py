import pandas as pd
import os

#Load Data
csv_file = os.path.join("./phishingemails_dataset", "Phishing_Email.csv")
data = pd.read_csv(csv_file)

thirdRow = data.iloc[3]
email_text = thirdRow['Email Text']
email_type = thirdRow['Email Type']

print("First email text:", email_text)
print("First email type:", email_type)
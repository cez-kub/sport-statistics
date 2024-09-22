import requests
import os
from datetime import datetime
import tabula
import pandas as pd

# Get the current date and time for file naming
now = datetime.now().strftime("%Y-%m-%d-%H%M%S")

# URL of the PDF file
pdf_url = 'https://wtafiles.wtatennis.com/pdf/rankings/Singles_Numeric.pdf'

# Get the project root directory 
project_root = os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))

# Download the PDF file
response = requests.get(pdf_url)
output_pdf_path = os.path.join(project_root, "data", "raw", f"wta-ranking-single-{now}.pdf") # Define the output path
print("Path: ", output_pdf_path)

os.makedirs(os.path.dirname(output_pdf_path), exist_ok=True) # Save the PDF to the specified location
with open(output_pdf_path, 'wb') as file:
    file.write(response.content)

print(f"PDF file downloaded to {output_pdf_path}")

# Parse the PDF and extract the table
tables = tabula.read_pdf(output_pdf_path, pages='all')
rankings_df = pd.concat(tables, ignore_index=True)

# Print the extracted DataFrame
print(rankings_df)

# Optional: Save the DataFrame to a CSV file
output_csv_path = os.path.join(project_root, "data", "raw", f"wta-ranking-single-{now}.csv")
rankings_df.to_csv(output_csv_path, index=False)

print(f"Ranking data saved as CSV to {output_csv_path}")
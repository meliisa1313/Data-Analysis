#By: Michał Marusiński

import re
import pandas as pd
import os
from pathlib import Path

def get_patient_number(file_name):
    match = re.search(r'S\d{2}', file_name, re.IGNORECASE)
    return match.group(0).upper()




def get_valid_patients(data: pd.DataFrame) -> list:
    return data['Numer osoby'].to_list()




def merge_csv_files(input_directory, valid_patients_list : list):
    
    list_of_files = os.listdir(input_directory)
    
    if "valid_patients_data.csv" in list_of_files:
        print("Merged file already exists")
        return pd.read_csv(os.path.join(input_directory, "valid_patients_data.csv"))
    
    else:
        
        merged_df = pd.DataFrame()
        for file in os.listdir(input_directory):
            
            if file.endswith('.csv'):
                
                patient_number = get_patient_number(file)
                if patient_number and patient_number in valid_patients_list:
                    
                    file_path = os.path.join(input_directory, file)
                    valid_patient_df = pd.read_csv(file_path)
                    merged_df = pd.concat([merged_df, valid_patient_df], ignore_index=True)
                    print(f"Merging data with patient: {patient_number} ---> file: {file_path}")
        
        if not merged_df.empty:
            
            df_path = Path(input_directory + r"\valid_patients_data.csv")
            merged_df.to_csv(df_path, index=False)
        return merged_df

#get_patient_number("2023_Feb_02_1229s70")




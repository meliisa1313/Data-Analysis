#By: Michał Marusiński



import pandas as pd
import math 


def clear_nan_values(data: pd.DataFrame) -> pd.DataFrame:
    columns_dropped = []

    print("Amount of NaN values in columns: ")
    for column in data.columns:
        
        nan_sum = data[column].isna().sum()
        print(f"Column: --- {column} --- amount of NaN values: --- {nan_sum} ---")
        
        if nan_sum > 683:
            
            data.drop([column], axis = 1, inplace = True)
            columns_dropped.append(column)
            continue
            
        nan_indices = data[column].index[data[column].isna()]
        
        for i in nan_indices:
            
            if data[[column]].dtypes.values == 'float64':
                
                if i == 0:  
                    
                    if not pd.isna(data.loc[i+1, column]):
                        data.loc[i, column] = data.loc[i + 1, column]
                    else:
                        data.loc[i, column] = data[column].mean()
                        
                elif i == data.shape[0] - 1:
                    
                    if not pd.isna(data.loc[i-1, column]):
                        data.loc[i, column] = data.loc[i - 1, column]
                    else:
                        data.loc[i, column] = data[column].mean()

                else:
                    
                        if pd.isna(data.loc[i - 1, column]) and pd.isna(data.loc[i + 1, column]):
                            data.loc[i, column] = data[column].mean()
                            
                        elif pd.isna(data.loc[i - 1, column]):
                            data.loc[i, column] = data.loc[i + 1, column]
                            
                        elif pd.isna(data.loc[i + 1, column]):
                            data.loc[i, column] = data.loc[i - 1, column]
                            
                        else:
                            data.loc[i, column] = ( data.loc[i - 1, column] + data.loc[i + 1, column] ) / 2 

                if column in ['Arousal_rating.response', 'Valence_rating.response']:
                    data.loc[i, column] = math.floor(data.loc[i,column])
                    
    print(f"Amount of columns dropped: {len(columns_dropped)}") 
               
    return data
#By: Michał Marusiński

from sklearn.metrics import classification_report, accuracy_score, confusion_matrix
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os
def evaluation(y_test: pd.Series, y_pred: pd.Series, name_of_classifier : str, feature_predicted : str, folder_path : str = os.getcwd(), cross_validation : bool = False,
               standarized : bool = False):
    
    
    folder_path = os.path.join(folder_path, name_of_classifier)
    
        
    
    if not os.path.exists(folder_path):
        os.makedirs(folder_path)
    
    
    accuracy = accuracy_score(y_test, y_pred)
    print(f'Accuracy: {accuracy}')
    print('Classification Report:')
    report = classification_report(y_test, y_pred)
    print(report)

    PATH_txt = os.path.join(folder_path, f"classification_report_{feature_predicted}")
        
    if standarized:
        PATH_txt += "_standarized"
        
    if cross_validation:
        PATH_txt+="_cross_validation.txt"
    else:
        PATH_txt+=".txt"
        
        
    with open(PATH_txt, 'w') as file:
        file.write(f'Accuracy: {accuracy}\n\n\n')
        file.write('Classification Report:\n')
        file.write(report)
        print(f"Accuracy score and classification report successfully saved to {PATH_txt}")
    
    plt.figure(figsize=(8, 4))
    sns.heatmap(confusion_matrix(y_test, y_pred), annot=True, fmt='d', cmap='Blues', xticklabels=['0', '1'], yticklabels=['0', '1'])
    plt.title('Confusion Matrix')
    plt.xlabel('Predicted')
    plt.ylabel('Real')
    
    
    PATH_png = os.path.join(folder_path, f"confusion_matrix_{feature_predicted}")
    
    if standarized:
        PATH_png += "_standarized"
    
    if cross_validation:
        PATH_png+="_cross_validation.png"
    else:
        PATH_png+=".png"
    
    plt.savefig(PATH_png)
    print(f"Confusion matrix successfully saved to {PATH_png}")
    plt.show()
#By: Michał Marusiński


param_grids = {
     'knn': {
        'n_neighbors': [3, 4, 5, 6, 7, 8],
        'weights': ['uniform', 'distance'],
        'metric': ['euclidean', 'manhattan']
    },
    'decision_tree': {
        'criterion': ['gini', 'entropy'],
        'splitter': ['best'],
        'max_depth': [10],
        'min_samples_split': [2, 4, 6],
        'min_samples_leaf': [1, 2]
    },
'random_forest': {
        'n_estimators': [50],
        'criterion': ['gini', 'entropy'],
        'max_depth': [10],
        'min_samples_split': [2, 4],
        'min_samples_leaf': [1, 2],
    },
'xgboost': {
        'n_estimators': [50, 100, 150],
        'learning_rate': [0.01, 0.1],
        'max_depth': [3, 6],
        'subsample': [0.8, 1.0],
        'colsample_bytree': [0.8, 1.0],
        'gamma': [0, 0.1],
        'reg_alpha': [0, 0.1],
        'reg_lambda': [1, 1.5]
    },
    'svm': {
        'C': [0.1, 1],
        'kernel': ['rbf', 'sigmoid'],
        'gamma': ['scale', 'auto'],
    },
    'lightgbm': {
        'n_estimators': [10, 50, 100, 150],
        'learning_rate': [0.01, 0.1],
        'num_leaves': [31, 50],
        'max_depth': [20, 40],
        'min_child_samples': [20, 40],
        'subsample': [0.8, 1.0],
        'colsample_bytree': [0.8, 1.0]
    }
}
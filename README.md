# data-analysis-4

Here - all of the Melisa's work was presented. In some of the files Jan made a contribution (in the beginning of all the files authors of them were written). Inside the main folder there are a few subfolders in which specific actions took place so to properly pigeonhole every single one. Subfolders:

- **Binary classification of ratings** --> folder consisting of created Models for predicting valence / arousal rating grade of every participant.

  - **EDA and preprocessing of data** --> Jupyter notebook consisting of full Exploratory Data Analysis of ratings files for every participant. A notebook consists of the process of merging every participant file into one big DataFrame. By then it's cleared out of unnecessary columns, NaN values etc. By then some histograms were plotted and scatter plots were done. Prepared DataFrame was updated after the script execution to make it ready for ML models.
    - `empty_values_clear_func` --> module with function to clear out NaN values by deleting / replacing them with mean values of their neighbours (depending on number of NaNs).
    - `patient_df_merge` --> module to merge all of participants' unique findings.

  - **rating 1 - 4 - 9** --> Folder consists of 2 Jupyter scripts (ML models for valence - arousal - all classifiers / - standardized) where 6 models were implemented - SVM, XGBoost, Decision Trees, Random Forest, k-Nearest Neighbours, LightGBM all of which were taken from the Sci-kit learn library. In each of the files there are 5 main steps: preparing preprocessed data (uploaded from EDA script) by labeling values into high (5-9 rating) / low (4 and lower) and splitting it into train/test. Then there are 4 processes of model testing (For every feature there's 2 of them, each consisting of testing models with random parameters or with GridSearch tuner). File with results of models is saved into a specified folder created after the script is run.
  
  - **rating 1 - 5 - 9** --> Similar to the previous file but with changed labeling type (1 - 5 low and 6 - 9 high).
    - `model_eval` --> module to make classification report and confusion matrix for given model into an input and to save them in txt and png.
    - `param_grids` --> huge dictionary of chosen hyperparameters for specific model types.

- **processing comments** --> folder to choose valid participants of the experiment based on given comments describing the course of the study.
  - `processing_comments_participants_pic` --> some kind of an interface to sort out valid patients: for a given comment we choose if the sample is valid (1) or invalid (0). That's how they were sorted. Unfortunately, some of the samples were initially sorted out wrong, that's why the second script (`processsing_comments_correction`) was done.
  - `Processing_comments_correction` --> Taken from rubbish some of the "invalid" files were presented to the user once again and the same method (valid/invalid) was implemented. Fortunately with that, 4 additional samples were saved from being doomed.

Of course, there are some general files that cannot be placed into specific folders because of their "short story". They are:

- **Preprocessed data - Files extractor** --> Jupyter notebook to extract separated files for each participant out of matlab file `preprocessed_pic_data.mat`. The script works properly, meaning that it generates separated (properly named) csv files for each of the patients.
- **Pupil diameter outliers handling** --> Processing of pupil diameter measurement depending on time (timestamp 0.001). First of all, basic descriptive statistics were calculated for a time course of the graph. Then with the help of the IQR outliers detection method, outlier values were selected and swapped with synthetic values made with interpolation.
- **What files look like** --> Jupyter Notebook to make a basic recognition of files (how they look like, what columns and types are there). This file is more like a cheat sheet made in the beginning of the project to make a quick realisation for future tasks, on what files an action should have been done and where are they (path).
- **EDA - raw data** --> For given raw data tables, some further preprocessing and examination were done (how many data points are missing in selected files).
- **Lightning conditions** --> Beginning of processing lightning conditions to further add it as a feature into the model. The result from the whole Jupyter notebook is just a simple linear plot, so not much. The plan was to make feature actions in this file, but another group member made their own notebook. I've decided to leave this file as it is.


# TFM: Acronym Disambiguation in Biomedical Spanish Literature

The following repository contains the code developed for IA Avanzada Master'thesis (UNED).

The objetive is disambiguate acronyms founded in biomedical spanish texts. 

Code is divided in three folders:
- **data**: All the data is stored in this folder. 
        - *ibereval_data*: Original data from IberEval (https://temu.bsc.es/BARR2/) for trainning and test processes.
        - *scrapping*: Medical texts obtained by Medline (https://medlineplus.gov/spanish/) scrapping.
        - *data_train*: Trainning and test IberEval original data after pre-processing for model input.
        - *data_predict*: Model outputs.
- **preprocessing**: Code for scrapping Medline and preprocess data model input.
- **analytics**: Model code (BETO Transformer).

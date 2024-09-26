import pickle
import os

# taking the best model for each output column
def load_models():
    # model_str = [['rf', 'lr', 'svm', 'knn' ,'xgb', 'lgbm'], ['rf', 'lr', 'svm', 'lgbm'], ['rf', 'lr', 'svm','xgb', 'lgbm'], ['lr', 'svm','xgb', 'lgbm'], ['rf', 'lr', 'svm' ,'xgb', 'lgbm'], ['rf', 'svm','xgb']]
    model_str = [['lr', 'svm', 'knn' ,'xgb', 'lgbm'], ['rf', 'lr', 'svm', 'lgbm'], ['rf', 'lr', 'svm','xgb', 'lgbm'], ['lr', 'svm','xgb', 'lgbm'], [ 'lr', 'svm' ,'xgb', 'lgbm'], ['rf', 'svm','xgb']]
    models = []
    for i in range(0, 6):
        temp_model = []
        for model_name in model_str[i]:
            file_path = os.path.join('models', f"{model_name}{i + 1}.sav")
            print(file_path)
            
            with open(file_path, 'rb') as file:
                curr_model_out = pickle.load(file)
            temp_model.append(curr_model_out)
        models.append(temp_model)
    return models    

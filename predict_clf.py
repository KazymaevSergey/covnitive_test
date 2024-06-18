# Класс для предсказания
from catboost import CatBoostClassifier


class Predict_ace():
    def __init__(self, model_catboost):
        
        self.clf = CatBoostClassifier().load_model(model_catboost)  #загрузка сохраненно     модели

    def predict(self, sample):
        return self.clf.predict([sample])
    
    def predict_proba(self, sample): 
        return self.clf.predict_proba([sample])
    
    def clf_classes(self):
        return self.clf.classes_
    
#


    
        
    

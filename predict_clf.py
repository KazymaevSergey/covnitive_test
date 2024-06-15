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
    
#ACE_III=[10, 56, 10, 15, 21, 21, 10, 76]

#p_value=Predict_ace('cat_category').predict_proba(ACE_III).round(2)
#classes=Predict_ace('cat_category').clf_classes()

#print(p_value[0])
#print(classes)

#print(dict(zip(classes, p_value[0])))



    
        
    

from yandex_cloud_ml_sdk import YCloudML
import streamlit as st
from anomal_predict import predict_anomal, pred_fluense
import numpy as np

flod_id=st.secrets.yandexGPT.fold_id
key_api=st.secrets.yandexGPT.openai_key

sdk = YCloudML(folder_id=flod_id, auth=key_api)

model = sdk.models.completions('yandexgpt')
model = model.configure(temperature=0.4)

columns_anomal=['ВНИМАНИЕ', 'ПАМЯТЬ', 'БЕГЛОСТЬ', 'РЕЧЬ', 'ЗРИТЕЛЬНО_ПРОСТРАНСТВЕННЫЕ']

#attention=16
#memory=23
#fluence=11
#speech=10
#spatial=15

#age=45

#ACE=attention+memory+fluence+speech+spatial

#ACE_anomal=np.array([attention, memory, fluence, speech, spatial])

absolut=np.array([18,26,14,26,16])

def function_interpetator(ACE_anomal):
  c={}
  for colum, value in zip(columns_anomal, ACE_anomal):
    x=predict_anomal(colum, value)
    if colum!='БЕГЛОСТЬ' and x=='норма':
      c[colum]=x
    elif colum!='БЕГЛОСТЬ' and x=='нарушение':
      c[colum]=x
    elif colum=='БЕГЛОСТЬ':
      c[colum]=pred_fluense(value)
  return c



def func_text(ACE_anomal):
    func_inter=[]
    cognitive=function_interpetator(ACE_anomal)
    for cog, inter, ace_val, ace_max in zip(cognitive.keys(), cognitive.values(), ACE_anomal, absolut):
        
        interet=cog+' '+inter+': '+str(ace_val)+' балл из '+str(ace_max)
        func_inter.append(interet)
    return func_inter


def damage(val_damage):
    if val_damage=='no_dam':
        pred_dam='не органического характера'
    elif val_damage=='damage':
        pred_dam='повреждение мозга'
    return pred_dam


       




def text_conclusion(step_pred, y_dam, ACE_anomal, ACE):
    
    pred_dam=damage(y_dam)
    func_inter=func_text(ACE_anomal)
    
    input_text='''напиши нейропсихологическое заключение короткое  когнитивных нарушени {}, {}, когнитивные функции {}, 
                Общий балл по Адденбруской когнитивной шкале {} из 100'''.format(step_pred, pred_dam, func_inter, ACE)
    result=model.run(input_text)
    
    return result[0].text





import joblib
import plotly.express as px
import numpy as np


columns_anomal=['ВНИМАНИЕ', 'ПАМЯТЬ', 'БЕГЛОСТЬ', 'РЕЧЬ', 'ЗРИТЕЛЬНО_ПРОСТРАНСТВЕННЫЕ']
dict_anomal_clf={}
for name in columns_anomal:
    clf=joblib.load(f'clf_anomal/{name}.pkl') 
  
    dict_anomal_clf[name]=clf
    

def predict_anomal(cognitive_name, val):
  pred=dict_anomal_clf.get(cognitive_name).predict([[val]])
  pred[pred==1]=0
  pred[pred==-1]=1

  if pred==0:
    pred_name='норма'
  elif pred==1:
    pred_name='нарушение'
  return pred_name


fluens_granz=10

def pred_fluense(val):

  fluence_pred=predict_anomal('БЕГЛОСТЬ', val)
  if fluence_pred=='нарушение' and val>=fluens_granz:
      fluence_pred='норма'
  else:
    fluence_pred=fluence_pred
  return fluence_pred


#attention=16
#memory=23
#fluence=11
#speech=10
#spatial=15

#age=45

#ACE=attention+memory+fluence+speech+spatial

#ACE_anomal=np.array([attention, memory, fluence, speech, spatial])

def dict_anomal(absolut, procent_anomal, ACE_anomal):
  dic={}
  for colum, value,absol, proc  in zip(columns_anomal, ACE_anomal,absolut, procent_anomal):
    x=predict_anomal(colum, value)
    if colum!='БЕГЛОСТЬ' and x=='норма':
      dic[colum]=f'норма: {value}/{absol}/{proc} '

    elif colum!='БЕГЛОСТЬ' and x=='нарушение':
      dic[colum]=f'нарушение: {value}/{absol}/{proc}'

    elif colum=='БЕГЛОСТЬ':
      dic[colum]=f'{pred_fluense(value)}: {value}/{absol}/{proc}'

  return dic


def color(ACE_anomal):
  c=[]
  for colum, value in zip(columns_anomal, ACE_anomal):
    x=predict_anomal(colum, value)
    if colum!='БЕГЛОСТЬ' and x=='норма':
      c.append(x)
    elif colum!='БЕГЛОСТЬ' and x=='нарушение':
      c.append(x)
    elif colum=='БЕГЛОСТЬ':
      c.append(pred_fluense(value))
  return c


def plot_neurocog(ACE_anomal, interpretir, age, ACE):
  absolut=np.array([18,26,14,26,16])
  
  if interpretir=='damage':
    inter='есть когнитивные нарушения'
    title=f'Возраст: {age}. ACE-III={ACE} - {inter}'
  elif interpretir=='no_dam':
    inter='незначительные когнитивные нарушения или отсутсвуют'
    title=f'Возраст: {age}.  ACE-III={ACE} - {inter}'
  

  
  procent_anomal=(ACE_anomal*100/absolut).round(2)
  bar_anomal=dict(zip(columns_anomal, procent_anomal))
  fig=px.bar(y=bar_anomal.keys(), x=bar_anomal.values(), orientation='h',
             text=dict_anomal(absolut, procent_anomal, ACE_anomal).values(), 
             color=color(ACE_anomal),  
             color_discrete_sequence=['green', 'blue'],
             labels={'color':'сохранность когнитивных функций', 
                     'y':'функции',
                     'x':'процент сохранности функции от максимального значения'}
            )
  
  fig.update_layout(
    title=dict(text=title)
                    )
  
  
  return fig



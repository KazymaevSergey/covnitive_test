import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
from predict_clf import Predict_ace
from data_db import insert_tab, creat_tab



st.title('Адденбрукская шкала оценки когнитивных функций III, бета-версия ')
st.write('Введите данные')


#ввод данных теста
def input_data():
    age=st.number_input("Возраст", step=1)
   
    
    diag=['нет ответа','нет_повреждений',"mci",'dementia','stroke', 'parkinson','barain_injury','другое']
    diagnos = st.radio(
        "выберите повреждения мозга",
        diag, index=0
        )

#ВНИМАНИЕ
    st.header('Внимание', divider='rainbow')


    at_time=st.number_input("Внимание: ориентирование во времени", min_value=0, max_value=5, step=1)
    st.write("от 0 до 5", at_time)

    at_place=st.number_input("Внимание: ориентирование в месте", min_value=0, max_value=5, step=1)
    st.write("от 0 до 5", at_place)

    at_three_words=st.number_input("Внимание: повторить 3 слова и запомнить", min_value=0, max_value=3, step=1)
    st.write("от 0 до 3", at_three_words)


    at_calculate=st.number_input("Внимание: серийный счет от 100 отнимать по 7", min_value=0, max_value=5, step=1)
    st.write("от 0 до 5", at_calculate)


    attantion=at_time+at_place+at_three_words+at_calculate

    st.subheader('Общий балл по вниманию', divider='blue')
    st.write(attantion)


#ПАМЯТЬ
    st.header('Память', divider='rainbow')
    mem_words=st.number_input("Память: Припомнить 3 слова", min_value=0, max_value=3, step=1)
    st.write("от 0 до 3", mem_words)

    mem_adr=st.number_input("Память: Запомнить адресс", min_value=0, max_value=7, step=1)
    st.write("от 0 до 7", mem_adr)

    mem_president=st.number_input("Память на президента, премьер-министра и т.д", min_value=0, max_value=4, step=1)
    st.write("от 0 до 4", mem_president)

    mem__remember_adr=st.number_input("Память: свободное припоминание адреса", min_value=0, max_value=7, step=1)
    st.write("от 0 до 7", mem__remember_adr)

    mem_uznav=st.number_input("Память: выбор из множества", min_value=0, max_value=5, step=1)
    st.write("от 0 до 5", mem_uznav)

    memory=mem_words+mem_adr+mem_president+mem__remember_adr+mem_uznav
    st.subheader('Общий балл по памяти', divider='blue')
    st.write(memory)



#БЕГЛОСТЬ
    st.header('Скорость вербальных ассоциаций', divider='rainbow')

    word_fluence=st.number_input("Называние за 1 минуту слов на букву", min_value=0, max_value=7, step=1)
    st.write("от 0 до 7", word_fluence)

    word_animal=st.number_input("Называние за  1 минуту животных", min_value=0, max_value=7, step=1)
    st.write("от 0 до 7", word_animal)

    fluence=word_fluence+word_animal
    st.subheader('Общий балл по скорости словесных ассоциаций', divider='blue')
    st.write(fluence)


#РЕЧЬ
    st.header('Речь', divider='rainbow')

    speech_komand=st.number_input("Речь: команды", min_value=0, max_value=3, step=1)
    st.write("от 0 до 3", speech_komand)

    speech_sentense=st.number_input("Речь: написание предложений", min_value=0, max_value=2, step=1)
    st.write("от 0 до 2", speech_sentense)

    speech_repit_word=st.number_input("Речь: повторение слов", min_value=0, max_value=2, step=1)
    st.write("от 0 до 2", speech_repit_word)

    speech_repit_poslov_1=st.number_input("Речь: повторение 1 пословицы", min_value=0, max_value=1, step=1)
    st.write("от 0 до 1", speech_repit_poslov_1)

    speech_repit_poslov_2=st.number_input("Речь: повторение  2 пословицы", min_value=0, max_value=1, step=1)
    st.write("от 0 до 1", speech_repit_poslov_2)

    speech_read=st.number_input("Речь: чтение", min_value=0, max_value=1, step=1)
    st.write("от 0 до 1", speech_read)

    speech_name=st.number_input("Речь: название", min_value=0, max_value=12, step=1)
    st.write("от 0 до 12", speech_name)

    speech_undestand=st.number_input("Речь: понимание", min_value=0, max_value=4, step=1)
    st.write("от 0 до 4", speech_undestand)

    speech=speech_komand+speech_sentense+speech_repit_word+speech_repit_poslov_1+speech_repit_poslov_2+speech_read+speech_name+speech_undestand
    st.subheader('Общий балл речь', divider='blue')
    st.write(speech)

#Зрительно-пространственные функции
    st.header('Зрительно-пространственные функции', divider='rainbow')
    spatial_endless=st.number_input("Копирование бесконечностей", min_value=0, max_value=1, step=1)
    st.write("от 0 до 1", spatial_endless)

    spatial_cub=st.number_input("Копирование куба", min_value=0, max_value=2, step=1)
    st.write("от 0 до 2", spatial_cub)

    spatial_clock=st.number_input("Тест часов", min_value=0, max_value=5, step=1)
    st.write("от 0 до 5", spatial_clock)

    spatial_punct=st.number_input("Подсчет точек", min_value=0, max_value=4, step=1)
    st.write("от 0 до 4", spatial_punct)

    spatial_albabet=st.number_input("Подсчет букв", min_value=0, max_value=4, step=1)
    st.write("от 0 до 4", spatial_albabet)

    spatial=spatial_endless+spatial_cub+spatial_clock+spatial_punct+spatial_albabet

    st.subheader('Общий балл по зрительно-пространственным функциям', divider='blue')
    st.write(spatial)


#СВЕДЕНИЕ В ОБЩЕЕ
    ACE=attantion+memory+fluence+speech+spatial
    m_ACE=m_ACE=at_time-1+word_animal+mem_adr+spatial_clock+mem__remember_adr
    
    return m_ACE, ACE, attantion, memory, fluence, speech, spatial, age, diagnos

m_ACE, ACE, attantion, memory, fluence, speech, spatial, age,  diagnos=input_data()

dic={'m-ACE':m_ACE,
    'ACE-III':ACE,
    'ВНИМАНИЕ':attantion,
     'ПАМЯТЬ':memory, 
     'БЕГЛОСТЬ':fluence, 
     'РЕЧЬ':speech, 
     'Зрительно-пространственные функции':spatial, 
     'Возраст':age 
     }
df=pd.DataFrame(dic, index=['Значение'])



#загрузка моделей предсказания

ACE_III=[m_ACE, ACE, attantion,memory,fluence, speech, spatial, age] #данные на основе которых строится предсказание


model_cat=Predict_ace('data/cat_category')
model_dam=Predict_ace('data/cat_dam')

y_pred_cat=model_cat.predict(ACE_III)[0][0]
y_pred_cat_proba=model_cat.predict_proba(ACE_III).max().round(2)

p_value=model_cat.predict_proba(ACE_III).round(2)
classes=model_cat.clf_classes()
data_graf_cat=dict(zip(classes, p_value[0]))

#степени повреждения мозга
y_pred_dam=model_dam.predict(ACE_III)[0]
y_pred_dam_proba=model_dam.predict_proba(ACE_III).max().round(2)




#Функция вывода результатов
def result():
    if st.button("Нажмите для получения результатов", type='primary'):
        st.subheader('Сводная таблица', divider='blue')
              #Вывод общих сведений
              
        if y_pred_dam=='damage':
            dam='повреждение мозга'
        else:
            dam='нет повреждений мозга'
            
        st.write(f'Возраст: {age} лет')

        total={ 'Возраст':age, 
                'm-ACE':m_ACE,
                'ACE-III':ACE,
                'ВНИМАНИЕ':attantion,
                'ПАМЯТЬ':memory, 
                'БЕГЛОСТЬ':fluence, 
                'РЕЧЬ':speech, 
                'Зрительно-пространственные функции':spatial, 
                "степень нарушения предсказание":y_pred_cat,
                "наличие повреждение мозга предсказание":dam,
                "степень нарушения специалист":assmet_cat,
                "наличие повреждение мозга специалист":assement_dam
     
                                                                        }
        df_total=pd.DataFrame(total, index=['Значение']).T
        df_total['Значение']=df_total['Значение'].astype(str) #чтоб не возникало ошибки при выводе таблицы, глюк streamlit
        st.table(df_total)
    
          #ГРАФИКИ

#1
        st.header('Когнитивный профиль', divider='red')
        fig1=px.bar(df[df.columns[0:2]].T,  
             orientation='h', 
            labels={'index':'балл', 'value':'значение'},
            text=[m_ACE, ACE],
            title=' Возраст: '+str(age)
           )

        fig1.add_vline(x=88, line_width=5, line_dash="dash", line_color="red")
        fig1.add_vline(x=82, line_width=5, line_dash="dash", line_color="red")
        fig1.add_vline(x=27, line_width=5, line_dash="dash", line_color="yellow")

        df_procent=((df[df.columns[2:7]]/[18,26,14,26,16])*100).T.round(2) #датафрейм для процентного представления потери баллов


#2
        fig2=px.bar(df_procent, text=df_procent['Значение'].values,
            orientation='h', 
            labels={'index':'функция', 'value':'процент сохранности функции от максимального значения'},
            title='Возраст: '+str(age),
            )

        st.plotly_chart(fig1, use_container_width=True)
        st.plotly_chart(fig2, use_container_width=True)
        
        #Массив для записи в базу данных
        ACE_db=[m_ACE, ACE, attantion, memory,fluence, speech, spatial]
        stepen=y_pred_cat
        damage=y_pred_dam
        massiv=[age]+ACE_db+[stepen,damage, diagnos]+[assmet_cat, assement_dam]
       
        creat_tab()
        insert_tab(massiv)
                                           
       
    
#функция предсказания
def predict():
       
    st.subheader('Баллы больше 88 считаются нормальными, ниже 82 - следует подозревать деменцию')
    if ACE<88 and ACE>=82:
        st.warning('Ниже нормы. ACE-III=  '+str(ACE))
        st.warning('Ниже нормы. m_ACE=  '+str(m_ACE))
    elif ACE<82:
        st.error('Следует подозревать деменцию. ACE-III=   '+str(ACE))
        st.error('Следует подозревать деменцию. m_ACE=   '+str(m_ACE))
   
    else:
        st.write('ACE-III= ',ACE)
        st.write('m-ACE= ',m_ACE)
    #предсказание степени выраженности нарушений
    
    
    st.subheader('Предсказание степени выраженности нарушений', divider='blue')
    if y_pred_cat=='незначительные' or y_pred_cat=='умеренные' :
        st.write('степень нарушения когнитивных функций: ', y_pred_cat)
        st.write('Вероятность достоверности прогноза: ', y_pred_cat_proba*100)
    else:
        st.warning('степень нарушения когнитивных функций: '+str(y_pred_cat))
        st.write('Вероятность достоверности прогноза: ', y_pred_cat_proba*100)
         
        st.header('График достоверности прогноза', divider='red')

   
    fig3=px.bar(y=data_graf_cat.keys(), 
            x= data_graf_cat.values(),
            orientation='h',
            text=data_graf_cat.values(),
            labels={'y':'категория',  'x':'вероятность'},
             
                       )
    st.plotly_chart(fig3, use_container_width=True)
    

#степени повреждения мозга
    st.subheader('Предсказание наличия повреждения мозга', divider='blue')
    
    if y_pred_dam=='damage':
        st.warning('есть вероятность органического повреждения мозга, проведите дополнительные исследования')
        st.write('Инсульт, ЧМТ, нейродегенеративные нарушения, MCI и т.п')
        st.write('Вероятность достоверности прогноза:   ', y_pred_dam_proba*100)
    elif y_pred_dam=='no_dam':
        st.write('отсутсутсвует органическое повреждение мозга')
        st.write('Вероятность достоверности прогноза:   ', y_pred_dam_proba*100)

    

#основная программа
#_____________________________________________#

st.header('РЕЗУЛТАТЫ', divider='rainbow')

predict()


#оценка степени выраженности
st.header('Оцените результаты прогноза')
st.subheader('Оцените результаты степени выраженности', divider='blue')


# Объединяем два массива
arr1 = np.array(['нет ответа'])
mas = np.append(arr1, classes)

cater=['нет ответа']+classes
assmet_cat=st.radio('согласны?', ['нет ответа','да', 'нет'], key=1, index=0)
if assmet_cat=='нет':
    assmet_cat=st.selectbox('что подходит лучше', mas, index=0)


#оценка наличия повреждения
st.subheader('Оцените результаты наличия повреждения мозга', divider='blue')
assement_dam=st.radio('согласны?',  ['нет ответа','да',  'нет'], key=2, index=0)
if assement_dam=='нет':
    assement_dam=st.selectbox('что подходит лучше', ['нет ответа','есть повреждение мозга', 'нет повреждения мозга'],index=0)







result()








    



   
    
    

   
  


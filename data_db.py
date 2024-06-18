import streamlit as st
from sqlalchemy import create_engine, text
import datetime


key=st.secrets['url']
enngine=create_engine(key)

def creat_tab():
    
    with enngine.connect() as con:
        con.execute(text('''
                     CREATE TABLE IF NOT EXISTS ace_db  ( 
            id SERIAL PRIMARY KEY,
            age int,
            m_ACE real,
            ACE real,
            attantion real,
            memory real,
            fluence real,
            speech real,
            spatial real,
            stepen text,
            damage text,
            diagnos text,
            assment_stepen text,
            assment_damage text,
            time text
                                             )
                     
                                         '''
                    )
                )
    
        con.commit()
        con.close()

def insert_tab(data):
    
    columns=['age',  'm_ACE', 'ACE',  'attantion',  'memory',
            'fluence',  'speech', 'spatial', 'stepen', 'damage', 'diagnos', 
            'assment_stepen', 'assment_damage']
    
    
    date=dict(zip(columns, data))
    date['time']=datetime.datetime.now()  
    
    
    
    
    with enngine.connect() as con:
        con.execute(text( ''' INSERT INTO ace_db (      
            age,
            m_ACE,
            ACE,
            attantion,
            memory,
            fluence,
            speech,
            spatial,
            stepen,
            damage,
            diagnos,
            assment_stepen,
            assment_damage,
            time)
                                  
            VALUES (
            :age,
            :m_ACE,
            :ACE,
            :attantion,
            :memory,
            :fluence,
            :speech,
            :spatial,
            :stepen,
            :damage,
            :diagnos,
            :assment_stepen,
            :assment_damage,
            :time)'''
                ),  [date]
    )
        con.commit()
        con.close()
    
    


    

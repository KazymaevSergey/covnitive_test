import streamlit as st
from sqlalchemy import text
import datetime



def insert_tab(data):
    columns=['age',  'm_ACE', 'ACE',  'attantion',  'memory',
            'fluence',  'speech', 'spatial', 'stepen', 'damage', 'diagnos', 
            'assment_stepen', 'assment_damage']
    
    
    date=dict(zip(columns, data))
    date['time']=datetime.datetime.now()
    
    
    
    conn = st.connection("neon", type="sql")
    with conn.session as session:
        session.execute(text( ''' INSERT INTO ace_db (      
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
 
        session.commit()
    


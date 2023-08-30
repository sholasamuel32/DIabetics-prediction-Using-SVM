# -*- coding: utf-8 -*-
"""
Created on Mon Aug 21 08:56:40 2023

@author: HP
"""


import pandas as pd
import pickle
import streamlit as st
from streamlit.components.v1 import html


def open_page():
    open_script= """
        <script type="text/javascript">
            window.open('http://localhost:8501/', '_blank').focus();
        </script>
    """ 
    html(open_script)


st.title('FEDERAL UNIVERSITY OYE-EKITI')
st.title('DIABETES PREDICTION USING SUPPORT VECTOR MACHINE LEARNING')
st.text(body = 'A study of University of Ilorin Teaching Hospital, Ilorin, Kwara State.')
st.image(image = 'logo.png', width = 500)
st.text(body = 'Written by:')
st.title('OYEDOKUN TAIWO OLUWASEUN - FTP/CSC/22/0046671')
st.text(body = 'Supervised by:')
st.title('Dr. BELLO, H. K.')
st.button('Open link', on_click=open_page())



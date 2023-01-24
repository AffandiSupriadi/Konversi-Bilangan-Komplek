import streamlit as st
import pandas as pd
import numpy as np
import math

st.set_page_config(
    page_title = "Konversi Bilangan Komplek",
    page_icon = "❤️",
)        
with open ('style.css') as f:
        st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)
col1, col2 = st.columns([1,11],gap= "medium")
with col1 :
        st.image("itenas.png", width=70)
with col2 :
        st.markdown("""
        <style>
        .big-font {
        font-size: 25px ;
        margin-bottom: 25px ;
        text-align: center :
        }
        </style>
        """, unsafe_allow_html=True)
        st.markdown('<h5 class="big-font"><b> Institut Teknologi Bandung</b></h5>', unsafe_allow_html=True)

st.title("Konversi Bilangan Komplek")
st.write("by: Affandi Supriadi")
st.write("Dosen: Ir. Rustamaji, M.T")

st.write(
        "Saya Affandi Supriadi dengan NRP 11-2021-020 mempersembahkan Aplikasi web konversi bilangan komplek, untuk memenuhi tugas dari mata kuliah Dasar Telekomunikasi."
    )
st.write("---")
col1, col2 = st.columns([1,11],gap= "medium")
with col2 :
        st.markdown("""
        <style>
        .big-font {
        font-size: 25px ;
        margin-bottom: 25px ;
        text-align: center :
        }
        </style>
        """, unsafe_allow_html=True)
        st.markdown('<h5 class="big-font"><b>Konversi kartesian ke polar</b></h5>', unsafe_allow_html=True)

col1, col2 = st.columns([1,11])
with col2 :
        st.image ("kartesian.jpg", width=300)
a = st.number_input ("Masukkan nilai bagian real = ")
b = st.number_input ("Masukkan nilai bagian imaginary = ")
hitung = st.button ("Konversi ke polar")
if hitung:
        if a == 0:
                a =0.0000001
                M = math.sqrt(math.pow(a,2)+math.pow(b,2))
                z = round(M,2)
                rad = math.atan (b/a)
                sudut = rad * 180/math.pi
                x = round(sudut,2)
                st.write("Nilai polarnya adalah", z , "∠", x,"° " )
        else :
                M = math.sqrt(math.pow(a,2)+math.pow(b,2))
                z = round(M,2)
                rad = math.atan (b/a)
                sudut = rad * 180/math.pi
                x = round(sudut,2)
                st.write("Nilai polarnya adalah", z , "∠", x,"° " )

                
st.write("---")
col1, col2 = st.columns([1,11],gap= "medium")
with col2 :
        st.markdown("""
        <style>
        .big-font {
        font-size: 25px ;
        margin-bottom: 25px ;
        text-align: center :
        }
        </style>
        """, unsafe_allow_html=True)
        st.markdown('<h5 class="big-font"><b>Konversi polar ke kartesian</b></h5>', unsafe_allow_html=True)
col1, col2 = st.columns([1,11])
with col2 :
        st.image ("polar.jpg", width=300)
M = st.number_input("Masukkan nilai Magnitudo = ")
sudut = st.number_input ("Masukkan nilai sudut (°) =")
hitung = st.button ("Konversi ke kartesian")
if hitung:
        rad = sudut * math.pi/180
        a = M * math.cos (rad)
        x = round (a,2)
        b = M * math.sin (rad)
        z = round (b,2)
        st.write("Nilai kartesiannya adalah",x,"+ j","(",z,")")

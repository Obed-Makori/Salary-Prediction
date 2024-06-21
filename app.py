# imports 
import streamlit as st
st.set_page_config(layout="wide", page_title='predict-salary',page_icon='icons8-salary-100.png')
from streamlit_option_menu import option_menu
import seaborn as sns
import plotly as pt
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

import warnings
import plotly_express as px
warnings.filterwarnings("ignore")
# used dataset
df=pd.read_csv('Salary Prediction dataset.csv')
#
selected = option_menu(None, 
                       ["Dashboard", "Report", "Predict", "Notebook"], 
    icons=['bar-chart-line-fill', 'clipboard2-data-fill', "graph-up", "journal-arrow-down"],
    default_index=0, orientation='horizontal')
# tittle
#st.markdown("<h1 style='text-align: center; color: #FF7F50;'>Emplpoyees' Salary Prediction</h1>", unsafe_allow_html=True)
# Dashboard
if selected=="Dashboard":
    st.markdown("<h2 style='text-align: center; color: red'> SALARY DASHBOARD </h2>", unsafe_allow_html=True)
    col1, col2, col3=st.columns(3)
    st.markdown("""
    <style>
    [data-testid=column]:nth-of-type(1) [data-testid=stVerticalBlock]{
        gap: 0rem;
    }
    </style>
    """,unsafe_allow_html=True)
    with col1:
            ##salary
        fig = px.histogram(df,
                        x='Salary',
                        marginal='box',
                        title='Distribution of Salary',
                        color='Education Level',
                        color_discrete_sequence=['red', 'grey', 'black']
                        )
        fig.update_layout(bargap=0.1,height=500)
        fig.update_layout(
            {
                #"paper_bgcolor": '#ff4b4b',
                #"plot_bgcolor": "rgba(0, 0, 0, 0)",
            }
        )
        st.plotly_chart(fig,use_container_width=True)  
        #################  graph 2
        #correlations
        df3=pd.read_csv('df.csv')
        fig, ax = plt.subplots()
        sns.heatmap(df3.corr(), ax=ax, cmap='YlGnBu',annot=True)
        st.write(fig)

 
        
    with col2:
         ##salary
        fig=px.histogram(df, 
                 x='Age', 
                 marginal='box',
                 nbins=47,
                 title='Distribution of Age',
                 color_discrete_sequence=['#ff4b4b']
                 )
        fig.update_layout(bargap=0.1,height=500)
        st.plotly_chart(fig,use_container_width=True) 
        # graph 3
        
       
        


    with col3:
        import streamlit_antd_components as sac

        # btn = sac.buttons(
        #     items=['Histogram', 'Bar Chart'],
        #     index=0,
        #     format_func='title',
        #     align='center',
        #     direction='horizontal',
        #     radius='lg',
        #     return_index=False,
        # )
        btn=st.selectbox(label='',options=['Education Level VS Salary','Education Level VS Age'],index=None,placeholder='Education Level...')
        if btn=='Education Level VS Salary':
                ##Categorical features
            fig = px.histogram(df,
                            x='Gender',
                            y='Salary',                                                   
                            color_discrete_sequence=['#ff4b4b']
                            )
            fig.update_layout(bargap=0.1,height=400)
            st.plotly_chart(fig,use_container_width=True)
        else:
            ##salary
            fig = px.histogram(df,
                            x='Age',
                            marginal='box',
                            title='Distribution of Salary',
                            color='Education Level',
                            #color_discrete_sequence=['red', 'grey', 'black']
                            )
            fig.update_layout(bargap=0.1)
            #borrowed settingd
            fig.update_layout(
                {
                    "paper_bgcolor": "rgba(0, 0, 0, 0)",
                    "plot_bgcolor": "rgba(0, 0, 0, 0)",
                }
            )
            # displaying the graph
            st.plotly_chart(fig)
             
#Report
if selected=="Report":
    st.markdown("<h2 style='text-align: center; color: red'> SALARY REPORT </h2>", unsafe_allow_html=True)
    def open_report(filepath):
        with open(filepath,'r') as file:
            return file.read()
    filepath='report.txt'
    report_content=open_report(filepath)
    st.write(report_content)
    
    # figure 1
    fig1=px.line(df,x='Years of Experience',y='Salary',title='Salary Correlations')
    st.plotly_chart(fig1)

                                                            # Predict
                                                                        # Prediction

if selected=="Predict":
     import joblib
     lenc=joblib.load('label_encoder.svm')
     model=joblib.load('version1.svm')
     # prediction form        
     with st.form('prediction-form',border=False,clear_on_submit=True):
         st.markdown("<h2 style='text-align: center; color: red'> PREDICTION FORM </h2>", unsafe_allow_html=True)
         sub={}
         #age
         sub['Age']=st.number_input("Age ", value=18)
         # Gender
         sub['Gender']=st.radio("Gender", ('Male','Female'))
         # Education Level
         sub['Education Level']=st.radio("Level of Education",["Bachelor's", "Master's", 'PhD'])
         #job titlle
         roles=[]
         for role in df['Job Title']:
             roles.append(role)
         roles.append('Other')
         sub['Job_ Title']=st.selectbox("Job Title",[None]+roles) 
         # years of experience
         sub['Years of Experience']=st.number_input("Years of Experience ", placeholder="years of experience",value=2)
        

                  
                     #submit form     ############
         ###make a dataframe
         sub_df=pd.DataFrame([sub])

         import pickle

         with open('gen.pickle','rb') as f:
             le=pickle.load(f)
         sub_df['Gender']=le.transform(sub_df['Gender'])
        

         
              
        # make a prediction        

                    
         submitted=st.form_submit_button(label='Predict')
         if submitted: 
             st.write(sub_df)            
              
# Notebook
if selected=="Notebook":
    st.markdown("<h2 style='text-align: center; color: red'> USED PYTHON NOTEBOOK </h2>", unsafe_allow_html=True)

    from streamlit_dynamic_filters import DynamicFilters

    data=pd.DataFrame([{
        'Region': ['North America', 'North America', 'North America', 'Europe', 'Europe', 'Asia', 'Asia'],
        'Country': ['USA', 'USA', 'Canada', 'Germany', 'France', 'Japan', 'China'],
        'City': ['New York', 'Los Angeles', 'Toronto', 'Berlin', 'Paris', 'Tokyo', 'Beijing']
        }])

    df = pd.DataFrame(data)

    dynamic_filters = DynamicFilters(df, filters=['Region', 'Country', 'City'])

    with st.sidebar:
        dynamic_filters.display_filters()

    dynamic_filters.display_df()

###############################   FOOTER

# footer="""<style>
# a:link , a:visited{
# color: blue;
# background-color: transparent;
# text-decoration: underline;
# }
# a:hover,  a:active {
# color: red;
# background-color: transparent;
# text-decoration: underline;
# }
# .footer {
# position: fixed;
# left: 0;
# bottom: 0;
# width: 100%;
# background-color: #0E1117;
# color: white;
# text-align: center;
# }
# </style>
# <div class="footer">
# <p>Developed by <a style='display: block; text-align: center;' href="https://twitter.com/ObedMakori254" target="_blank"; text-color: green>Makori Obed</a></p>
# </div>
# """
# st.markdown(footer,unsafe_allow_html=True)
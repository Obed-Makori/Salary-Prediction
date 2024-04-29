import streamlit as st
st.set_page_config(layout="wide", page_title='predict-salary',page_icon='icons8-salary-100.png')
from streamlit_option_menu import option_menu
import seaborn as sns
import plotly as pt
import pandas as pd
import numpy as np

import warnings
import plotly_express as px
warnings.filterwarnings("ignore")

# used dataset
df=pd.read_csv('Salary Prediction dataset.csv')

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
        
        st.write(df.tail(3))
        # gender distribution pie chart
        gender_counts=df['Gender'].value_counts()
        fig=px.pie(df,names=gender_counts.index, values=gender_counts.values)
        st.plotly_chart(fig, theme=None, use_container_width=True)
        
    with col2:
        st.write(df.head(3))
        fig=px.bar(df, x=gender_counts.index, y=gender_counts.values)
        st.plotly_chart(fig,theme=None,use_container_width=True)

       



    with col3:
        import streamlit_antd_components as sac

        btn = sac.buttons(
            items=['Histogram', 'Bar Chart'],
            index=0,
            format_func='title',
            align='center',
            direction='horizontal',
            radius='lg',
            return_index=False,
        )
        
        if btn=='Histogram':
            # fig 1 column 3
            fig1=px.histogram(df['Salary'], x=df['Salary'], nbins=20)
            st.plotly_chart(fig1, theme=None, use_container_width=True)
        else:
            # fig 2 column 3
            fig=px.bar(df, x=gender_counts.index, y=gender_counts.values)
            st.plotly_chart(fig,theme=None,use_container_width=True)
#Report
# Dashboard
if selected=="Report":
    st.markdown("<h2 style='text-align: center; color: red'> SALARY REPORT </h2>", unsafe_allow_html=True)

    st.write("Salary Dataset Analysis")

# Dashboard
if selected=="Predict":
    st.markdown("<h2 style='text-align: center; color: red'> PREDICTION FORM </h2>", unsafe_allow_html=True)
    st.write('Quicky predict Your Salary,..Key In your Details: -')



   
    
    


# Dashboard
if selected=="Notebook":
    st.markdown("<h2 style='text-align: center; color: red'> USED PYTHON NOTEBOOK </h2>", unsafe_allow_html=True)

    from streamlit_dynamic_filters import DynamicFilters

    data = {
        'Region': ['North America', 'North America', 'North America', 'Europe', 'Europe', 'Asia', 'Asia'],
        'Country': ['USA', 'USA', 'Canada', 'Germany', 'France', 'Japan', 'China'],
        'City': ['New York', 'Los Angeles', 'Toronto', 'Berlin', 'Paris', 'Tokyo', 'Beijing']
        }

    df = pd.DataFrame(data)

    dynamic_filters = DynamicFilters(df, filters=['Region', 'Country', 'City'])

    with st.sidebar:
        dynamic_filters.display_filters()

    dynamic_filters.display_df()




###############################   FOOTER

import streamlit as st

footer="""<style>
a:link , a:visited{
color: blue;
background-color: transparent;
text-decoration: underline;
}

a:hover,  a:active {
color: red;
background-color: transparent;
text-decoration: underline;
}

.footer {
position: fixed;
left: 0;
bottom: 0;
width: 100%;
background-color: #0E1117;
color: white;
text-align: center;
}
</style>
<div class="footer">
<p>Developed by <a style='display: block; text-align: center;' href="https://twitter.com/ObedMakori254" target="_blank"; text-color: green>Makori Obed</a></p>
</div>
"""
st.markdown(footer,unsafe_allow_html=True)



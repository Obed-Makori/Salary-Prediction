import streamlit as st

# Function to read the content of the text file
def read_text_file(file_path):
    with open(file_path, 'r') as file:
        return file.read()

# Path to your text file
file_path = 'report.txt'

# Read the content of the text file
file_content = read_text_file(file_path)

# Display the content in the Streamlit app
st.title('Text File Content')
st.write(file_content)
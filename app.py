import streamlit as st
from process_report import clean_report
from summarization import summarize_report
from qa_model import load_qa_model, get_answer

# Title of the app
st.title("AI-Driven Cybersecurity Audit Analysis")
st.sidebar.header("Upload Your Report")

# File uploader for report
uploaded_file = st.file_uploader("Choose a cybersecurity audit report", type="txt")

if uploaded_file:
    report = uploaded_file.read().decode("utf-8")
    
    # Clean the uploaded report
    cleaned_report = clean_report(report)
    
    # Summarize the cleaned report
    summarized_report = summarize_report(cleaned_report)
    
    # Display the summary
    st.subheader("Report Summary")
    st.write(summarized_report)

    # Chat functionality
    st.subheader("Ask Questions about the Report")
    user_query = st.text_input("Enter your question:")

    if user_query:
        model = load_qa_model()
        answer = get_answer(model, cleaned_report, user_query)
        st.write(answer)

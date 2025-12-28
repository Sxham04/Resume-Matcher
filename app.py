import streamlit as st
import en_core_web_sm
import fitz
import re
import pandas as pd

# Load the NLP model
nlp = en_core_web_sm.load()

def extract_text_from_pdf(file_obj):
    #streamlit file_uploader returns a file-like object
    doc = fitz.open(stream=file_obj.read(), filetype="pdf")
    text = ""
    for page in doc:
        text += page.get_text()
    return text

def clean_text(text):
    text = text.lower()
    text = re.sub(r'[^a-z\s]', '', text) 
    doc = nlp(text)
    tokens = [t.lemma_ for t in doc if not t.is_stop and not t.is_punct and not t.is_space]
    return " ".join(tokens)

#UI
st.title("📄 AI Resume-Job Matcher")
st.markdown("Rank multiple resumes based on a job description using NLP.")

st.sidebar.header("Job Details")
jd_input = st.sidebar.text_area("Paste the Job Description here:", height=300)

uploaded_files = st.file_uploader("Upload Resumes (PDF)", type=["pdf"], accept_multiple_files=True)

if st.button("Calculate Match Scores"):
    if not jd_input:
        st.error("Please provide a job description!")
    elif not uploaded_files:
        st.warning("Please upload at least one resume.")
    else:
        results = []
        cleaned_jd = clean_text(jd_input)
        jd_doc = nlp(cleaned_jd)

        for file in uploaded_files:
            #process each file
            raw_text = extract_text_from_pdf(file)
            cleaned_resume = clean_text(raw_text)
            resume_doc = nlp(cleaned_resume)
            
            #calculate Similarity
            score = resume_doc.similarity(jd_doc)
            
            results.append({
                "Candidate": file.name,
                "Match Score": round(score * 100, 2)
            })
        
        #display Results
        df_results = pd.DataFrame(results).sort_values(by="Match Score", ascending=False)
        st.subheader("Ranking Results")
        st.dataframe(df_results, use_container_width=True)
        st.success("Analysis Complete!")
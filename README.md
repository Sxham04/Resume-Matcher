# AI Resume-Job Matching System

A high-performance NLP application designed to automate the initial screening process by ranking resumes against a job description using semantic similarity.

## Overview

This project leverages NLP to convert unstructured PDF resumes into vector representations, calculating a "Match Score" relative to a specific Job Description.

## Key Features

* **Multi-Format Support:** Bulk upload of PDF resumes using `PyMuPDF`.
* **Intelligent Preprocessing:** Advanced text cleaning (stop-word removal, lemmatization, regex).
* **Semantic Analysis:** Uses SpaCy's vectorization for Cosine Similarity comparisons.
* **Interactive Dashboard:** Clean, sidebar-driven Streamlit interface.
* **Bias Mitigation:** Logic designed to prioritize skills over demographic data.

## Tech Stack

* **Language:** Python 3.9+
* **NLP Library:** SpaCy (`en_core_web_sm`)
* **Web Framework:** Streamlit
* **Data Handling:** Pandas
* **PDF Parsing:** PyMuPDF (fitz)

## Installation & Setup

1. Clone the repository.
2. Install dependencies: `pip install -r requirements.txt`.
3. Download the language model: `python -m spacy download en_core_web_sm`.
4. Run the app: `streamlit run app.py`.

## Ethical Considerations

Includes a discussion on algorithmic bias and the importance of anonymizing resumes for fair ranking.

## Images and UI

the initial UI
<img width="1916" height="749" alt="image" src="https://github.com/user-attachments/assets/2a88c61d-b668-4bac-b84c-0eadcb9bcc80" />

write the requirements or skills you are looking for in a candidate inside the designated dialog box
<img width="383" height="490" alt="image" src="https://github.com/user-attachments/assets/ad029049-35b6-47ea-8342-845f4257153f" />

upload all the pdf(s) you want to analyze and rank based on the similarity of the requirements
<img width="1319" height="617" alt="image" src="https://github.com/user-attachments/assets/104862d1-515d-4673-9db6-08a2355bc067" />

click on the 'calculate match scores' button in order to run the program
the program will return a table, ranking the submitted resume' based on the similarity or requirements met
<img width="1014" height="863" alt="image" src="https://github.com/user-attachments/assets/f590b391-25a7-4695-ba01-de6a1308b88d" />

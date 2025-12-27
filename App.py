import streamlit as st
import joblib
import time
model = joblib.load("model.pkl")
vectorizer = joblib.load("vectorizer.pkl")

st.title("Email Spam Detector")
st.caption("Determine if your message from email is safe or suspicious in seconds.")
st.divider()

input_text = st.text_area("Enter your email message:")

if st.button("Predict", use_container_width=True):
    if input_text:
        data = vectorizer.transform([input_text])
        prediction = model.predict(data)[0]

        progress = st.progress(0)
        for i in range(100):
            time.sleep(0.01) 
            progress.progress(i + 1)

        if prediction == "spam":
            st.error("This email is SPAM")
            st.snow()
        else:
            st.success("This email is NOT SPAM")
            st.balloons()

        st.divider()
    else:
        st.write("Please enter some text.")

# CSS for styling
st.markdown("""
<style>
/* Remove all shadows from all buttons */
button {
    box-shadow: none !important;
    text-transform: none;
}

/* GitHub deep link button styling */
a[data-testid="stLinkButton"] {
    text-decoration: none;
    width: 100%;
}

a[data-testid="stLinkButton"] > button {
    background-color: #0366d6; /* GitHub Blue */
    color: #ffffff;
    border-radius: 8px;
    padding: 0.6em 1.2em;
    font-size: 14px;
    font-weight: 500;
    border: 1px solid #0366d6;
    transition: background-color 0.2s, border-color 0.2s;
    width: 100% !important;
    box-shadow: none !important;
}

/* Attractive hover effect */
a[data-testid="stLinkButton"] > button:hover {
    background-color: #0056b3 !important;
    border-color: #0056b3 !important;
    color: #ffffff !important;
}

/* Click effect */
a[data-testid="stLinkButton"] > button:active {
    background-color: #004085 !important;
    transform: translateY(1px);
}
</style>
""", unsafe_allow_html=True)


st.link_button("View on GitHub", "https://github.com/username/repo", use_container_width=True)
st.caption(" Machine Learning Project With Support Vector Machine(SVM)")



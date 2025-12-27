import streamlit as st
import joblib
import time
model = joblib.load("models/model.pkl")
vectorizer = joblib.load("models/vectorizer.pkl")

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
    text-decoration: none !important;
    width: 100% !important;
}

a[data-testid="stLinkButton"] p {
    color: #ffffff !important;
}

a[data-testid="stLinkButton"] > div {
    background-color: #0366d6 !important;
    border: 1px solid #0366d6 !important;
    border-radius: 8px !important;
    transition: all 0.2s ease !important;
}

/* Attractive hover effect */
a[data-testid="stLinkButton"]:hover > div {
    background-color: #0056b3 !important;
    border-color: #0056b3 !important;
}

/* Click effect */
a[data-testid="stLinkButton"]:active > div {
    background-color: #004085 !important;
    transform: translateY(1px) !important;
}
</style>
""", unsafe_allow_html=True)


st.link_button("View on GitHub", "https://github.com/sowmiyan-s/Email-Spam-Detection", use_container_width=True)


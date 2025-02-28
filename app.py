import streamlit as st

# Portfolio data (Modify this with actual project details)
portfolio = {
    "Data Science": [
        {"title": "Customer Segmentation", "link": "https://your-ds-project.com"},
        {"title": "Sales Forecasting", "link": "https://your-ds-project2.com"},
    ],
    "Machine Learning": [
        {"title": "Spam Detection Model", "link": "https://your-ml-project.com"},
        {"title": "Stock Price Prediction", "link": "https://your-ml-project2.com"},
    ],
    "Deep Learning": [
        {"title": "Image Classification", "link": "https://your-dl-project.com"},
        {"title": "Speech Recognition", "link": "https://your-dl-project2.com"},
    ],
    "AI Chatbots": [
        {"title": "Travel Planning AI Assistant", "link": "https://travelbookingassistant-b5k669k2bkk3jeewz7uiwk.streamlit.app/"},
        {"title": "Symptom Assessment Assistant", "link": "https://symptomchecker-7gfmqvakqyanbbpfb5ybuj.streamlit.app/"},
        {"title": "AI-Powered Career Toolkit", "link": "https://resumecoverletterwriter-9lwongwhsygod6c6whtmd6.streamlit.app/"},
          {"title": "Real Estate Property Advisor", "link": "https://realestate-lm7f4skfmrk88qqjqvi3qx.streamlit.app/"},
        {"title": "AI Personal Finance Assistant", "link": "https://personalfinanceassistant-cxm7iwsskydnmd7ziajlcx.streamlit.app/"},
          {"title": "AI Student Assistant", "link": "https://mathsloving-bjmlf6stjvkycvjhgpvmte.streamlit.app/"},
        {"title": "Social Media AI Assistant", "link": "https://linkedinpost-vgf8rqswygtrqfsbxmhvyh.streamlit.app/"},
          {"title": "Lead Generation Assistant", "link": "https://leadgenerationqualificationbot-gtfdzkeumv38abcydiskvl.streamlit.app/"},
        {"title": "AI Legal Advisor", "link": "https://ailegaladvisor-rcmcuixqvasjjgp5aeuvfs.streamlit.app/"},
        {"title": "Voice & Multilingual AI Chatbot", "link": "https://textspeech-gwwephrm5g5ra9nbrnlhpx.streamlit.app/"},
    ]
}

st.set_page_config(page_title="My Portfolio", layout="wide")

# Custom CSS for enhanced styling
st.markdown(
    """
    <style>
        body {
            background-color: #121212;
            color: white;
        }

        .main-title {
            text-align: center;
            font-size: 2.5rem;
            font-weight: bold;
            margin-bottom: 20px;
        }

        .section-title {
            font-size: 2rem;
            margin-top: 30px;
            border-bottom: 2px solid #1db954;
            padding-bottom: 5px;
        }

        .card {
            background-color: #1e1e1e;
            padding: 15px;
            border-radius: 10px;
            margin-bottom: 15px;
            box-shadow: 0px 4px 10px rgba(255, 255, 255, 0.1);
            transition: transform 0.3s ease-in-out;
            text-align: center;
        }

        .card:hover {
            transform: scale(1.05);
        }

        .card a {
            color: #1db954;
            text-decoration: none;
            font-weight: bold;
        }

        .footer {
            text-align: center;
            padding: 10px;
            margin-top: 20px;
            border-top: 1px solid #555;
        }
    </style>
    """,
    unsafe_allow_html=True,
)

# Sidebar Navigation
st.sidebar.title("Navigation")
page = st.sidebar.radio("Go to", ["Home", "About", "Contact"])

if page == "Home":
    st.markdown("<h1 class='main-title'>🚀 My AI & Data Science Portfolio</h1>", unsafe_allow_html=True)
    st.write("Welcome to my portfolio showcasing projects in Data Science, Machine Learning, Deep Learning, and AI.")
    
    for category, projects in portfolio.items():
        st.markdown(f"<h2 class='section-title'>{category}</h2>", unsafe_allow_html=True)
        for project in projects:
            st.markdown(
                f"<div class='card'>"
                f"<h3>{project['title']}</h3>"
                f"<a href='{project['link']}' target='_blank'>View Project</a>"
                "</div>",
                unsafe_allow_html=True,
            )

elif page == "About":
    st.title("About Me")
    st.write("Hi, I'm Ebiet Matthew Monday! 🚀")
    st.write("I'm a passionate Data Scientist, Machine Learning Engineer, Deep Learning Specialist, and AI Chatbot Developer dedicated to building intelligent solutions that drive innovation and solve real-world problems. With expertise in predictive analytics, natural language processing (NLP), deep learning architectures, and AI automation, I create cutting-edge projects that empower businesses and enhance user experiences.")
    st.markdown("What I Do:")
    st.write("✅ Data Science – Transforming raw data into actionable insights")
    st.write("✅ Machine Learning – Developing predictive models for smarter decision-making")
    st.write("✅ Deep Learning – Building advanced neural networks for AI-driven applications")
    st.write("✅ AI Chatbots – Crafting intelligent virtual assistants for businesses")
    st.write("I thrive on solving complex challenges and pushing the boundaries of AI technology. Let's collaborate and build something groundbreaking!")

elif page == "Contact":
    st.title("Contact Me")
    st.write("Feel free to reach out for collaborations or inquiries.")
    st.write("📧 Email: ebietmonday@gmail.com")
    st.write("🔗 LinkedIn: [Ebiet Monday](https://www.linkedin.com/in/ebiet/)")
    st.write("🐦 Twitter: [Ebiet Monday](https://x.com/Christebiet)")

# Footer
st.markdown("<div class='footer'>© 2025 Ebiet Matthew Monday | All Rights Reserved</div>", unsafe_allow_html=True)

import streamlit as st
from base64 import b64encode

def web_portfolio():
    # Set the page title and layout
    st.set_page_config(page_title="Shrinidhi Bhat's Portfolio", layout="wide", page_icon="🤖")
    
    st.write(f"""
    <div class="title" style="text-align: center;">
    <span style='font-size: 32px;'> Hello! My name is Shrinidhi Bhat </span> 👋
    </div>
    """, unsafe_allow_html=True)

    # Add padding to the title
    st.markdown("<style>div.block-container{padding-top: 4rem;}</style>", unsafe_allow_html=True)

    # Add profile image
    with open('image_zapikanka.jpg', 'rb') as image_file:
        # Use of base64 encoding to display the image
        image = "data:image/jpeg;base64," + b64encode(image_file.read()).decode()

    # For PDF files
    with open('CV.pdf', 'rb') as pdf_file:
        pdf_bytes = pdf_file.read()

    # Display the information
    st.write(f"""
    <div style="display: flex; justify-content: center; align-items: center; padding: 20px;">
    <div class="box">
    <img src="{image}" alt="Shrinidhi Bhat" style="width: 200px; height: 300px;">
    </div>
    </div>
    """, unsafe_allow_html=True)
    # border-radius: 50%; margin-right: 20px;

    # Set the current title
    st.write(f"""
    <div class="subtitle" style="text-align: center;"> Computer Vision Researcher and AI Engineer </div>""",
    unsafe_allow_html=True)

    # Create a dictionary to store social media icons and links
    social_media = {
        "LinkedIn": ["https://www.linkedin.com/in/shrinidhi-bhat-9635a615a/", "https://cdn-icons-png.flaticon.com/128/2504/2504923.png"],
        "GitHub": ["https://github.com/Shrinidhibhat87", "https://cdn-icons-png.flaticon.com/128/5968/5968866.png"],
    }

    # Create a horizontal layout for the icons on html
    social_media_html = [
        f"<a href='{social_media[platform][0]}' target='_blank' style='margin: right: 10px;'>"
        f"<img class='social-icon' src='{social_media[platform][1]}' alt='{platform}' style='width: 40px; height: 40px;'></a>"
        for platform in social_media
    ]

    # Apply these icons using st.write
    st.write(f"""
    <div style="display: flex; justify-content: center; margin-bottom: 20px;">{''.join(social_media_html)}</div>""", unsafe_allow_html=True)

    # Download button for CV
    st.write("""
    <div style="display: flex; justify-content: center; margin-bottom: 20px;">
        <div>
            <style>
                div.stDownloadButton > button {
                    margin: 0 auto;
                    display: block;
                    padding: 10px 20px;
                    font-size: 16px;
                    font-weight: bold;
                    background-color: #262626;
                    color: white;
                    border: none;
                    border-radius: 5px;
                    transition: background-color 0.3s ease;
                }
                div.stDownloadButton > button:hover {
                    background-color: #45a049;
                }
            </style>
            """, unsafe_allow_html=True)
    st.download_button("Download CV", data=pdf_bytes, file_name="CV.pdf", mime="application/pdf")
    st.write("</div></div>", unsafe_allow_html=True)

    # Define available sections
    sections = ["About Me", "Work Experiences", "Projects", "Articles"]

    # Initialize session state to remember selected section
    if 'selected_section' not in st.session_state:
        st.session_state.selected_section = "About Me"  # Default section

    # Custom CSS to style the buttons
    st.markdown("""
    <style>
    div.stButton > button {
        margin: 0 20px;
        padding: 20px 30px;
        font-size: 18px;
        font-weight: bold;
        background-color: #262626;
        color: white;
        border: none;
        border-radius: 10px;
        transition: background-color 0.3s ease;
    }
    div.stButton > button:hover {
        background-color: #45a049;
    }
    </style>
    """, unsafe_allow_html=True)

    # Display section navigation as buttons in a row
    cols = st.columns(len(sections), gap="small")
    for i, section in enumerate(sections):
        with cols[i]:
            if st.button(section):
                st.session_state.selected_section = section

    # Show content based on which section is selected
    selected_section = st.session_state.selected_section

    if selected_section == "About Me":
        st.markdown("""
        <div style="text-align: center;">
            <h3 style="font-size: 24px; font-weight: bold;">About Me</h3>
        </div>
        <div style="display: flex; justify-content: center; padding: 20px;">
            <div style="text-align: left; max-width: 800px;">
                <p>👁️ I am a <b>Computer Vision PhD Student and a Data Science Researcher</b> at <a href="https://www.fz-juelich.de/en/ias/ias-9" target="_blank">Forschungszentrum Jülich IAS-9 Team</a></p>
                <p>❤️ Passionate about 🤖 <i>Robotics</i>, <i>Computer Vision</i>, and <i>Machine Learning</i>.</p>
                <p>🎓 Graduated from RWTH Aachen University with a Masters in <i>Robotic Systems Engineering</i></p>
                <p>🚘 Master thesis at BMW: <i>Bandwidth Efficient Learning on Vision Transformers For Semantic Segmentation</i></p>
            </div>
        </div>
        """, unsafe_allow_html=True)

    elif selected_section == "Work Experiences":
        st.markdown("""
        <div style="text-align: center;">
            <h3 style="font-size: 24px; font-weight: bold;">Work Experiences</h3>
        </div>
        <div style="display: flex; justify-content: center; padding: 20px;">
            <ul>
                <li>Dummy Work Experience 1: <i>Software Engineer at Example Company</i></li>
            </ul>
        </div>
        """, unsafe_allow_html=True)

    elif selected_section == "Projects":
        st.markdown("""
        <div style="text-align: center;">
            <h3 style="font-size: 24px; font-weight: bold;">Projects</h3>
        </div>
        <div style="display: flex; justify-content: center; padding: 20px;">
            <ul>
                <li><a href="https://github.com/example-project" target="_blank">Dummy Project 1</a></li>
            </ul>
        </div>
        """, unsafe_allow_html=True)

    elif selected_section == "Articles":
        st.markdown("""
        <div style="text-align: center;">
            <h3 style="font-size: 24px; font-weight: bold;">Articles</h3>
        </div>
        <div style="display: flex; justify-content: center; padding: 20px;">
            <ul>
                <li><a href="https://medium.com/example-article" target="_blank">Dummy Article 1</a></li>
            </ul>
        </div>
        """, unsafe_allow_html=True)
    


if __name__ == "__main__":
    # Run the web portfolio function
    web_portfolio()

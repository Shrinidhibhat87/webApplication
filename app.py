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

    # About Me
    st.write(f"""
    <div style="text-align: center;">
    ##
    </div>
    """, unsafe_allow_html=True)

    st.write(f"""
    <div style="text-align: center;">
    <h3>About Me</h3>
    </div>
    """, unsafe_allow_html=True)

    st.write(f"""
    <div style="display: flex; justify-content: center; padding: 20px;">
        <div style="text-align: left; max-width: 800px;">
            <p>👁️ I am a <b>Computer Vision PhD Student and a Data Science Researcher</b> at <a href="https://www.fz-juelich.de/en/ias/ias-9" target="_blank">Forschungszentrum Jülich IAS-9 Team</a></p>
            <p>❤️ I am passionate about 🤖 <i>Robotics</i>, <i>Computer Vision</i>, and <i>Machine Learning</i>.</p>
            <p>🎓 I graduated from RWTH Aachen University with a Masters in <i>Robotic Systems Engineering</i></p>
            <p>🚘 I did my Master thesis at BMW with the topic being: <i>Bandwidth Efficient Learning on Vision Transformers For Semantic Segmentation</i></p>
            <p>🤖 I was a Research Intern in the <i>Robot Learning</i> team at Bosch center of AI where I worked on a <i>Multi-view segmentation pipeline</i></p>
            <p>💼 I have a full time working experience (2+ years) as an Embedded Firmware Developer at <a href="https://www.westerndigital.com/" target="_blank">Western Digital India</a>.</p>
            <p>⏳ Outside of work, I play football ⚽ and badminton 🏸. I enjoy outdoor activities like hiking ⛰️ and via ferrata 🧗. I also read books 📖.</p>
            <p>📫 You can reach me at <a href="mailto:shrinidhi.bhat@rwth-aachen.de">shrinidhi.bhat@rwth-aachen.de</a></p>
        </div>
    </div>
    """, unsafe_allow_html=True)

    # Let them download the CV
    st.download_button(label="Download CV", data=pdf_bytes, file_name="CV.pdf", mime="application/pdf", key="download-cv")
    


if __name__ == "__main__":
    # Run the web portfolio function
    web_portfolio()
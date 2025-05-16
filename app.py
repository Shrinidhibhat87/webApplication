import os
import streamlit as st
from base64 import b64encode

def web_portfolio():
    # Set the page title and layout
    st.set_page_config(page_title="Shrinidhi Bhat's Portfolio", layout="wide", page_icon="🤖")
    
    st.write(f"""
    <div class="title" style="text-align: center; margin-left: 100px;">
    <span style='font-size: 32px;'> Welcome to my portfolio! My name is Shrinidhi Bhat </span> 👋
    </div>
    """, unsafe_allow_html=True)

    # Add padding to the title
    st.markdown("<style>div.block-container{padding-top: 4rem;}</style>", unsafe_allow_html=True)

    # Add profile image
    with open('images/image_zapikanka.jpg', 'rb') as image_file:
        # Use of base64 encoding to display the image
        image = "data:image/jpeg;base64," + b64encode(image_file.read()).decode()
    
    # Create two columns for layout
    col1, col2 = st.columns([1, 3], gap="small")

    # For PDF files
    with open('CV.pdf', 'rb') as pdf_file:
        pdf_bytes = pdf_file.read()

    with col1:
        # Display the information
        st.write(f"""
        <div style="display: flex; justify-content: left; align-items: left;  margin-left: 50px; padding: 10px;">
        <div class="box">
        <img src="{image}" alt="Shrinidhi Bhat" style="width: 300px; height: 375px;">
        </div>
        </div>
        """, unsafe_allow_html=True)
        # border-radius: 50%; margin-right: 20px;
        # Set the current title
        st.write(f"""
        <div class="subtitle" style="text-align: left; margin-left: 50px;"> Computer Vision Researcher and AI Engineer </div>""",
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
        <div style="display: flex; justify-content: left; margin-left: 150px;">{''.join(social_media_html)}</div>""", unsafe_allow_html=True)
        # Download button for CV
        st.write("""
        <style>
            div.stDownloadButton > button {
                display: block;
                padding: 10px 20px;
                font-size: 16px;
                font-weight: bold;
                background-color: #262626;
                color: white;
                border: none;
                border-radius: 5px;
                transition: background-color 0.3s ease;
                margin-left: 120px;
                margin-top: 15px;
            }
            div.stDownloadButton > button:hover {
                background-color: #45a049;
            }
            .download-container {
                display: flex;
                justify-content: center;
                margin-bottom: 20px;
            }
        </style>
        <div class="download-container"></div>
        """, unsafe_allow_html=True)

        st.download_button("Download CV", data=pdf_bytes, file_name="Resume.pdf", mime="application/pdf")

    with col2:
        # Display the "About Me" section
        st.markdown("""
        <div style="text-align: left; margin-left: 400px;">
            <h3 style="font-size: 24px; font-weight: bold;">About Me</h3>
        </div>
        <div style="padding: 20px;">
            <div style="text-align: left; max-width: 1000px;">
            <p>👁️ I am a <b>Computer Vision PhD Student and a Data Science Researcher</b> at <a href="https://www.fz-juelich.de/en/ias/ias-9" target="_blank">Forschungszentrum Jülich Materials Data Science and Informatics Team</a></p>
            <p>❤️ Passionate about 🤖 <i>Robotics</i>, <i>Computer Vision</i>, and <i>Machine Learning</i>.</p>
            <p>🎓 Graduated from RWTH Aachen University with a Masters in <i>Robotic Systems Engineering</i></p>
            <p>🚘 Master thesis at <a href="https://www.bmwgroup.com/en/general/approach-autonomous-driving-campus.html" target="_blank"> BMW Autonomous driving campus</a> on <i>Bandwidth Efficient Learning on Vision Transformers For Semantic Segmentation</i></p>
            <p>🤖 I was a Research Intern in the <a href="https://www.bosch-ai.com/research/fields-of-expertise/reinforcement-learning-control-and-optimization/" target="_blank"> <i>Robot Learning</i></a> team at Bosch center of AI where I worked on a <i>Multi-view segmentation pipeline</i></p>
            <p>💼 I have a full time working experience (2+ years) as an Embedded Firmware Developer at <a href="https://www.westerndigital.com/" target="_blank">Western Digital India</a>.</p>
            <p>⏳ Outside of work, I play football ⚽ and badminton 🏸. I enjoy outdoor activities like hiking ⛰️ and via ferrata 🧗. I also read books 📖.</p>
            <p>📫 You can reach me at <a href="mailto:shrinidhi.bhat@rwth-aachen.de">shrinidhi.bhat@rwth-aachen.de</a></p>
            </div>
        </div>
        """, unsafe_allow_html=True)

    # Define available sections
    sections = ["Work Experiences", "Projects", "Articles"]

    # Initialize session state to remember selected section
    if 'selected_section' not in st.session_state:
        # Default section
        st.session_state.selected_section = "Work Experiences"

    # Custom CSS to style the buttons
    st.markdown("""
    <style>
    div.stButton > button {
        margin-left: 265px;
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



    if selected_section == "Work Experiences":
        # Sample experience data (replace with yours in order)
        work_experiences = [
            {
                "title": "PhD Student (Computer Vision and Data Science)",
                "company": "Forschungszentrum Jülich IAS-9, Germany",
                "timeline": "01/2025 - Present",
                "topic": "Computer Vision methods for in-situ Scanning transmission electron microscopy",
                "tech stack": "Python, PyTorch, OpenCV, Numpy, Weights & Biases, LiberTEM, Matplotlib, CI/CD",
                "points": [
                    "Researching on computer vision methods to automate defect detection and tracking methods for novel 4D-STEM images.",
                    "Building an entire infrastructure for end-to-end computer vision pipeline for training and deployment"
                ]
            },
            {
                "title": "Master Thesis - Computer Vision",
                "company": "BMW, München",
                "timeline": "03/2024 - 07/2024",
                "topic": "Bandwidth Efficient Learning on Vision Transformers for Semantic Segmentation",
                "tech stack": "Python, PyTorch, HuggingFace, Tensorboard, Matplotlib, Docker, CI/CD, Pillow",
                "points": [
                    "Integrated Mask2Former, a SoTA vision transformer model into existing stack and created pipeline for scalable cluster training.",
                    "Pioneered architecture for image compression using attention maps, optimizing storage efficiency by 30%.",
                    "Developed custom torchvision transforms, reducing bandwidth usage by over 70%.",
                    "Used VAE-based generative AI for image reconstruction to optimize segmentation model performance."
                ]
            },
            {
                "title": "Robotics Intern - Robotic Perception",
                "company": "Bosch Center for AI, Renningen",
                "timeline": "09/2023 - 02/2024",
                "project": "3D Multiview segmentation pipeline for scene understanding",
                "tech stack": "Python, PyTorch, ROS2, Docker, ROS2 services, Open3D, OpenCV, RViz, Numpy, RestFul API, Meshlab, CI/CD, Code review",
                "points": [
                    "Designed and developed a 3D Multi-view segmentation pipeline on a multi-thread ROS2 node for the geometric perception stack of a household Robotic application",
                    "Implemented custom python libraries to construct and register 3D pointclouds for mapping in SLAM using RGBD data.",
                    "Developed a baseline library function that maps segments from one frame to another at the rate of 20Hz using 3D pointclouds.",
                    "Integrated SAM (Segment Anything Model), a SoTA foundational model for segmentation from RestFul API in the ROS2 node using ROS2 services.",
                    "Integrated GLIP, a vision-language model that takes language as input and outputs bounding box coordinates from a Docker container."
                ]
            },
            {
                "title": "Embedded AI- Working Student",
                "company": "Aptiv PLC, Wuppertal",
                "timeline": "09/2022 - 08/2023",
                "project": "Development and thorough unit testing of an optimization tool for the Aptiv Embedded AI Stack.",
                "tech stack": "JavaScript, Python, PyTorch, Docker, Github Actions, CI/CD, NPM, Jest, ONNXRuntime, TVM, ONNX",
                "points": [
                    "Customized and optimized Netron, a visualization tool, for efficient model optimization while also reducing debug time by over 50",
                    "Developed features for model optimization, for all edge frameworks like ONNXRuntime, TVM, ONNX.",
                    "Built the entire unit testing architecture for the tool using npm and jest.",
                    "Deployed the containerized testing architecture on a CI/CD pipeline using GitHub actions.",
                ]
            },
            {
                "title": "Engineer - Firmware Development",
                "company": "Western Digital India, Bangalore",
                "timeline": "07/2019 - 09/2021",
                "products": "18, 20, 22TB HDDs (Product Development) ; 16/18 TBs (Product Sustenance)",
                "tech stack": "C++, Git, Jenkins, CMake, Python, Jira, Agile, SAFe",
                "points": [
                    "Designed and optimized algorithms to prioritize commands for HDD processing, utilizing complex data structures like Queue, Graphs, Hashmaps",
                    "Implemented features to seamlessly integrate incoming commands into the appropriate data structures. Constructed and used ETL for analysis",
                    "Designed and delivered on Customer facing failure demands along with Value demands in the Dispatch eHDD team.",
                    "Engaged in end-to-end software development, testing, and validation within an Agile framework following SAFe methodologies.",
                ]
            },
            {
                "title": "Embedded IoT Intern",
                "company": "TAAL Tech India, Bangalore",
                "timeline": "12/2018 - 06/2019",
                "project": "Smart Building Lighting application.",
                "tech stack": "C, BLE Mesh protocol, UART protocol",
                "points": [
                    "Developed the firmware for BLE Mesh protocol from the ground up for a smart building lighting application.",
                    "Developed and tested the firmware on nRF52840 chipset that communicated with a mobile application",
                    "Integrated nRF52840 with UART for communication with sensors and drivers connected to the microcontroller",
                ]
            },
        ]

        # Inject CSS for box styling and background fading with dynamic theme support
        theme = st.get_option("theme.base")  # Get the current theme (light or dark)
        text_color = "#FFFFFF" if theme == "dark" else "#000000"  # White for dark theme, black for light theme
        background_color = "#581845" if theme == "dark" else "#F0F0F0"  # Dark purple for dark theme, light gray for light theme

        st.markdown(f"""
            <style>
            .experience-box {{
            background-color: {background_color};
            border-radius: 15px;
            padding: 20px;
            margin-bottom: 20px;
            box-shadow: 0 4px 8px rgba(0,0,0,0.1);
            transition: all 0.3s ease-in-out;
            color: {text_color};
            }}
            .experience-title {{
            font-size: 20px;
            font-weight: bold;
            }}
            .experience-company {{
            font-size: 18px;
            font-weight: 600;
            }}
            .experience-timeline {{
            font-size: 14px;
            color: #777;
            }}
            .experience-topic, .experience-project, .experience-products {{
            font-size: 16px;
            font-weight: 500;
            margin-top: 10px;
            font-style: italic;
            }}
            .experience-tech-stack {{
            font-size: 16px;
            font-weight: 500;
            margin-top: 10px;
            font-style: italic;
            }}
            .experience-points {{
            margin-top: 10px;
            }}
            </style>
        """, unsafe_allow_html=True)

        # Render the experience cards
        for idx, exp in enumerate(work_experiences):
            box_class = "experience-box"

            # Determine which key to display (topic, project, or products)
            description_key = "topic" if "topic" in exp else "project" if "project" in exp else "products"

            st.markdown(f"""
            <div class="{box_class}">
                <div class="experience-title">{exp['title']} - <span class="experience-company">{exp['company']}</span> 
                <span class="experience-timeline">({exp['timeline']})</span>
                </div>
                <div class="experience-{description_key}">{description_key.capitalize()}: {exp[description_key]}</div>
                <ul class="experience-points">
                {''.join(f"<li>{point}</li>" for point in exp['points'])}
                </ul>
            </div>
            """, unsafe_allow_html=True)

    elif selected_section == "Projects":

        # Theme-aware styling
        theme = st.get_option("theme.base")
        text_color = "#FFFFFF" if theme == "dark" else "#000000"

        # Title
        st.markdown("""
        <div style="text-align: center;">
            <h1>Projects</h1>
        </div>
        """, unsafe_allow_html=True)

        # List of projects
        projects = [
            {
            "title": "3D Bounding Box Prediction",
            "description": "Built an end-to-end pipeline using 3DETR for predicting bounding box corners on point cloud data.",
            "image_path": "images/3dboundingbox.png",
            "github_url": "https://github.com/Shrinidhibhat87/codingchallenge_sereact",
            "points": [
                "Developed an end-to-end deep learning pipeline for 3D bounding box prediction, integrating a custom dataloader, data augmentation, and a transformer-based model architecture.",
                "Conducted extensive research on state-of-the-art transformer methodologies, adapting them to enhance performance on limited datasets.",
                "Optimized model performance by refining loss functions and systematically tuning hyperparameters, achieving a mean Intersection over Union (IoU) of 0.27 with only 100 samples.",
                "Utilized Weights and Biases for comprehensive experiment tracking, enabling effective monitoring and analysis of model training and validation metrics."
            ]
            },
            {
            "title": "Master Thesis - Transformer based Compression for Semantic Segmentation",
            "description": "Integrated Mask2Former and built a bandwidth efficient semantic segmentation framework on CityScapes dataset.",
            "image_path": "images/master_thesis.png",
            "github_url": "https://github.com/Shrinidhibhat87/MasterThesis",
            "points": [
                "Designed and developed the entire architecture for bandwidth efficient semantic segmentation using Mask2Former.",
                "Build custom dataloaders and torchvision transforms to reduce bandwidth usage by over 70%.",
                "Integrated VAE for image reconstruction to compare with baseline model performance."
            ]
            },
            {
            "title": "Monocular visual odometry",
            "description": "Built a monocular visual odometry pipeline using OpenCV, FAST, and the Lucas-Kanade optical flow algorithm (KLT) for feature tracking.",
            "image_path": "images/visual_odometry.png",
            "github_url": "https://github.com/Shrinidhibhat87/monocular_visual_odometry",
            "points": [
                "Developed monocular visual odometry algorithm that estimates camera motion between consecutive frames.",
                "Implemented image preprocessing, FAST feature detection, 5-point algorithm for essential matrix estimation, RANSAC for outlier rejection.",
                "Ensured clean, modular, and well structured C++ code with Git version control for effective collaboration and continuous integration."
            ]
            }
        ]

        # Inject CSS for styling project descriptions
        st.markdown("""
        <style>
        .project-description {
            font-size: 18px;
        }
        </style>
        """, unsafe_allow_html=True)

        # Render each project
        for project in projects:
            # Use two columns: image on left, text on right
            col1, col2 = st.columns([1, 4], gap="small")
            
            with col1:
                if os.path.exists(project["image_path"]):
                    st.image(project["image_path"], width=400)
                else:
                    st.warning(f"Image not found: {project['image_path']}")

            with col2:
                st.markdown(f"### [{project['title']}]({project['github_url']})")
                st.markdown(f"<p class='project-description'>{project['description']}</p>", unsafe_allow_html=True)
                st.markdown("<ul>", unsafe_allow_html=True)
                for point in project["points"]:
                    st.markdown(f"<li>{point}</li>", unsafe_allow_html=True)
                st.markdown("</ul>", unsafe_allow_html=True)
            
            st.markdown("---")

    elif selected_section == "Articles":
        # Theme-aware styling
        theme = st.get_option("theme.base")
        text_color = "#FFFFFF" if theme == "dark" else "#000000"
        background_color = "#581845" if theme == "dark" else "#F0F0F0"

        # Title
        st.markdown("""
        <div style="text-align: center;">
            <h1>Articles</h1>
        </div>
        """, unsafe_allow_html=True)

        # List of articles
        articles = [
            {
                "title": "Supervised 3D Bounding Box Detection Pipeline",
                "description": "A comprehensive guide to building an end-to-end pipeline for 3D object detection using transformer-based architectures.",
                "image_path": "images/3dboundingbox.png",
                "url": "https://medium.com/@shrinidhi.bhat/supervised-3d-bounding-box-detection-pipeline-e6a8c9976165",
                "date": "April 2025",
                "reading_time": "8 min read"
            }
            # Add more articles here as needed
        ]

        # CSS for article cards
        st.markdown(f"""
        <style>
        .article-card {{
            background-color: {background_color};
            border-radius: 15px;
            padding: 20px;
            margin-bottom: 20px;
            box-shadow: 0 4px 8px rgba(0,0,0,0.1);
            transition: all 0.3s ease-in-out;
            color: {text_color};
            display: flex;
            align-items: center;
        }}
        .article-card:hover {{
            transform: translateY(-5px);
            box-shadow: 0 6px 12px rgba(0,0,0,0.15);
        }}
        .article-image {{
            flex: 1;
            margin-right: 20px;
        }}
        .article-content {{
            flex: 3;
        }}
        .article-title {{
            font-size: 22px;
            font-weight: bold;
            margin-bottom: 10px;
        }}
        .article-meta {{
            font-size: 14px;
            color: #777;
            margin-bottom: 10px;
        }}
        .article-description {{
            font-size: 16px;
            margin-bottom: 15px;
        }}
        .read-more-btn {{
            display: inline-block;
            padding: 8px 16px;
            background-color: #262626;
            color: white;
            text-decoration: none;
            border-radius: 5px;
            font-weight: bold;
            transition: background-color 0.3s ease;
        }}
        .read-more-btn:hover {{
            background-color: #45a049;
        }}
        </style>
        """, unsafe_allow_html=True)

        # Render each article
        for article in articles:
            st.markdown(f"""
            <div class="article-card">
                <div class="article-image">
                    <img src="data:image/jpeg;base64,{b64encode(open(article['image_path'], 'rb').read()).decode()}" alt="{article['title']}" style="width:100%; border-radius:10px;">
                </div>
                <div class="article-content">
                    <div class="article-title">{article['title']}</div>
                    <div class="article-meta">{article['date']} · {article['reading_time']}</div>
                    <div class="article-description">{article['description']}</div>
                    <a href="{article['url']}" target="_blank" class="read-more-btn">Read on Medium</a>
                </div>
            </div>
            """, unsafe_allow_html=True)


if __name__ == "__main__":
    # Run the web portfolio function
    web_portfolio()

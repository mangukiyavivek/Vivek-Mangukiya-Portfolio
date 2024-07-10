import streamlit as st

# Adding CSS for animations and styling
st.markdown(
    """
    <style>
    @keyframes fadeIn {
        from {opacity: 0;}
        to {opacity: 1;}
    }
    .fade-in {
        animation: fadeIn 2s;
    }
    .big-font {
        font-size: 50px !important;
        text-align: center;
    }
    .contact, .skills, .education, .profile, .experience, .projects {
        margin-top: 20px;
    }
    </style>
    """,
    unsafe_allow_html=True
)

def display_animation(text):
    st.markdown(f'<div class="fade-in">{text}</div>', unsafe_allow_html=True)

# Title Section
display_animation('<div class="big-font">VIVEK MANGUKIYA</div>')

# Image Section
st.image('IMG_1510.JPG',width=300, use_column_width=False)

# Contact Section
contact = """
<div class="contact">
    <h2>Contact</h2>
    <ul>
        <li>Email: vivekmangukiya1102@gmail.com</li>
        <li>Location: Surat, Gujarat, India</li>
        <li>LinkedIn: <a href="https://www.linkedin.com/in/vivek-mangukiya-51881b203/">Vivek Mangukiya</a></li>
        <li>Upwork: <a href="https://www.upwork.com/freelancers/~01ccb1aedfbc60406f?viewMode=1">Vivek Mangukiya</a></li>
        <li>Github: <a href="https://github.com/mangukiyavivek">mangukiyavivek</a></li>
    </ul>
</div>
"""
display_animation(contact)

# Skills & Tools Section
skills = """
<div class="skills">
    <h2>Skills & Tools</h2>
    <ul>
        <li>Python, FastAPI, Django</li>
        <li>Streamlit, AWS</li>
        <li>Docker, Git</li>
        <li>MySQL, PostgreSQL, SQLite</li>
        <li>Beautifulsoup, Selenium, Web-Scraping</li>
    </ul>
</div>
"""
display_animation(skills)

# Education Section
education = """
<div class="education">
    <h2>Education</h2>
    <ul>
        <li>BE Computer Engineering</li>
        <li>Bhagwan Mahavir University, 2021-2024</li><br>    
        <li>Diploma Computer Engineering</li>
        <li>Gujarat Technological University, 2018-2021</li>
    </ul>
</div>
"""
display_animation(education)

# Profile Section
profile = """
<div class="profile">
    <h2>Profile</h2>
    <h3>Python Developer</h3>
    <p>Experienced Python developer with a strong background in web development and data analysis. Proficient in building robust APIs using FastAPI, automating tasks with web scraping tools like BeautifulSoup, and creating interactive data visualizations with Streamlit. Skilled in managing relational databases such as MySQL and PostgreSQL. Passionate about delivering high-quality, scalable solutions that drive business success.</p>
</div>
"""
display_animation(profile)

# Experience Section
experience = """
<div class="experience">
    <h2>Experience</h2>
    <h3>Web Developer</h3>
    <h6>2023/07 TO 2023/09</h6>
    <ul>
        <li>During my web development internship, I cultivated proficiency in creating dynamic and user-friendly websites. Engaging with seasoned developers, I actively contributed to various web projects, gaining insights into modern development practices. Through troubleshooting and optimizing website performance, I honed my problem-solving skills. This internship experience reinforced my understanding of web technologies and frameworks, preparing me for a successful career in web development.</li>
    </ul>
</div>
"""
display_animation(experience)

# Projects Section
projects = """
<div class="projects">
    <h2>Projects</h2>
    <ul>
    <h5> 1) Attendance Management System </h5>
    <h6> Diploma 2018 - 2021 </h6>
        <li>An Attendance Management System records and maintains students' attendance data using smart devices. The system collects, manages, stores, and processes attendance records, generating daily reports that enable faculty to track student presence with high accuracy and efficiency</li><br>
    <h5> 2) Lab Tracker </h5>
    <h6> BEng 2021 - 2024 </h6>    
        <li>The main goal of this project is to overcome the issues between faculty and students during laboratory sessions. The website is primarily used by students and faculty to track pending practicals and to conduct practicals online. The front-end is developed using HTML, CSS, and JavaScript, while the back-end is built with PHP and MySQL.</li>
    </ul>
</div>
"""
display_animation(projects)

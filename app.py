import streamlit as st


st.set_page_config(
    page_title="Sam Cole, M.S. Technology Innovation (Robotics) 2025",
    page_icon="🦧",
    layout="centered",  # centered or wide
    initial_sidebar_state="auto",
)

col1, col2 = st.columns([0.3, 0.7])
with col1:
    st.image("apple_vision_pro.jpg")
    
with col2:
    st.markdown(
        """
    # Sam Cole (He/Him)
    - M.S. Technology Innovation (Robotics), University of Washington 2025
    - B.S. Computer Engineering, California Polytechnic University San Luis Obispo 2022
    """
    )

st.markdown("""
# About  
Hello! I am a Masters student at the University of Washington originally from
Sonoma County, California. I am passionate about entrepreneurship and 
everything robotics, but love solving complex problems that make businesses more 
effcient. I consider myself a jack of all trades and have experience 
in **Robotics Sim/Manipulation/Navigation, Machine Learning,
Web Development, Embedded Systems, Startups, and Process Automation**. 

""")



st.markdown("""# Work Experience""")

# st.markdown("#### Simulation Software Engineering Intern")
col1, col2 = st.columns([0.25, 0.75])

col1.markdown("""
    <style>
    .company-img img {
        width: 85%;
        border-radius: 10%;
    }
    </style>
    **Reliable Robotics**  
    June 2023 - Sep 2023

    <div class="company-img">

    ![](https://media.licdn.com/dms/image/C560BAQHjktxC_txolA/company-logo_200_200/0/1630597143184/reliablerobotics_logo?e=1720051200&v=beta&t=U3BEbIGVeTR93PV_b570w995ovd-zcyi2G7zeBa6YzE)
    </div>  
    """,
unsafe_allow_html=True)

with col2:
    st.markdown("""
    #### Simulation Software Engineering Intern
    - Independently added new test hardware/software to HITL aircraft simulation for anti skid brake testing.
    - Developed hardware driver and simulation module for generating PWM signals using a UEI DAQ.
    - Validated work by running takeoff/landing simulations and stimulating test flight computer.
    """, unsafe_allow_html=True)
st.markdown("<br/>", unsafe_allow_html=True)

col1, col2 = st.columns([0.25, 0.75])

col1.markdown("""
    <style>
    .company-img img {
        width: 85%;
        border-radius: 10%;
    }
    </style>
    **TensorMaker**  
    Feb 2023 - May 2023

    <div class="company-img">

    ![](https://media.licdn.com/dms/image/C4E0BAQHbhOMEr6KrDA/company-logo_100_100/0/1676702855927/tensormaker_logo?e=1720051200&v=beta&t=GJcBNVGk_jiEb81G-z35plAKcq8EyfcPRd5U0aDHoR8)
    </div>  
    """,
unsafe_allow_html=True)

with col2:
    st.markdown("""
    #### Co-Founder, Chief Technology Officer
    - Developed an MVP for a no-code Computer Vision ML platform using **Django** and **React JS**
    - Finalist in Cal Poly CIE Innovation Quest 2023
    """, unsafe_allow_html=True)
st.markdown("<br/>", unsafe_allow_html=True)
col1, col2 = st.columns([0.25, 0.75])

col1.markdown("""
    <style>
    .company-img img {
        width: 85%;
        border-radius: 10%;
    }
    </style>
    **TechnipFMC Schilling Robotics**  
    Jun 2022 - Sep 2022

    <div class="company-img">

    ![](https://media.licdn.com/dms/image/D560BAQHw_lZxbXIEew/company-logo_200_200/0/1702465362752/technipfmc_logo?e=1720051200&v=beta&t=hSwhoCSDdRqNIDwC4olNdf4JNaf874vYEonzRBDtHrk)
    </div>  
    """,
unsafe_allow_html=True)

with col2:
    st.markdown("""
    #### Software Engineering Intern
- Independently developed a simulation layer in Ignition Gazebo for a **ROS2** underwater flight control stack.
- Developed a **ROS2** hardware driver for servo system derived from in-house technical datasheet.
    """, unsafe_allow_html=True)

st.markdown("<br/>", unsafe_allow_html=True)
col1, col2 = st.columns([0.25, 0.75])

col1.markdown("""
    <style>
    .company-img img {
        width: 85%;
        border-radius: 10%;
    }
    </style>
    **Lockheed Martin Space**  
    Jun 2021 - Oct 2021

    <div class="company-img">

    ![](https://media.licdn.com/dms/image/C4E0BAQHF1YKEZdN4LA/company-logo_200_200/0/1668532986109/lockheed_martin_logo?e=1720051200&v=beta&t=4yQwGOfksNgamUH4IU3CF6zAhT37R53vqldEPmtIo-0)
    </div>  
    """,
unsafe_allow_html=True)

with col2:
    st.markdown("""
    #### Software Engineering Intern
- Developed a custom Computer Vision data pipeline using Intel RealSense depth cameras.
- Assisted in developing network architecture to share and visualize data captured with depth cameras.
- Assisted in developing an HLS live streaming setup with multiple cameras and multiple Nvidia Jetson Nanos, using Gstreamer.
    """, unsafe_allow_html=True)


st.markdown("""
# Hobbies
In my freetime I enjoy bouldering 🪨, lifting weights 💪, backpacking 🎒,  and playing the guitar 🎸

""")


st.markdown(""" 
# Projects  
### Alzi - Alzheimers Caregiver Chatbot 
**Dec 2023 - Present** 
- Product Development and backend deveolper for Alzi, a AI powered chatbot designed to 
alleviate the stress placed upon family caregivers of early stage Alzheimers patients.
- Built and [hosted an MVP](https://witty-pebble-0b4c4811e.4.azurestaticapps.net/) in Django, React JS and MongoDB
- Formulated Business Proposal and Pitch Deck for the business.
- Qualified for Microsoft Imagine 2024.

### UW Personal Robotics Lab 
**March 2024 - Present**
- Working under PhD candidate, Sidharth Talia, on developing a Visual Interial Odometry
system for use with MuSHR racecar project using the Intel D435 Depth Camera.
""")


ft = """
<style>
a:link , a:visited{
color: #BFBFBF;  /* theme's text color hex code at 75 percent brightness*/
background-color: transparent;
text-decoration: none;
}

a:hover,  a:active {
color: #0283C3; /* theme's primary color*/
background-color: transparent;
text-decoration: underline;
}

#page-container {
  position: relative;
  min-height: 10vh;
}

footer{
    visibility:hidden;
}

.footer {
position: relative;
left: 0;
top:230px;
bottom: 0;
width: 100%;
background-color: transparent;
color: #808080; /* theme's text color hex code at 50 percent brightness*/
text-align: left; /* you can replace 'left' with 'center' or 'right' if you want*/
}
</style>

<div id="page-container">

<div class="footer">
<p style='font-size: 0.875em;'>Made with <a style='display: inline; text-align: left;' href="https://streamlit.io/" target="_blank">Streamlit</a><br 'style= top:3px;'>
with <img src="https://em-content.zobj.net/source/skype/289/red-heart_2764-fe0f.png" alt="heart" height= "10"/><a style='display: inline; text-align: left;' href="https://github.com/sape94" target="_blank"> by sape94</a></p>
</div>

</div>
"""
st.write(ft, unsafe_allow_html=True)
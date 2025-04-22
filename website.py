import streamlit as st
import cohere

print("Sending to Cohere...")
co = cohere.ClientV2("fRgcHaVtXuuC2Q59x3t5kYzRElBLx4bldXCuFOZn")
print("Received response.")

st.set_page_config(page_title="Solace", page_icon='🌙')

st.markdown("""
    <style>
    
        header[data-testid="stHeader"] {
            background-color: transparent;
        }

        .stApp {
            background-image: url("https://marketplace.canva.com/EAGK_VGJ-wk/1/0/1600w/canva-purple-illustrative-lavender-desktop-wallpaper-IJjKe9JIOeM.jpg");
            background-size: cover;
            background-repeat: no-repeat;
            background-attachment: fixed;
            background-position: center;
        }
        
        .eht7o1d3 {
            background-color: transparent;
        }
    </style>
""", unsafe_allow_html=True)

if 'chat_history' not in st.session_state:
    st.session_state.chat_history = [{"role": "system",
                                      "content": "You are a helpful chatbot for people who feel depressed or are having hurtful thoughts. You are there to help people with mental problems for phsycological support and emotional wellbeing. You will help them cope with thier situation, whatever that maybe. If they try to deviate the topic, bring them back to the topic of mental wellbeing. dont give your responses too long. make them short and consise."}, ]


st.title("SOLACE 🌙")
st.subheader("𝗦ervice 𝗢f 𝗟ove 𝗔nd 𝗖are for 𝗘motions")
st.subheader("I'm a chatbot designed to care for your emotional well-being. Talk to me about any problems you might have!")
user_input = st.chat_input("You:")

st.markdown("""
    <style>
        #bb0e3299 {
            text-align: center;
            color: black;
        }
        #e7ae617f {
            text-align: center;
            color: black;
        }
        #i-m-a-chatbot-designed-to-care-for-your-emotional-well-being-talk-to-me-about-any-problems-you-might-have {
            font-style: italic;
            color: black;
        }
    </style> 
    """, unsafe_allow_html=True)

if user_input:
    st.session_state.chat_history.append({"role": "user", 'content': user_input})

    response = co.chat(
        model="command-a-03-2025",
        messages=st.session_state.chat_history
    )

    reply = response.message.content[0].text
    st.session_state.chat_history.append({"role": "assistant", "content": reply})


for msg in st.session_state.chat_history[1:]:
    if msg['role'] == 'user':
        st.markdown(f'<div style="background-color:#40605b; border-radius: 15px; padding: 10px; margin-bottom: 10px; margin-left: 500px; color: #ffffff;">'
                        f'<b>You:</b> {msg["content"]}</div>', unsafe_allow_html=True)
    else:
        st.markdown(f'<div style="background-color: #352d3f; border-radius: 15px; padding: 10px; margin-bottom: 10px; margin-right: 300px; color: #ffffff;">'
                        f'<b>Bot:</b> {msg["content"]}</div>', unsafe_allow_html=True)
        
#------BREATHING----
st.markdown("""
     <div style="position: fixed; top:30%; right: 300px; transform: translateY(-50%); z-index: 999;">
        <a href="https://mindfuldevmag.com/breathing-timer/" target="_blank" style="text-decoration: none;">
            <img src="https://cdn-icons-png.flaticon.com/128/2451/2451263.png" 
                 alt="Breathing Icon" width="120" height="120" 
                        transition: transform 0.2s ease-in-out;" 
                 onmouseover="this.style.transform='scale(1.1)'" 
                 onmouseout="this.style.transform='scale(1)'">
                 <p style="margin-top: 8px; color: black; font-size: 20px;">𝑵𝒆𝒆𝒅 𝒂 𝒃𝒓𝒆𝒂𝒕𝒉𝒆𝒓?</p>
        </a>
    </div>
""", unsafe_allow_html=True)


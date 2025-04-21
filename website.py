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
            background-image: url("https://img.freepik.com/free-photo/beautiful-outdoor-view-with-tropical-beach-sea_74190-6852.jpg");
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
        st.markdown(f'<div style="background-color: #e8be32; border-radius: 15px; padding: 10px; margin-bottom: 10px; margin-left: 500px; color: #000000;">'
                        f'<b>You:</b> {msg["content"]}</div>', unsafe_allow_html=True)
    else:
        st.markdown(f'<div style="background-color: #F1F0F0; border-radius: 15px; padding: 10px; margin-bottom: 10px; margin-right: 300px; color: #000000;">'
                        f'<b>Bot:</b> {msg["content"]}</div>', unsafe_allow_html=True)
        

import cohere

co = cohere.ClientV2("fRgcHaVtXuuC2Q59x3t5kYzRElBLx4bldXCuFOZn")

conversation_history = [
                {"role": "system", "content": "You are a helpful chatbot for people who feel depressed or are having hurtful thoughts. You are there to help people with mental problems for phsycological support and emotional wellbeing. You will help them cope with thier situation, whatever that maybe. If they try to deviate the topic, bring them back to the topic of mental wellbeing. dont give your responses too long. make them short and consise."}
]

def psychology_chat(user_input):

    conversation_history.append({"role": "system", "content": user_input})
    
    response=co.chat(
        model="command-a-03-2025",
        messages=conversation_history
    )
    return response.message.content[0].text

    next_reply = response.message.content[0].text
    conversation_history.append({"role": "assistant", "content": next_reply})
    
print('Emotional Support Chatbot ~ Type exit to stop \n')
while True:
    user_input = input("You: ")
    if user_input.lower() == "exit":
        break

    response = psychology_chat(user_input)
    print("Bot: ", response)

    
import streamlit as st

# Define function to set background
def set_background():
    st.markdown("""
        <style>
        .stApp {
            background-color: beige;
        }
        .stTitle {
            background-color: green;
            color: white;
            padding: 10px;
        }
        </style>
    """, unsafe_allow_html=True)

def main():
    set_background()  # Set background color

    st.markdown('<h1 class="stTitle">Mental Health and Relationship Questionnaire</h1>', unsafe_allow_html=True)
    
    # Initialize session state
    if 'step' not in st.session_state:
        st.session_state.step = 0
        st.session_state.answers = {}

    # Start button
    if st.session_state.step == 0:
        if st.button("Get Started"):
            st.session_state.step = 1
            st.rerun()
    
    # Question 1: Mental State
    elif st.session_state.step == 1:
        answer = st.radio("Choose your current mental state:", [i for i in range(1, 11)], horizontal=True, help="0 = Not good to 10 = Absolutely fine")
        st.write(f"You selected: {answer}")
        if st.button("Next"):
            st.session_state.answers['mental_state'] = answer  
            st.session_state.step = 2 
            st.rerun()  




    # Question 2: Self-Care
    elif st.session_state.step == 2:
        answer = st.radio("How often do you take time for self-care?", ["Never", "Sometimes", "Often", "Always"])
        if st.button("Next"):
            st.session_state.answers['self_care'] = answer
            st.session_state.step = 3
            st.rerun()

    # Question 3: Stress/Anxiety
    elif st.session_state.step == 3:
        answer = st.radio("How often do you feel stressed or anxious?", ["Never", "Sometimes", "Often", "Always"])
        if st.button("Next"):
            st.session_state.answers['stress_anxiety'] = answer
            st.session_state.step = 4
            st.rerun()

    # Question 4: Talking About Feelings
    elif st.session_state.step == 4:
        answer = st.radio("Do you find it difficult to talk about your feelings with others?", ["Yes", "No"])
        if st.button("Next"):
            st.session_state.answers['talk_feelings'] = answer
            if answer == "Yes":
                st.session_state.step = 4.1  
            else:
                st.session_state.step = 4.2  
            st.rerun()

    # Page 4.1: Difficult to talk about feelings
    elif st.session_state.step == 4.1:
        st.write(
            "It is okay to find it difficult, many of us find it difficult. But I believe going through this process will help you as it helped me and many others before. Together, we are stronger."
        )
        if st.button("Next"):
            st.session_state.step = 5
            st.rerun()

    # Page 4.2: Comfortable talking about feelings
    elif st.session_state.step == 4.2:
        st.write(
            "That is great! Being able to open to others gets you one step closer to healing. Let's continue the good work together."
        )
        if st.button("Next"):
            st.session_state.step = 5
            st.rerun()

    # Question 5: Relationship Satisfaction
    elif st.session_state.step == 5:
        answer = st.radio("If any, how satisfied are you with your relationship?", ["Not Satisfied", "Could be better", "Very Satisfied", "Not applicable"])
        if st.button("Next"):
            st.session_state.answers['relationship_satisfaction'] = answer
            if answer in ["Not Satisfied", "Could be better"]:
                st.session_state.step = 5.5
            else:
                st.session_state.step = 6
            st.rerun()

    # Question 5.5: Improving Relationship
    elif st.session_state.step == 5.5:
        st.text_input("In a few words, please describe how your relationship could be more satisfying:")
        if st.button("Next"):
            st.session_state.step = 6
            st.rerun()

    # Question 6: Support System
    elif st.session_state.step == 6:
        answer = st.slider("Do you feel supported by your friends and family?", 0, 10)
        if st.button("Next"):
            st.session_state.answers['support_system'] = answer
            st.session_state.step = 7
            st.rerun()

    # Question 7 (Conflict Handling) - Checkboxes with descriptions
    elif st.session_state.step == 7:
        st.write("**Multiple answers can be chosen**")
        
        options = [
            "I handle conflicts by making sure to openly and calmly communicate my feelings, and I try to listen actively to the other person's perspective without interrupting or judging.",
            "I focus on understanding the other person's emotions and needs, and I make an effort to empathize with their perspective, even if I don't fully agree.",
            "I try to identify areas where we can agree or compromise, so we can work towards a solution that benefits both of us.",
            "I reflect on my own actions and take accountability for any part I may have played in the conflict, apologizing if needed.",
            "If emotions run high, I suggest taking a short break to cool down and revisit the issue when both parties are calmer and more focused.",
            "I focus on addressing the specific problem rather than blaming the person, and I work collaboratively to come up with a practical solution.",
            "If the conflict feels too big to resolve on our own, I’m open to seeking guidance from a counselor or mediator to gain a fresh perspective.",
            "When I deem him/her non-reasonable, I lose patience and if he/she does not want to listen, it becomes a shouting match"
        ]
        selected_options = []
        for option in options:
            selected = st.checkbox(option)
            if selected:
                selected_options.append(option)

        if st.button("Next"):
            st.session_state.answers['q8'] = selected_options
            st.session_state.step = 8
            st.rerun()

    # Question 8: Future Goals
    elif st.session_state.step == 8:
        answer = st.radio("Do you have clear goals for the future?", ["Yes", "No"])
        if st.button("Next"):
            st.session_state.answers['future_goals'] = answer
            st.session_state.step = 9
            st.rerun()

    # Question 9: Challenge Comfort Zone
    elif st.session_state.step == 9:
        answer = st.radio("How often do you challenge yourself to step out of your comfort zone?", ["Never", "Sometimes", "Often", "Always"])
        if st.button("Next"):
            st.session_state.answers['challenge_comfort_zone'] = answer
            st.session_state.step = 10
            st.rerun()

    # Question 10: Burnout
    elif st.session_state.step == 10:
        answer = st.radio("Do you feel burnt out from your current responsibilities?", ["Yes", "No"])
        if st.button("Next"):
            st.session_state.answers['burnout'] = answer
            st.session_state.step = 11
            st.rerun()

    # Question 11: Overwhelm
    elif st.session_state.step == 11:
        answer = st.radio("In the past week, how often did you feel overwhelmed?", ["Never", "A little", "A lot", "Constantly"])
        if st.button("Next"):
            st.session_state.answers['overwhelmed'] = answer
            st.session_state.step = 12
            st.rerun()

    # Question 12: Stress Management
    elif st.session_state.step == 12:
        answer = st.radio("Do you have strategies to manage stress?", ["Yes", "No"])
        if st.button("Next"):
            st.session_state.answers['stress_management'] = answer
            if answer == "Yes":
                st.session_state.step = 12.5
            else:
                st.session_state.step = 13
            st.rerun()

    # Question 12.5: Coping Techniques
    elif st.session_state.step == 12.5:
        answer = st.radio("Would you like to know about our techniques to cope with stress?", ["Yes", "No (I find my strategy efficient enough)"])
        if st.button("Next"):
            st.session_state.step = 13
            st.rerun()

    # Question 13: Comfort Discussing Issues
    elif st.session_state.step == 13:
        answer = st.slider("How comfortable are you discussing personal issues with close friends or family?", 0, 10)
        if st.button("Next"):
            st.session_state.answers['comfort_discussing'] = answer
            st.session_state.step = 14
            st.rerun()

    # Profile Generation
    elif st.session_state.step == 14:
        st.subheader("Your Profile:")
        st.write(st.session_state.answers)

        # Calculate Help Time (based on answers)
        help_time = 5  # default for positive answers
        if st.session_state.answers['mental_state'] <= 3 or st.session_state.answers['stress_anxiety'] == 'Always':
            help_time = 30  # high need for help
        elif st.session_state.answers['mental_state'] <= 5:
            help_time = 15  # moderate need

        st.write(f"Suggested help duration: {help_time} days")
        
        if st.button("Restart"):
            st.session_state.step = 0
            st.session_state.answers = {}
            st.rerun()

    # Previous button functionality
    if st.session_state.step > 0 and st.session_state.step not in [4.1, 4.2, 5.5, 12.5]:
        if st.button("Previous"):
            st.session_state.step -= 1
            st.rerun()


if __name__ == "__main__":
    main()

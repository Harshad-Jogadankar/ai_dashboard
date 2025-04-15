import streamlit as st
from simple_auth import sign_in, sign_up, reset_password


def show_login_page():
   
    st.markdown("""
        <style>
        html, body, [data-testid="stAppViewContainer"] {
            width: 100vw;
            display: flex;
            justify-content: center;
            align-items: center;
            min-height: 100vh;
        }
        body {
            background: linear-gradient(135deg, #FFE5E2, #FFF0F0);
            background-size: 400% 400%;
            animation: gradient 15s ease infinite;
        }
        @keyframes gradient {
            0% { background-position: 0% 50%; }
            50% { background-position: 100% 50%; }
            100% { background-position: 0% 50%; }
        }
        .auth-container {
            max-width: 400px;
            margin: auto;
            padding: 30px;
            background: rgba(255, 255, 255, 0.95);
            border-radius: 12px;
            backdrop-filter: blur(10px);
            box-shadow: 0 8px 32px 0 rgba(221, 71, 55, 0.2);
            border: 1px solid rgba(221, 71, 55, 0.2);
        }
        .auth-title {
            text-align: center;
            margin-bottom: 30px;
            padding: 10px;
            border-radius: 5px;
            color: #DD4737;
            font-weight: bold;
            font-size: 24px;
            text-shadow: 1px 1px 2px rgba(0, 0, 0, 0.1);
        }
        .stTextInput input {
            color: #000000;
            background: white;
            border-radius: 5px;
            border: 1px solid #DD4737;
            padding: 10px;
        }
        .stButton button {
            color: white;
            background: #DD4737;
            border-radius: 5px;
            padding: 10px 20px;
            font-weight: bold;
            transition: all 0.3s ease;
        }
        .stButton button:hover {
            background: #C13A2B;
            transform: translateY(-2px);
            box-shadow: 0 5px 15px rgba(221, 71, 55, 0.4);
        }
        [data-testid="stBlock"] {
            border: none !important;
            padding: 0 !important;
        }
        </style>
    """, unsafe_allow_html=True)

    # Wrap your form in the styled container
    st.markdown('<div class="auth-container">', unsafe_allow_html=True)

    st.markdown('<h2 class="auth-title">Login to AI Dashboard Generator</h2>', unsafe_allow_html=True)
    
    with st.form("login_form"):
        email = st.text_input("Email")
        password = st.text_input("Password", type="password")
        submit = st.form_submit_button("Login")
        
        if submit:
            user = sign_in(email, password)
            if user:
                # Store user info in session state
                st.session_state['user'] = user
                st.session_state['authenticated'] = True
                st.rerun()
    
    col1, col2 = st.columns(2)
    with col1:
        if st.button("Forgot Password?"):
            st.session_state['show_reset'] = True
            st.session_state['show_login'] = False
            st.rerun()
    with col2:
        if st.button("Create Account"):
            st.session_state['show_signup'] = True
            st.session_state['show_login'] = False
            st.rerun()
    
    st.markdown('</div>', unsafe_allow_html=True)

def show_signup_page():
    st.markdown("""
        <style>
        body {
            background: linear-gradient(135deg, #DD4737, #FF6B6B);
            background-size: 400% 400%;
            animation: gradient 15s ease infinite;
        }
        @keyframes gradient {
            0% {
                background-position: 0% 50%;
            }
            50% {
                background-position: 100% 50%;
            }
            100% {
                background-position: 0% 50%;
            }
        }
        .auth-container {
            max-width: 400px;
            margin: 0 auto;
            padding: 20px;
            background: rgba(255, 255, 255, 0.9);
            border-radius: 10px;
            backdrop-filter: blur(10px);
            box-shadow: 0 8px 32px 0 rgba(31, 38, 135, 0.37);
            border: 1px solid rgba(255, 255, 255, 0.18);
        }
        .auth-title {
            text-align: center;
            margin-bottom: 30px;
            padding: 10px;
            border-radius: 5px;
            color: #DD4737;
            font-weight: bold;
            text-shadow: 1px 1px 2px rgba(0, 0, 0, 0.1);
        }
        .stTextInput input {
            color: #000000;
            background: white;
            border-radius: 5px;
            border: 1px solid #DD4737;
            padding: 10px;
        }
        .stButton button {
            color: white;
            background: #DD4737;
            border-radius: 5px;
            padding: 10px 20px;
            font-weight: bold;
            transition: all 0.3s ease;
        }
        .stButton button:hover {
            background: #C13A2B;
            transform: translateY(-2px);
            box-shadow: 0 5px 15px rgba(221, 71, 55, 0.4);
        }
        </style>
    """, unsafe_allow_html=True)
    
    st.markdown('<div class="auth-container">', unsafe_allow_html=True)
    st.markdown('<h2 class="auth-title">Create Account</h2>', unsafe_allow_html=True)
    
    with st.form("signup_form"):
        email = st.text_input("Email")
        password = st.text_input("Password", type="password")
        confirm_password = st.text_input("Confirm Password", type="password")
        submit = st.form_submit_button("Sign Up")
        
        if submit:
            if not email or not password or not confirm_password:
                st.error("Please fill in all fields")
            elif password != confirm_password:
                st.error("Passwords do not match")
            else:
                user = sign_up(email, password)
                if user:
                    st.success("Account created successfully! Please login.")
                    st.session_state['show_signup'] = False
                    st.session_state['show_login'] = True
                    st.rerun()
    
    if st.button("Back to Login"):
        st.session_state['show_signup'] = False
        st.session_state['show_login'] = True
        st.rerun()
    
    st.markdown('</div>', unsafe_allow_html=True)

def show_reset_password_page():
    st.markdown("""
        <style>
        body {
            background: linear-gradient(135deg, #DD4737, #FF6B6B);
            background-size: 400% 400%;
            animation: gradient 15s ease infinite;
        }
        @keyframes gradient {
            0% {
                background-position: 0% 50%;
            }
            50% {
                background-position: 100% 50%;
            }
            100% {
                background-position: 0% 50%;
            }
        }
        .auth-container {
            max-width: 400px;
            margin: 0 auto;
            padding: 20px;
            background: rgba(255, 255, 255, 0.9);
            border-radius: 10px;
            backdrop-filter: blur(10px);
            box-shadow: 0 8px 32px 0 rgba(31, 38, 135, 0.37);
            border: 1px solid rgba(255, 255, 255, 0.18);
        }
        .auth-title {
            text-align: center;
            margin-bottom: 30px;
            padding: 10px;
            border-radius: 5px;
            color: #DD4737;
            font-weight: bold;
            text-shadow: 1px 1px 2px rgba(0, 0, 0, 0.1);
        }
        .stTextInput input {
            color: #000000;
            background: white;
            border-radius: 5px;
            border: 1px solid #DD4737;
            padding: 10px;
        }
        .stButton button {
            color: white;
            background: #DD4737;
            border-radius: 5px;
            padding: 10px 20px;
            font-weight: bold;
            transition: all 0.3s ease;
        }
        .stButton button:hover {
            background: #C13A2B;
            transform: translateY(-2px);
            box-shadow: 0 5px 15px rgba(221, 71, 55, 0.4);
        }
        </style>
    """, unsafe_allow_html=True)
    
    st.markdown('<div class="auth-container">', unsafe_allow_html=True)
    st.markdown('<h2 class="auth-title">Reset Password</h2>', unsafe_allow_html=True)
    
    with st.form("reset_form"):
        email = st.text_input("Email")
        submit = st.form_submit_button("Send Reset Link")
        
        if submit:
            if reset_password(email):
                st.success("Password reset link sent to your email!")
                st.session_state['show_reset'] = False
                st.session_state['show_login'] = True
                st.rerun()
    
    if st.button("Back to Login"):
        st.session_state['show_reset'] = False
        st.session_state['show_login'] = True
        st.rerun()
    
    st.markdown('</div>', unsafe_allow_html=True) 
import streamlit as st


def apply_custom_css(sidebar_state="open"):
    st.markdown(
        """
        <style>
        header[data-testid="stHeader"],
        [data-testid="stToolbar"],
        [data-testid="stDecoration"],
        #MainMenu,
        footer {
            display: none !important;
            visibility: hidden !important;
        }

        .stApp {
            background: linear-gradient(135deg, #F8FAFC 0%, #EEF2F7 100%);
            color: #111827;
        }

        * {
            color: #111827 !important;
            font-family: Inter, Segoe UI, Arial, sans-serif;
        }

        .block-container {
            padding-top: 1.4rem !important;
            padding-left: 0.6rem !important;
            padding-right: 1.6rem !important;
            max-width: 100% !important;
        }

        .page-header-title {
            font-size: 42px;
            font-weight: 950;
            color: #0F172A !important;
            margin-bottom: 0.5rem;
        }

        .page-header-subtitle {
            font-size: 15px;
            color: #475569 !important;
            margin-bottom: 2rem;
        }

        .live-card,
        .metric-card,
        .table-card,
        .system-card {
            background: #FFFFFF !important;
            border: 1px solid #E5E7EB !important;
            border-radius: 20px !important;
            box-shadow:
                0 8px 20px rgba(15,23,42,0.06),
                0 20px 40px rgba(15,23,42,0.08) !important;
        }

        div[data-testid="stVerticalBlockBorderWrapper"] {
            background: #FFFFFF !important;
            border: 1px solid #E5E7EB !important;
            border-radius: 20px !important;
            box-shadow:
                0 8px 20px rgba(15,23,42,0.06),
                0 20px 40px rgba(15,23,42,0.08) !important;
            padding: 14px !important;
            overflow: hidden !important;
        }

        .chart-card {
            background: #FFFFFF !important;
            border: 1px solid #E5E7EB !important;
            border-radius: 20px !important;
            box-shadow:
                0 8px 20px rgba(15,23,42,0.06),
                0 20px 40px rgba(15,23,42,0.08) !important;
            padding: 16px !important;
            margin-bottom: 20px !important;
            overflow: hidden !important;
        }

        .live-card {
            padding: 1rem 1.15rem;
            min-height: 70px;
        }

        .live-dot {
            display: inline-block;
            width: 14px;
            height: 14px;
            background: #22C55E;
            border-radius: 50%;
            box-shadow: 0 0 14px rgba(34,197,94,0.65);
            margin-right: 8px;
        }

        .live-text {
            color: #15803D !important;
            font-size: 16px;
            font-weight: 900;
        }

        .last-updated {
            font-size: 13px;
            color: #64748B !important;
            margin-top: 1rem;
            font-weight: 700;
        }

        .metric-card {
            padding: 1.25rem;
            min-height: 140px;
        }

        .metric-label {
            font-size: 14px;
            font-weight: 850;
            color: #334155 !important;
        }

        .metric-value {
            font-size: 31px;
            font-weight: 950;
            margin-top: 1.1rem;
            color: #0F172A !important;
        }

        .metric-change {
            color: #16A34A !important;
            font-size: 13px;
            margin-top: 1rem;
            font-weight: 900;
        }

        .table-card {
            padding: 1rem;
        }

        .system-card {
            padding: 18px;
        }

        .system-title {
            font-size: 15px;
            font-weight: 800;
            margin-bottom: 10px;
            color: #334155 !important;
        }

        .system-value {
            font-size: 30px;
            font-weight: 950;
            color: #15803D !important;
            margin-bottom: 18px;
        }

        .progress-bg {
            width: 100%;
            height: 10px;
            background: #E5E7EB;
            border-radius: 999px;
            overflow: hidden;
        }

        .progress-fill {
            height: 100%;
            background: linear-gradient(90deg, #22C55E, #16A34A);
            border-radius: 999px;
        }

        div[data-testid="stButton"] button {
            background: #FFFFFF !important;
            border: 1px solid #CBD5E1 !important;
            border-radius: 14px !important;
            color: #0F172A !important;
            font-weight: 800 !important;
            font-size: 14px !important;
            min-height: 44px !important;
            box-shadow: 0 6px 14px rgba(15,23,42,0.06);
        }

        div[data-testid="stButton"] button:hover {
            background: #F1F5F9 !important;
            border-color: #22C55E !important;
        }

        div[data-testid="stButton"] button[kind="primary"] {
            background: linear-gradient(135deg, #22C55E, #15803D) !important;
            border: 1px solid #15803D !important;
            color: #FFFFFF !important;
            box-shadow: 0 10px 24px rgba(34,197,94,0.25);
        }

        div[data-testid="stButton"] button[kind="primary"] * {
            color: #FFFFFF !important;
        }

        div[data-testid="stTextInput"] input {
            background: #FFFFFF !important;
            color: #0F172A !important;
            -webkit-text-fill-color: #0F172A !important;
            border: 1px solid #CBD5E1 !important;
            border-radius: 14px !important;
            font-size: 16px !important;
            font-weight: 700 !important;
        }

        div[data-testid="stTextInput"] input::placeholder {
            color: #94A3B8 !important;
            -webkit-text-fill-color: #94A3B8 !important;
        }

        div[data-testid="stDataFrame"] {
            border-radius: 14px;
            overflow: hidden;
            box-shadow: 0 10px 24px rgba(15,23,42,0.06);
        }

        .stAlert {
            background: #FFFFFF !important;
            border-radius: 16px !important;
            border: 1px solid #E5E7EB !important;
            box-shadow: 0 10px 24px rgba(15,23,42,0.06);
        }
        </style>
        """,
        unsafe_allow_html=True,
    )
# --- Imports ---
import streamlit as st
import pandas as pd
# from google.cloud import bigquery # Not needed if not running live queries
import time

# --- CONFIGURATION ---
GCP_PROJECT_ID = "my-gcp-project-468616"
# This app embeds Looker Studio dashboards which are connected to BigQuery datasets.
# The specific tables are noted within each page's code block.

# --- APP INTERFACE ---
st.set_page_config(page_title="Agent Analytics Hub", layout="wide", page_icon="🕵️")

# --- SIDEBAR ---
st.sidebar.title("🧭 Navigation")
page = st.sidebar.radio("Go to", [
    "🏠 Dashboard Overview",
    "📊 Social Media Analysis",
    "📋 Complaint Analysis",
    "📉 Trend Analysis", # Icon updated for consistency
    "ℹ️ About"
])

# --- MAIN CONTENT ---
st.markdown("<h1 style='text-align: center; color: #003366;'>Agent Analytics Hub 🕵️</h1>", unsafe_allow_html=True)
st.markdown(
    """
    <div style='text-align: center; color:  #e0e0e0; font-size: 18px;'>
    Welcome to the Agent Analytics Hub.<br>
    Analyze customer feedback, monitor social media sentiment, and review complaint trends using interactive dashboards.
    </div>
    """, unsafe_allow_html=True
)

st.divider()

# --- Animations and Effects ---
if "last_page" not in st.session_state:
    st.session_state.last_page = page

if page != st.session_state.last_page:
    st.toast(f"Switched to {page}", icon="🔄")
    st.session_state.last_page = page

if page == "🏠 Dashboard Overview":
    st.header("🏠 Dashboard Overview")
    st.info("Select a dashboard from the sidebar to view detailed analytics.")
    st.markdown(
        """
        - 📊 **Social Media Analysis:** Explore customer sentiment and trends across social platforms.
        - 📋 **Complaint Analysis:** Dive into complaint data and identify key areas for improvement.
        - 📉 **Performance Trend Analysis:** Analyze detailed product feedback and performance metrics from historical data.
        """
    )
    st.success("Your analytics journey starts here.")
    st.toast("Welcome to the Dashboard Overview.", icon="👋")
    st.progress(100, text="Dashboard loaded.")

elif page == "📊 Social Media Analysis":
    st.header("📊 Social Media Analysis")
    st.write("Get a complete overview of social media feedback and sentiment.")
    # Data source for this dashboard: `review_dataset.processed_product_reviews`
    progress_bar = st.progress(0, text="Loading Social Media Dashboard...")
    for percent_complete in range(0, 101, 10):
        time.sleep(0.03)
        progress_bar.progress(percent_complete, text=f"Loading Social Media Dashboard... {percent_complete}%")
    progress_bar.empty()
    with st.spinner("Finalizing dashboard..."):
        time.sleep(0.3)
        looker_studio_url_1 = "https://lookerstudio.google.com/embed/reporting/66dbd436-1ac5-46fa-9a67-b4384db6a2d6/page/JrlWF"
        st.components.v1.iframe(looker_studio_url_1, height=550, scrolling=True)
    st.info("💡 Tip: Use filters in the dashboard for deeper insights.")
    st.toast("Social Media Dashboard is ready.", icon="✅")

elif page == "📋 Complaint Analysis":
    st.header("📋 Complaint Analysis")
    st.write("Analyze customer complaints and track resolution performance.")
    # Data source for this dashboard: `review_dataset.processed_product_reviews` (or a similar table)
    progress_bar = st.progress(0, text="Loading Complaint Dashboard...")
    for percent_complete in range(0, 101, 10):
        time.sleep(0.03)
        progress_bar.progress(percent_complete, text=f"Loading Complaint Dashboard... {percent_complete}%")
    progress_bar.empty()
    with st.spinner("Finalizing dashboard..."):
        time.sleep(0.3)
        looker_studio_url_2 = "https://lookerstudio.google.com/embed/u/0/reporting/fb60b83c-ea69-4f1a-993c-f329fd21f366/page/tMxWF"
        st.components.v1.iframe(looker_studio_url_2, height=550, scrolling=True)
    st.warning("Review complaint trends to improve customer satisfaction.")
    st.toast("Complaint Dashboard is ready.", icon="✅")

# --- UPDATED BLOCK FOR THE NEW PAGE ---
elif page == "📉 Trend Analysis":
    st.header("📉 Trend Analysis")
    st.write("Drill down into specific product feedback and attribute performance.")

    # --- Data Source Note ---
    # This dashboard is powered by a different BigQuery table: `trend_analysis_dataset.historical_performance`
    # (Replace with your actual table name if different)

    progress_bar = st.progress(0, text="Loading Performance Trend Dashboard...")
    for percent_complete in range(0, 101, 10):
        time.sleep(0.03)
        progress_bar.progress(percent_complete, text=f"Loading Performance Trend Dashboard... {percent_complete}%")
    progress_bar.empty()
    with st.spinner("Finalizing dashboard..."):
        time.sleep(0.3)
        looker_studio_url_3 = "https://lookerstudio.google.com/embed/reporting/12e0f067-f32d-43f9-bf6d-e04e82ffaac8/page/p_c5tagt8dwd"

        # --- LOGIC CORRECTED: This will now display the dashboard directly ---
        st.components.v1.iframe(looker_studio_url_3, height=550, scrolling=True)

    st.success("Analyze product strengths and weaknesses to guide improvements.")
    st.toast("Performance Trend Dashboard is ready.", icon="✅")

elif page == "ℹ️ About":
    st.header("ℹ️ About This App")
    st.markdown(
        """
        **Agent Analytics Hub** is designed to help teams understand customer feedback and improve service quality.<br>
        - Built with Streamlit and Google BigQuery<br>
        - Integrates Looker Studio dashboards for rich visual analytics
        """, unsafe_allow_html=True
    )
    st.success("For questions or feedback, contact your analytics team.")
    st.toast("Thanks for checking out the About section.", icon="ℹ️")

st.divider()
st.caption("© 2025 Agent Analytics Hub | Powered by Streamlit & Google Cloud")

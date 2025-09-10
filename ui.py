import streamlit as st

# Page setup
st.set_page_config(page_title="FloatChat - Ocean Data Discovery", page_icon="🌊", layout="wide")
# Load CSS file
with open("style.css") as f:
    st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

st.markdown('<p class="title">Hello with External CSS</p>', unsafe_allow_html=True)
st.button("Styled Button")


# Load custom CSS
with open("ui.css") as f:
    st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

# Header
col1, col2 = st.columns([3, 2])
with col1:
    st.markdown('<div class="header"><h1>🌊 FloatChat - Ocean Data Discovery</h1></div>', unsafe_allow_html=True)
with col2:
    st.markdown('<div class="header" style="text-align:right; padding-top:1.2rem;">'
                '<a href="#dashboard">Dashboard</a>'
                '<a href="#catalog">Data Catalog</a>'
                '<a href="#help">Help</a>'
                '</div>', unsafe_allow_html=True)

# Tabs
tab1, tab2, tab3 = st.tabs(["Chat Interface", "Data Visualization", "Export Data"])

# --- Chat Interface ---
with tab1:
    col1, col2 = st.columns([1, 2])
    with col1:
        st.markdown("### 💬 Chat with OceanAI")
        st.container()  # Chat messages will appear here
        st.markdown("### Quick Queries")
        st.button("Show floats near Hawaii")
        st.button("Salinity trends last 6 months")
        st.button("Temperature at 200m depth")
        st.button("Compare BGC parameters")
        st.text_input("Ask about ocean data...", label_visibility="collapsed")
        st.button("Send")
    with col2:
        st.markdown("### 🌊 Data Visualization")
        st.markdown("#### ARGO Float Locations")
        st.empty()  # Placeholder for map
        col3, col4 = st.columns(2)
        with col3:
            st.markdown("#### Salinity Profile")
            st.empty()
        with col4:
            st.markdown("#### Temperature Over Time")
            st.empty()
        st.markdown("#### Depth Comparison")
        st.empty()

# --- Data Visualization ---
with tab2:
    st.markdown("## 📊 Advanced Data Visualization")
    col1, col2 = st.columns(2)
    with col1:
        st.markdown("### Map Visualization Options")
        st.selectbox("Select Map Overlay", ["Temperature", "Salinity", "Chlorophyll", "Oxygen"])
        st.date_input("Select Date Range")
        st.button("Update Map")
    with col2:
        st.markdown("### Data Filtering")
        st.slider("Depth Range (m)", 0, 2000, (0, 1000))
        st.multiselect("Ocean Basin", ["Pacific", "Atlantic", "Indian", "Southern", "Arctic"])
        st.button("Apply Filters")
    st.markdown("### Time Series Data")
    st.radio("Select Chart Type", ["Line Chart", "Area Chart"], horizontal=True)
    st.empty()  # Placeholder for chart

# --- Export Data ---
with tab3:
    st.markdown("## 📥 Data Export")
    col1, col2 = st.columns(2)
    with col1:
        st.markdown("### Export Options")
        st.selectbox("Select Export Format", ["CSV", "NetCDF", "JSON", "Excel"])
        st.selectbox("Select Data Range", ["All Data", "Current View", "Custom Selection"])
        st.checkbox("Include Metadata", value=True)
        st.button("Generate Export")
    with col2:
        st.markdown("### Download")
        st.info("Click the button below to download your data in the selected format.")
        st.empty()  # Placeholder for download button
    st.markdown("### Data Preview")
    st.empty()  # Placeholder for table

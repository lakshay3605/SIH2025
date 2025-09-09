import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
import plotly.graph_objects as go
from datetime import datetime, timedelta
import time
import random

# Set page configuration
st.set_page_config(
    page_title="FloatChat - Ocean Data Discovery",
    page_icon="🌊",
    layout="wide",
    initial_sidebar_state="expanded"
)


# Load CSS file
with open("style.css") as f:
    st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

st.markdown('<p class="title">Hello with External CSS</p>', unsafe_allow_html=True)
st.button("Styled Button")


# Initialize session state for chat messages
if "messages" not in st.session_state:
    st.session_state.messages = [
        {"role": "assistant", "content": "Hello! I'm your ocean data assistant. How can I help you explore ARGO data today?", "timestamp": "10:00 AM"}
    ]

# Initialize session state for map data
if "map_data" not in st.session_state:
    st.session_state.map_data = pd.DataFrame({
        'lat': [random.uniform(-60, 60) for _ in range(50)],
        'lon': [random.uniform(-180, 180) for _ in range(50)],
        'size': [random.randint(5, 15) for _ in range(50)],
        'color': [random.choice(['#ff9e00', '#48cae4', '#9d4edd', '#f72585', '#4cc9f0']) for _ in range(50)],
        'value': [random.uniform(0, 30) for _ in range(50)]
    })

# Header
col1, col2 = st.columns([3, 2]) 
with col1:
    st.markdown('<div class="header"><h1>🌊 FloatChat - Ocean Data Discovery</h1></div>', unsafe_allow_html=True)
with col2:
    st.markdown('<div class="header" style="text-align: right; padding-top: 1.2rem;">'
                '<a href="#dashboard" style="color: #90e0ef; text-decoration: none; margin: 0 10px;">Dashboard</a>'
                '<a href="#catalog" style="color: #90e0ef; text-decoration: none; margin: 0 10px;">Data Catalog</a>'
                '<a href="#help" style="color: #90e0ef; text-decoration: none; margin: 0 10px;">Help</a>'
                '</div>', unsafe_allow_html=True)

# Main content
tab1, tab2, tab3 = st.tabs(["Chat Interface", "Data Visualization", "Export Data"])

with tab1:
    col1, col2 = st.columns([1, 2])
    
    with col1:
        st.markdown("### 💬 Chat with OceanAI")
        
        # Display chat messages
        chat_container = st.container()
        with chat_container:
            for message in st.session_state.messages:
                div_class = "chat-message assistant" if message["role"] == "assistant" else "chat-message user"
                st.markdown(f'<div class="{div_class}"><p>{message["content"]}</p>'
                           f'<div class="timestamp">{message["timestamp"]}</div></div>', 
                           unsafe_allow_html=True)
        
        # Suggested queries
        st.markdown("### Quick Queries")
        suggested_queries = [
            "Show floats near Hawaii",
            "Salinity trends last 6 months",
            "Temperature at 200m depth",
            "Compare BGC parameters"
        ]
        
        for query in suggested_queries:
            if st.button(query, key=query):
                # Add user message to chat
                now = datetime.now().strftime("%H:%M")
                st.session_state.messages.append({"role": "user", "content": query, "timestamp": now})
                
                # Generate AI response
                with st.spinner("Processing..."):
                    time.sleep(1)  # Simulate processing time
                    responses = {
                        "Show floats near Hawaii": "I found 12 ARGO floats near Hawaii in the last month. Here are their trajectories and data profiles.",
                        "Salinity trends last 6 months": "Salinity has shown a slight decrease of 0.2 PSU in the Pacific Ocean over the last 6 months. Here's the trend analysis.",
                        "Temperature at 200m depth": "The average temperature at 200m depth is 15.3°C across all ARGO floats. Here's the spatial distribution.",
                        "Compare BGC parameters": "I've compared Bio-Geo-Chemical parameters across different ocean basins. The Indian Ocean shows higher chlorophyll concentrations."
                    }
                    ai_response = responses.get(query, "I'm processing your request. Here are the results visualized on the map and graphs.")
                    
                    now = datetime.now().strftime("%H:%M")
                    st.session_state.messages.append({"role": "assistant", "content": ai_response, "timestamp": now})
                
                # Rerun to update the chat
                st.rerun()
        
        # Chat input
        user_input = st.text_input("Ask about ocean data...", key="user_input", label_visibility="collapsed")
        if st.button("Send", key="send_button"):
            if user_input:
                # Add user message to chat
                now = datetime.now().strftime("%H:%M")
                st.session_state.messages.append({"role": "user", "content": user_input, "timestamp": now})
                
                # Generate AI response
                with st.spinner("Processing..."):
                    time.sleep(1.5)  # Simulate processing time
                    ai_response = f"I'm processing your request for '{user_input}'. Here are the results visualized on the map and graphs."
                    now = datetime.now().strftime("%H:%M")
                    st.session_state.messages.append({"role": "assistant", "content": ai_response, "timestamp": now})
                
                # Rerun to update the chat
                st.rerun()
    
    with col2:
        st.markdown("### 🌊 Data Visualization")
        
        # Map visualization
        st.markdown("#### ARGO Float Locations")
        st.map(st.session_state.map_data, size='size', color='color', use_container_width=True)
        
        # Graph visualizations
        col3, col4 = st.columns(2)
        
        with col3:
            st.markdown("#### Salinity Profile")
            # Generate sample data
            depth = np.arange(0, 1000, 10)
            salinity = 35 + 0.1 * np.sin(depth/50) + 0.05 * np.random.randn(len(depth))
            
            fig = go.Figure()
            fig.add_trace(go.Scatter(x=salinity, y=depth, mode='lines', name='Salinity', line=dict(color='#48cae4')))
            fig.update_layout(
                xaxis_title="Salinity (PSU)",
                yaxis_title="Depth (m)",
                yaxis=dict(autorange='reversed'),
                height=250,
                margin=dict(l=20, r=20, t=30, b=20),
                plot_bgcolor='rgba(0,0,0,0)',
                paper_bgcolor='rgba(0,0,0,0)',
                font=dict(color='#e0f7fa')
            )
            st.plotly_chart(fig, use_container_width=True)
        
        with col4:
            st.markdown("#### Temperature Over Time")
            # Generate sample data
            dates = pd.date_range(end=pd.Timestamp.today(), periods=30, freq='D')
            temperature = 20 + 5 * np.sin(np.arange(30)/5) + 0.5 * np.random.randn(30)
            
            fig = go.Figure()
            fig.add_trace(go.Scatter(x=dates, y=temperature, mode='lines+markers', name='Temperature', line=dict(color='#f72585')))
            fig.update_layout(
                xaxis_title="Date",
                yaxis_title="Temperature (°C)",
                height=250,
                margin=dict(l=20, r=20, t=30, b=20),
                plot_bgcolor='rgba(0,0,0,0)',
                paper_bgcolor='rgba(0,0,0,0)',
                font=dict(color='#e0f7fa')
            )
            st.plotly_chart(fig, use_container_width=True)
        
        # Additional graph
        st.markdown("#### Depth Comparison")
        # Generate sample data
        oceans = ['Pacific', 'Atlantic', 'Indian', 'Southern', 'Arctic']
        avg_temp = [18.5, 16.2, 22.1, 3.4, -1.2]
        
        fig = go.Figure()
        fig.add_trace(go.Bar(x=oceans, y=avg_temp, marker_color=['#ff9e00', '#48cae4', '#9d4edd', '#f72585', '#4cc9f0']))
        fig.update_layout(
            xaxis_title="Ocean",
            yaxis_title="Average Temperature (°C)",
            height=250,
            margin=dict(l=20, r=20, t=30, b=20),
            plot_bgcolor='rgba(0,0,0,0)',
            paper_bgcolor='rgba(0,0,0,0)',
            font=dict(color='#e0f7fa')
        )
        st.plotly_chart(fig, use_container_width=True)

with tab2:
    st.markdown("## 📊 Advanced Data Visualization")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("### Map Visualization Options")
        map_type = st.selectbox("Select Map Overlay", ["Temperature", "Salinity", "Chlorophyll", "Oxygen"])
        date_range = st.date_input("Select Date Range", 
                                  value=(datetime.now() - timedelta(days=30), datetime.now()),
                                  max_value=datetime.now())
        
        if st.button("Update Map"):
            st.success("Map updated with selected parameters!")
    
    with col2:
        st.markdown("### Data Filtering")
        depth_range = st.slider("Depth Range (m)", 0, 2000, (0, 1000))
        ocean_basin = st.multiselect("Ocean Basin", 
                                    ["Pacific", "Atlantic", "Indian", "Southern", "Arctic"],
                                    default=["Pacific", "Atlantic", "Indian"])
        
        if st.button("Apply Filters"):
            st.success("Filters applied to all visualizations!")
    
    # Generate some sample time series data
    time_series_data = pd.DataFrame({
        'date': pd.date_range(end=pd.Timestamp.today(), periods=90, freq='D'),
        'temperature': 20 + 5 * np.sin(np.arange(90)/10) + 0.8 * np.random.randn(90),
        'salinity': 35 + 0.5 * np.sin(np.arange(90)/15) + 0.2 * np.random.randn(90)
    })
    
    st.markdown("### Time Series Data")
    chart_type = st.radio("Select Chart Type", ["Line Chart", "Area Chart"], horizontal=True)
    
    if chart_type == "Line Chart":
        fig = px.line(time_series_data, x='date', y=['temperature', 'salinity'],
                     labels={'value': 'Measurement', 'variable': 'Parameter'},
                     color_discrete_map={'temperature': '#f72585', 'salinity': '#48cae4'})
    else:
        fig = px.area(time_series_data, x='date', y=['temperature', 'salinity'],
                     labels={'value': 'Measurement', 'variable': 'Parameter'},
                     color_discrete_map={'temperature': '#f72585', 'salinity': '#48cae4'})
    
    fig.update_layout(
        height=400,
        plot_bgcolor='rgba(0,0,0,0)',
        paper_bgcolor='rgba(0,0,0,0)',
        font=dict(color='#e0f7fa'),
        legend=dict(orientation="h", yanchor="bottom", y=1.02, xanchor="right", x=1)
    )
    st.plotly_chart(fig, use_container_width=True)

with tab3:
    st.markdown("## 📥 Data Export")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("### Export Options")
        export_format = st.selectbox("Select Export Format", ["CSV", "NetCDF", "JSON", "Excel"])
        data_range = st.selectbox("Select Data Range", ["All Data", "Current View", "Custom Selection"])
        
        if data_range == "Custom Selection":
            custom_dates = st.date_input("Select Custom Date Range", 
                                        value=(datetime.now() - timedelta(days=30), datetime.now()),
                                        max_value=datetime.now())
        
        include_metadata = st.checkbox("Include Metadata", value=True)
        
        if st.button("Generate Export"):
            with st.spinner("Preparing your data for export..."):
                time.sleep(2)
                st.success("Your data is ready for download!")
    
    with col2:
        st.markdown("### Download")
        st.info("Click the button below to download your data in the selected format.")
        
        # Create sample data for download
        sample_data = pd.DataFrame({
            'date': pd.date_range(end=pd.Timestamp.today(), periods=10, freq='D'),
            'latitude': [random.uniform(-60, 60) for _ in range(10)],
            'longitude': [random.uniform(-180, 180) for _ in range(10)],
            'temperature': [random.uniform(0, 30) for _ in range(10)],
            'salinity': [random.uniform(33, 37) for _ in range(10)],
            'depth': [random.uniform(0, 2000) for _ in range(10)]
        })
        
        if export_format == "CSV":
            csv = sample_data.to_csv(index=False)
            st.download_button(
                label="Download CSV",
                data=csv,
                file_name="argo_data.csv",
                mime="text/csv"
            )
        elif export_format == "Excel":
            # For Excel format, we need to use a different approach
            st.warning("Excel export requires additional setup. Please use CSV format for now.")
        else:
            st.warning(f"{export_format} export requires additional setup. Please use CSV format for now.")
    
    st.markdown("### Data Preview")
    st.dataframe(sample_data, use_container_width=True)



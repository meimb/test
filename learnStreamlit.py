import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

def main():
    st.title("Interactive Streamlit Commands Tutorial")
    st.write("Select a command category and specific command to learn how to use it!")

    # Dictionary of command categories and their commands
    commands = {
        "Layout & Organization": {
            "st.title": {
                "code": 'st.title("My App")',
                "description": "Creates a main title for your app.",
                "demo": lambda: st.title("Example Title")
            },
            "st.header": {
                "code": 'st.header("Section")',
                "description": "Creates a section header.",
                "demo": lambda: st.header("Example Header")
            },
            "st.columns": {
                "code": """
col1, col2 = st.columns(2)
with col1:
    st.write("Column 1")
with col2:
    st.write("Column 2")""",
                "description": "Creates multiple columns for layout.",
                "demo": lambda: create_columns_demo()
            }
        },
        "Input Widgets": {
            "st.button": {
                "code": 'st.button("Click Me")',
                "description": "Creates a clickable button.",
                "demo": lambda: create_button_demo()
            },
            "st.text_input": {
                "code": 'st.text_input("Enter text", "Default value")',
                "description": "Creates a text input field.",
                "demo": lambda: create_text_input_demo()
            },
            "st.slider": {
                "code": 'st.slider("Select value", 0, 100, 50)',
                "description": "Creates a slider for numerical input.",
                "demo": lambda: create_slider_demo()
            }
        },
        "Display Data": {
            "st.dataframe": {
                "code": """
data = pd.DataFrame({
    'Column 1': [1, 2, 3],
    'Column 2': ['A', 'B', 'C']
})
st.dataframe(data)""",
                "description": "Displays a pandas DataFrame.",
                "demo": lambda: create_dataframe_demo()
            },
            "st.metric": {
                "code": 'st.metric(label="Revenue", value="$500", delta="$20")',
                "description": "Displays a metric with an optional delta value.",
                "demo": lambda: st.metric(label="Revenue", value="$500", delta="$20")
            }
        },
        "Media & Visualization": {
            "st.pyplot": {
                "code": """
fig, ax = plt.subplots()
ax.plot([1, 2, 3], [1, 4, 9])
st.pyplot(fig)""",
                "description": "Displays a matplotlib figure.",
                "demo": lambda: create_pyplot_demo()
            }
        }
    }

    # Sidebar for navigation
    st.sidebar.header("Navigation")
    category = st.sidebar.selectbox("Select Category", list(commands.keys()))
    command = st.sidebar.selectbox("Select Command", list(commands[category].keys()))

    # Main content area
    st.header(f"Learning {command}")
    
    # Create tabs for different aspects
    tab1, tab2, tab3 = st.tabs(["Description", "Code", "Demo"])
    
    with tab1:
        st.write(commands[category][command]["description"])
    
    with tab2:
        st.code(commands[category][command]["code"], language="python")
    
    with tab3:
        st.write("Live Demo:")
        commands[category][command]["demo"]()

def create_columns_demo():
    col1, col2 = st.columns(2)
    with col1:
        st.write("This is column 1")
        st.button("Column 1 Button")
    with col2:
        st.write("This is column 2")
        st.button("Column 2 Button")

def create_button_demo():
    if st.button("Click Me!"):
        st.write("Button was clicked!")
    else:
        st.write("Button is waiting to be clicked!")

def create_text_input_demo():
    text = st.text_input("Enter your name", "John Doe")
    st.write(f"Hello, {text}!")

def create_slider_demo():
    value = st.slider("Select a value", 0, 100, 50)
    st.write(f"Selected value: {value}")

def create_dataframe_demo():
    df = pd.DataFrame({
        'Column 1': [1, 2, 3],
        'Column 2': ['A', 'B', 'C']
    })
    st.dataframe(df)

def create_pyplot_demo():
    fig, ax = plt.subplots()
    x = np.linspace(0, 10, 100)
    ax.plot(x, np.sin(x))
    ax.set_title("Simple Sine Wave")
    st.pyplot(fig)

if __name__ == "__main__":
    main()

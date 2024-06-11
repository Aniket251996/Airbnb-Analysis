import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import plotly.express as px

# Load the dataset
df = pd.read_csv(r"C:\Users\ronit\python\airbnb_project\airbnb_data_2.csv")

# Set the title for your Streamlit app
st.title('AirBnb Data Analysis')

# Display the dataset
# st.write(df)

def Property_price():
    fig = px.scatter_mapbox(df, lat="latitude", lon="longitude", hover_name="Property_Name", hover_data=["Price", "Country"],
                        color_discrete_sequence=["blue"], zoom=2, height=700)
    fig.update_layout(mapbox_style="open-street-map")
    fig.update_layout(title="Airbnb Listings Map")
    st.plotly_chart(fig)
    return
if st.sidebar.button('Property Price'):
    Property_price()


option = ('Room Type', 'Property Type', 'Country')

def Price_variation(option):
    if option == 'Room Type':
        df2 = df.groupby('Room_type')['Price'].mean().reset_index()
        plt.figure(figsize=(10,6))
        sns.barplot(data=df2, x='Room_type', y='Price')
        plt.xticks(rotation=90)
        plt.xlabel('Room Type')
        plt.ylabel('Mean Price')
        plt.title('Mean Price by Room Type')
        st.pyplot(plt.gcf())
    
    elif option =='Property Type':
        # Grouping data to calculate mean price for each property type
        df2 = df.groupby('Property_type')['Price'].mean().reset_index()
        # Plotting
        plt.figure(figsize=(10, 6))
        sns.barplot(data=df2, x='Property_type', y='Price')
        plt.xticks(rotation=90)
        plt.ylim(0, 3200)  # Set y-axis limit
        plt.xlabel('Property Type')
        plt.ylabel('Mean Price')
        plt.title('Mean Price by Property Type')
        st.pyplot(plt.gcf())
    
    elif option =='Country':
        #Avg Listing Price in each Countries
        # Group by 'Country' and calculate the mean price
        df1 = df.groupby('Country')['Price'].mean().reset_index()
        # Create choropleth map
        fig = px.choropleth(df1, locations='Country', locationmode='country names', color='Price',
                            color_continuous_scale='Viridis', range_color=(df1['Price'].min(), df1['Price'].max()),
                            labels={'Price': 'Average Price'}, title='Avg Listing Price in each Countries')
        fig.update_layout(height=800, width=800)
        st.plotly_chart(fig)  # Use st.plotly_chart to display Plotly figures

    return

st.sidebar.header('Variation of Price based on:')
selected_option = st.sidebar.selectbox('Select the option below:', option, index=None)

# Streamlit Run button
if st.sidebar.button('Click Here to know the price variation'):
    Price_variation(selected_option)


# To see basic charts and Insight
st.sidebar.header("Basic Charts and its distribution")
option1 = ("Property Type", "Room Type", "Bed Type","Price",'Reviews') 

def Basic_chart(option1):
    if option1 == 'Property Type':
        # Create a histogram of the 'Property_type' variable
        plt.figure(figsize=(8, 6))
        sns.histplot(data=df, x='Property_type')
        plt.xticks(rotation=90)  # Rotate x-axis labels for better readability
        plt.xlabel('Property Type')  # Add x-axis label
        plt.ylabel('Frequency')  # Add y-axis label
        plt.title('Distribution of Property Types')  # Add title
        st.pyplot(plt.gcf())

    elif option1 == 'Room Type':
        # Create a histogram of the 'Room_type' variable
        plt.figure(figsize=(8, 6))
        sns.histplot(data=df, x='Room_type')
        plt.xticks(rotation=90)  # Rotate x-axis labels for better readability
        plt.xlabel('Room Type')  # Add x-axis label
        plt.ylabel('Frequency')  # Add y-axis label
        plt.title('Distribution of Room Types')  # Add title
        st.pyplot(plt.gcf())
    
    elif option1 == 'Bed Type':
        # Create a histogram of the 'Bed_type' variable with adjusted figure size and binning
        plt.figure(figsize=(10, 6))
        sns.histplot(data=df, x='Bed_type', binwidth=0.5,kde_kws={"shade": True})  # Adjust binwidth as needed
        plt.xticks(rotation=90)  # Rotate x-axis labels for better readability
        plt.xlabel('Bed Type')  # Add x-axis label
        plt.ylabel('Frequency')  # Add y-axis label
        plt.title('Distribution of Bed Types')
        plt.ylim(0,None)  
        st.pyplot(plt.gcf())

    elif option1 == 'Reviews':
        sns.boxplot(data= df, y='Reviews_count')
        plt.title('Box plot for Review')
        st.pyplot(plt.gcf())
        
        sns.histplot(data= df['Reviews_count'],kde=True)
        plt.xlim(0,150)
        plt.title('Review density chart')
        st.pyplot(plt.gcf())

    elif option1 =='Price':
        sns.boxplot(data=df,y='Price')
        plt.title('Box plot for price')
        st.pyplot(plt.gcf())


    return

selected_option1 = st.sidebar.selectbox('Select the option', option1, index=None)
if st.sidebar.button('Click here to see the chart'):
    Basic_chart(selected_option1)




import streamlit as st
import pandas as pd
import os

st.title("🗂️ User Data Records")
st.write("Below is the list of users who submitted diabetes predictions.")

filePath = "user_data.csv"

# Check if the file exists
if os.path.exists(filePath):
    # Load the data from CSV
    df = pd.read_csv(filePath)

    # Ensure 'Name' and 'Contact' columns are treated as strings
    df['Name'] = df['Name'].astype(str)
    df['Contact'] = df['Contact'].astype(str)

    # Search functionality
    search_term = st.text_input("Search by Name or Contact")

    if search_term:
        df = df[df['Name'].str.contains(search_term, case=False) | df['Contact'].str.contains(search_term, case=False)]

    # Display the filtered dataframe
    st.dataframe(df)
    st.success(f"Total Records: {len(df)}")

    if not df.empty:
        # Add button to clear all data except header
        if st.button("🗑️ Delete All Records (Keep Header)"):
            # Get the column names
            columns = df.columns.tolist()
            # Create empty DataFrame with the same headers
            df_empty = pd.DataFrame(columns=columns)
            df_empty.to_csv(filePath, index=False)
            st.success("✅ All records deleted. Only header remains.")
            st.rerun()  # Refresh the page

        # Add a download button for CSV file
        csv = df.to_csv(index=False)
        st.download_button(
            label="Download CSV",
            data=csv,
            file_name="user_data.csv",
            mime="text/csv"
        )

    else:
        st.warning("No user data available yet. Please submit predictions first.")
else:
    st.warning("No user data available yet. Please submit predictions first.")

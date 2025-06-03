import pandas as pd
import folium
from folium import plugins

# --- Configuration ---
CSV_FILE_PATH = 'data.csv'  # Make sure this path is correct
LATITUDE_COLUMN = 'latitude'
LONGITUDE_COLUMN = 'longitude'
SCALAR_VALUE_COLUMN = 'scalar_value' # Name of the column with your scalar variable

# --- Load data from CSV ---
try:
    df = pd.read_csv(CSV_FILE_PATH)
except FileNotFoundError:
    print(f"Error: The file '{CSV_FILE_PATH}' was not found.")
    print("Please make sure the CSV file is in the same directory as your script, or provide the full path.")
    exit()

# Check if essential columns exist
if not all(col in df.columns for col in [LATITUDE_COLUMN, LONGITUDE_COLUMN, SCALAR_VALUE_COLUMN]):
    print(f"Error: CSV file must contain '{LATITUDE_COLUMN}', '{LONGITUDE_COLUMN}', and '{SCALAR_VALUE_COLUMN}' columns.")
    exit()

# Extract data in the format [latitude, longitude, scalar_value] for the heatmap
# Ensure the columns are converted to appropriate numeric types if they aren't already
heat_data = df[[LATITUDE_COLUMN, LONGITUDE_COLUMN, SCALAR_VALUE_COLUMN]].values.tolist()

# --- Create the map ---
# Create a map centered around the approximate center of the UK

#uk_center_lat = 54.0
#uk_center_lon = -2.0

# 50.3755° N, 4.1427° W
uk_center_lat = 50.0
uk_center_lon = -2
#m = folium.Map(location=[uk_center_lat, uk_center_lon], zoom_start=6)
m = folium.Map(location=[uk_center_lat, uk_center_lon], zoom_start=8)

# Add the heatmap layer
plugins.HeatMap(heat_data).add_to(m)

# Optional: Add markers for individual points if you want to see them along with the heatmap
# for index, row in df.iterrows():
#     folium.Marker(
#         location=[row[LATITUDE_COLUMN], row[LONGITUDE_COLUMN]],
#         popup=f"{row['city']}: {row[SCALAR_VALUE_COLUMN]}", # Assuming a 'city' column exists
#         tooltip=f"{row['city']}"
#     ).add_to(m)

# --- Display or save the map ---
# To save the map as an HTML file
m.save("uk_heatmap_from_csv.html")

# To display the map directly in a Jupyter Notebook or similar environment
m

Route Animation & CO₂ Data Visualization – Mexico City
Developed for BE-IN-G as part of a logistics optimization initiative (Summer 2024)

Overview
This project visualizes animated walking routes and vehicle-based CO₂ emissions across Mexico City. 
Combining GPS data, environmental sensors, and interactive mapping tools provides dynamic and data-rich visuals for eco-optimized logistics planning.

Key Features
🚶 Route Animation with Google Maps Polyline
Uses the Google Maps API Polyline function to draw animated routes from origin to destination.
Places marker pins along each coordinate in the route.
Captures a screenshot at each step, simulating real-time movement.
All screenshots are compiled into a GIF animation showing the full route traversal.
A loading/progress bar tracks the route rendering process for user feedback.

🌫️ CO₂ Data Visualization
Integrates CO₂ sensor data collected from logistics vehicles.
Overlay emission intensity on the map to highlight environmental impact per route.
Helps identify cleaner, low-emission paths through data-driven visualization.

🧠 Image Processing & Environmental Mapping
Applies custom filtering and coordinate mapping to enhance accuracy of CO₂ overlays.
Uses image manipulation tools to generate high-resolution environmental maps.

📈 Logistics Integration
Final visualizations were presented to stakeholders and used in internal strategy sessions.
Informed route planning with an emphasis on sustainability and efficiency.

Technologies Used
- Google Maps JavaScript API (Polyline, Markers, Map rendering)
- Python (automation, data handling)
- Selenium / Pyppeteer (for capturing screenshots)
- OpenCV / PIL (GIF generation and image processing)
- Pandas, NumPy (data transformation)
- tqdm (progress/loading bar)
- Matplotlib / Plotly (CO₂ data visualization)

Outcome
The project helped BE-IN-G:
- Understand the relationship between routing and emissions.
- Improve last-mile delivery logistics with environmental considerations.
- Communicate data insights effectively through animated and interactive visuals.

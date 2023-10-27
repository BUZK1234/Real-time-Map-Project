# Real-time Map Project

This is a real-time map project that reads data from a CSV file and displays it on an interactive map using Flask and Leaflet.

## Getting Started

### Prerequisites

Before you begin, make sure you have the following installed:

- Python 3.x
- Pip (Python package manager)

### Installation

1. Clone this repository to your local machine:

   ```bash
   git clone https://github.com/yourusername/real-time-map.git
Change into the project's directory:

bash
Copy code
cd real-time-map
Create a virtual environment to isolate project dependencies (optional but recommended):

bash
Copy code
python -m venv venv
Activate the virtual environment:

On Windows (PowerShell):

bash
Copy code
.\venv\Scripts\Activate
On macOS and Linux:

bash
Copy code
source venv/bin/activate
Install project dependencies:

bash
Copy code
pip install -r requirements.txt
Start the Flask application:

bash
Copy code
python app.py
Usage
This project reads data from a CSV file containing latitude and longitude coordinates and displays them on a map in real-time. The data is updated every 5 seconds.

To view the map, open a web browser and navigate to http://localhost:8080.

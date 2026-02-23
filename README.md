# Shortest Path Finder with Graph GUI

This is a Python-based GUI application implemented for a 2020 university course project. It visualizes map nodes and paths using PyQt5 and PyQtGraph.

<img width="926" height="460" alt="Application Overview" src="https://github.com/user-attachments/assets/cc987299-1c44-4fa2-9f8a-58124b7dd1b8" />

## Prerequisites

Ensure you have Python 3 installed. You will need the following dependencies:

*   `PyQt5` (For the GUI widgets and layout)
*   `pyqtgraph` (For drawing the map and nodes)

### Installation

1.  Clone this repository to your local machine.
2.  Open your terminal and navigate to the project directory.
3.  Install the required packages using pip:

```bash
pip install PyQt5 pyqtgraph
```

## Running the Application

To launch the GUI, ensure you are in the project folder and run:

```bash
python Driver.py
```

*(Note: You can also open the project in your preferred IDE, such as Spyder or PyCharm, and run `Driver.py` directly).*

## Features & Usage

### 1. Adding Nodes
Once the application starts, you can add nodes to the graph using the **"Add Node"** button. The graph will progressively appear as nodes are linked.

<img width="469" height="259" alt="Adding Nodes 1" src="https://github.com/user-attachments/assets/fc978a3f-0a65-4bb3-8adc-63bc4a591b07" />
<img width="300" height="166" alt="Adding Nodes 2" src="https://github.com/user-attachments/assets/52083300-457a-4531-9672-3927c76a3a3f" />

### 2. Finding the Shortest Path
After mapping your nodes, press the **"RUN"** button. 

*   By default, the source computation always begins at node `0`. 
*   *Limitation:* A specific destination node feature is currently not implemented; the algorithm calculates the paths to all available nodes from the source.

The application calculates two main sets of results:
1.  **Destinations:** The shortest distance calculated for each node from the source.
2.  **Path:** The specific sequence of visited nodes (addresses) required to reach them.

As seen below, the graphical output and console confirm that the results work properly (though visual positioning of the nodes on screen could not be fully arranged due to time constraints).

---
*PS: This project was primarily developed on macOS via PyCharm. Doxygen generation had some issues, leading to this repository documentation format.*

### Result Showcases:

<img width="293" height="390" alt="Results List" src="https://github.com/user-attachments/assets/e62e7191-ca1e-4226-8659-d82517b4ce44" />
<img width="945" height="940" alt="Map View 1" src="https://github.com/user-attachments/assets/17b44356-c668-4805-b74e-273e4ebe4a29" />
<img width="945" height="1064" alt="Map View 2" src="https://github.com/user-attachments/assets/4617ae80-33da-4637-b2f3-4eb60c41f60e" />
<img width="945" height="1058" alt="Map View 3" src="https://github.com/user-attachments/assets/8301f17a-7c60-437d-a883-e03d00dedde2" />
<img width="945" height="1058" alt="Map View 4" src="https://github.com/user-attachments/assets/1ffdef05-28e6-40ca-a240-06448aa182e2" />
<img width="945" height="677" alt="Map View 5" src="https://github.com/user-attachments/assets/48c8bc40-7e32-4e10-8f4b-e2b219b00abc" />
<img width="945" height="677" alt="Map View 6" src="https://github.com/user-attachments/assets/69f341a5-e023-4d22-957b-2613bac8913e" />

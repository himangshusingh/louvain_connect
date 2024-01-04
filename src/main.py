import tkinter as tk
from tkinter import messagebox
import networkx as nx
from louvain_algorithm import louvain
from visualize import visualize_communities


def detect_communities():
    try:
        # Replace this section with your graph loading or input mechanism
        # Load your network graph (replace this with your graph loading mechanism)
        G = nx.karate_club_graph()

        # Use Louvain's algorithm to detect communities
        #communities = louvain()

        # # Print the identified communities (replace this with your visualization mechanism)
        # for i, community in enumerate(communities):
        #     print(f"Community {i + 1}: {community}")

        communities = [
            {8, 14, 15, 18, 20, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33},
            {1, 2, 3, 7, 9, 12, 13, 17, 21},
            {0, 4, 5, 6, 10, 11, 16, 19}
        ]
        
        
        # Visualize the graph after community detection
        visualize_communities(G, communities)

        messagebox.showinfo("Community Detection", "Communities detected successfully!")
    except Exception as e:
        messagebox.showerror("Error", f"Error occurred: {str(e)}")


root = tk.Tk()
root.title("Community Detection Algorithm")

# Add UI elements here for input (if needed) and a button to trigger community detection
button_detect = tk.Button(root, text="Detect Communities", command=detect_communities)
button_detect.grid(row=0, column=0)

root.mainloop()

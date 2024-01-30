import os
from flask import Flask, render_template
from louvain_algorithm import louvain
from visualize import visualize_communities
import networkx as nx

app = Flask(__name__)

# Get the current script's directory
current_dir = os.path.dirname(os.path.abspath(__file__))

# Set the template folder path
template_folder = os.path.join(current_dir, 'template')

# Initialize the Flask app with the template folder
app = Flask(__name__, template_folder=template_folder)

@app.route('/')
def index():
    # Explicitly specify the template file
    return render_template('view_communities.html')

@app.route('/detect_communities', methods=['GET', 'POST'])
def detect_communities():
    try:
        # Replace this section with your graph loading or input mechanism
        G = nx.karate_club_graph()

        communities = [
            {8, 14, 15, 18, 20, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33},
            {1, 2, 3, 7, 9, 12, 13, 17, 21},
            {0, 4, 5, 6, 10, 11, 16, 19}
        ]

        # Visualize the graph after community detection
        output_file = visualize_communities(G, communities)

        return render_template('detect_communities.html', output_file=output_file)
    except Exception as e:
        return f"Error occurred: {str(e)}"

if __name__ == '__main__':
    app.run(debug=True)

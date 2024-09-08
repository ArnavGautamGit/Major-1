import subprocess
import re
import networkx as nx
import matplotlib.pyplot as plt

# Step 1: Run traceroute and get the output
def run_traceroute(target):
    try:
        traceroute_command = ['traceroute', target]
        result = subprocess.run(traceroute_command, capture_output=True, text=True)
        return result.stdout
    except Exception as e:
        print(f"An error occurred while running traceroute: {e}")
        return None

# Step 2: Extract IP addresses from the traceroute output
def extract_ips(traceroute_output):
    if traceroute_output:
        # Regular expression to match IP addresses in the traceroute output
        ip_regex = r'\((\d{1,3}(?:\.\d{1,3}){3})\)'
        return re.findall(ip_regex, traceroute_output)
    return []

# Step 3: Plot the network diagram using networkx and matplotlib
def plot_network(ips):
    G = nx.Graph()

    # Add nodes (IP addresses)
    for ip in ips:
        G.add_node(ip)

    # Connect each node with the next to simulate the path
    for i in range(len(ips) - 1):
        G.add_edge(ips[i], ips[i + 1])

    # Draw the network graph
    plt.figure(figsize=(10, 6))
    nx.draw(G, with_labels=True, node_color='lightblue', font_weight='bold')
    plt.title("Network Diagram")
    plt.show()

# Main function to run the tool
if __name__ == "__main__":
    target = input("Enter the target domain or IP address (e.g., google.com): ")
    
    # Step 1: Run TraceRoute
    print(f"Running traceroute for {target}...")
    traceroute_output = run_traceroute(target)
    
    # Step 2: Extract IP addresses
    ips = extract_ips(traceroute_output)
    
    if ips:
        print("Found the following IP addresses:")
        print(ips)
        
        # Step 3: Plot the network diagram
        print("Plotting the network diagram...")
        plot_network(ips)
    else:
        print("No IP addresses were found. Please check the target or traceroute output.")

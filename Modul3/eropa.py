import matplotlib.pyplot as plt
import networkx as nx


def main():
    G = nx.Graph()

    edges = [
        ("Oradea", "Zerind", 71), ("Oradea", "Sibiu", 151),
        ("Zerind", "Arad", 75), ("Arad", "Sibiu", 140),
        ("Arad", "Timisoara", 118), ("Timisoara", "Lugoj", 111),
        ("Lugoj", "Mehadia", 70), ("Mehadia", "Drobeta", 75),
        ("Drobeta", "Craiova", 120), ("Craiova", "Rimnicu Vilcea", 146),
        ("Craiova", "Pitesti", 138), ("Rimnicu Vilcea", "Sibiu", 80),
        ("Rimnicu Vilcea", "Pitesti", 97), ("Sibiu", "Fagaras", 99),
        ("Fagaras", "Bucharest", 211), ("Pitesti", "Bucharest", 101),
        ("Bucharest", "Giurgiu", 90), ("Bucharest", "Urziceni", 85),
        ("Urziceni", "Hirsova", 98), ("Urziceni", "Vaslui", 142),
        ("Hirsova", "Eforie", 86), ("Vaslui", "Iasi", 92),
        ("Iasi", "Neamt", 87)
    ]
    G.add_weighted_edges_from(edges)

    all_shortest_paths = dict(nx.shortest_path(G, weight='weight'))

    print("=== Semua Pasangan Shortest Path (Eropa) ===")
    for source, paths in all_shortest_paths.items():
        for target, path in paths.items():
            if source != target:
                print(f"{source} -> {target}: {path}")

    pos = {
        "Oradea": (1, 8), "Zerind": (0.5, 6.5), "Arad": (0, 5),
        "Timisoara": (0.2, 3), "Lugoj": (1.5, 2.2), "Mehadia": (1.6, 1.2),
        "Drobeta": (1.5, 0), "Craiova": (3.5, 0), "Rimnicu Vilcea": (3.2, 4),
        "Sibiu": (2.8, 5.5), "Fagaras": (4.5, 5.5), "Pitesti": (4.5, 3),
        "Bucharest": (6.5, 1.5), "Giurgiu": (6, 0), "Urziceni": (8, 2.5),
        "Hirsova": (9.5, 2.5), "Eforie": (10, 0.5), "Vaslui": (9, 5.5),
        "Iasi": (8, 7), "Neamt": (6.5, 8)
    }

    plt.figure(figsize=(12, 8))
    nx.draw(G, pos, with_labels=True, node_color='lightgray', node_shape='s', node_size=800, font_weight='bold',
            font_size=9)
    edge_labels = nx.get_edge_attributes(G, 'weight')
    nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels)
    plt.title("Graf Peta Eropa (Romania)")
    plt.show()


if __name__ == "__main__":
    main()

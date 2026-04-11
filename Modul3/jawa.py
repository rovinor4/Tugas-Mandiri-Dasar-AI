import matplotlib.pyplot as plt
import networkx as nx


def main():
    G = nx.Graph()

    edges = [
        ("Jakarta", "Bandung", 270), ("Jakarta", "Cirebon", 327),
        ("Bandung", "Cirebon", 120), ("Bandung", "Yogyakarta", 373),
        ("Cirebon", "Semarang", 305), ("Cirebon", "Yogyakarta", 210),
        ("Semarang", "Yogyakarta", 109), ("Semarang", "Surakarta", 97),
        ("Semarang", "Surabaya", 369), ("Yogyakarta", "Surakarta", 60),
        ("Surakarta", "Malang", 370), ("Surabaya", "Malang", 94)
    ]
    G.add_weighted_edges_from(edges)

    all_shortest_paths = dict(nx.shortest_path(G, weight='weight'))

    print("=== Semua Pasangan Shortest Path (Jawa) ===")
    for source, paths in all_shortest_paths.items():
        for target, path in paths.items():
            if source != target:
                print(f"{source} -> {target}: {path}")

    pos = {
        "Jakarta": (0, 4), "Bandung": (2, 1.5), "Cirebon": (3.5, 3.5),
        "Semarang": (7, 3), "Yogyakarta": (6.5, 1), "Surakarta": (8, 1.5),
        "Surabaya": (11, 3), "Malang": (10.5, 1)
    }

    plt.figure(figsize=(10, 5))
    nx.draw(G, pos, with_labels=True, node_color='white', edgecolors='black', node_size=1000, font_weight='bold',
            font_size=9)
    edge_labels = nx.get_edge_attributes(G, 'weight')
    nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels)
    plt.title("Graf Peta Pulau Jawa")
    plt.show()


if __name__ == "__main__":
    main()

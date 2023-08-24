public class Edge {
    int value;
    Node source;
    Node target;

    public Edge(int value, Node a, Node b) {
        this.value = value;
        this.source = a;
        this.target = b;
    }
}

import java.util.ArrayList;
import java.util.List;
import java.util.Stack;

public class Graph {
    List<Node> nodes;
    Node root;

    public Graph() {
        this.nodes = new ArrayList<Node>(); 

        Node a = new Node("A");
        Node b = new Node("B");
        Edge ab = new Edge(2, a, b);

        this.nodes.add(a);
        this.nodes.add(b);

        this.root = a;
        Node c = new Node("C");
        Edge ca = new Edge(3, c, a);
        this.nodes.add(c);
        a.edges.add(ab);
        a.edges.add(ca);
    }

    public Node recursiveSearchByDeep(String tgtName, Stack<Node> toEval, List<Node> evaluated) {
        if (toEval.isEmpty()) {
            System.out.println("Es vacio");
            return null;
        }

        Node root = toEval.pop();
        if (root.name.equals(tgtName)) {
            System.out.println("Se econtró root: " + root.name);
            return root;
        }

        evaluated.add(root);

        for (Edge e : root.edges) {
            if (!evaluated.contains(e.target)) {
                toEval.push(e.target);
                System.out.println("Se evaluó e: " + e.value);
            }

            System.out.println("Entró al foreach: " + e.value);
        }

        return recursiveSearchByDeep(tgtName, toEval, evaluated);
    }
}

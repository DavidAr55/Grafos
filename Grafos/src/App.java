import java.util.Stack;

public class App {
    public static void main(String[] args) throws Exception {

        Graph graph = new Graph();
        Stack<Node>a = new Stack<>();
        for(int i = 0; i < graph.nodes.size(); i++) {
            a.push(graph.nodes.get(i));
        }
        graph.recursiveSearchByDeep("Q", a, new Stack<>());
    }
}

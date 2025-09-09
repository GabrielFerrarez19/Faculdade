import java.util.*;

public class FeiraDeLivros {
    private TreeSet<Livro> livros;
    private TreeMap<String, TreeSet<String>> autores;

    public FeiraDeLivros() {
        livros = new TreeSet<>();
        autores = new TreeMap<>();
    }

    public void cadastrarLivro(String titulo, String autor, int ano) {
        Livro livro = new Livro(titulo, autor, ano);
        livros.add(livro);

        autores.putIfAbsent(autor, new TreeSet<>());
        autores.get(autor).add(titulo);
    }

    public void exibirLivros() {
        System.out.println("\nTodos os livros:");
        for (Livro l : livros) {
            System.out.println(l);
        }
    }

    public void exibirAutoresELivros() {
        System.out.println("\nAutores e seus livros:");
        for (Map.Entry<String, TreeSet<String>> entry : autores.entrySet()) {
            System.out.println(entry.getKey() + ":");
            for (String titulo : entry.getValue()) {
                System.out.println("- " + titulo);
            }
        }
    }
}

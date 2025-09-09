import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        FeiraDeLivros feira = new FeiraDeLivros();

        while (true) {
            System.out.println("\n1 - Cadastrar livro");
            System.out.println("2 - Mostrar todos os livros");
            System.out.println("3 - Mostrar autores e seus livros");
            System.out.println("0 - Sair");
            System.out.print("Escolha uma opção: ");
            int opcao = Integer.parseInt(scanner.nextLine());

            if (opcao == 0) break;

            switch (opcao) {
                case 1:
                    System.out.print("Título: ");
                    String titulo = scanner.nextLine();
                    System.out.print("Autor: ");
                    String autor = scanner.nextLine();
                    System.out.print("Ano de publicação: ");
                    int ano = Integer.parseInt(scanner.nextLine());

                    feira.cadastrarLivro(titulo, autor, ano);
                    System.out.println("Livro cadastrado com sucesso!");
                    break;

                case 2:
                    feira.exibirLivros();
                    break;

                case 3:
                    feira.exibirAutoresELivros();
                    break;

                default:
                    System.out.println("Opção inválida.");
            }
        }

        scanner.close();
    }
}

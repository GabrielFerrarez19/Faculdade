import com.google.gson.Gson;
import com.google.gson.reflect.TypeToken;

import java.io.*;
import java.lang.reflect.Type;
import java.util.*;

public class CadastroDeNomes {
    private static final String ARQUIVO_JSON = "C:\\Users\\gabri\\OneDrive\\Documentos\\Faculdade\\Segundo ano\\Primeiro semestre\\Estrutura de dados 2\\Lista2\\src\\nomes.json";
    private static ArrayList<String> nomes = new ArrayList<>();
    private static final Scanner scanner = new Scanner(System.in);
    private static final Gson gson = new Gson();
    

    public static void main(String[] args) {
        carregarNomes();

        int opcao;
        do {
            mostrarMenu();
            opcao = scanner.nextInt();
            scanner.nextLine(); // Limpa o buffer

            switch (opcao) {
                case 1 -> adicionarNome();
                case 2 -> listarNomes();
                case 3 -> removerNome();
                case 4 -> buscarNome();
                case 5 -> salvarNomes();
                case 6 -> carregarNomes();
                case 0 -> System.out.println("Saindo...");
                default -> System.out.println("Opção inválida!");
            }
        } while (opcao != 0);
    }

    private static void mostrarMenu() {
        System.out.println("\n--- MENU ---");
        System.out.println("1 - Adicionar nome");
        System.out.println("2 - Listar nomes");
        System.out.println("3 - Remover nome");
        System.out.println("4 - Buscar nome");
        System.out.println("5 - Salvar nomes em arquivo JSON");
        System.out.println("6 - Carregar nomes de arquivo JSON");
        System.out.println("0 - Sair");
        System.out.print("Escolha uma opção: ");
    }

    private static void adicionarNome() {
        System.out.print("Digite o nome: ");
        String nome = scanner.nextLine().trim();

        if (nome.isEmpty()) {
            System.out.println("Nome não pode ser vazio!");
        } else if (nomes.contains(nome)) {
            System.out.println("Nome já existe!");
        } else {
            nomes.add(nome);
            System.out.println("Nome adicionado com sucesso.");
        }
    }

    private static void listarNomes() {
        if (nomes.isEmpty()) {
            System.out.println("Nenhum nome cadastrado.");
            return;
        }

        Collections.sort(nomes);
        System.out.println("\n--- Lista de Nomes ---");
        for (int i = 0; i < nomes.size(); i++) {
            System.out.println((i + 1) + ". " + nomes.get(i));
        }
    }

    private static void removerNome() {
        System.out.print("Digite o nome a ser removido: ");
        String nome = scanner.nextLine();

        if (nomes.remove(nome)) {
            System.out.println("Nome removido com sucesso.");
        } else {
            System.out.println("Nome não encontrado.");
        }
    }

    private static void buscarNome() {
        System.out.print("Digite o nome a buscar: ");
        String nome = scanner.nextLine();

        if (nomes.contains(nome)) {
            System.out.println("Nome encontrado na lista.");
        } else {
            System.out.println("Nome não encontrado.");
        }
    }

    private static void salvarNomes() {
        try (Writer writer = new FileWriter(ARQUIVO_JSON)) {
            gson.toJson(nomes, writer);
            System.out.println("Nomes salvos em " + ARQUIVO_JSON);
        } catch (IOException e) {
            System.out.println("Erro ao salvar nomes: " + e.getMessage());
        }
    }

    private static void carregarNomes() {
        File file = new File(ARQUIVO_JSON);
        if (!file.exists()) {
            System.out.println("Arquivo de nomes não encontrado. Criando nova lista.");
            nomes = new ArrayList<>();
            return;
        }

        try (Reader reader = new FileReader(file)) {
            Type type = new TypeToken<ArrayList<String>>() {}.getType();
            nomes = gson.fromJson(reader, type);
            System.out.println("Nomes carregados de " + ARQUIVO_JSON);
        } catch (IOException e) {
            System.out.println("Erro ao carregar nomes: " + e.getMessage());
        }
    }
}

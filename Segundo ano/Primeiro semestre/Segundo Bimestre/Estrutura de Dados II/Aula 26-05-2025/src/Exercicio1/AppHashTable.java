import java.util.Hashtable;
import java.util.Scanner;

public class AppHashTable {
    private static Scanner input = new Scanner(System.in);
    private static Hashtable<String, Aluno> alunos = new Hashtable<>();

    public static int menu() {
        System.out.println("1 - Cadastrar");
        System.out.println("2 - Listar todos");
        System.out.println("3 - Buscar pela matrícula");
        System.out.println("0 - Sair");
        System.out.print("Escolha: ");
        int op = input.nextInt();
        input.nextLine(); // limpar buffer
        return op;
    }

    public static void cadastrar() {
        System.out.println("---- Cadastro ----");
        System.out.print("Matrícula: ");
        String matricula = input.nextLine();

        if (alunos.containsKey(matricula)) {
            System.out.println("Matrícula já cadastrada");
            return;
        }

        System.out.print("Nome: ");
        String nome = input.nextLine();
        System.out.print("Email: ");
        String email = input.nextLine();
        System.out.print("Curso: ");
        String curso = input.nextLine();

        Aluno obj = new Aluno(nome, email, matricula, curso);
        alunos.put(matricula, obj);
        System.out.println("Aluno cadastrado com sucesso!");
    }

    public static void buscar() {
        System.out.println("---- Buscar ----");
        System.out.print("Matrícula: ");
        String matricula = input.nextLine();

        if (alunos.containsKey(matricula)) {
            Aluno alu = alunos.get(matricula);
            System.out.println("Aluno encontrado: " + alu);
        } else {
            System.out.println("Matrícula " + matricula + " não encontrada.");
        }
    }

    public static void main(String[] args) {
        int opcao;
        do {
            opcao = menu();
            switch (opcao) {
                case 1:
                    cadastrar();
                    break;
                case 2:
                    System.out.println("---- Lista de Alunos ----");
                    for (Aluno aluno : alunos.values()) {
                        System.out.println(aluno);
                    }
                    break;
                case 3:
                    buscar();
                    break;
                case 0:
                    System.out.println("Saindo...");
                    break;
                default:
                    System.out.println("Opção inválida");
                    break;
            }
        } while (opcao != 0);
    }
}

package exercicio1;

public class Main {
    public static void main(String[] args) {
        //comentario
        //instanciar objeto Aluno
        Aluno al  = new Aluno();
        al.nome = "Bill Gates";
        al.nota1 = 10;
        al.nota2 = 7;
        al.CalculaMedia();
        System.out.println("Média: " + al.media);

    }
}

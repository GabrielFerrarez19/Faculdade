package exercicio1;
import java.util.Scanner;

public class Ex1 {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        double soma = 0;
        for (int i = 0; i < 3; i++) {
            System.out.println("Digite a nota i+1 do aluno:");
            double nota = sc.nextDouble();
            soma += nota;
        }

        double media = soma/3;

        if (media >= 7){
            System.out.println("Aluno aprovado: " + media);
        }else{
            double pf = 7 - media;
            System.out.println("Aluno em prova final, nota minima: " + pf);
        }

    }
}

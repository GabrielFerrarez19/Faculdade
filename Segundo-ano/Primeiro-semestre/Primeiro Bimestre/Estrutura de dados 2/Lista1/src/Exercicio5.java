import java.util.Scanner;

public class Exercicio5 {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int valor;

        int[] array = {10, 23, 45, 67, 89, 12, 34, 56, 78, 90};

        System.out.println("Digite o valor um valor: ");
        valor = sc.nextInt();
        
        for (int i = 0; i < array.length; i++) {
            if(valor==array[i]){
                System.out.println("Você achou o valor, e ele esta na casa: " + i);
            }else{
                System.out.println("O Numero digitado não esta na lista.");
            }
        }
    }
}

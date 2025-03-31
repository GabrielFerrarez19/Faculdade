import java.util.Scanner;

public class Exercicio2 {
    public static void main(String[] args) {
        float[] array = new float[10]; 
        Scanner Sc = new Scanner(System.in);
        float soma = 0;


        for (int i = 0; i < array.length; i++) {
            System.out.println("Digite os valores do Array: ");
            array[i] = Sc.nextFloat();
            soma += array[i]; 
        }

        System.out.println("Media: " + soma/array.length);
    }
}

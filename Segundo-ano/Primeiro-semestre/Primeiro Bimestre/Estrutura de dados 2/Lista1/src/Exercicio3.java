import java.util.ArrayList;
import java.util.Arrays;
import java.util.Scanner;

public class Exercicio3 {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        float[] array = new float[10]; 
        ArrayList<Float> arrayPar = new ArrayList<>();

        for (int i = 0; i < array.length; i++) {
            System.out.print("Digite um valor para o array: ");
            array[i] = sc.nextFloat();

            if (array[i] % 2 == 0) { 
                arrayPar.add(array[i]);
            }
        }

        sc.close();

        System.out.println("Números pares no array: " + arrayPar);
    }
}

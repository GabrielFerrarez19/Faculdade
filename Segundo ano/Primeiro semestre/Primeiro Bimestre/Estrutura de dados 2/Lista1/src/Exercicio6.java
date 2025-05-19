import java.util.HashSet;
import java.util.Scanner;
import java.util.Set;

public class Exercicio6 {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        System.out.print("Digite o tamanho do array: ");
        int n = sc.nextInt();
        int[] array = new int[n];

        System.out.println("Digite os elementos do array:");
        for (int i = 0; i < n; i++) {
            array[i] = sc.nextInt();
        }

        Set<Integer> valoresUnicos = new HashSet<>();

        for (int num : array) {
            valoresUnicos.add(num);
        }

        System.out.println("Array sem duplicatas:");
        for (int num : valoresUnicos) {
            System.out.print(num + " ");
        }

        sc.close();
    }
}

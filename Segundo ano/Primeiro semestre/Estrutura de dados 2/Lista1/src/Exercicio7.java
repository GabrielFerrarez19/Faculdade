import java.util.Scanner;

public class Exercicio7 {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        System.out.print("Digite o tamanho do array: ");
        int n = sc.nextInt();
        int[] array = new int[n];

        System.out.println("Digite os elementos do array:");
        for (int i = 0; i < n; i++) {
            array[i] = sc.nextInt();
        }

        System.out.print("Digite o número de posições para rotacionar: ");
        int k = sc.nextInt();

        k = k % n;

        rotateArray(array, k);

        System.out.println("Array após rotação:");
        for (int num : array) {
            System.out.print(num + " ");
        }

        sc.close();
    }

    public static void rotateArray(int[] array, int k) {
        // Rotaciona o array
        reverseArray(array, 0, array.length - 1); 
        reverseArray(array, 0, k - 1);             
        reverseArray(array, k, array.length - 1);  
    }

    public static void reverseArray(int[] array, int start, int end) {
        while (start < end) {
            int temp = array[start];
            array[start] = array[end];
            array[end] = temp;
            start++;
            end--;
        }
    }
}

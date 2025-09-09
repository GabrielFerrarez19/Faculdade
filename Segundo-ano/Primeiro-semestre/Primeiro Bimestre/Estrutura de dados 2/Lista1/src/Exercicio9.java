import java.util.Scanner;

public class Exercicio9 {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        System.out.print("Digite o tamanho do primeiro array: ");
        int n1 = sc.nextInt();
        int[] array = new int[n1];

        System.out.println("Digite os elementos do primeiro array ordenado:");
        for (int i = 0; i < n1; i++) {
            array[i] = sc.nextInt();
        }
        
        int maxSum = findMaxSubarraySum(array);
        
        System.out.println("A maior soma de subarray é: " + maxSum);
    }

    public static int findMaxSubarraySum(int[] array) {
        int maxSoFar = array[0];
        int maxEndingHere = array[0];

        for (int i = 1; i < array.length; i++) {
            maxEndingHere = Math.max(array[i], maxEndingHere + array[i]);
            
            maxSoFar = Math.max(maxSoFar, maxEndingHere);
        }

        return maxSoFar;
    }
}

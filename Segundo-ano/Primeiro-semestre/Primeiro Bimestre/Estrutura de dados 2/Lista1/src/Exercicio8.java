import java.util.Scanner;

public class Exercicio8 {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        System.out.print("Digite o tamanho do primeiro array: ");
        int n1 = sc.nextInt();
        int[] array1 = new int[n1];

        System.out.println("Digite os elementos do primeiro array ordenado:");
        for (int i = 0; i < n1; i++) {
            array1[i] = sc.nextInt();
        }

        System.out.print("Digite o tamanho do segundo array: ");
        int n2 = sc.nextInt();
        int[] array2 = new int[n2];

        System.out.println("Digite os elementos do segundo array ordenado:");
        for (int i = 0; i < n2; i++) {
            array2[i] = sc.nextInt();
        }

        int[] mergedArray = mergeSortedArrays(array1, array2);

        System.out.println("Array mesclado antes da ordenação: ");
        for (int num : mergedArray) {
            System.out.print(num + " ");
        }
        System.out.println();

        selectionSort(mergedArray);

        System.out.println("Array ordenado:");
        for (int num : mergedArray) {
            System.out.print(num + " ");
        }

        sc.close();
    }

    public static int[] mergeSortedArrays(int[] array1, int[] array2) {
        int n1 = array1.length;
        int n2 = array2.length;

        int[] mergedArray = new int[n1 + n2];

        int i = 0, j = 0, k = 0;

        while (i < n1 && j < n2) {
            if (array1[i] <= array2[j]) {
                mergedArray[k] = array1[i];
                i++;
            } else {
                mergedArray[k] = array2[j];
                j++;
            }
            k++;
        }

        while (i < n1) {
            mergedArray[k] = array1[i];
            i++;
            k++;
        }

        while (j < n2) {
            mergedArray[k] = array2[j];
            j++;
            k++;
        }

        return mergedArray;
    }

    public static void selectionSort(int[] array) {
        int n = array.length;

        for (int i = 0; i < n - 1; i++) {
            int minIndex = i;

            for (int j = i + 1; j < n; j++) {
                if (array[j] < array[minIndex]) {
                    minIndex = j;
                }
            }

            if (minIndex != i) {
                int temp = array[i];
                array[i] = array[minIndex];
                array[minIndex] = temp;
            }
        }
    }
}

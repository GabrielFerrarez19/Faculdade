import java.util.Scanner;

public class Exercicio1 {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        boolean stop = true;
        int i = 0;
        float soma = 0;
        float[] valores = new float[10]; 

        while (stop && i < valores.length) {
            System.out.print("Digite um valor (ou um número negativo para parar): ");
            float valor = sc.nextFloat(); 

            if (valor < 0) { 
                stop = false;
            } else {
                valores[i] = valor;
                i++; 
            }
        }

        sc.close(); 

        System.out.println("Valores digitados:");
        for (int j = 0; j < i; j++) {
            System.out.println(valores[j]);
            soma += valores[j]; 
        }
        System.out.println("Soma dos valores: "+soma);
    }
}


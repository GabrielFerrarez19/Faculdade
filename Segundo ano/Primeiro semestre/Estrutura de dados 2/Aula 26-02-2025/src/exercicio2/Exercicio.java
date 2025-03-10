/*
Exercício 2: Verificador de Número Primo
Crie um programa que leia um número inteiro do usuário e verifique se ele é um número primo.
Requisitos:
Utilizar Scanner para entrada de dados.
Utilizar estrutura de repetição (for ou while).
Exibir mensagem informando se o número é primo ou não.
*/

package exercicio2;

import java.util.Scanner;

public class Exercicio {
    public static void main(String[] args) {
        Scanner in = new Scanner(System.in);

        System.out.print("Digite o número que deseja verificar: ");
        int num = in.nextInt();
        in.close(); 

        if (num <= 1) {
            System.out.println("O número digitado deve ser maior que 1.");
            return; 
        }

        boolean ehPrimo = true; 

        for (int i = 2; i <= Math.sqrt(num); i++) {
            if (num % i == 0) {
                ehPrimo = false;
                break; 
            }
        }

        if (ehPrimo) {
            System.out.println(num + " é primo.");
        } else {
            System.out.println(num + " não é primo.");
        }
    }
}


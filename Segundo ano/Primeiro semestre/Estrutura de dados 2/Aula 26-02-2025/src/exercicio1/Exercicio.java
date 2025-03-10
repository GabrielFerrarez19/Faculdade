/*
Exercício 1: Calculadora Simples
Crie um programa em Java que peça ao usuário dois números inteiros e uma operação matemática (+, -, *, /).
O programa deve exibir o resultado da operação escolhida.
Requisitos:
Utilizar Scanner para entrada de dados.
Utilizar estrutura condicional (if-else ou switch).
Criar uma classe CalculadoraSimples com um método main.
*/

package exercicio1;

import java.util.Scanner;

public class Exercicio {
    public static void main(String[] args) {

        Scanner li = new Scanner(System.in);

        float valor1, valor2, resultado = 0;
        String operacao;

        System.out.print("Digite o primeiro valor:");
        valor1 = li.nextFloat();

        System.out.print("Digite o segundo valor:");
        valor2 = li.nextFloat();

        System.out.print("Digite qual operação quer fazer (+, -, *, /):");
        operacao = li.next();

            switch (operacao) {
                case "+":
                    resultado = valor1 + valor2;
                    break;
                case "-":
                    resultado = valor1 - valor2;
                    break;
                case "*":
                    resultado = valor1 * valor2;
                    break;
                case "/":
                    if (valor2 != 0) {
                        resultado = valor1 / valor2;
                    } else {
                        System.out.println("Erro: divisão por zero!");
                        return;
                    }
                    break;
                default:
                    System.out.println("Operação inválida!");
                    return;
        }

        System.out.println("Resultado: " + resultado);
        
    }
}

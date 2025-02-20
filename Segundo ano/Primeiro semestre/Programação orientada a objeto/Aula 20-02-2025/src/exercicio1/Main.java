package exercicio1;

import java.util.Scanner;

public class Main {
    
    public static void main(String[] args) {
        Veiculo ve = new Veiculo();
        Scanner scanner  = new Scanner(System.in);
        
        System.out.print("Digite o ano de fabricação do veiculo: ");
        ve.anoFabricacao = scanner.nextInt(); 

        int idade = ve.idade();

        System.out.println(idade);

        System.out.print("Digite o valor do veículo: ");
        ve.valor = scanner.nextDouble();  

        double ipva = ve.valorIPVA();
        double seguro = ve.valorSeguro();

        System.out.println("O valor do IPVA é: R$" + ipva);
        System.out.println("O valor do seguro é: R$" + seguro);

        scanner.close();  
    }
}

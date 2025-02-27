package atividade1;

import java.util.Scanner;

public class Main {

    public static void main(String[] args) {     

    Scanner in = new Scanner(System.in);
    Conta con = new Conta();

    System.out.println("Seu saldo é " + con.verificaSaldo());
    System.out.println("Seu limite é " + con.verificaLimite());
    
    String sair = " ";

    while (sair.equals(" ")) {
        
    System.out.println("Digite\n1-para saque \n2-para deposito \n3-para alterar limite \n4-Aumentar limite \n5-Diminuir limite \nDigite 6 para sair");
    int operacao = in.nextInt();

    if(operacao == 1){
        System.out.print("Digite o valor do saque: ");
        con.saque(in.nextDouble());
    }else if(operacao == 2){
        System.out.print("Digite o valor do deposito: ");
        con.deposito(in.nextDouble());
    }else if(operacao == 3){
        System.out.print("Digite o valor de limite que deseja: ");
        con.alteraLimite(in.nextDouble());
    }else if(operacao == 4){
        System.out.print("Digite quanto que almentar de limite: ");
        con.aumentaLimite(in.nextDouble());
    }else if(operacao == 5){
        System.out.println("Digite quanto que diminuir do seu limite: ");
    }else if(operacao == 6){
        sair = "sair";
    }
    }

}
}

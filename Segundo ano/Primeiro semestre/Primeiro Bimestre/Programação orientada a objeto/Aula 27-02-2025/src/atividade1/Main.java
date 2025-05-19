package atividade1;

import java.util.Scanner;

public class Main {

    public static void main(String[] args) {     

    Scanner in = new Scanner(System.in);
    Conta con = new Conta();

    System.out.print("Digite o nome completo do portador da conta: ");
    con.dono = in.nextLine();

    System.out.print("Digite o numero da conta: ");
    con.numero = in.nextInt();

    System.out.println("Olá " + con.dono);
    System.out.println("Numero da conta: " + con.numero);
    System.out.println("Seu saldo é " + con.verificaSaldo());
    System.out.println("Seu limite é " + con.verificaLimite());

    
    boolean sair = true;

    while (sair) {
        
    System.out.println("Digite\n1-Saque \n2-Deposito \n3-Alterar limite \n4-Aumentar limite \n5-Diminuir limite \n6-Para verficar seu saldo\n7-Para verificar seu limite\n8-Para sair");
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
        System.out.println("Seu saldo atual é " + con.verificaSaldo());
    }else if(operacao == 7){
        System.out.println("Seu limite atual é " + con.verificaLimite());
    }else if(operacao == 8){
        sair = false;
    }
    }

}
}

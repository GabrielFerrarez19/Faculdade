package atividade1;

public class Conta {
    String dono;
    int numero;
    double saldo;
    double limite;


public Conta(){
    String dono = "Fulano";
    int numero = 123;
    double saldo = 0;
    double limite = 100;
}

void saque(double valor){
    if (valor > saldo+limite){
        System.out.println("Saldo insuficiente");
    }else{
        saldo = (saldo + limite) - valor;
        System.out.println("Saldo restante " + saldo);
    }
}

void deposito(double valor){
    if(valor <= 0){
        System.out.println("valor invalido");
    }else{
        saldo = saldo + valor;
        System.out.println("Seu saldo agora é " + saldo);
    }
}

double verificaSaldo(){
    return saldo;
}

double verificaLimite(){
    return limite;
}

void alteraLimite(double valor){
    if(saldo>limite){
        limite = valor;
        System.out.println("Seu limite agora é " + limite);
    }else{
        System.out.println("Alteração não aprovada");
    }
}

void aumentaLimite(double valor){
    if(saldo>limite){
        limite = limite + valor;
        System.out.println("Seu limite agora é " + limite);
    }else{
        System.out.println("Aumento não aprovada");
    }
}

void diminuiLimite(double valor){
    if(valor <= limite){
        limite = limite - valor;
        System.out.println("Seu limite agora é " + limite);
    }else{
        System.out.println("Valor digitado deixara seu limite negativo");
    }
}

}

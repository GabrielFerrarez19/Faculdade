package exemplo1;

public class ContaPoupanca implements Conta {
    private int saldo;


    @Override
    public void mostrarsaldo() {
        System.out.println("Saldo: " + saldo);
    }

    @Override
    public void depositar(double valor) {
        saldo+=valor;
    }

    @Override
    public void sacar(double valor) {
        if(valor<=saldo){
            saldo-=valor;
        }else{
            System.out.println("Saldo insuficiente");
        }
    }

    public int getSaldo() {
        return saldo;
    }

    public void setSaldo(int saldo) {
        this.saldo = saldo;
    }
    
}

package exemplo1;

public class ContaCorrente implements Conta{
    private double saldo;
    private double limite = limitePadrao;


    @Override
    public void mostrarsaldo() {
        System.out.println("Saldo CC:" + saldo);
    }

    @Override
    public void depositar(double valor) {
        saldo+=valor; 
    }

    @Override
    public void sacar(double valor) {
        if(valor <=saldo+limite){
            saldo-=valor;
        }else{
            System.out.println("Saldo insuficiente");
        }
    }

    public double getSaldo() {
        return saldo;
    }

    public void setSaldo(double saldo) {
        this.saldo = saldo;
    }

    public double getLimite() {
        return limite;
    }

    public void setLimite(double limite) {
        this.limite = limite;
    }

    
    
}

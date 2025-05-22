package exemplo1;

public class Aviao extends Veiculo{
    private int numeroANAC;

    public String getNomeImposto(){
        return "IMPOSTO ANAC";
    }

    @Override
    public double getValorImposto(double valorDoVeiculo) {
        return valorDoVeiculo * 12 / 100;
    }
    
    public int getNumeroANAC() {
        return numeroANAC;
    }

    public void setNumeroANAC(int numeroANAC) {
        this.numeroANAC = numeroANAC;
    }

}

package exemplo1;

public class Barco extends Veiculo{
    private int numeroRegistro;

    public int getNumeroRegistro() {
        return numeroRegistro;
    }

    public void setNumeroRegistro(int numeroRegistro) {
        this.numeroRegistro = numeroRegistro;
    }

    public String getNomeImposto(){
        return "IMPOSTO PORTUARIO";
    }

    @Override
    public double getValorImposto(double valorDoVeiculo) {
        return valorDoVeiculo * 8 / 100;
    }
    
}

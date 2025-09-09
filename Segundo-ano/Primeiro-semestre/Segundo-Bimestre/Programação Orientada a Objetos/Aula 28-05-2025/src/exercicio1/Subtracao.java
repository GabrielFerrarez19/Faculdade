package exercicio1;

public class Subtracao implements OperacaoMatematica{
    @Override
    public double calcula(double a,double b) {
        double subtracao = a - b;
        return subtracao;
    }
    
}

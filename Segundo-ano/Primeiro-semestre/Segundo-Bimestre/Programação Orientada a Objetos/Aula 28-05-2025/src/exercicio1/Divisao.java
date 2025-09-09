package exercicio1;

public class Divisao implements OperacaoMatematica{
    @Override
    public double calcula(double a,double b) {
        double divisao = a / b;
        return divisao;
    }
    
}

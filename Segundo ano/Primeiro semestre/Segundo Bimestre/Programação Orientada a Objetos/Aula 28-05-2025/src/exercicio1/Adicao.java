package exercicio1;

public class Adicao implements OperacaoMatematica{
    private double a; 
    private double b;

    @Override
    public double calcula(double a, double b) {
        double soma = a + b;
        return soma;
    }

}

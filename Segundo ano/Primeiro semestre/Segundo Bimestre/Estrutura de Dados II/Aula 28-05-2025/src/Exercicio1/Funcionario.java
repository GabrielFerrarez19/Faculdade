public class Funcionario {
    private String documento;
    private String nome;
    private double salario;

    public Funcionario(String documento, String nome){
        setDucumentos(documento);
        setNome(nome); 
    }
    
    public String getDucumentos() {
        return documento;
    }
    private void setDucumentos(String ducumentos) {
        this.documento = ducumentos;
    }
    public String getNome() {
        return nome;
    }
    public void setNome(String nome) {
        this.nome = nome;
    }
    public double getSalario() {
        return salario;
    }
    public void setSalario(double salario) {
        this.salario = salario;
    }

    @Override
    public String toString(){
        return "Funcionario{" +
                "nome='" + nome + '\'' +
                ", CPF='" + documento + '\'' +
                ", Salario='" + salario + '\'' +
                '}';
    }

    
}

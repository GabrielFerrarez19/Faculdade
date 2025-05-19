package exercicio1;

public class Pessoa {
    private String CPF;
    private String nome;
    private String idade;


    public void setCPF(String cPF) {
        CPF = cPF;
    }

    public void setIdade(String idade) {
        this.idade = idade;
    }

    public void setNome(String nome) {
        this.nome = nome;
    }

    public String getCPF() {
        return CPF;
    }

    public String getIdade() {
        return idade;
    }
    
    public String getNome() {
        return nome;
    }
}

package modificadores_de_acesso.pacote1;

public class Pessoa {
    private String nome;
    private int idade;

    //construtores deve sempre serem publicos acessivel por qualquer classe
    public Pessoa(String novoNome, int novaIdade){
        nome = novoNome;
        idade = novaIdade;

        if( novaIdade >= 0 && novaIdade <=120){
            idade = novaIdade;
        }else{
            System.out.println("Idade invalida");
            idade = 0;
        }
    }

    //atributo publico: acessivel por qualquer classe
    public String pegaNome(){
        return nome;
    }

    public int pegaIdade(){
        return idade;
    }

    //atributo protegido: acessivel por outras classes
    //apenas do mesmo pacote
    protected void aniversario(){
        idade++;
    }

    public void alteraIdade(novaIdade)){
        if( novaIdade >= 0 && novaIdade <=120){
            idade = novaIdade;
        }else{
            System.out.println("Idade invalida");
            idade = 0;
        }
    }
}

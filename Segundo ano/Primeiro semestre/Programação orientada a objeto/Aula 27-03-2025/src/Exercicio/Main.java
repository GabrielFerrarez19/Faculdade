import java.util.ArrayList;

class Responsavel {
    private String nome;
    private String cpf;
    private String telefone;
    private String email;
    private Endereco endereco;
    private ArrayList<Crianca> criancas;

    public Responsavel(String nome) {
        this.nome = nome;
        this.criancas = new ArrayList<>();
    }

    public String getNome() { 
        return nome; }

    public void setNome(String nome) { this.nome = nome; }

    public Endereco getEndereco() { 
        return endereco; }

    public void setEndereco(Endereco endereco) { this.endereco = endereco; }

    public ArrayList<Crianca> getCriancas() { 
        return criancas; }

    public void addCrianca(Crianca crianca) { this.criancas.add(crianca); }
}

class Endereco {
    private String logradouro;
    private String numero;
    private String bairro;
    private Cidade cidade;

    public Endereco(String logradouro, String numero, String bairro, Cidade cidade) {
        this.logradouro = logradouro;
        this.numero = numero;
        this.bairro = bairro;
        this.cidade = cidade;
    }

    public String getEnderecoCompleto() {
        return logradouro + ", " + numero + " - " + bairro + ", " + cidade.getNome() + "/" + cidade.getEstado();
    }
}

class Crianca {
    private String nome;
    private int idade;

    public Crianca(String nome) {
        this.nome = nome;
    }

    public String getNome() { 
        return nome; }
}

class Cidade {
    private String nome;
    private String estado;

    public Cidade(String nome, String estado) {
        this.nome = nome;
        this.estado = estado;
    }

    public String getNome() { 
        return nome; }
    public String getEstado() { 
        return estado; }
}

public class Main {
    public static void main(String[] args) {
        Cidade cidade = new Cidade("Patolandia", "MG");
        Endereco endereco = new Endereco("Rua Pimenta de Padua", "350", "Centro", cidade);

        Responsavel donald = new Responsavel("Donald");
        Responsavel patinhas = new Responsavel("Patinhas");
        Responsavel margarida = new Responsavel("Margarida");

        Crianca zezinho = new Crianca("Zezinho");
        Crianca luizinho = new Crianca("Luizinho");
        Crianca huguinho = new Crianca("Huguinho");
        Crianca patolino = new Crianca("Patolino");

        donald.addCrianca(zezinho);
        donald.addCrianca(luizinho);

        patinhas.addCrianca(zezinho);
        patinhas.addCrianca(huguinho);
        patinhas.addCrianca(patolino);

        margarida.addCrianca(zezinho);

        ArrayList<Responsavel> responsaveis = new ArrayList<>();
        responsaveis.add(donald);
        responsaveis.add(patinhas);
        responsaveis.add(margarida);

        for (Responsavel r : responsaveis) {
            System.out.println("Responsável: " + r.getNome());
            System.out.println("Endereço: " + endereco.getEnderecoCompleto());
            System.out.println("Crianças sob sua responsabilidade:");
            for (Crianca c : r.getCriancas()) {
                System.out.println("- " + c.getNome());
            }
            System.out.println();
        }
    }
}
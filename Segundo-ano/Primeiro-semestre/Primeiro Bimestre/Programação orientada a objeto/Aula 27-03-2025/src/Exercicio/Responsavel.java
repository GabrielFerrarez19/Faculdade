import java.util.ArrayList;

class Responsavel {
    private String nome;
    private String cpf;
    private String telefone;
    private String email;
    private Endereco endereco;
    private ArrayList<Crianca> criancas;

    public Responsavel(String nome, String cpf, String telefone, String email, Endereco endereco) {
        this.nome = nome;
        this.cpf = cpf;
        this.telefone = telefone;
        this.email = email;
        this.endereco = endereco;
        this.criancas = new ArrayList<>();
    }

    public String getNome() { return nome; }
    public String getCpf() { return cpf; }
    public String getTelefone() { return telefone; }
    public String getEmail() { return email; }
    public Endereco getEndereco() { return endereco; }
    public ArrayList<Crianca> getCriancas() { return criancas; }

    public void adicionarCrianca(Crianca crianca) { criancas.add(crianca); }

    public void mostrarDados() {
        System.out.println("Responsável: " + nome);
        System.out.println("CPF: " + cpf);
        System.out.println("Telefone: " + telefone);
        System.out.println("Email: " + email);
        System.out.println("Endereço: " + endereco.getLogradouro() + ", " + endereco.getNumero() + " - " + endereco.getBairro());
        System.out.println("Cidade: " + endereco.getCidade().getNome() + "/" + endereco.getCidade().getEstado());
        System.out.print("Crianças: ");
        for (Crianca c : criancas) {
            System.out.print(c.getNome() + " ");
        }
        System.out.println("\n---------------------");
    }
}
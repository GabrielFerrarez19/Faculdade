import java.util.ArrayList;

class Responsavel {
    private String nome;
    private String cpf;
    private String telefone;
    private String email;
    private Endereco endereco;
    private ArrayList<Crianca> criancas;

    public Responsavel() {
        this.criancas = new ArrayList<>();
    }

    public String getNome() { 
        return nome; }

    public void setNome(String nome) { this.nome = nome; }

    public String getCpf() { 
        return cpf; }

    public void setCpf(String cpf) { this.cpf = cpf; }

    public String getTelefone() { 
        return telefone; }

    public void setTelefone(String telefone) { this.telefone = telefone; }

    public String getEmail() { 
        return email; }

    public void setEmail(String email) { this.email = email; }

    public Endereco getEndereco() { 
        return endereco; }

    public void setEndereco(Endereco endereco) { this.endereco = endereco; }

    public ArrayList<Crianca> getCriancas() { 
        return criancas; }

    public void setCriancas(ArrayList<Crianca> criancas) { this.criancas = criancas; }
}

class Endereco {
    private String logradouro;
    private String numero;
    private String bairro;
    private Responsavel responsavel;
    private Cidade cidade;

    public String getLogradouro() { 
        return logradouro; }

    public void setLogradouro(String logradouro) { this.logradouro = logradouro; }

    public String getNumero() { 
        return numero; }

    public void setNumero(String numero) { this.numero = numero; }

    public String getBairro() { 
        return bairro; }

    public void setBairro(String bairro) { this.bairro = bairro; }

    public Responsavel getResponsavel() { 
        return responsavel; }

    public void setResponsavel(Responsavel responsavel) { this.responsavel = responsavel; }

    public Cidade getCidade() { 
        return cidade; }

    public void setCidade(Cidade cidade) { this.cidade = cidade; }
}

class Crianca {
    private String nome;
    private int idade;
    private ArrayList<Responsavel> responsaveis;

    public Crianca() {
        this.responsaveis = new ArrayList<>();
    }

    public String getNome() { 
        return nome; }

    public void setNome(String nome) { this.nome = nome; }

    public int getIdade() { 
        return idade; }

    public void setIdade(int idade) { this.idade = idade; }

    public ArrayList<Responsavel> getResponsaveis() { 
        return responsaveis; }

    public void setResponsaveis(ArrayList<Responsavel> responsaveis) { this.responsaveis = responsaveis; }
}

class Cidade {
    private String nome;
    private String estado;
    private ArrayList<Endereco> enderecos;

    public Cidade() {
        this.enderecos = new ArrayList<>();
    }

    public String getNome() { 
        return nome; }

    public void setNome(String nome) { this.nome = nome; }

    public String getEstado() { 
        return estado; }

    public void setEstado(String estado) { this.estado = estado; }

    public ArrayList<Endereco> getEnderecos() { 
        return enderecos; }
        
    public void setEnderecos(ArrayList<Endereco> enderecos) { this.enderecos = enderecos; }
}
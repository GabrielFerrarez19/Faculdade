public class Aluno {
    private String nome;
    private String email;
    private String matricula;
    private String curso;

    public Aluno(String nome, String email, String matricula, String curso) {
        this.nome = nome;
        this.email = email;
        this.matricula = matricula;
        this.curso = curso;
    }

    public String getNome() {
        return nome;
    }
    public void setNome(String nome) {
        this.nome = nome;
    }
    public String getEmail() {
        return email;
    }
    public void setEmail(String email) {
        this.email = email;
    }
    public String getMatricula() {
        return matricula;
    }
    public void setMatricula(String matricula) {
        this.matricula = matricula;
    }
    public String getCurso() {
        return curso;
    }
    public void setCurso(String curso) {
        this.curso = curso;
    }

    @Override
    public String toString() {
        return "Aluno{" +
                "nome='" + nome + '\'' +
                ", email='" + email + '\'' +
                ", matricula='" + matricula + '\'' +
                ", curso='" + curso + '\'' +
                '}';
    }
}

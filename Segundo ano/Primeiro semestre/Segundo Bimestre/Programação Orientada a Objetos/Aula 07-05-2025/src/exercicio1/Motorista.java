package exercicio1;

public class Motorista extends Pessoa{
    private String categoria;
    private String dataEmicaoCNH;


    @Override
    public void setCPF(String CPF) {
        super.setCPF(CPF);
    }

    @Override
    public void setIdade(String idade) {
        super.setIdade(idade);
    }

    @Override
    public void setNome(String nome) {
        super.setNome(nome);
    }


    public void setDataEmicaoCNH(String dataEmicaoCNH) {
        this.dataEmicaoCNH = dataEmicaoCNH;
    }

    public void setCategoria(String categoria) {
        this.categoria = categoria;
    }

    @Override
    public String getCPF() {
        return super.getCPF();
    }

    public String getDataEmicaoCNH() {
        return dataEmicaoCNH;
    }

}

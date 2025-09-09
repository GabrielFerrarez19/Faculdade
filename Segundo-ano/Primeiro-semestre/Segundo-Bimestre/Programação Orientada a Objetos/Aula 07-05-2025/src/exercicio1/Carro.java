package exercicio1;

public class Carro {
    private String modelo;
    private String marca;
    private int anoFabricacao;
    private int capacidade;

    public String getModelo() {
        return modelo;
    }

    public int getAnoFabricacao() {
        return anoFabricacao;
    }

    public int getCapacidade() {
        return capacidade;
    }
    public String getMarca() {
        return marca;
    }
    
    public void setAnoFabricacao(int anoFabricacao) {
        this.anoFabricacao = anoFabricacao;
    }

    public void setCapacidade(int capacidade) {
        this.capacidade = capacidade;
    }

    public void setMarca(String marca) {
        this.marca = marca;
    }

    public void setModelo(String modelo) {
        this.modelo = modelo;
    }

}

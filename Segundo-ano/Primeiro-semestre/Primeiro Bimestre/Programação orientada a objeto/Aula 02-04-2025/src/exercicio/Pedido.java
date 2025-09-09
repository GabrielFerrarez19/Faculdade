package exercicio;

public class Pedido {
    private String produto;
    private int quantidade;
    private double preco;
    private Cliente cliente;

    public Cliente getCliente() {
        return cliente;
    }
    public String getProduto() {
        return produto;
    }
    public int getQuantidade() {
        return quantidade;
    }
    public double getPreco() {
        return preco;
    }

    public void setProduto(String produto) {
        this.produto = produto;
    }
    public void setQuantidade(int quantidade) {
        this.quantidade = quantidade;
    }
    public void setPreco(double preco) {
        this.preco = preco;
    }
    public void setCliente(Cliente cliente){
        this.cliente = cliente;
    }
    
}
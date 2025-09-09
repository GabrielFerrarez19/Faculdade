package encapsulamento.exemplo1;

public class Produto {
    private String descricao;
    private double preco;

    public String getDescricao(){
        return descricao;
    }

    public void setDescricao(String descricao){
        this.descricao = descricao;
    }
    
    public double getPreco(){
        return preco;
    }
    public void setPreco(double preco){
        if(preco < 0){
            System.out.println("Preço invalido");
        } else{
            this.preco = preco;
        }
    }
} 
package exercicio;

import java.util.LinkedList;

public class Cliente {
    private String nome;
    private String telefone;
    private LinkedList<Pedido> pedidos = new LinkedList<>();


    public LinkedList<Pedido> getPedidos(){
        return pedidos;
    }
    public String getNome(){
        return nome;
    }
    public String getTelefone(){
        return telefone;
    }

    public void setTelefone(String telefone){
        this.telefone = telefone;
    }
    public void setNome(String nome){
        this.nome = nome;
    }
    public void setPedidos(LinkedList<Pedido> pedidos){
        this.pedidos = pedidos;
    }

}

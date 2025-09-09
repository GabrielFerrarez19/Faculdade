package mensagem.exemplo;

public class Garcom {
    private String nome;
    private Cozinheiro cozinheiro;

    public Garcom(String nome){
        this.nome = nome;
    }

    public String getNome(){
        return nome;
    }

    public Cozinheiro gCozinheiro(){
        return cozinheiro;
    }

    public setCozinheiro(Cozinheiro cozinheiro){
        this.cozinheiro = cozinheiro;
    }

    public void atender(String prato){
        System.out.println("anota pedido");
        cozinheiro.cozinhar(prato);
        System.out.println("Serve o prato");
    }  
}

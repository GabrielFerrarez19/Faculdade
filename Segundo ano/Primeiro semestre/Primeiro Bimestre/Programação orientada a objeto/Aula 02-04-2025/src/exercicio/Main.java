package exercicio;

public class Main {
    public static void main(String[] args) {
        Cliente c1= new Cliente();
        c1.setNome("Donald");
        c1.setTelefone("9999-9999");

        Pedido p1 = new Pedido();
        p1.setProduto("Açai");
        p1.setQuantidade(4);
        p1.setPreco(20);

        //associação do pedido1
        p1.setCliente(c1);
        c1.getPedidos().add(p1);

        Pedido p2 = new Pedido();
        p2.setProduto("Pão de Queijo");
        p2.setQuantidade(20);
        p2.setPreco(15);

        //associacao do pedido2
        p2.setCliente(c1);
        c1.getPedidos().add(p2);

        //exibe os dados
        System.out.println("Cliente: " + c1.getNome());
        for (Pedido p: c1.getPedidos()){
            System.out.println(p.getProduto());
        }

        Cliente c2= new Cliente();
        c2.setNome("Patinhas");
        c2.setTelefone("1234-9999");

        Pedido p3 = new Pedido();
        p3.setProduto("Queijo");
        p3.setQuantidade(4);
        p3.setPreco(20);

        Pedido p4 = new Pedido();
        p4.setProduto("Pão");
        p4.setQuantidade(20);
        p4.setPreco(5);

        Pedido p5 = new Pedido();
        p5.setProduto("Arroz");
        p5.setQuantidade(20);
        p5.setPreco(5);

        c2.getPedidos().add(p3);
        c2.getPedidos().add(p4);
        c2.getPedidos().add(p5);
        
        System.out.println("------------------------");
        System.out.println("Cliente: " + c2.getNome());
        for (Pedido p: c2.getPedidos()){
            System.out.println(p.getProduto());
        }
    }

}

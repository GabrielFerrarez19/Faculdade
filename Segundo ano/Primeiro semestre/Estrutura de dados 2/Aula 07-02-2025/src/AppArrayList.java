import java.util.ArrayList;

public class AppArrayList {
    public static void main(String[] args) throws Exception {
        ArrayList<Produto> listArray = new ArrayList<Produto>();
        Produto arroz = new Produto("Arroz",32);
        listArray.add(arroz);
        listArray.add(new Produto("Feijão",9));
        listArray.add(new Produto("Leite", 4.95));
        System.out.println("ArrayList de Produtos");
        for (Produto p : listArray) {
            System.out.println(p);
        }
    }
}

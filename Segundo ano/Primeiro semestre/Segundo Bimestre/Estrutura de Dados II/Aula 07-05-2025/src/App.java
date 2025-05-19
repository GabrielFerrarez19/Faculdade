import java.util.ArrayList;
import java.util.Random;


public class App {


    public static int funcaoHash(String palavra , int tam) {
        int hash = 0;
        // ex Abobora  -> pega letra A -> int da tablea ascii
        // A -> valor 65
        // 65 -> 0
        //90 ->25
        hash = 13+palavra.toUpperCase().charAt((0));//pega inicial

        return hash % tam;
    }

    public static void main(String[] args) throws Exception{
        int totalCategorias = 26;
        ArrayList<String>totalHash[] = new ArrayList[totalCategorias];
        //inicializar tabela 
        for (int i = 0; i < totalHash.length; i++) {
            System.out.println(i + " - " + totalHash[i]);
            totalHash[i] = new ArrayList<String>();
        }
        
        System.out.println("---INSTANCIAS---");
        for (int i = 0; i < totalHash.length; i++) {
            System.out.println(i + " ->" + totalHash[i]);
        }

        System.out.println("Adicionando palavras...");
        for (int i = 0; i < 100; i++) {
            String palavra = GeradorPalavras.gerarPalavraAleatoria(3,10);
            int categoria = funcaoHash(palavra, totalCategorias);
            totalHash[categoria].add(palavra);
        }

        System.out.println("---PREENCHIDA---");
        for (int i = 0; i < totalHash.length; i++) {
            System.out.println(i + "-> total = " + totalHash[i]);
        }
    }

    
}

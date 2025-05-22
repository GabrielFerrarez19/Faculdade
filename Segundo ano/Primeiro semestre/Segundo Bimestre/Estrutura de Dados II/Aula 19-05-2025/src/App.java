import java.lang.reflect.Array;
import java.util.ArrayList;
import java.util.List;

public class App {

    public static int funcaoHash(String palavra, int tam){
        int hash = 0;
        //  ex: Abobora  -> pega letra A->int da tabela ascii
        // A -> valor 65
        /// 65 -> 0
        /// 90 -> 25
        hash = 13+palavra.toUpperCase().charAt(0);  // pega a inicial

        return hash % tam;
    }

    public static boolean buscarPalavra(String palavra, ArrayList<String>[] tabelaHash, int tam) {
	    
        return true;
    }
    
    public static void main(String[] args) throws Exception {
        int totalCategorias = 26;
        ArrayList<String> tabelaHash[] =  new ArrayList[totalCategorias];
        // inicializar a tabela
        for (int i = 0; i < tabelaHash.length; i++) {
            System.out.println(i + "-> " + tabelaHash[i]);
            tabelaHash[i] = new ArrayList<String>();
        }
        System.out.println("---INSTANCIADAS---");
        for (int i = 0; i < tabelaHash.length; i++) {
            System.out.println(i + "-> " + tabelaHash[i]);
        }
        System.out.println("Adicionando palavras...");
        List<String> listaPalavra = GeradorPalavras.lerPalavras();
        for (String palavra : listaPalavra) {
            palavra = palavra.toUpperCase();
            int categoria = funcaoHash(palavra, totalCategorias);
            tabelaHash[categoria].add(palavra);     
        }
        // for (int i = 0; i < 100; i++) {
        //     String palavra = GeradorPalavras.gerarPalavraAleatoria(3, 10);
        //     int categoria = funcaoHash(palavra, totalCategorias);
        //     tabelaHash[categoria].add(palavra);            
        // }
        System.out.println("---PREENCHIDA---");
        for (int i = 0; i < tabelaHash.length; i++) {
            ArrayList<String> el = tabelaHash[i];
            String letra = el.get(0);
            System.out.println(i + " "+ letra + "-> total = " + el.size());
        }
    }
}
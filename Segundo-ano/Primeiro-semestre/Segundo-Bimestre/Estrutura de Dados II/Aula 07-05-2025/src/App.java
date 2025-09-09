import java.util.ArrayList;
import java.util.Random;
import javax.swing.JOptionPane;

public class App {

    public static int funcaoHash(String palavra, int tam) {
        int hash = 0;
        hash = 13 + palavra.toUpperCase().charAt(0);
        return hash % tam;
    }

    public static void main(String[] args) throws Exception {
        int totalCategorias = 26;
        ArrayList<String>[] totalHash = new ArrayList[totalCategorias];

        // inicializar tabela
        for (int i = 0; i < totalHash.length; i++) {
            totalHash[i] = new ArrayList<String>();
        }

        System.out.println("---INSTANCIAS---");
        for (int i = 0; i < totalHash.length; i++) {
            System.out.println(i + " -> " + totalHash[i]);
        }

        System.out.println("Adicionando palavras...");
        for (int i = 0; i < 100; i++) {
            String palavra = GeradorPalavras.gerarPalavraAleatoria(3, 10); // Supondo que GeradorPalavras esteja definido corretamente
            int categoria = funcaoHash(palavra, totalCategorias);
            totalHash[categoria].add(palavra);
        }

        System.out.println("---PREENCHIDA---");
        for (int i = 0; i < totalHash.length; i++) {
            System.out.println(i + " -> total = " + totalHash[i]);
        }

        String opcao = null;
        do {
            String procurar = JOptionPane.showInputDialog("Digite a palavra que deseja procurar: ");

            boolean result = buscarPalavra(procurar, totalHash, totalCategorias);
            if (result) {
                JOptionPane.showMessageDialog(null, "Palavra encontrada! " + procurar);
            } else {
                JOptionPane.showMessageDialog(null, "Palavra não encontrada! " + procurar);
            }
            opcao = JOptionPane.showInputDialog("Deseja continuar? (S/N)");

        } while (opcao.equalsIgnoreCase("S"));

    }

    public static boolean buscarPalavra(String palavra, ArrayList<String>[] totalHash, int totalCategorias) {
        int categoria = funcaoHash(palavra, totalCategorias);
        return totalHash[categoria].contains(palavra);
    }

    
}

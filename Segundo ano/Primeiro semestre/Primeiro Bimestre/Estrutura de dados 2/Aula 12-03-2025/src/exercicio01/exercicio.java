//Crie um programa que receba uma array (vetor) de N elementos e calcule a soma de todos os elementos

package exercicio01;

import javax.swing.JOptionPane;

public class exercicio {
    public static String imprimir(int[]v) {
        String saida =" ";
        for (int i = 0; i < v.length; i++) {
            saida = saida + v[i] + " ";
        }
        JOptionPane.showMessageDialog(null, saida);
        System.out.println();
        return saida;
    }

    public static void main(String[] args) {
        int soma = 0;
        int totalNumeros = 0;
        //entrada de dados usando uma clase JOptionPane
        String totalNumerosStr = JOptionPane.showInputDialog("Tamanho do vetor:");
        //converte (altera) de String para int
        totalNumeros = Integer.parseInt(totalNumerosStr);
        //criar vetor
        int []numeros = new int[totalNumeros];
        //preencher o vetor
        for (int i = 0; i < numeros.length; i++) {
            String aux = JOptionPane.showInputDialog("Digite o numero " + (i+1) +":");
            numeros[i] = Integer.valueOf(aux);
        }
        String s =imprimir(numeros);
        //soma todos os numeros
        for (int i = 0; i < numeros.length; i++) {
            soma = soma + numeros[i];
        }
        JOptionPane.showMessageDialog(null, "Vetor: "+ s + " Soma: " + soma);

    }
}

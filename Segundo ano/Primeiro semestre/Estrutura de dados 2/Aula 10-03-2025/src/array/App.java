package array;

public class App {
    public static void imprimir(int []aux){
        for (int i = 0; i < aux.length; i++) {
            System.out.println(i + " >> " + aux[i]);
        }
    }
    public static void main(String[] args) {
        int tamanho = 15;
        //int []numeros = new int[15];
        int []numero = new int[tamanho];
        System.out.println(numero);
        String []palavra = {"ola","mundo","abobora"};
        System.out.println(palavra);
        Cliente []cliente = new Cliente[100];
        System.out.println(cliente);

        //adiciono elemento no vetor numeros
        numero[5] = 357;

    }
}

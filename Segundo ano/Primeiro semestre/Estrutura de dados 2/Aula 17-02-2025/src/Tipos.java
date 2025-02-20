public class Tipos {
    public static void main(String[] args) {
        System.out.println(Integer.MAX_VALUE);
        System.out.println(Integer.MIN_VALUE);
        Byte numero = 127;
        System.out.println("---teste---");
        System.out.println(numero);
        //numero = numero++;
        //System.out.println(numero++);
        System.out.println(++numero);
        //tipos primeitivos inteiros 
        byte valor1 = 127;  //byte -> 7 bits pro numero 1 bit sinal
        byte valor2 = -128;
        //short [- 32768, 32767]
        short valor3 = 32767;   //short -> 15 bits pro numero 1 bit sinal
        //int [-2147483648, 2147483647]
        int valor4 = 2147483647; //int 4 bytes = 31 bits e 1 bit sinal
        //l bit sinal 63 bits pro numero
        long valor5 = 9223372036854775807l;
        //numeros reais 
        float valor6 = 1.0f/3.0f;   //4 bytes
        double valor7 = 1.0/3.0;    //8 bytes -> maior precisão
        System.out.println(valor6);
        System.out.println(valor7);
        //caracteres
        char valor8 = 'a';
        char valor9 = 'A';
        System.out.println(valor8);
        System.out.println(valor9);
        valor8++;// valor8 = valor8 + 1
        //valor9 = valor9 + 1; da erro
        System.out.println(valor8);
        char valor10 = 100;
        System.out.println(valor10);
        int valor11 = '$';
        System.out.println(valor11);
        //caracteres especiais 
        // \n enter (quebra de linha)
        // \t tab
        // \f pagina (form feed)
        // \'' - para exibir as aspas 
        System.out.println("\fola mundo\nhoje\testa\" calor");
        //string assim esta errado, String assim ok
        String valor12 = "Vai toma no cu";
        System.out.println(valor12);
        System.out.println(valor12.toUpperCase());
        //tipo logico - boolean 
        boolean valor13 = false;
        System.out.println(valor13);
    }
}
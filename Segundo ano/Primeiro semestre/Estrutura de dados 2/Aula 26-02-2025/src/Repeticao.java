public class Repeticao {
    public static void main(String[] args) {
        for(int i = 0; i<=10; i++){
            System.out.println(i);
        }
        System.out.println("---");
        for(int i = 10; i >= 1; i--){
            System.out.println("=====");
        }
        int j = 20;
        while (j>10){
            System.out.println("ola " + j);
            j--;
        }
        System.out.println("******");
        int y = 20;
        do{
            System.out.println("oi " + y);
        }
        while(y < 30);
    }
}

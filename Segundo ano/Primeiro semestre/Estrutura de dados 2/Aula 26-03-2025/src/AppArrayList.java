import java.util.ArrayList;
import java.util.Collections;
import java.util.Random;

public class AppArrayList {
    public static void main(String[] args) {
        // array heterogeneo -  armazena valores de tipos diferentes
        ArrayList vetor = new ArrayList();
        
        System.out.println(vetor.size());
        System.out.println(vetor.isEmpty());
        vetor.add(231);
        vetor.add("Bicicleta");
        System.out.println(vetor.size());
        System.out.println(vetor.isEmpty());
        System.out.println(vetor);
        // armazenar apenas inteiros
        ArrayList<Integer> nums = new ArrayList<Integer>();
        nums.add(8);
        // nums.add("Teste"); // erro
        Random rnd = new Random();            
        for (int index = 0; index < 10; index++) {
            nums.add(rnd.nextInt(1000));
            System.out.println(nums);
        }
        boolean estaNoArray = nums.contains(8);
        System.out.println(estaNoArray);
        // funcao para ordenar os elementos de uma ArrayList
        Collections.sort(nums);
        System.out.println(nums);
    }    
}
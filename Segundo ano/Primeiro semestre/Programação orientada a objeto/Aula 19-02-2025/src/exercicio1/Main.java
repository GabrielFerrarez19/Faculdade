package exercicio1;

public class Main {
    public static void main(String[] args) {
        Pessoa ze = new Pessoa();

        ze.alteraNome("José Silva");
        ze.alteraAltura(1.65);
        ze.alteraPeso(301);

        System.out.println("Nome: " + ze.retornaNome());
        System.out.println("Altura: " + ze.retornaAltura());
        System.out.println("Peso: " + ze.retornaPeso());
        System.out.println("IMC: " + ze.retornaIMC());

    }
}
 
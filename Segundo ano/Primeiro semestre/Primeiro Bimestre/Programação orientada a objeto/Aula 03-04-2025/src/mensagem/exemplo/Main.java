package mensagem.exemplo;

public class Main {
    public static void main(String[] args) {
        Cozinheiro c = new Cozinheiro("Jaqcin");
        Garcom g = new Garcom("Joaquim");

        //atribuir o cozinehro para o garçom:
        g.setCozinheiro(c);

        //executa ação com envio de mensagem:
        g.atender();

        //adicione um parametro Steing na ação do Garçom 
        //de atender, Neste paramentro deve ser passado
        //o nome do prato. o garçom deve repassar este 
        //nome do prato para o cozinheiro,
        //Quando o cozinheiro for cozinhar ele devera
        //ter os seguintes passos adicionar:
        //se o prato for macarrão: fazer molho
        //Se o prato for risoto: preparar caldo de legumes
        //Se o prato for pizza: aquecer o forno
        //Se o prato for tapioca: adicionar recheio da tapioca
    }
}

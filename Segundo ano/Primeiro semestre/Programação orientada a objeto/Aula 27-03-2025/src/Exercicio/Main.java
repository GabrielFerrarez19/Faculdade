public class Main {
    public static void main(String[] args) {
        
        Cidade cidade = new Cidade("Springfield", "IL");
        Endereco endereco = new Endereco("Rua Evergreen Terrace", "742", "Centro", cidade);
        
        Crianca bart = new Crianca("Bart");
        Crianca lisa = new Crianca("Lisa");
        Crianca maggie = new Crianca("Maggie");
        Crianca milhouse = new Crianca("Milhouse");
        
        Responsavel homer = new Responsavel("Homer Simpson", "111.222.333-44", "(11) 90000-1111", "homer@email.com", endereco);
        Responsavel marge = new Responsavel("Marge Simpson", "555.666.777-88", "(21) 91111-2222", "marge@email.com", endereco);
        Responsavel ned = new Responsavel("Ned Flanders", "999.888.777-66", "(31) 92222-3333", "ned@email.com", endereco);
        
        homer.adicionarCrianca(bart);
        homer.adicionarCrianca(lisa);

        marge.adicionarCrianca(bart);
        marge.adicionarCrianca(maggie);
        marge.adicionarCrianca(milhouse);

        ned.adicionarCrianca(bart);

        homer.mostrarDados();
        marge.mostrarDados();
        ned.mostrarDados();
    }
}

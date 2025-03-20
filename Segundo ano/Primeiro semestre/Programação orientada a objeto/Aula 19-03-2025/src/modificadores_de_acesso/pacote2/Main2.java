package modificadores_de_acesso.pacote2;

import modificadores_de_acesso.pacote1.Pessoa;

public class Main2 {
    public static void main(String[] args) {
        
        //altere o contrutor para permitir idade apenas entre 0 a 120, qualquer idade fora deste intervalo, atribua 0 para a idade
        //e mostre uma mensagem informando o usuaruio de que o valor é invalido 

        //crie um metodo chamado alteraIdade que receba uma nova idade e tenha os mesmos criterios do contrutor para aceitar apenas idade entre 
        //0 e 120.
        Pessoa p = new Pessoa("Bill", 50);
        //p.aniversario();

        System.out.println("Nome " + p.pegaNome());

    }
      
}

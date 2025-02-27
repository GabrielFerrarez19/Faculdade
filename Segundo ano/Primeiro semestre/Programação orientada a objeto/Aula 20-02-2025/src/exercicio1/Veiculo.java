package exercicio1;

public class Veiculo {
    String placa;
    String modelo;
    String marca;
    int anoFabricacao;
    double valor;

    int idade(){
        if(anoFabricacao <= 2025){
            return 2025-anoFabricacao;
        }else{
            System.out.println("Ano de fabricação e invalido!!!");
            return 0;
        }
    }

    double valorIPVA(){
        if(anoFabricacao < 1970){
            return 0;
        }else{
            return valor*0.04;
        }
    }

    double valorSeguro(){
        return valor*0.06;
    }
}

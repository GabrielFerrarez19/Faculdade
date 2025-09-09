package model;

import java.util.*;

public class MapaCidades {
    private TreeSet<Cidade> cidades;
    private HashMap<Cidade, Set<Rota>> grafo;

    public MapaCidades() {
        cidades = new TreeSet<>();
        grafo = new HashMap<>();
    }

    public void adicionarCidade(Cidade cidade) {
        cidades.add(cidade);
        grafo.putIfAbsent(cidade, new HashSet<>());
    }

    public void conectarCidades(Cidade origem, Cidade destino, int distancia) {
        if (!cidades.contains(origem) || !cidades.contains(destino)) {
            System.out.println("Uma ou ambas as cidades não estão cadastradas.");
            return;
        }

        grafo.get(origem).add(new Rota(destino, distancia));
        grafo.get(destino).add(new Rota(origem, distancia)); // Grafo não direcionado
    }

    public void listarConexoes(Cidade cidade) {
        System.out.println("Conexões de " + cidade.getNome() + ":");
        Set<Rota> rotas = grafo.get(cidade);
        if (rotas.isEmpty()) {
            System.out.println("  Nenhuma conexão.");
        } else {
            for (Rota rota : rotas) {
                System.out.println("  -> " + rota);
            }
        }
    }

    public boolean existeCaminho(Cidade origem, Cidade destino) {
        Set<Cidade> visitadas = new HashSet<>();
        return buscaProfundidade(origem, destino, visitadas);
    }

    private boolean buscaProfundidade(Cidade atual, Cidade destino, Set<Cidade> visitadas) {
        if (atual.equals(destino)) return true;
        visitadas.add(atual);

        for (Rota rota : grafo.get(atual)) {
            Cidade vizinha = rota.getDestino();
            if (!visitadas.contains(vizinha)) {
                if (buscaProfundidade(vizinha, destino, visitadas)) {
                    return true;
                }
            }
        }
        return false;
    }

    public void listarCidadesSemConexao() {
        for (Cidade cidade : cidades) {
            if (grafo.get(cidade).isEmpty()) {
                System.out.println("  - " + cidade.getNome());
            }
        }
    }

    // Funcionalidade bônus: cidade mais populosa
    public Cidade cidadeMaisPopulosa() {
        return cidades.stream().max(Comparator.comparingInt(Cidade::getPopulacao)).orElse(null);
    }
}

package model;

public class Rota {
    private Cidade destino;
    private int distanciaKm;

    public Rota(Cidade destino, int distanciaKm) {
        this.destino = destino;
        this.distanciaKm = distanciaKm;
    }

    public Cidade getDestino() {
        return destino;
    }

    public int getDistanciaKm() {
        return distanciaKm;
    }

    @Override
    public String toString() {
        return "Destino: " + destino.getNome() + " - Distância: " + distanciaKm + "km";
    }
}

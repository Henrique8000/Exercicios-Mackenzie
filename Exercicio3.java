public class Exercicio3 {
    public static void main(String[] args) {
        
        double preco = 100.00;

        double desconto = (preco / 100) * 15;

        double precoFinal = preco - desconto;

        System.out.println("Original: " + preco);
        System.out.println("Desconto: " + desconto);
        System.out.println("Preço final: " + precoFinal);

    }
}

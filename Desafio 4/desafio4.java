import java.util.Scanner;

public class desafio4 {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        while (true) {
            System.out.println("Digite uma string (ou 'sair' para encerrar o programa): ");
            String str = sc.nextLine();
            if (str.equalsIgnoreCase("sair")) {
                System.out.println("Encerrando o programa...");
                break;
            }
            String strInvertida = inverteString(str);
            System.out.println("String invertida: " + strInvertida);
        }
        sc.close();
    }

    public static String inverteString(String str) {
        char[] arrayChar = str.toCharArray();
        int tamanho = arrayChar.length;
        for (int i = 0; i < tamanho / 2; i++) {
            char temp = arrayChar[i];
            arrayChar[i] = arrayChar[tamanho - 1 - i];
            arrayChar[tamanho - 1 - i] = temp;
        }
        return new String(arrayChar);
    }
}
